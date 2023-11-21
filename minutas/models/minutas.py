from typing import List

from num2words import num2words
from utils.document import Document
from utils.exceptions import ValidationError
from utils.validators import Validator
from utils.validating_dictionaries.dictionary_poderdantes import dictionary_validator_poderdantes
from utils.validating_dictionaries.dictionary_apoderado import dictionary_validator_apoderado
from utils.validating_dictionaries.dictionary_representante_banco import dictionary_validator_representante_banco
from utils.validating_dictionaries.dictionary_inmueble import dictionary_validator_inmueble
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_parqueaderos
from utils.validating_dictionaries.dictionary_depositos import dictionary_validator_depositos
from utils.validating_dictionaries.dictionary_apoderado_banco import dictionary_validator_apoderado_banco
from utils.validating_dictionaries.dictionary_banco import dictionary_validator_banco
from utils.validating_dictionaries.dictionary_prestamo import dictionary_validator_prestamo
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_direccion
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_matricula
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_tipo_ficha_catastral
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_numero_ficha_catastral
from utils.validating_dictionaries.dictionary_apoderado_banco import dictionary_validator_escritura

from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos

from .apoderado import Apoderado
from .apoderado_banco import ApoderadoBanco
from .depositos import Deposito
from .inmueble import InmueblePrincipal
from .parqueaderos import Parqueadero
from .poderdantes import Poderdante
from .representante_banco import RepresentanteBanco
from .banco import Banco
from .prestamo import Prestamo


class DocumentoMinuta(Document):
    apoderado: Apoderado
    poderdantes: List[Poderdante]
    inmueble: InmueblePrincipal
    depositos: List[Deposito]
    parqueaderos: List[Parqueadero]
    apoderado_banco: ApoderadoBanco
    representante_banco: RepresentanteBanco
    banco: Banco
    prestamo: Prestamo

    generate_html_functions = [
        'generar_titulo_documento',
        'generar_parrafo_apoderado',
        'generar_parrafo_poderdantes',
        'generar_primero_constitucion_hipoteca',
        'generar_direccion_inmueble',
        'generar_direccion_parqueaderos',
        'generar_direccion_depositos',
        'generar_matriculas_inmobiliarias',
        'generar_fichas_catastrales',
        'generar_regimen_propiedad_horizontal',
        'generar_paragrafo_primero',
        'generar_paragrafo_segundo',
        'generar_titulo_de_adquisicion',
        'generar_garantia_de_propiedad_y_libertad',
        'generar_obligaciones_garantizadas',
        'generar_paragrafo_primero_aprobacion_de_credito',
        'generar_paragrafo_segundo_prestamos',
        'generar_paragrafo_tercero_no_se_extingue_hipoteca',
        'generar_quinto_aceleracion_del_plazo',
        'generar_sexto_cesion_de_credito',
        'generar_septimo_costos_y_gastos_judiciales',
        'generar_octavo_secuestre',
        'generar_noveno_vigencia_de_hipoteca',
        'generar_decimo_seguros',
        'generar_decimo_primero_convenio',
        'generar_decimo_segundo_poder',
        'generar_decimo_tercero_inputacion_de_pago',
        'generar_datos_apoderado_banco',
        'generar_datos_representante_banco',
        'generar_constitucion_banco_union',
        'generar_aprobacion_credito_al_hipotecante',
        'generar_afectacion_vivienda_familiar',
        'generar_lectura_escritura_por_otorgantes',
        'generar_paz_y_salvo',
        'generar_firma_comprador',
        'generar_firma_hipotecante',
        'generar_firma_apoderado_banco',
        'generar_estilos'
    ]

    def __init__(
        self,
        apoderado: Apoderado,
        poderdantes: List[Poderdante],
        inmueble: InmueblePrincipal,
        depositos: List[Deposito],
        parqueaderos: List[Parqueadero],
        apoderado_banco: ApoderadoBanco,
        representante_banco: RepresentanteBanco,
        banco: Banco,
        prestamo: Prestamo
    ):
        self.apoderado = apoderado
        self.poderdantes = poderdantes
        self.inmueble = inmueble
        self.depositos = depositos
        self.parqueaderos = parqueaderos
        self.apoderado_banco = apoderado_banco
        self.representante_banco = representante_banco
        self.banco = banco
        self.prestamo = prestamo
        self.validate_data()

    def validate_data(self):
        self.validar_poderdantes()
        self.validar_apoderado()
        self.validar_apoderado_banco()
        self.validar_representante_banco()
        self.validar_inmueble()
        self.validar_parqueaderos()
        self.validar_depositos()
        self.validar_banco()
        self.validar_prestamo()

    def validar_poderdantes(self):
        if self.cantidad_poderdantes == 0 and self.cantidad_poderdantes > 2:
            raise ValidationError(
                'Debe haber al menos un poderdante y no más de dos poderdantes.')
        obligatorios = {
            "nombre": "nombre",
            "tipo_identificacion": "tipo de identificación",
            "numero_identificacion": "número de identificación",
            "ciudad_expedicion_identificacion": "ciudad de expedición de identificación",
            "domicilio": "domicilio",
            "estado_civil": "estado civil",
            "genero": "genero",
        }
        for poderdante in self.poderdantes:
            for obligatorio, value in obligatorios.items():
                has_valor = hasattr(poderdante, obligatorio)
                if not has_valor:
                    raise ValidationError(
                        f'Atributo faltante de poderdante: {value}')
                get_valor = getattr(poderdante, obligatorio)
                if not get_valor:
                    raise ValidationError(
                        f'Dato faltante de poderdante: {value}')

        for poderdante in self.poderdantes:
            atributos_poderdante = poderdante.__dict__
            Validator.validate_dict(
                atributos_poderdante, dictionary_validator_poderdantes, 'Poderdantes')

    def validar_apoderado(self):
        if self.apoderado is None:
            raise ValidationError(
                'No hay datos de apoderado. Favor de agregar datos')

        obligatorios = {
            "nombre": "nombre",
            "tipo_identificacion": "tipo de identificación",
            "numero_identificacion": "número de identificación",
            "ciudad_expedicion_identificacion": "ciudad de expedición de identificación",
            "genero": "genero",
        }
        for obligatorio, value in obligatorios.items():
            valor = getattr(self.apoderado, obligatorio)
            if not valor:
                raise ValidationError(f'Dato faltante de apoderado: {value}')

        atributos_apoderado = self.apoderado.__dict__
        Validator.validate_dict(
            atributos_apoderado, dictionary_validator_apoderado, 'Apoderado')

    def validar_apoderado_banco(self):
        if self.apoderado_banco is None:
            raise ValidationError(
                'No hay datos de apoderado especial. Favor de agregar datos')

        if self.apoderado_banco.nombre not in [apoderado['nombre'] for apoderado in apoderados_banco]:
            obligatorios = {
                "nombre": "nombre",
                "tipo_identificacion": "tipo de identificación",
                "numero_identificacion": "número de identificación",
                "ciudad_expedicion_identificacion": "ciudad de expedición de identificación",
                'ciudad_residencia': 'ciudad de residencia',
                "genero": "genero",
                'tipo_apoderado': 'tipo de apoderado',
                'tipo_poder': 'tipo de poder'
            }
            for obligatorio, value in obligatorios.items():
                valor = getattr(self.apoderado_banco, obligatorio)
                if not valor:
                    raise ValidationError(
                        f'Dato faltante de Apoderado del banco: {value}')

            atributos_apoderado_banco = self.apoderado_banco.__dict__
            atributos_a_evaluar = {
                'nombre': atributos_apoderado_banco.get('nombre'),
                'tipo_identificacion': atributos_apoderado_banco.get('tipo_identificacion'),
                'numero_identificacion': atributos_apoderado_banco.get('numero_identificacion'),
                'ciudad_expedicion_identificacion': atributos_apoderado_banco.get('ciudad_expedicion_identificacion'),
                'ciudad_residencia': atributos_apoderado_banco.get('ciudad_residencia'),
                'genero': atributos_apoderado_banco.get('genero'),
                'tipo_apoderado': atributos_apoderado_banco.get('tipo_apoderado'),
                'tipo_poder': atributos_apoderado_banco.get('tipo_poder')
            }

            Validator.validate_dict(
                atributos_a_evaluar, dictionary_validator_apoderado_banco, 'Apoderado del banco')

            if self.apoderado_banco.tipo_poder == 'Escriturado':
                valor = getattr(self.apoderado_banco, 'escritura')
                if not valor:
                    raise ValidationError(
                        f'Dato faltante de Apoderado del banco: Escritura pública')

                atributo_escritura = {
                    'escritura': atributos_apoderado_banco.get('escritura')
                }
                Validator.validate_dict(
                    atributo_escritura, dictionary_validator_escritura, 'Apoderado del banco')

    def validar_representante_banco(self):
        if self.representante_banco is None:
            raise ValidationError(
                'No hay datos de representante legal. Favor de agregar datos')

        if self.representante_banco.nombre not in [representante['nombre'] for representante in representantes_banco]:
            obligatorios = {
                'nombre': 'nombre',
                'tipo_identificacion': 'tipo de identificación',
                'numero_identificacion': 'número de identificación',
                'ciudad_expedicion_identificacion': 'ciudad de expedición de identificación',
                'ciudad_residencia': 'ciudad de residencia',
                'genero': 'genero',
                'tipo_representante': 'tipo de representante'
            }
            for obligatorio, value in obligatorios.items():
                valor = getattr(self.representante_banco, obligatorio)
                if not valor:
                    raise ValidationError(
                        f'Dato faltante de representante del banco: {value}')

            atributos_representante_banco = self.representante_banco.__dict__
            Validator.validate_dict(
                atributos_representante_banco, dictionary_validator_representante_banco, 'Representante del banco')

    def validar_banco(self):
        if self.banco is None:
            raise ValidationError(
                'No hay datos de banco. Favor de agregar datos')

        if self.banco.nombre not in [banco['nombre'] for banco in bancos]:
            obligatorios = {
                'nombre': 'nombre',
                'nit': 'NIT',
            }
            for obligatorio, value in obligatorios.items():
                valor = getattr(self.banco, obligatorio)
                if not valor:
                    raise ValidationError(f'Dato faltante de banco: {value}')
            atributos_banco = self.banco.__dict__
            Validator.validate_dict(
                atributos_banco, dictionary_validator_banco, 'Banco')

    def validar_prestamo(self):
        if self.prestamo is None:
            raise ValidationError(
                'No hay datos del prestamo. Favor de agregar datos')
        obligatorios = {
            'cantidad_banco_a_hipotecante': 'prestamo otorgado por el banco a la parte hipotecante',
            'cantidad_dada_a_constructora': 'precio otorgado por el banco a la constructora',
            'gastos_de_gestion': 'gastos de gestión y trámite del crédito'
        }
        for obligatorio, value in obligatorios.items():
            valor = getattr(self.prestamo, obligatorio)
            if not valor:
                raise ValidationError(f'Dato faltante de prestamo: {value}')
        atributos_prestamo = self.prestamo.__dict__
        Validator.validate_dict(
            atributos_prestamo, dictionary_validator_prestamo, 'Prestamo')

    def validar_inmueble(self):
        if self.inmueble is None:
            raise ValidationError(
                'No hay datos de inmueble. Favor de agregar datos')
        obligatorios = {
            'cantidad_banco_a_hipotecante': 'prestamo otorgado por el banco a la parte hipotecante',
            'cantidad_dada_a_constructora': 'precio otorgado por el banco a la constructora',
            'gastos_de_gestion': 'gastos de gestión y trámite del crédito'
        }
        for obligatorio, value in obligatorios.items():
            valor = getattr(self.prestamo, obligatorio)
            if not valor:
                raise ValidationError(f'Dato faltante del prestamo: {value}')
        atributos_prestamo = self.prestamo.__dict__
        Validator.validate_dict(
            atributos_prestamo, dictionary_validator_prestamo, 'Prestamo')

        obligatorios = {
            'nombre': 'nombre',
            'numero': 'número',
            'direccion': 'dirección',
            'ciudad_y_o_departamento': 'ciudad de ubicación',
            'matricula': 'matrícula inmobiliaria',
            'municipio_de_registro_orip': 'municipio de registro de la Orip',
            'tipo_ficha_catastral': 'tipo de ficha catastral',
            'numero_ficha_catastral': 'número de ficha catastral',
            # 'linderos_especiales': 'linderos especiales',
        }
        for obligatorio, value in obligatorios.items():
            valor = getattr(self.inmueble, obligatorio)
            if not valor:
                raise ValidationError(f'Dato faltante de inmueble: {value}')
        # TODO revisar linderos especiales

        atributos_inmueble = self.inmueble.__dict__
        Validator.validate_dict(
            atributos_inmueble, dictionary_validator_inmueble, 'Inmueble')

    def validar_parqueaderos(self):
        if len(self.parqueaderos) > 2:
            raise ValidationError('No puede haber más de dos "parqueaderos".')

        obligatorios = {
            'nombre': 'nombre',
            'numero': 'número',
            # 'linderos_especiales': 'linderos especiales'
        }

        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                atributos_parqueaderos = parqueadero.__dict__
                for obligatorio, value in obligatorios.items():
                    valor = getattr(parqueadero, obligatorio)
                    if not valor:
                        raise ValidationError(
                            f'Dato faltante de parqueadero: {value}')
                atributo_nombre_y_numero = {
                    'nombre': atributos_parqueaderos.get('nombre'),
                    'numero': atributos_parqueaderos.get('numero')
                }
                Validator.validate_dict(
                    atributo_nombre_y_numero, dictionary_validator_parqueaderos, 'Parqueaderos')

                if parqueadero.direccion:
                    atributo_direccion = {
                        'direccion': atributos_parqueaderos.get('direccion')
                    }
                    Validator.validate_dict(
                        atributo_direccion, dictionary_validator_direccion, 'Parqueaderos')

                if parqueadero.matricula:
                    matricula = getattr(parqueadero, 'matricula')
                    if not matricula:
                        raise ValidationError(
                            'Dato faltante de parqueadero: matrícula inmobiliaria')
                    atributo_matricula = {
                        'matricula': atributos_parqueaderos.get('matricula')
                    }
                    Validator.validate_dict(
                        atributo_matricula, dictionary_validator_matricula, 'Parqueaderos')

                if parqueadero.tipo_ficha_catastral:
                    atributo_tipo_ficha_catastral = {
                        'tipo_ficha_catastral': atributos_parqueaderos.get('tipo_ficha_catastral')
                    }
                    Validator.validate_dict(
                        atributo_tipo_ficha_catastral, dictionary_validator_tipo_ficha_catastral, 'Parqueaderos')

                if parqueadero.numero_ficha_catastral:
                    ficha_catastral = getattr(
                        parqueadero, 'numero_ficha_catastral')
                    if not ficha_catastral:
                        raise ValidationError(
                            'Dato faltante de parqueadero: número de ficha catastral')
                    atributo_ficha_catastral = {
                        'numero_ficha_catastral': atributos_parqueaderos.get('numero_ficha_catastral')
                    }
                    Validator.validate_dict(
                        atributo_ficha_catastral, dictionary_validator_numero_ficha_catastral, 'Parqueaderos')

    def validar_depositos(self):
        if len(self.depositos) > 2:
            raise ValidationError('No puede haber más de dos "depósitos".')

        obligatorios = {
            'nombre': 'nombre',
            'numero': 'número',
            'linderos_especiales': 'linderos especiales'
        }
        if self.depositos:
            for deposito in self.depositos:
                atributos_parqueaderos = deposito.__dict__
                for obligatorio, value in obligatorios.items():
                    valor = getattr(deposito, obligatorio)
                    if not valor:
                        raise ValidationError(
                            f'Dato faltante de depósito: {value}')

                atributo_nombre_y_numero = {
                    'nombre': atributos_parqueaderos.get('nombre'),
                    'numero': atributos_parqueaderos.get('numero')
                }
                Validator.validate_dict(
                    atributo_nombre_y_numero, dictionary_validator_parqueaderos, 'Depósitos')

                if deposito.direccion:
                    atributo_direccion = {
                        'direccion': atributos_parqueaderos.get('direccion')
                    }
                    Validator.validate_dict(
                        atributo_direccion, dictionary_validator_direccion, 'Depósitos')

                if deposito.matricula:
                    matricula = getattr(deposito, 'matricula')
                    if not matricula:
                        raise ValidationError(
                            'Dato faltante de deposito: matrícula inmobiliaria')
                    atributo_matricula = {
                        'matricula': atributos_parqueaderos.get('matricula')
                    }
                    Validator.validate_dict(
                        atributo_matricula, dictionary_validator_matricula, 'Depósitos')

                if deposito.tipo_ficha_catastral:
                    atributo_tipo_ficha_catastral = {
                        'tipo_ficha_catastral': atributos_parqueaderos.get('tipo_ficha_catastral')
                    }
                    Validator.validate_dict(
                        atributo_tipo_ficha_catastral, dictionary_validator_tipo_ficha_catastral, 'Depósitos')

                if deposito.numero_ficha_catastral:
                    ficha_catastral = getattr(
                        deposito, 'numero_ficha_catastral')
                    if not ficha_catastral:
                        raise ValidationError(
                            'Dato faltante de deposito: número de ficha catastral')
                    atributo_ficha_catastral = {
                        'numero_ficha_catastral': atributos_parqueaderos.get('numero_ficha_catastral')
                    }
                    Validator.validate_dict(
                        atributo_ficha_catastral, dictionary_validator_numero_ficha_catastral, 'Depósitos')

    def estado_civil_es_union(self, estado_civil):
        estados_civiles_union = [
            'Casado con sociedad conyugal vigente',
            'Casado sin sociedad conyugal vigente',
            'Soltero con unión marital de hecho y sociedad patrimonial vigente',
            'Soltero con unión marital de hecho sin sociedad patrimonial vigente'
        ]
        return estado_civil in estados_civiles_union

    def multiples_inmuebles(self):
        inmuebles = 0
        if self.inmueble:
            inmuebles += 1
        if self.parqueaderos:
            inmuebles += len(self.parqueaderos)
        if self.depositos:
            inmuebles += len(self.depositos)
        return inmuebles > 1

    @property
    def cantidad_poderdantes(self):
        return len(self.poderdantes)

    def generar_titulo_documento(self):
        resultado = ''
        resultado += '<title>Minuta</title>'
        resultado += '<div class="titulo"><p>'
        resultado += '<b>---------------------------------'
        resultado += 'CONTRATO DE HIPOTECA---------------------------------</b></p></div>'
        return resultado

    # TODO Pendiente en relación a la escritura, de momento se queda abierto linea 523
    def generar_parrafo_apoderado(self):
        resultado = ''
        resultado += '<div class="parrafos"><p>'
        resultado += f'Presente nuevamente <b><u>{self.apoderado.nombre}</u>,</b> mayor de edad, '
        resultado += f'{self.apoderado.identificado} con <b><u>{self.apoderado.tipo_identificacion}'
        resultado += f'</u></b> No. <b><u>{self.apoderado.numero_identificacion}</u></b> de '
        resultado += f'<b><u>{self.apoderado.ciudad_expedicion_identificacion}</u></b>, quien '
        resultado += 'conforme al Poder General a él otorgado por medio de la __________________ '
        resultado += 'el cual se protocoliza con la presente escritura para los fines legales, '
        resultado += 'cuya vigencia, autenticidad y alcance se hace responsable; actúa en nombre y '
        resultado += 'representación de '
        return resultado

    def generar_parrafo_poderdantes(self):
        resultado = ''
        for index, poderdante in enumerate(self.poderdantes):

            if index == len(self.poderdantes) - \
                    1 and len(self.poderdantes) > 1:
                resultado += ' y '
            resultado += f'<b><u>{poderdante.nombre}</u>,</b> mayor de edad, '
            resultado += f'{poderdante.identificado} con '
            resultado += f'<b><u>{poderdante.tipo_identificacion}</u></b> No. '
            resultado += f'<b><u>{poderdante.numero_identificacion}</u></b> de '
            resultado += f'<b><u>{poderdante.ciudad_expedicion_identificacion}</u>,</b> de '
            resultado += f'estado civil <b><u>{poderdante.estado_civil_genero.upper()}</u>,</b> '
            resultado += f'{poderdante.domiciliado} y {poderdante.residenciado} en '
            resultado += f'<b><u>{poderdante.domicilio}</u></b>'
        if len(self.poderdantes) == 1:
            resultado += '. Quien en el presente contrato se denominará '
        elif len(self.poderdantes) > 1:
            resultado += '. Quienes en el presente contrato se denominarán '
        resultado += '<b>LA PARTE HIPOTECANTE</b> y manifestó: '
        return resultado

    def generar_primero_constitucion_hipoteca(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'los siguientes inmuebles, los cuales se hipotecan'
        else:
            t_inmuebles = 'el siguiente inmueble, el cual se hipoteca'
        resultado = ''
        resultado += '<b>PRIMERO. CONSTITUCIÓN DE HIPOTECA ABIERTA SIN LÍMITE DE CUANTÍA:</b> '
        resultado += 'Que <b>LA PARTE HIPOTECANTE</b> con el propósito de garantizar a '
        resultado += f'<b>“{self.banco.nombre.upper()}”</b>, el pago del crédito de vivienda '
        resultado += 'a largo plazo, que éste le conceda, y ejercitando la facultad prevista '
        resultado += 'en el Artículo 2438 del Código Civil, constituye en favor de '
        resultado += f'<b>“{self.banco.nombre.upper()}”</b>, hipoteca abierta de primer grado '
        resultado += f'sin límite en su cuantía sobre {t_inmuebles} como cuerpo cierto:</p>'
        return resultado

    def generar_direccion_inmueble(self):
        resultado = ''
        resultado += f'<p><b><u>{self.inmueble.nombre.upper()} {self.inmueble.numero.upper()} '
        resultado += f'{self.inmueble.direccion.upper()} '
        resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}</u></b></p>'
        if self.inmueble.linderos_especiales:
            resultado += f'<p>{self.inmueble.linderos_especiales}</p>'
        return resultado

    def generar_direccion_parqueaderos(self):
        resultado = ''
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f'<b><u>{parqueadero.nombre.upper()} {parqueadero.numero} '
                resultado += f'{self.inmueble.direccion.upper()} '
                resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}</u></b>'
                if parqueadero.linderos_especiales:
                    resultado += f'<p>{parqueadero.linderos_especiales}</p>'
        return resultado

    def generar_direccion_depositos(self):
        resultado = ''
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'<b><u>{deposito.nombre.upper()} {deposito.numero} '
                resultado += f'{self.inmueble.direccion.upper()} '
                resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}</u></b>'
                if deposito.linderos_especiales:
                    resultado += f'<p>{deposito.linderos_especiales}</p>'
        return resultado

    def generar_matriculas_inmobiliarias(self):
        if self.parqueaderos or self.depositos:
            if any(parqueadero.matricula or deposito.matricula for parqueadero in self.parqueaderos for deposito in self.depositos):
                inmuebles = 'Inmuebles identificados con los folios de matrículas inmobiliarias'
            else:
                inmuebles = 'Inmueble identificado con el folio de matrícula inmobiliaria'
        else:
            inmuebles = 'Inmueble identificado con el folio de matrícula inmobiliaria'

        matriculas = [self.inmueble.matricula]
        for parqueadero in self.parqueaderos:
            if self.parqueaderos and parqueadero.matricula:
                matriculas += [parqueadero.matricula]
        for deposito in self.depositos:
            if self.depositos and deposito.matricula:
                matriculas += [deposito.matricula]
        resultado = ''
        resultado += f'<p>{inmuebles} No. <b><u>{", ".join(matriculas)}'
        for parqueadero in self.parqueaderos:
            for deposito in self.depositos:
                if parqueadero.matricula or deposito.matricula:
                    resultado += '</u></b> respectivamente'

        resultado += '</u></b> de la Oficina de Registro de Instrumentos Públicos de '
        resultado += f'<b><u>{self.inmueble.municipio_de_registro_orip}</u></b> '
        return resultado

    def generar_fichas_catastrales(self):
        resultado = ''
        if self.inmueble.tipo_ficha_catastral == "Mayor Extensión":
            fichas = getattr(self.inmueble, 'numero_ficha_catastral', None)
            if isinstance(fichas, list) and all(isinstance(ficha, dict) for ficha in fichas):
                resultado += 'y ficha catastral No. <b><u>'
                resultado += ' y '.join(
                    [value for ficha in fichas for value in ficha.values()])
                resultado += ' En Mayor Extensión.</u></b> '
        elif self.inmueble.tipo_ficha_catastral == "Individual":
            if self.parqueaderos or self.depositos:
                if any(parqueadero.numero_ficha_catastral or deposito.numero_ficha_catastral for parqueadero in self.parqueaderos for deposito in self.depositos):
                    resultado += 'y fichas catastrales individuales No. <b><u>'
                else:
                    resultado += 'y ficha catastral individual No. <b><u>'
            else:
                resultado += 'y ficha catastral individual No. <b><u>'

            fichas_catastrales = self.inmueble.numero_ficha_catastral
            resultado += ', '.join([', '.join(ficha.values())
                                   for ficha in fichas_catastrales])
            resultado += '</u></b>'
            if self.parqueaderos or self.depositos:
                resultado += ', '

                if self.parqueaderos:
                    resultado += '<b><u>'
                    resultado += ', '.join([
                        parqueadero.numero_ficha_catastral for parqueadero in self.parqueaderos if parqueadero.numero_ficha_catastral])
                    resultado += '</u></b>'
                if self.depositos:
                    resultado += '<b><u>'
                    resultado += ', '
                    resultado += ', '.join([
                        deposito.numero_ficha_catastral for deposito in self.depositos if deposito.numero_ficha_catastral])
                    resultado += '</u></b>'
            for parqueadero in self.parqueaderos:
                for deposito in self.depositos:
                    if parqueadero.matricula or deposito.matricula:
                        resultado += ' respectivamente.</p>'
                    else:
                        resultado += '</p>'

        return resultado

    # TODO pendiente el tema de las escrituras, de momento se queda abierto linea 643

    def generar_regimen_propiedad_horizontal(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'Los inmuebles objeto de la presente hipoteca fueron sometidos'
        else:
            t_inmuebles = 'El inmueble objeto de la presente hipoteca fue sometido'
        resultado = ''
        resultado += f'<p><b>RÉGIMEN DE PROPIEDAD HORIZONTAL:</b> {t_inmuebles} al régimen '
        resultado += 'legal de propiedad horizontal, de conformidad con la Ley 675 de '
        resultado += 'agosto 3 de 2001 por medio de _______________________________ , '
        resultado += 'debidamente registrada en el Folio de Matrícula Inmobiliaria No. '
        resultado += f'<b><u>{self.inmueble.matricula}</u></b> de la Oficina de Registro '
        resultado += 'de Instrumentos Públicos de <b><u>'
        resultado += f'{self.inmueble.municipio_de_registro_orip}.</u></b></p>'
        return resultado

    def generar_paragrafo_primero(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'a los inmuebles hipotecados'
        else:
            t_inmuebles = 'al inmueble hipotecado'
        resultado = ''
        resultado += '<p><b>PARÁGRAFO PRIMERO:</b> La hipoteca se extiende a muebles que por '
        resultado += f'accesión {t_inmuebles} se reputen inmuebles, a todas las '
        resultado += 'edificaciones, mejoras e instalaciones existentes y a las que llegaren '
        resultado += 'a levantarse o a integrarse a el inmueble en el futuro y se extiende '
        resultado += 'también a las pensiones devengadas por el arrendamiento de los bienes '
        resultado += 'hipotecados y a la indemnización debida por las aseguradoras de este bien, '
        resultado += 'según los artículos 2445 y 2446 del Código Civil. ------<br>'
        return resultado

    def generar_paragrafo_segundo(self):
        resultado = ''
        resultado += '<b>PARÁGRAFO SEGUNDO:</b> El producto inicial del mutuo se destinará '
        resultado += 'de conformidad con la ley 546 de 1999 a la adquisición de vivienda nueva o '
        resultado += 'usada, o la construcción de vivienda individual, o al mejoramiento de esta '
        resultado += 'tratándose de vivienda de interés social. ------<br>'
        return resultado

    def generar_titulo_de_adquisicion(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'los inmuebles dados en garantía hipotecaria fueron adquiridos'
        else:
            t_inmuebles = 'el inmueble dado en garantía hipotecaria fue adquirido'
        resultado = ''
        resultado += f'<b>SEGUNDO: TÍTULO DE ADQUISICIÓN:</b> Que {t_inmuebles} '
        resultado += 'por la PARTE HIPOTECANTE por medio de la presente escritura '
        resultado += 'pública. ------<br>'
        return resultado

    def generar_garantia_de_propiedad_y_libertad(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'dichos inmuebles son'
            han = 'han sido afectados'
            dados = 'dados'
            hallan = 'hallan libres'
        else:
            t_inmuebles = 'dicho inmueble es'
            han = 'ha sido afectado'
            dados = 'dado'
            hallan = 'halla libre'
        resultado = ''
        resultado += '<b>TERCERO: GARANTÍA DE PROPIEDAD Y LIBERTAD:</b> Que garantiza que '
        resultado += f'{t_inmuebles} de su propiedad exclusiva, que no {han} a vivienda '
        resultado += f'familiar, ni {dados} en arrendamiento por escritura pública, '
        resultado += f'ni en anticresis y que se {hallan} de hipotecas, embargos, censos, '
        resultado += 'condiciones resolutorias, registro por demanda civil, servidumbres '
        resultado += 'pasivas, uso o usufructo y cualquier otra clase de gravámenes o '
        resultado += 'desmembraciones; y que se obliga a mantenerlo en este estado por todo '
        resultado += 'el plazo otorgado para el pago de la deuda.<br>'
        return resultado

    def generar_obligaciones_garantizadas(self):
        resultado = ''
        resultado += '<b>CUARTO: OBLIGACIONES GARANTIZADAS:</b> Teniendo en cuenta que la '
        resultado += 'hipoteca constituida en el presente instrumento es de naturaleza abierta '
        resultado += 'y sin límite en la cuantía, garantiza el cumplimiento de todas las '
        resultado += 'obligaciones que <b>LA PARTE HIPOTECANTE</b> conjunta o separadamente '
        resultado += 'haya adquirido o adquiera en el futuro en favor de <b>'
        resultado += f'{self.banco.nombre.upper()}</b>, en los términos y condiciones '
        resultado += 'previstos en los respectivos documentos que contengan las obligaciones '
        resultado += 'principales y accesorias, en razón de contratos de mutuo o por '
        resultado += 'cualquiera otra causa que <b>LA PARTE HIPOTECANTE</b> conjunta o '
        resultado += 'separadamente quede obligado por cualquier concepto; ya sea porque obre '
        resultado += 'exclusivamente en su propio nombre, con otra u otras firmas, en razón de '
        resultado += 'préstamos o créditos de otro orden, o cualquier otro género de obligaciones '
        resultado += 'que consten o estén incorporados en títulos-valores o en cualquier otro '
        resultado += 'documento de carácter comercial o civil, otorgados, girados, avalados, '
        resultado += 'aceptados, endosados, o firmados por <b>LA PARTE HIPOTECANTE</b> '
        resultado += 'conjunta o separadamente, en forma tal que este quede obligado ya sea '
        resultado += 'individual, conjunta o solidariamente con otra u otras personas naturales '
        resultado += f'o jurídicas para con <b>{self.banco.nombre.upper()}. ------</b><br>'
        return resultado

    def generar_paragrafo_primero_aprobacion_de_credito(self):
        number_to_word_hipotecante = num2words(
            self.prestamo.cantidad_banco_a_hipotecante, lang='es')
        number_format_hipotecante = f'{self.prestamo.cantidad_banco_a_hipotecante:,}'

        number_to_word_constructora = num2words(
            self.prestamo.cantidad_dada_a_constructora, lang='es')
        number_format_constructora = f'{self.prestamo.cantidad_dada_a_constructora:,}'

        number_to_word_gastos = num2words(
            self.prestamo.gastos_de_gestion, lang='es')
        number_format_gastos = f'{self.prestamo.gastos_de_gestion:,}'

        if self.multiples_inmuebles():
            t_inmuebles = 'de los bienes inmuebles'
        else:
            t_inmuebles = 'del bien inmueble'
        if self.cantidad_poderdantes > 1:
            deudores = 'los deudores certifican que a la fecha no han'
        elif self.cantidad_poderdantes == 1:
            deudores = 'el deudor certifica que a la fecha no ha'
        resultado = ''
        resultado += '<b>PARÁGRAFO PRIMERO:</b> El crédito inicialmente aprobado por <b>'
        resultado += f'{self.banco.nombre.upper()}</b>, en favor de <b>LA PARTE HIPOTECANTE'
        resultado += f'</b> asciende a la cantidad de <b><u>{number_to_word_hipotecante.upper()} '
        resultado += f'PESOS MCTE (${number_format_hipotecante})</u></b> de los cuales la '
        resultado += f'suma de <b><u>{number_to_word_constructora.upper()} PESOS MCTE ('
        resultado += f'${number_format_constructora})</u></b> corresponden al '
        resultado += f'saldo del precio {t_inmuebles} objeto de esta hipoteca, que desembolsará '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, a la parte vendedora, por cuenta del '
        resultado += 'deudor hipotecante y la diferencia es decir la suma de <b> '
        resultado += f'<u>{number_to_word_gastos.upper()} PESOS MCTE ('
        resultado += f'${number_format_gastos})</u></b> corresponden a los gastos de gestión y '
        resultado += 'trámite del crédito en el exterior que se giran por instrucción del '
        resultado += 'cliente directamente al Bróker. La garantía cubre también toda clase '
        resultado += 'de obligaciones que <b>LA PARTE HIPOTECANTE</b> conjunta o '
        resultado += 'separadamente contraiga en el futuro en favor de <b>'
        resultado += f'{self.banco.nombre}</b>, conforme a lo ya expresado en esta cláusula '
        resultado += 'y a lo establecido en la cláusula séptima y décima de esta hipoteca. '
        resultado += 'Esta liquidación es con el fin de determinar los derechos notariales y '
        resultado += 'de registro de la presente hipoteca. Adicionalmente, para dar '
        resultado += 'cumplimiento a lo ordenado por el artículo 58 de la ley 788 de 2002, '
        resultado += f'{deudores} recibido desembolsos efectivos de créditos que estén '
        resultado += ' garantizados con la presente hipoteca. Es decir, que el desembolso '
        resultado += 'es cero (0). ----------<br>------<br>'
        return resultado

    def generar_paragrafo_segundo_prestamos(self):
        resultado = ''
        resultado += '<b>PARÁGRAFO SEGUNDO:</b> La entrega del(los) préstamo(s) se hará '
        resultado += 'de acuerdo con las disponibilidades de tesorería de <b> '
        resultado += f'{self.banco.nombre.upper()}</b> y el(los) contrato(s) de mutuo '
        resultado += 'constará(n) en el(los) documento(s) que contenga(n) la(s) '
        resultado += 'obligación(es). ------<br>'
        return resultado

    def generar_paragrafo_tercero_no_se_extingue_hipoteca(self):
        resultado = ''
        resultado += '<b>PARÁGRAFO TERCERO:</b> La hipoteca no se extingue por el hecho de '
        resultado += 'ampliarse, cambiarse o renovarse la obligación u obligaciones '
        resultado += 'garantizadas por ella. La hipoteca garantiza y se extiende a cualquier '
        resultado += 'saldo a cargo de <b>LA PARTE HIPOTECANTE,</b> sea que provenga de '
        resultado += 'capital o de intereses gastos, comisiones, etc. ------<br>'
        return resultado

    def generar_quinto_aceleracion_del_plazo(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
            inmuebles_hipotecados = f'{inmuebles} hipotecados son perseguidos'
            inmuebles_desmejoran = f'{inmuebles} mismos desmejoran o sufren desprecios tales que no lleguen'
            inmuebles_determinan = f'{inmuebles} que se determinan en el presente contrato son gravados'
        else:
            inmuebles = 'el inmueble'
            inmuebles_hipotecados = f'{inmuebles} hipotecado es perseguido'
            inmuebles_desmejoran = f'{inmuebles} mismo desmejora o sufre desprecio tal que no llegue'
            inmuebles_determinan = f'{inmuebles} que se determina en el presente contrato es gravado'

        if self.cantidad_poderdantes > 1:
            hipotecantes = 'Lo hipotecantes enajenan'
        elif self.cantidad_poderdantes == 1:
            hipotecantes = 'El hipotecante enajena'

        resultado = ''
        resultado += '<b>QUINTO. ACELERACIÓN DEL PLAZO:</b> Que <b> LA PARTE HIPOTECANTE</b> '
        resultado += f'reconoce y acepta el derecho de <b>{self.banco.nombre.upper()}</b> '
        resultado += 'para declarar por sí mísma y unilateralmente extinguido el plazo de la '
        resultado += 'deuda y para exigir de inmediato el pago de la totalidad de ella, con '
        resultado += 'intereses, accesorios, costas, gastos y honorarios de cobranzas judicial '
        resultado += 'en los casos en que hubiere lugar, en cualquiera de los casos que siguen: '
        resultado += '1. Si <b>LA PARTE HIPOTECANTE</b> no atiende o incumple las obligaciones '
        resultado += 'que contrae según esta escritura, o las que contraiga conjunta o '
        resultado += f'separadamente a favor de <b>{self.banco.nombre.upper()}</b>, de acuerdo '
        resultado += 'con los documentos o títulos-valores respectivos; o no satisface las '
        resultado += ' cuotas de amortización o los intereses en los términos previstos en los '
        resultado += f'documentos respectivos; 2. Si {inmuebles_hipotecados} en '
        resultado += 'todo o en parte por un tercero o en ejercicio de cualquier acción legal; 3. '
        resultado += f'Si {inmuebles_desmejoran} a ser garantía suficiente del crédito, a juicio '
        resultado += f'de un perito que designe <b>{self.banco.nombre.upper()}</b>, 4. Si '
        resultado += f'{inmuebles_determinan} con hipoteca(s) distinta(s) a la(s) constituida(s) '
        resultado += 'mediante esta escritura, sin previo, expreso y escrito consentimiento de '
        resultado += f'<b>{self.banco.nombre.upper()}</b>; 5. Si {hipotecantes} en '
        resultado += f'todo o en parte {inmuebles} sin consentimiento previo, expreso y escrito de '
        resultado += f'<b>{self.banco.nombre.upper()}</b>; 6. <b>LA PARTE HIPOTECANTE</b> hubiere '
        resultado += 'invertido la suma adeudada en forma diversa a la disposición legal que '
        resultado += 'autoriza la línea de crédito; 7. Por inexactitud o falsedad en los '
        resultado += 'documentos en virtud de los cuales se haya obtenido la adjudicación del '
        resultado += 'crédito. ------<br> <b>PARÁGRAFO:</b> En todos los casos y para todos los '
        resultado += 'efectos, será suficiente prueba de incumplimiento el simple dicho al '
        resultado += f'respecto del representante legal de <b>{self.banco.nombre.upper()}</b>, '
        resultado += 'por lo que se puede hacer efectiva la responsabilidad de <b>LA PARTE '
        resultado += 'HIPOTECANTE</b> y la garantía hipotecaria con sólo presentar el o los '
        resultado += 'títulos insolutos que se quieran hacer efectivos y copia de la presente '
        resultado += 'escritura, sin necesidad de requerimiento judicial alguno. ------<br>'
        return resultado

    def generar_sexto_cesion_de_credito(self):
        if self.multiples_inmuebles():
            inmuebles = 'de los inmuebles'
        else:
            inmuebles = 'del inmueble'
        resultado = ''
        resultado += '<b>SEXTO: CESIÓN DE CRÉDITO Y GARANTÍA:</b> Que <b>LA PARTE HIPOTECANTE</b> '
        resultado += 'acepta desde ahora, con todas las consecuencias señaladas en la ley sin '
        resultado += 'necesidad de notificación alguna, en cuanto la ley lo permita, cualquier '
        resultado += f'endoso o traspaso que <b>{self.banco.nombre.upper()}</b> haga de las '
        resultado += 'obligaciones amparadas con esta u otras garantías, de la garantía misma y de '
        resultado += f'los contratos que celebre con relación a la administración {inmuebles}. '
        resultado += 'Igualmente, la hipoteca podrá ser cedida a petición de <b>LA PARTE '
        resultado += 'HIPOTECANTE</b>, a favor de otra entidad financiera, para tal efecto '
        resultado += f'<b>{self.banco.nombre.upper()}</b> autorizará la cesión de la hipoteca, '
        resultado += 'una vez <b>LA PARTE HIPOTECANTE</b> entrega la oferta vinculante del '
        resultado += 'nuevo acreedor. ------<br>'
        return resultado

    def generar_septimo_costos_y_gastos_judiciales(self):
        resultado = ''
        resultado += '<b>SÉPTIMO. COSTAS Y GASTOS JUDICIALES:</b> Que serán de cargo de '
        resultado += '<b>LA PARTE HIPOTECANTE</b> el valor de las costas y gastos judiciales '
        resultado += 'a que hubiere lugar, agencias en derecho, honorarios de abogados que en '
        resultado += f'nombre de <b>{self.banco.nombre.upper()}</b>, promuevan la acción o las '
        resultado += 'acciones para obtener el recaudo del crédito, seguros, impuestos, cuotas '
        resultado += 'de administración, contribuciones de valorización, cuentas de servicios '
        resultado += 'públicos, y en general todos aquellos gastos en que tenga que incurrir '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, por incumplimiento de sus '
        resultado += 'obligaciones, los del otorgamiento y registro de esta escritura; los de '
        resultado += 'cancelación de la hipoteca en su oportunidad; los de expedición de una '
        resultado += 'primera copia registrada de este contrato con mérito ejecutivo y los de '
        resultado += 'expedición de un Certificado de Libertad y Propiedad en que conste la '
        resultado += 'anotación del gravamen hipotecario aquí constituido, documentos éstos '
        resultado += f'destinados a <b>{self.banco.nombre.upper()}</b> y que <b>LA PARTE '
        resultado += 'HIPOTECANTE</b> se obliga a entregar en sus dependencias como previo e '
        resultado += 'indispensable requisito para el perfeccionamiento del crédito o créditos '
        resultado += 'que le vaya a conceder. ------<br>'
        resultado += '<b>PARÁGRAFO:</b> Que <b>LA PARTE HIPOTECANTE</b> se obliga a pagar a '
        resultado += f'<b>{self.banco.nombre.upper()}</b> todos los gastos que se generen desde '
        resultado += 'el estudio hasta el perfeccionamiento del crédito o créditos que le haya '
        resultado += 'otorgado o le otorgue en el futuro tales como la totalidad de impuesto de '
        resultado += 'timbre de conformidad con la ley, el estudio de títulos, visitas que le '
        resultado += f'sean facturadas por <b>{self.banco.nombre.upper()}</b>, etc------<br>'
        return resultado

    def generar_octavo_secuestre(self):
        resultado = ''
        resultado += '<b>OCTAVO. SECUESTRE:</b> Que en caso de acción judicial <b>LA PARTE '
        resultado += 'HIPOTECANTE</b> se adhiere al nombramiento del secuestre que haga '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, de acuerdo con lo establecido en '
        resultado += ' el numeral 4°, literal D, del artículo cuarenta y ocho (48°) del Código '
        resultado += 'General del Proceso; y renuncia al derecho establecido en el parágrafo 2 '
        resultado += 'del artículo 444 del mismo Código. ------<br>'
        return resultado

    def generar_noveno_vigencia_de_hipoteca(self):
        resultado = ''
        resultado += '<b>NOVENO. VIGENCIA DE LA HIPOTECA:</b> Que la hipoteca aquí constituida '
        resultado += f'estará vigente mientras <b>{self.banco.nombre.upper()}</b> no la cancele, '
        resultado += 'y mientras exista a su favor y a cargo de <b>LA PARTE HIPOTECANTE '
        resultado += '</b> conjunta o separadamente cualquier obligación pendiente y sin '
        resultado += 'solucionar de manera total o parcial, sea que provenga de capital o de '
        resultado += 'intereses, gastos, costos, comisiones, etc. <b>LA PARTE HIPOTECANTE</b> '
        resultado += 'tendrá derecho a que se cancele la hipoteca en cualquier momento en que '
        resultado += f'esté a paz y salvo con <b>{self.banco.nombre.upper()}</b>, por todo '
        resultado += 'concepto siempre que esta así lo certifique por escrito, y en ningún caso '
        resultado += 'la hipoteca se extinguirá sino mediante cancelación expresa y por escrito '
        resultado += f'que haga <b>{self.banco.nombre.upper()}</b>------<br>'
        return resultado

    def generar_decimo_seguros(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
            inmuebles_hipotecados = f'{inmuebles} hipotecados'
            inmuebles_asegurados = f'asegurados {inmuebles}'
        else:
            inmuebles = 'el inmueble'
            inmuebles_hipotecados = f'{inmuebles} hipotecado'
            inmuebles_asegurados = f'asegurado {inmuebles}'
        resultado = ''
        resultado += '<b>DÉCIMO. SEGUROS:</b> Que <b>LA PARTE HIPOTECANTE</b> se obliga a '
        resultado += f'contratar en favor de <b>{self.banco.nombre.upper()}</b> un seguro de '
        resultado += 'vida y un seguro de incendio y terremoto o todo riesgo en construcción '
        resultado += f'por {inmuebles_hipotecados} en un plazo máximo de treinta (30) días'
        resultado += ' contados a partir de la fecha de aprobación del crédito y se obliga a '
        resultado += f'mantener dichos seguros en favor de <b>{self.banco.nombre.upper()}</b> por '
        resultado += 'todo el tiempo de duración de la deuda en las siguientes condiciones: El '
        resultado += 'seguro de incendio y terremoto se tomará por el valor comercial '
        resultado += f'{inmuebles}, el seguro de vida se tomará por una cantidad no inferior al '
        resultado += 'valor aprobado y se obliga a mantenerlo por una cantidad no inferior al '
        resultado += 'saldo total de la deuda, y en caso del seguro de todo riesgo en construcción '
        resultado += 'se tomará por el valor del proyecto. Los seguros deberán tomarse con un '
        resultado += 'índice variable que periódicamente señale <b>'
        resultado += f'{self.banco.nombre.upper()}</b> Todo lo anterior dentro de las pólizas '
        resultado += f'globales establecidas por <b>{self.banco.nombre.upper()}</b>, o '
        resultado += 'individualmente tomados según sea el caso, dentro de la libertad que tiene '
        resultado += 'el(los) deudor(es) de asegurar el bien hipotecado con la Compañía de seguros '
        resultado += 'que escoja, con la cobertura y demás condiciones exigidas por '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, según sea el caso, para que en el '
        resultado += 'evento de muerte o siniestro el monto de la indemnización se aplique '
        resultado += 'preferencialmente a la deuda, y el exceso, si lo hubiere, se entregue a '
        resultado += '</b> Que <b>LA PARTE HIPOTECANTE</b> o a sus causahabientes, sobre este '
        resultado += 'punto, se aplicará además el Art.1101 del Código del Comercio. Si <b>LA '
        resultado += 'PARTE HIPOTECANTE</b> no cumple con esta obligación <b> '
        resultado += f'{self.banco.nombre.upper()}</b> queda autorizada desde ahora para hacerlo '
        resultado += 'por su cuenta y para cargarle el valor de las primas de seguro, pudiendo '
        resultado += 'aplicar preferencialmente cualquier abono al pago de dichos seguros. Es '
        resultado += f'entendido que la obligación de mantener {inmuebles_asegurados} y la(s) '
        resultado += 'vida(s) de <b>LA PARTE HIPOTECANTE</b> es por cuenta de este; en caso de que '
        resultado += 'no lo haga, no implica, en ningún caso, ni en forma alguna, responsabilidad '
        resultado += f'para <b>{self.banco.nombre.upper()}</b>, quien puede o no hacer uso de la '
        resultado += 'facultad consignada en esta misma cláusula. ------<br>'
        resultado += '<b>PARÁGRAFO PRIMERO. LA PARTE HIPOTECANTE</b> cede a <b> '
        resultado += f'{self.banco.nombre.upper()}</b>, el valor del monto de la '
        resultado += 'indemnización que llegare a pagar la compañía de seguros hasta la cantidad '
        resultado += 'que fuere necesaria para cubrirle, en caso de siniestro, el saldo pendiente '
        resultado += 'de la deuda. ------<br>'
        resultado += '<b>PARÁGRAFO SEGUNDO.</b> Durante la vigencia de la presente obligación, '
        resultado += '<b>LA PARTE HIPOTECANTE</b> se obliga para con <b>'
        resultado += f'{self.banco.nombre.upper()}</b> a aportar anualmente los certificados de '
        resultado += 'tradición de los inmuebles objeto de la presente hipoteca y en caso de no '
        resultado += f'aportarlo, autoriza a <b>{self.banco.nombre.upper()}</b> a solicitarlos '
        resultado += 'a cargo de <b>LA PARTE HIPOTECANTE</b> sin que esto lo exima de la '
        resultado += 'responsabilidad. ------<br>'
        return resultado

    def generar_decimo_primero_convenio(self):
        resultado = '<b>DÉCIMO PRIMERO. CONVENIO:</b> Que ni la constitución de la hipoteca '
        resultado += 'anterior, ni la firma de esta escritura, obligan a <b> '
        resultado += f'{self.banco.nombre.upper()}</b> a la entrega de sumas de dinero, ni '
        resultado += 'a la promesa o compromiso de celebrar ningún contrato,ni al '
        resultado += 'perfeccionamiento del contrato de mutuo, el cual solo se perfecciona '
        resultado += 'con la entrega del crédito, por ser el mutuo un contrato real, siendo '
        resultado += 'estas operaciones materia de convenio entre las partes, que estarán '
        resultado += 'representadas en documentos separados, que deberán ser firmados para '
        resultado += 'el perfeccionamiento del crédito por <b>LA PARTE HIPOTECANTE</b>, los '
        resultado += 'codeudores y avalistas correspondientes. Como consecuencia de lo '
        resultado += 'anterior, <b>LA PARTE HIPOTECANTE</b> reconoce expresamente que '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, no está obligada a dar o a '
        resultado += 'entregar suma alguna en virtud del presente documento. Si en el '
        resultado += 'lapso entre la aprobación del crédito y su probable perfeccionamiento, '
        resultado += f'<b>{self.banco.nombre.upper()}</b> conoce de hechos sucedidos antes '
        resultado += 'o después de aquella, los cuales la hubieren impedido aprobar '
        resultado += 'el crédito, podrá darlo por desistido.<br>'
        resultado += '<b>PARÁGRAFO.</b> Con la constitución de la presente hipoteca se '
        resultado += ' garantizan exclusivamente los créditos ya otorgados o los que '
        resultado += f'voluntariamente quiera otorgarle(s) <b>{self.banco.nombre.upper()}'
        resultado += '</b>, comprendiendo además los intereses, costas, gastos, seguros, '
        resultado += 'comisiones, etc. ------<br>'
        return resultado

    def generar_decimo_segundo_poder(self):
        resultado = ''
        resultado += '<b>DÉCIMO SEGUNDO. PODER:</b> Que, en caso de pérdida o '
        resultado += 'destrucción de la primera copia para exigir mérito ejecutivo, '
        resultado += 'el (los) comparecientes mediante este mismo instrumento confieren '
        resultado += 'poder especial hasta la cancelación total del crédito, al '
        resultado += f'representante legal o apoderado de <b>{self.banco.nombre.upper()}</b> '
        resultado += 'para solicitar al señor Notario mediante escritura pública, se sirva '
        resultado += 'compulsar una copia substitutiva con igual mérito. ------<br>'
        return resultado

    def generar_decimo_tercero_inputacion_de_pago(self):
        resultado = ''
        resultado += '<b>DÉCIMO TERCERO. IMPUTACIÓN DE PAGO.</b> Cualquier pago que hiciera '
        resultado += f'<b>LA PARTE HIPOTECANTE</b> a <b>{self.banco.nombre.upper()}</b> '
        resultado += 'se imputará de la siguiente manera: 1) Pólizas de incendio, terremoto '
        resultado += 'y vida, 2) Garantía del Fondo Nacional de Garantías, 3) Impuestos y/o '
        resultado += 'valorizaciones a que haya lugar 4) Intereses de mora, si los hubiere. '
        resultado += '5) Intereses corrientes. 6) Comisiones. 7) Gastos para el recobro de '
        resultado += 'la obligación. 8) A capital y, por último, 9) Al prepago de la '
        resultado += ' obligación. ------<br>'
        return resultado

    # TODO Agregar datos de escritura linea 1030
    def generar_datos_apoderado_banco(self):
        resultado = ''
        nombre = self.apoderado_banco.nombre.upper()
        ciudad_residencia = self.apoderado_banco.ciudad_residencia
        tipo_identificacion = self.apoderado_banco.tipo_identificacion
        numero_identificacion = self.apoderado_banco.numero_identificacion
        ciudad_expedicion_identificacion = self.apoderado_banco.ciudad_expedicion_identificacion
        tipo_apoderado = self.apoderado_banco.tipo_apoderado
        tipo_poder = self.apoderado_banco.tipo_poder
        naturaleza = self.apoderado_banco.naturaleza
        vecino = self.apoderado_banco.vecino
        identificado = self.apoderado_banco.identificado
        doctor = self.apoderado_banco.doctor

        resultado += f'Presente {doctor}, <u><b>{nombre}, '
        resultado += f'</b></u>{naturaleza}, mayor de edad, {vecino} de <u><b>'
        resultado += f'{ciudad_residencia}</b></u> {identificado} con '
        resultado += f'<u><b>{tipo_identificacion}</b></u> No. '
        resultado += f'<u><b>{numero_identificacion}</b></u> de '
        resultado += f'<u><b>{ciudad_expedicion_identificacion}</b>'
        resultado += '</u> quien comparece en este acto en su calidad de '
        resultado += f'<u><b>{self.apoderado_banco.apoderado} {tipo_apoderado}</b>'
        resultado += '</u> acorde con el Poder '
        if self.apoderado_banco.tipo_poder == 'Autenticado':
            resultado += 'a ella conferido por '
        elif self.apoderado_banco.tipo_poder == 'Escriturado':
            resultado += 'constituido por '
            resultado += f'<u><b>{tipo_poder}</b></u> debidamente inscrito en '
            resultado += 'la Cámara de Comercio de Cali según certificado de la Existencia '
            resultado += 'Representación legal que se protocoliza con este instrumento, '
            resultado += 'conferido por '

        return resultado

    def generar_datos_representante_banco(self):
        resultado = ''
        nombre = self.representante_banco.nombre.upper()
        ciudad_residencia = self.representante_banco.ciudad_residencia
        tipo_identificacion = self.representante_banco.tipo_identificacion
        numero_identificacion = self.representante_banco.numero_identificacion
        ciudad_expedicion_identificacion = self.representante_banco.ciudad_expedicion_identificacion
        tipo_representante = self.representante_banco.tipo_representante
        doctor = self.representante_banco.doctor
        vecino = self.representante_banco.vecino
        identificado = self.representante_banco.identificado

        resultado += f'{doctor} <u><b>{nombre},</b></u> mayor de edad, {vecino} de '
        resultado += f'<u><b>{ciudad_residencia},</b></u> {identificado} con '
        resultado += f'<u><b>{tipo_identificacion}</b></u> No. '
        resultado += f'<u><b>{numero_identificacion}</b></u> de '
        resultado += f'<u><b>{ciudad_expedicion_identificacion},</b></u> '
        resultado += 'quien comparece en este acto en calidad de '
        resultado += f'<u><b>{tipo_representante}</b></u> '

        return resultado

    def generar_constitucion_banco_union(self):
        resultado = ''
        resultado += f'de <b>{self.banco.nombre.upper()}</b> antes <b>GIROS & FINANZAS COMPAÑÍA DE '
        resultado += 'FINANCIAMIENTO S.A.</b>, sociedad constituida legalmente mediante Escritura '
        resultado += 'Escritura Pública No. 5938 del 05 de diciembre de 1963, otorgada en la '
        resultado += 'Notaria Cuarta (04) del Círculo de Bogotá, inscrita en la Cámara de '
        resultado += 'Comercio de Cali, el 7 de noviembre de 2000, bajo el número 7516 del Libro '
        resultado += 'IX, sociedad convertida a establecimiento Bancario y modificada su razón '
        resultado += 'social mediante Escritura Pública No. 3140 del 16 de Junio de 2022, otorgada '
        resultado += 'en la Notaría Cuarta del Círculo de Cali, inscrita en la Cámara de Comercio '
        resultado += 'de Cali el 28 de Junio de 2022, bajo el No. 12001 del Libro IX, entidad '
        resultado += 'vigilada por la Superintendencia Financiera, con permiso de funcionamiento '
        resultado += 'otorgado mediante Resolución número 549 del 31 de mayo de 2022, todo lo cual '
        resultado += 'se acredita con el Certificado de Existencia y Representación Legal '
        resultado += 'expedido por la Cámara de Comercio de Cali, y manifestó: Que acepta la '
        resultado += 'presente escritura por estar de acuerdo con todo lo expresado en ella, '
        resultado += 'especialmente la hipoteca que a favor de '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, se constituye por el presente '
        resultado += 'instrumento.<br>'
        resultado += '---------------------------------------------------------------------'
        resultado += '--------------------------------------<br>'
        return resultado

    def generar_aprobacion_credito_al_hipotecante(self):
        number_to_word_hipotecante = num2words(
            self.prestamo.cantidad_banco_a_hipotecante, lang='es')
        number_format_hipotecante = f'{self.prestamo.cantidad_banco_a_hipotecante:,}'
        resultado = ''
        resultado += 'Para dar cumplimiento a lo ordenado en la Resolución No. 00536 del 22 de '
        resultado += 'Enero de 2021, aclarada por Resolución 0545 del 25 de Enero de 2021 '
        resultado += 'proferida por la Superintendencia de Notariado y Registro, se adjunta con '
        resultado += f'esta escritura la carta expedida por <b>"{self.banco.nombre.upper()}"</b>, '
        resultado += 'donde aprueba un crédito al Hipotecante por la suma de '
        resultado += f'<b><u>{number_to_word_hipotecante.upper()} PESOS MCTE '
        resultado += f'(${number_format_hipotecante})</u></b>, la misma que '
        resultado += 'tomará el Notario para la liquidación de los derechos notariales. ---------'
        resultado += '------------------------------------------------------------------<br>'
        return resultado

    def generar_afectacion_vivienda_familiar(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles que hipotecan'
        else:
            inmuebles = 'el inmueble que hipoteca'
        resultado = ''
        resultado += '<b>APLICACIÓN A LA LEY 0258 de 1996: AFECTACIÓN A VIVIENDA FAMILIAR:</b> '
        resultado += 'A continuación, el(la) notario(a) interroga bajo juramento a '
        resultado += f'{self.apoderado.apoderado} de <b>LA PARTE HIPOTECANTE</b>, si '
        resultado += f'{inmuebles} por el presente Instrumento se encuentra Afectado al '
        resultado += 'Régimen de Vivienda Familiar, a lo que responde: <b>NO.</b> '
        resultado += f'El Notario deja constancia que {inmuebles} <b>NO</b> se afecta a vivienda '
        resultado += 'familiar por NO reunir los requisitos de Ley.'
        resultado += '-------------------------------------<br>'
        return resultado

    def generar_lectura_escritura_por_otorgantes(self):
        resultado = ''
        resultado += 'Leída la presente escritura por los otorgantes, la aceptan, la aprueban y '
        resultado += 'la firman por ante mí el Notario, que de lo expuesto doy fé, advertidos de '
        resultado += 'las formalidades legales del registro, dentro del término perentorio de dos '
        resultado += '(2) meses contados a partir de la fecha de otorgamiento de este instrumento, '
        resultado += 'cuyo incumplimiento causará intereses moratorios por mes o fracción de mes '
        resultado += 'de retardo, de acuerdo al Artículo 231 de la Ley 233 de Diciembre 20 de '
        resultado += '1995; lo encontraron conforme a su pensamiento y voluntad y por no '
        resultado += 'observarse error alguno en su contenido le imparten su aprobación y proceden '
        resultado += 'a firmarlo con el suscrito Notario, que da fe, declarando los comparecientes '
        resultado += 'estar enterados de que un error no corregido en esta escritura antes de ser '
        resultado += 'firmada, da lugar a una Escritura Aclaratoria que conlleva nuevos gastos '
        resultado += 'para los contratantes, conforme manda el Artículo 102 del Decreto Ley 960 de '
        resultado += '1970, de todo lo cual se dan por enterados y firman en constancia. '
        resultado += 'Derechos $ Decreto 1681 Septiembre 16 de 1996. Modificado mediante '
        resultado += 'Resolución No.726 Enero 29 de 2016. Retención en la Fuente $ IVA: $ Recaudos '
        resultado += 'Superintendencia y Fondo de Notariado $ '
        return resultado

    def generar_paz_y_salvo(self):
        resultado = ''
        resultado += 'EXENTOS DE PAZ Y SALVO NACIONAL Decrero 2503 Diciembre 29 de 1987.'
        resultado += 'Se agregan comprobantes. Presentaron PAZ Y SALVO MUNICIPAL No.(s) ________, '
        resultado += 'por concepto de PREDIAL UNIFICADO, a nombre de ______________., '
        resultado += 'PREDIOS GLOBALES: ______________, ubicado(s) En: _________; AVALUO(S):$'
        resultado += '________.oo, de fecha: ______________, válido(s) hasta _______________. '
        resultado += 'Presentaron PAZ Y SALVO(S) de VALORIZACION No.(s):___________, '
        resultado += 'correspondiente al (los) mismo(s) predio(s) y vigente(s) a la fecha. La '
        resultado += 'presente escritura se corrió en las hojas números:<br></div>'
        resultado += '<div class="seccion_firmas">'
        resultado += 'LOS VENDEDORES,<br><br><br> _____________________<br>_________<br>'
        resultado += 'NIT: _____________<br><br><br>'
        return resultado

    def generar_firma_comprador(self):
        resultado = ''
        resultado += 'EL COMPRADOR E HIPOTECANTE<br><br><br><br>'
        resultado += '_______________________________<br>'
        resultado += f'<b>{self.apoderado.nombre.upper()}<br>'
        if self.apoderado.tipo_identificacion == 'Cédula de ciudadanía':
            resultado += 'C.C. '
        elif self.apoderado.tipo_identificacion == 'Cédula de extranjería':
            resultado += 'C.E '
        elif self.apoderado.tipo_identificacion == 'Pasaporte':
            resultado += 'Pasaporte '
        resultado += f'{self.apoderado.numero_identificacion} de '
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion}</b><br>'
        resultado += 'En representación de<br>'
        return resultado

    def generar_firma_hipotecante(self):
        resultado = ''
        for index, poderdante in enumerate(self.poderdantes):
            resultado += f'<b>{poderdante.nombre.upper()}</b><br>'
            if poderdante.tipo_identificacion == 'Cédula de Ciudadanía':
                resultado += '<b>C.C.'
            elif poderdante.tipo_identificacion == 'Cédula de Extranjería':
                resultado += '<b>C.E.'
            elif poderdante.tipo_identificacion == 'Pasaporte':
                resultado += '<b>Pasaporte'
            resultado += f' {poderdante.numero_identificacion} de '
            resultado += f'{poderdante.ciudad_expedicion_identificacion}</b><br><br>'
            if index < len(self.poderdantes) - 1:
                resultado += 'y<br><br>'
        return resultado

    def generar_firma_apoderado_banco(self):
        resultado = ''
        resultado += 'EL ACREEDOR,<br><br><br><br>'
        resultado += '____________________________<br>'
        resultado += f'<b>{self.apoderado_banco.nombre.upper()}<br>'
        resultado += f'{self.apoderado_banco.abreviacion_identificacion} '
        resultado += f'{self.apoderado_banco.numero_identificacion} expedida en '
        resultado += f'{self.apoderado_banco.ciudad_expedicion_identificacion}</b><br>'
        resultado += f'{self.apoderado_banco.apoderado} {self.apoderado_banco.tipo_apoderado} '
        resultado += f'de <br><b>{self.banco.nombre.upper()}<br>'
        resultado += f'NIT. {self.banco.nit}</b><br><br><br><br>'
        resultado += 'LA NOTARÍA.<br><br><br><br>____________________</div>'
        return resultado

    def generar_estilos(self):
        resultado = ''
        resultado += '<style>'
        resultado += 'div.titulo {text-align: center; font-weight: bold; font-size: 17px; '
        resultado += 'font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.parrafos {text-align: justify; font-size: 16px; list-style: '
        resultado += 'lower-alpha; font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.seccion_firmas {font-size: 16px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif;}div.padding {padding-top: 50px; padding-right: 50px; '
        resultado += 'padding-bottom: 30px; padding-left: 50px;}</style>'
        return resultado
