from typing import List

from datetime import datetime
from num2words import num2words
from utils.document import Document
from utils.exceptions import ValidationError
from utils.validators import Validator

from utils.validating_dictionaries.dictionary_apoderado import dictionary_validator_apoderado_compraventa_leasing
from utils.validating_dictionaries.dictionary_poderdantes import dictionary_validator_poderdantes_compraventa_leasing
from utils.validating_dictionaries.dictionary_inmueble import dictionary_validator_inmueble_compraventa_leasing
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_parqueaderos_compraventa_leasing
from utils.validating_dictionaries.dictionary_depositos import dictionary_validator_depositos_compraventa_leasing
from utils.validating_dictionaries.dictionary_apoderado_banco import dictionary_validator_apoderado_banco_compraventa_leasing
from utils.validating_dictionaries.dictionary_representante_banco import dictionary_validator_representante_banco_compraventa_leasing
from utils.validating_dictionaries.dictionary_banco import dictionary_validator_banco_compraventa_leasing
from utils.validating_dictionaries.dictionary_compraventa import dictionary_validator_compraventa_leasing

from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.fechas import MESES_INGLES_ESPANOL

from .apoderado import ApoderadoCompraventaLeasing
from .apoderado_banco import ApoderadoBancoCompraventaLeasing
from .depositos import DepositoCompraventaLeasing
from .inmueble import InmuebleCompraventaLeasing
from .parqueaderos import ParqueaderoCompraventaLeasing
from .poderdantes import PoderdanteCompraventaLeasing
from .representante_banco import RepresentanteBancoPromesaCompraventa
from .banco import BancoCompraventaLeasing
from .compraventa import CompraventaLeasing


class DocumentoCompraventaLeasing(Document):
    apoderado: ApoderadoCompraventaLeasing
    poderdantes: List[PoderdanteCompraventaLeasing]
    inmueble: InmuebleCompraventaLeasing
    depositos: List[DepositoCompraventaLeasing]
    parqueaderos: List[ParqueaderoCompraventaLeasing]
    apoderado_banco: ApoderadoBancoCompraventaLeasing
    representante_banco: RepresentanteBancoPromesaCompraventa
    banco: BancoCompraventaLeasing
    compraventa: CompraventaLeasing

    generate_html_functions = [
        'generar_titulo_documento',
        'generar_datos_inmuebles',
        'generar_matriculas_inmobiliarias_seccion_inicial',
        'generar_fichas_catastrales_seccion_inicial',
        'generar_cuantia',
        'generar_notaria',
        'generar_clausula_objeto',
        'generar_direccion_inmueble',
        'generar_direccion_parqueaderos',
        'generar_direccion_depositos',
        'generar_matriculas_inmobiliarias',
        'generar_fichas_catastrales',
        'generar_paragrafo_primero',
        'generar_paragrafo_tradicion_inmueble',
        'generar_paragrafo_precio',
        'generar_clausula_limitaciones_gravamenes',
        'generar_clausula_obligacion_sanear',
        'generar_clausula_entrega',
        'generar_clausula_gastos_notariales',
        'generar_datos_apoderado_banco',
        'generar_datos_representante_banco',
        'generar_constitucion_banco_union',
        'generar_clausula_banco_aceptacion',
        'generar_clausula_banco_compra',
        'generar_firma_vendedor',
        'generar_firma_locatario',
        'generar_firma_poderdante',
        'generar_firma_comprador',
        'generar_estilos'
    ]

    def __init__(
        self,
        apoderado: ApoderadoCompraventaLeasing,
        poderdantes: List[PoderdanteCompraventaLeasing],
        inmueble: InmuebleCompraventaLeasing,
        parqueaderos: List[ParqueaderoCompraventaLeasing],
        depositos: List[DepositoCompraventaLeasing],
        apoderado_banco: ApoderadoBancoCompraventaLeasing,
        representante_banco: RepresentanteBancoPromesaCompraventa,
        banco: BancoCompraventaLeasing,
        compraventa: CompraventaLeasing
    ):
        self.apoderado = apoderado
        self.poderdantes = poderdantes
        self.inmueble = inmueble
        self.parqueaderos = parqueaderos
        self.depositos = depositos
        self.apoderado_banco = apoderado_banco
        self.representante_banco = representante_banco
        self.banco = banco
        self.compraventa = compraventa
        self.validate_data()

    def validate_data(self):
        self.validar_apoderado()
        self.validar_poderdantes()
        self.validar_inmueble()
        self.validar_parqueaderos()
        self.validar_depositos()
        self.validar_apoderado_banco()
        self.validar_representante_banco()
        self.validar_banco()
        self.validar_compraventa()

    def validar_apoderado(self):
        if self.apoderado:
            atributos_apoderado = self.apoderado.__dict__
            Validator.validate_dict(atributos_apoderado,
                                    dictionary_validator_apoderado_compraventa_leasing,
                                    'Apoderado')

    def validar_poderdantes(self):
        if self.cantidad_poderdantes == 0 and self.cantidad_poderdantes > 2:
            raise ValidationError(
                'Debe haber al menos un poderdante y no más de dos poderdantes.')

    def validar_inmueble(self):
        atributos_inmueble = self.inmueble.__dict__
        Validator.validate_dict(atributos_inmueble,
                                dictionary_validator_inmueble_compraventa_leasing,
                                'Inmueble')

    def validar_parqueaderos(self):
        if len(self.parqueaderos) > 2:
            raise ValidationError('No puede haber más de dos "parqueaderos".')

        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                atributos_parqueaderos = parqueadero.__dict__
            Validator.validate_dict(atributos_parqueaderos,
                                    dictionary_validator_parqueaderos_compraventa_leasing,
                                    'Parqueaderos')

    def validar_depositos(self):
        if len(self.depositos) > 2:
            raise ValidationError('No puede haber más de dos "depósitos".')

        if self.depositos:
            for deposito in self.depositos:
                atributos_depositos = deposito.__dict__
            Validator.validate_dict(atributos_depositos,
                                    dictionary_validator_depositos_compraventa_leasing,
                                    'Depósitos')

    def validar_apoderado_banco(self):
        if self.apoderado_banco.nombre not in [apoderado['nombre'] for apoderado in apoderados_banco]:
            atributos_apoderado_banco = self.apoderado_banco.__dict__
            Validator.validate_dict(atributos_apoderado_banco,
                                    dictionary_validator_apoderado_banco_compraventa_leasing,
                                    'Apoderado del banco')

        for poderdante in self.poderdantes:
            atributos_poderdante = poderdante.__dict__
            Validator.validate_dict(atributos_poderdante,
                                    dictionary_validator_poderdantes_compraventa_leasing,
                                    'Poderdantes')

    def validar_representante_banco(self):
        if self.representante_banco.nombre not in [representante['nombre'] for representante in representantes_banco]:
            atributos_representante_banco = self.representante_banco.__dict__
            Validator.validate_dict(atributos_representante_banco,
                                    dictionary_validator_representante_banco_compraventa_leasing,
                                    'Representante del banco')

    def validar_banco(self):
        if self.banco.nombre not in [banco['nombre'] for banco in bancos]:
            atributos_banco = self.banco.__dict__
            Validator.validate_dict(atributos_banco,
                                    dictionary_validator_banco_compraventa_leasing,
                                    'Banco')

    def validar_compraventa(self):
        atributos_compraventa = self.compraventa.__dict__
        Validator.validate_dict(atributos_compraventa,
                                dictionary_validator_compraventa_leasing,
                                'Compraventa')

    def estado_civil_es_union(self, estado_civil):
        estados_civiles_union = [
            'Casado con sociedad conyugal vigente',
            'Casado sin sociedad conyugal vigente',
            'Soltero con unión marital de hecho y sociedad patrimonial vigente',
            'Soltero con unión marital de hecho sin sociedad patrimonial vigente'
        ]
        return estado_civil in estados_civiles_union

    @property
    def cantidad_poderdantes(self):
        return len(self.poderdantes)

    def multiples_inmuebles(self):
        inmuebles = 0
        if self.inmueble:
            inmuebles += 1
        if self.parqueaderos:
            inmuebles += len(self.parqueaderos)
        if self.depositos:
            inmuebles += len(self.depositos)
        return inmuebles > 1

    def generar_titulo_documento(self):
        resultado = ''
        resultado += '<title>Compraventa Leasing</title>'
        resultado += '<div class="titulo"><p>'
        resultado += '<b>ESCRITURA NÚMERO<br><br>FECHA: ______ DE _______ DEL DOS MIL '
        resultado += 'VEINTITRÉS _______ (2023)<br>***************************<br> OTORGADA '
        resultado += 'ANTE LA NOTARÍA _______ DEL CIRCULO DE ***********************<br>'
        resultado += 'SUPERINTENDENCIA DE NOTARIADO Y REGISTRO<br>FORMATO DE CALIFICACION<br>'
        resultado += 'ACTO O CONTRATO: COMPRAVENTA *****************************<br>'
        resultado += 'PERSONAS QUE INTERVIENEN EN EL ACTO:<br>'
        resultado += 'VENDEDOR: ________________________________________.<br>'
        resultado += 'COMPRADOR:	BANCO UNIÓN********************<br>'
        resultado += ''
        return resultado

    def generar_datos_inmuebles(self):
        if self.multiples_inmuebles():
            inmuebles = 'INMUEBLES'
        else:
            inmuebles = 'INMUEBLE'
        resultado = ''
        resultado += f'{inmuebles}: {self.inmueble.nombre.upper()} {self.inmueble.numero}, '
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f'{parqueadero.nombre} {parqueadero.numero}, '
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'{deposito.nombre} {deposito.numero}, '
        resultado += f'{self.inmueble.direccion}, {self.inmueble.ciudad_y_o_departamento}'
        resultado += '</b></p></div>'
        return resultado

    def generar_matriculas_inmobiliarias_seccion_inicial(self):
        matriculas_presentes = False

        for parqueadero in self.parqueaderos:
            if parqueadero.matricula:
                matriculas_presentes = True
                break

        if not matriculas_presentes:
            for deposito in self.depositos:
                if deposito.matricula:
                    matriculas_presentes = True
                    break

        if matriculas_presentes:
            inmuebles = 'MATRÍCULAS INMOBILIARIAS'
        else:
            inmuebles = 'MATRÍCULA INMOBILIARIA'

        matriculas_parqueaderos = [
            parqueadero.matricula for parqueadero in self.parqueaderos if parqueadero.matricula]
        matriculas_depositos = [
            deposito.matricula for deposito in self.depositos if deposito.matricula]

        matriculas = ', '.join(matriculas_parqueaderos + matriculas_depositos)
        if matriculas:
            matriculas = f'{self.inmueble.matricula}, {matriculas}'
        else:
            matriculas = self.inmueble.matricula
        if ', ' in matriculas:
            matriculas = matriculas.rsplit(', ', 1)
            matriculas = ' y '.join(matriculas)
        resultado = f'<div class="parrafos"><p><b>{inmuebles}: <u>{matriculas}</u></b> '
        if matriculas_presentes:
            resultado += '</u></b> respectivamente '

        resultado += '</u></b> de la Oficina de Registro de Instrumentos Públicos de '
        resultado += f'<b><u>{self.inmueble.municipio_de_registro_orip}</u></b>'
        return resultado

    def generar_fichas_catastrales_seccion_inicial(self):
        resultado = ''
        if self.inmueble.tipo_ficha_catastral == "Mayor Extensión":
            fichas = getattr(self.inmueble, 'numero_ficha_catastral')
            if isinstance(fichas, list) and all(isinstance(ficha, dict) for ficha in fichas):
                resultado += ' y ficha catastral No. <b><u>'
                resultado += ', '.join([', '.join(ficha_values.values())
                                       for ficha_values in fichas[:-1]])
                if len(fichas) > 1:
                    resultado += ' y ' + ', '.join(fichas[-1].values())
                elif len(fichas) == 1:
                    resultado += ', '.join(fichas[-1].values())
                resultado += ' Folio en Mayor Extensión.</u></b> '
        elif self.inmueble.tipo_ficha_catastral == "Individual":
            fichas_presentes = False
            for parqueadero in self.parqueaderos:
                if parqueadero.numero_ficha_catastral:
                    fichas_presentes = True
                    break

            if not fichas_presentes:
                for deposito in self.depositos:
                    if deposito.numero_ficha_catastral:
                        fichas_presentes = True
                        break

            if fichas_presentes:
                resultado += ' y fichas catastrales individuales No. <b><u>'
            else:
                resultado += 'y ficha catastral individual No. <b><u>'

            fichas_catastrales = self.inmueble.numero_ficha_catastral
            resultado += ', '.join([', '.join(ficha.values())
                                   for ficha in fichas_catastrales])
            resultado += '</u></b>'

            if any(parqueadero.numero_ficha_catastral for parqueadero in self.parqueaderos if parqueadero.numero_ficha_catastral) or any(deposito.numero_ficha_catastral for deposito in self.depositos if deposito.numero_ficha_catastral):
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

    def generar_cuantia(self):
        number_to_word_leasing = num2words(
            self.compraventa.cantidad_compraventa, lang='es')
        number_format_leasing = f'{self.compraventa.cantidad_compraventa:,}'
        resultado = ''
        resultado += f'<p><b>CUANTÍA: {number_to_word_leasing.upper()} PESOS MCTE '
        resultado += f'(${number_format_leasing}).</b></p>'
        return resultado

    def generar_notaria(self):
        resultado = ''
        resultado += '<p>En la ciudad de _______, capital del Departamento de ___________, '
        resultado += 'a los ________ ( ) días del mes de ______ del año dos mil _______ '
        resultado += '(__________), ante mí, ________________ <b> NOTARÍA PÚBLICA NÚMERO '
        resultado += '___________ DEL CIRCULO DE ________,</b> comparecieron los '
        resultado += 'señores _______________________, mayores de edad, identificados con '
        resultado += 'las Cédulas de ciudadanía número ________________, respectivamente, '
        resultado += 'de estado civil _____________, hábiles para contratar y obligarse, '
        resultado += 'actuando en sus propios nombres, manifestaron:</p'
        return resultado

    def generar_clausula_objeto(self):
        if self.multiples_inmuebles():
            inmuebles = 'los siguientes inmuebles'
        else:
            inmuebles = 'el siguiente inmueble'
        resultado = ''
        resultado += '<b>PRIMERO:  Objeto:</b> Que por el presente Instrumento público '
        resultado += 'transfiere a título de venta real y enajenación perpetua a favor de '
        resultado += f'{self.banco.nombre.upper()}, acorde con la cesión de la posición '
        resultado += 'contractual en el contrato de promesa de compraventa suscrito el '
        resultado += '_________________, mismo que se protocoliza con la presente escritura'
        resultado += f', el dominio y la posesión que tienen y ejerce sobre {inmuebles}:'
        resultado += '<br><br><br>'
        return resultado

    def generar_direccion_inmueble(self):
        resultado = f'<p><b><u>{self.inmueble.nombre.upper()} {self.inmueble.numero.upper()}, '
        resultado += f'{self.inmueble.direccion.upper()}, '
        resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}.</u></b></p>'
        if self.inmueble.linderos_especiales:
            resultado += f'<p>{self.inmueble.linderos_especiales}</p>'
        else:
            resultado += '<br><br>'
        return resultado

    def generar_direccion_parqueaderos(self):
        resultado = ''
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado = f'<b><u>{parqueadero.nombre.upper()} {parqueadero.numero}, '
                resultado += f'{parqueadero.direccion.upper()}.</u></b>'
                if parqueadero.linderos_especiales:
                    resultado += f'<p>{parqueadero.linderos_especiales}</p>'
                else:
                    resultado += '<br><br>'
        return resultado

    def generar_direccion_depositos(self):
        resultado = ''
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'<b><u>{deposito.nombre.upper()} {deposito.numero}, '
                resultado += f'{deposito.direccion.upper()}.</u></b>'
                if deposito.linderos_especiales:
                    resultado += f'<p>{deposito.linderos_especiales}</p>'
                else:
                    resultado += '<br><br>'
        return resultado

    def generar_matriculas_inmobiliarias(self):
        matriculas_presentes = False

        for parqueadero in self.parqueaderos:
            if parqueadero.matricula:
                matriculas_presentes = True
                break

        if not matriculas_presentes:
            for deposito in self.depositos:
                if deposito.matricula:
                    matriculas_presentes = True
                    break

        if matriculas_presentes:
            inmuebles = 'Inmuebles identificados con los folios de matrículas inmobiliarias'
        else:
            inmuebles = 'Inmueble identificado con el folio de matrícula inmobiliaria'

        matriculas_parqueaderos = [
            parqueadero.matricula for parqueadero in self.parqueaderos if parqueadero.matricula]
        matriculas_depositos = [
            deposito.matricula for deposito in self.depositos if deposito.matricula]

        matriculas = ', '.join(matriculas_parqueaderos + matriculas_depositos)
        if matriculas:
            matriculas = f'{self.inmueble.matricula}, {matriculas}'
        else:
            matriculas = self.inmueble.matricula
        if ', ' in matriculas:
            matriculas = matriculas.rsplit(', ', 1)
            matriculas = ' y '.join(matriculas)
        resultado = f'{inmuebles} No. <b><u>{matriculas}</u></b> '
        if matriculas_presentes:
            resultado += '</u></b> respectivamente '

        resultado += '</u></b> de la Oficina de Registro de Instrumentos Públicos de '
        resultado += f'<b><u>{self.inmueble.municipio_de_registro_orip.upper()}</u></b>'
        return resultado

    def generar_fichas_catastrales(self):
        resultado = ''
        if self.inmueble.tipo_ficha_catastral == "Mayor Extensión":
            fichas = getattr(self.inmueble, 'numero_ficha_catastral')
            if isinstance(fichas, list) and all(isinstance(ficha, dict) for ficha in fichas):
                resultado += ' y ficha catastral No. <b><u>'
                resultado += ', '.join([', '.join(ficha_values.values())
                                       for ficha_values in fichas[:-1]])
                if len(fichas) > 1:
                    resultado += ' y ' + ', '.join(fichas[-1].values())
                elif len(fichas) == 1:
                    resultado += ', '.join(fichas[-1].values())
                if self.inmueble.numero_chip:
                    resultado += f'<b><u> y CHIP {self.inmueble.numero_chip}'
                resultado += ' Folio de Mayor Extensión.</u></b> '
        elif self.inmueble.tipo_ficha_catastral == "Individual":
            fichas_presentes = False
            for parqueadero in self.parqueaderos:
                if parqueadero.numero_ficha_catastral:
                    fichas_presentes = True
                    break

            if not fichas_presentes:
                for deposito in self.depositos:
                    if deposito.numero_ficha_catastral:
                        fichas_presentes = True
                        break

            if fichas_presentes:
                resultado += ' y fichas catastrales individuales No. <b><u>'
            else:
                resultado += 'y ficha catastral individual No. <b><u>'

            fichas_catastrales = self.inmueble.numero_ficha_catastral
            resultado += ', '.join([', '.join(ficha.values())
                                   for ficha in fichas_catastrales])
            resultado += '</u></b>'

            if any(parqueadero.numero_ficha_catastral for parqueadero in self.parqueaderos if parqueadero.numero_ficha_catastral) or any(deposito.numero_ficha_catastral for deposito in self.depositos if deposito.numero_ficha_catastral):
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

    def generar_paragrafo_primero(self):
        resultado = ''
        resultado += '<p><b>PARÁGRAFO PRIMERO. -</b> No obstante, la mención del área del '
        resultado += 'inmueble anteriormente descrito y de la longitud de sus linderos, '
        resultado += 'la venta se hace como de cuerpo cierto, de tal suerte que '
        resultado += 'cualquier eventual diferencia que pueda resultar entre las cabidas '
        resultado += 'reales y las cabidas aquí declaradas, no dará lugar a reclamo por '
        resultado += 'ninguna de las partes.</p>'
        return resultado

    def generar_paragrafo_tradicion_inmueble(self):
        if self.multiples_inmuebles():
            inmuebles = 'Los inmuebles'
            fueron = 'fueron adquiridos'
        else:
            inmuebles = 'El inmueble'
            fueron = 'fue adquirido'
        resultado = ''
        resultado += f'<p><b>SEGUNDO: Tradición del Inmueble:</b> {inmuebles} objeto del '
        resultado += f'presente estudio {fueron} por <b>LOS VENDEDORES,</b> a '
        resultado += 'título de Restitución En Fiducia Mercantil de parte de FIDUCIARIA '
        resultado += 'DAVIVIENDA S.A. COMO VOCERA Y ADMINISTRADORA DEL FIDEICOMISO '
        resultado += 'LOTES GALICIA - NIT 830053700-6, mediante la Escritura Pública '
        resultado += 'No. 4127 del 29 de octubre de 2020, registrada en la matrícula '
        resultado += 'inmobiliaria No. 370-1024296.</p>'
        return resultado

    def generar_paragrafo_precio(self):
        fecha = datetime.strptime(
            self.compraventa.fecha_compraventa, "%d/%m/%Y").date()
        dia = fecha.day
        mes = MESES_INGLES_ESPANOL[fecha.strftime('%B')]
        anio = fecha.year

        cantidad_compraventa_letra = num2words(
            self.compraventa.cantidad_compraventa, lang='es')
        cantidad_compraventa_numero = f'{self.compraventa.cantidad_compraventa:,}'

        cuota_inicial_letra = num2words(
            self.compraventa.cuota_inicial, lang='es')
        cuota_inicial_numero = f'{self.compraventa.cuota_inicial:,}'

        cantidad_restante_letra = num2words(
            self.compraventa.cantidad_restante, lang='es')
        cantidad_restante_numero = f'{self.compraventa.cantidad_restante:,}'

        resultado = ''
        resultado += '<p><b>TERCERO: Precio:</b> Que el precio de la presente compraventa '
        resultado += f'es la suma de <b>{cantidad_compraventa_letra.upper()} PESOS MCTE '
        resultado += f'(${cantidad_compraventa_numero}),</b> que se pagarán así: a) La suma de '
        resultado += f'<b>{cuota_inicial_letra.upper()} PESOS MCTE (${cuota_inicial_numero}),'
        resultado += '</b> ya recibida a entera satisfacción a la firma de esta escritura '
        resultado += 'pública. Este valor fue entregado a <b>LA VENDEDORA</b> por cuenta de '
        for poderdante in self.poderdantes:
            resultado += f'<b>{poderdante.nombre.upper()},</b> mayor de edad, '
            resultado += f'{poderdante.identificado} con {poderdante.tipo_identificacion} '
            resultado += f'<b>No. {poderdante.numero_identificacion} de '
            resultado += f'{poderdante.ciudad_expedicion_identificacion},</b> '
        resultado += 'quien ostentaba la calidad de promitente comprador, en virtud del '
        resultado += f'contrato de promesa de compraventa suscrito <b>el {dia} de {mes} '
        resultado += f'de {anio},</b> calidad que cedió a <b>{self.banco.nombre.upper()}</b> '
        resultado += 'en razón del ________________ que se suscribe para obtener el crédito '
        resultado += 'necesario para pagar el saldo de la obligación con la sociedad '
        resultado += 'vendedora; b) El saldo, es decir  la  suma de <b>'
        resultado += f'{cantidad_restante_letra.upper()} PESOS MCTE (${cantidad_restante_numero})'
        resultado += ',</b> que cancelará el <b>COMPRADOR</b> una vez salga la escritura pública '
        resultado += 'de compraventa debidamente registrada de la Oficina de Registro de '
        resultado += 'Instrumentos Públicos a satisfacción de la compradora. <b>PARÁGRAFO '
        resultado += 'PRIMERO.</b>  No obstante, la forma de pago <b>EL VENDEDOR</b> renuncia '
        resultado += 'expresamente al ejercicio de la acción resolutoria que de ella pueda '
        resultado += 'derivarse y en consecuencia otorga el presente título firme e irresoluble. '
        return resultado

    def generar_clausula_limitaciones_gravamenes(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles sobre los cuales recaen'
            inmuebles_libres = 'dichos inmuebles se hallan libres'
        else:
            inmuebles = 'el inmueble sobre el cual recae'
            inmuebles_libres = 'dicho inmueble se halla libre'
        resultado = ''
        resultado += '<b>CUARTO. - Limitaciones y Gravámenes:</b> Que los derechos de dominio '
        resultado += 'que se transfieren mediante la presente escritura, son de plena y '
        resultado += 'exclusiva propiedad del <b>VENDEDOR,</b> y que no han sido enajenados '
        resultado += f'por acto anterior al presente, que {inmuebles} '
        resultado += 'actualmente los posee de manera regular, pacífica y pública y que  '
        resultado += f'{inmuebles_libres} de censos, anticresis, servidumbres, '
        resultado += 'desmembraciones y patrimonio de familia inembargable. '
        return resultado

    def generar_clausula_obligacion_sanear(self):
        resultado = ''
        resultado += '<b>QUINTO. - OBLIGACIÓN DE SANEAR:</b> Que, en todo caso, se obliga a '
        resultado += 'salir al saneamiento de los derechos que transfiere por cualquier vicio '
        resultado += 'que se llegare a presentar en los casos previstos por la Ley. '
        return resultado

    def generar_clausula_entrega(self):
        if self.multiples_inmuebles():
            inmuebles = 'de los inmuebles'
        else:
            inmuebles = 'del inmueble'
        resultado = ''
        resultado += f'<b>SEXTO: ENTREGA:</b> Que el <b>VENDEDOR</b> hará entrega {inmuebles} '
        resultado += 'objeto del presente contrato al <b>COMPRADOR</b> o a quien este '
        resultado += 'determine el día _________________________.'
        return resultado

    def generar_clausula_gastos_notariales(self):
        resultado = ''
        resultado += '<b>SÉPTIMO: Gastos Notariales de Impuesto y Registro:</b> Que los '
        resultado += 'gastos notariales que ocasione el otorgamiento del presente instrumento '
        resultado += 'público serán sufragados por <b>EL VENDEDOR y EL COMPRADOR</b> en igual '
        resultado += 'proporción. Los gastos de beneficencia, tesorería y registro que '
        resultado += 'demande el otorgamiento de esta escritura pública serán a cargo de '
        resultado += '<b>EL COMPRADOR. OCTAVO: Documentos que se protocolizan:</b> Que con el '
        resultado += 'presente instrumento protocoliza los siguientes documentos: <b>1.</b> '
        resultado += 'Fotocopia de la cédula de ciudadanía de cada uno de los comparecientes. '
        resultado += '<b>2.</b> Certificados de existencia y representación de las sociedades '
        resultado += f'<b>{self.banco.nombre.upper()}</b> '
        return resultado

    def generar_datos_apoderado_banco(self):
        resultado = ''
        resultado += f'<b>ACEPTACIÓN</b> Presente {self.apoderado_banco.doctor}, '
        resultado += f'<u><b>{self.apoderado_banco.nombre.upper()},</b></u> '
        resultado += f'mayor de edad, {self.apoderado_banco.vecino} de <u><b>'
        resultado += f'{self.apoderado_banco.ciudad_residencia}</b></u> '
        resultado += f'{self.apoderado_banco.identificado} con '
        resultado += f'<u><b>{self.apoderado_banco.tipo_identificacion}</b></u> No. '
        resultado += f'<u><b>{self.apoderado_banco.numero_identificacion}</b></u> de '
        resultado += f'<u><b>{self.apoderado_banco.ciudad_expedicion_identificacion}</b>'
        resultado += '</u> quien comparece en este acto en su calidad de '
        resultado += f'<u><b>{self.apoderado_banco.apoderado} {self.apoderado_banco.tipo_apoderado}'
        resultado += f'</b></u><b>{self.banco.nombre.upper()},</b> acorde con el Poder '
        resultado += f'{self.apoderado_banco.tipo_apoderado} '
        if self.apoderado_banco.tipo_poder == 'Autenticado':
            resultado += f'a {self.apoderado_banco.el} conferido por '
        elif self.apoderado_banco.tipo_poder == 'Escriturado':
            resultado += f'constituido por <u><b>{self.apoderado_banco.escritura},</b></u> '
            resultado += f'a {self.apoderado_banco.el} conferido por '
        return resultado

    def generar_datos_representante_banco(self):
        resultado = f'{self.representante_banco.doctor} '
        resultado += f'<u><b>{self.representante_banco.nombre.upper()},</b></u> mayor de edad, '
        resultado += f'{self.representante_banco.vecino} de '
        resultado += f'<u><b>{self.representante_banco.ciudad_residencia},</b></u> '
        resultado += f'{self.representante_banco.identificado} con '
        resultado += f'<u><b>{self.representante_banco.tipo_identificacion}</b></u> No. '
        resultado += f'<u><b>{self.representante_banco.numero_identificacion}</b></u> de '
        resultado += f'<u><b>{self.representante_banco.ciudad_expedicion_identificacion},</b></u> '
        resultado += 'quien compareció en ese acto en nombre y por cuenta en su calidad de '
        resultado += f'<u><b>{self.representante_banco.tipo_representante}</b></u> '
        return resultado

    def generar_constitucion_banco_union(self):
        resultado = f'de <b>{self.banco.nombre.upper()}</b> antes <b>GIROS & FINANZAS COMPAÑÍA DE '
        resultado += 'FINANCIAMIENTO S.A.</b>, sociedad constituida legalmente mediante '
        resultado += 'Escritura Pública No. 5938 del 05 de diciembre de 1963, otorgada en la '
        resultado += 'Notaria Cuarta (04) del Círculo de Bogotá, inscrita en la Cámara de '
        resultado += 'Comercio de Cali, el 7 de noviembre de 2000, bajo el número 7516 del Libro '
        resultado += 'IX, sociedad convertida a establecimiento Bancario y modificada su razón '
        resultado += 'social mediante Escritura Pública No. 3140 del 16 de Junio de 2022, otorgada '
        resultado += 'en la Notaría Cuarta del Círculo de Cali, inscrita en la Cámara de Comercio '
        resultado += 'de Cali el 28 de Junio de 2022, bajo el No. 12001 del Libro IX, con permiso '
        resultado += 'de funcionamiento otorgado mediante Resolución número 0549 del 31 de Mayo de '
        resultado += '2022, todo lo cual se acredita  con el Certificado de Existencia y '
        resultado += 'Representación Legal expedido por la Cámara de Comercio de Cali y por la'
        resultado += 'Superintendencia Financiera y Manifestó: '
        return resultado

    def generar_clausula_banco_aceptacion(self):
        resultado = ''
        resultado += '<b>PRIMERO: Aceptación:</b> Que acepta la presente escritura con todas y '
        resultado += 'cada una de las cláusulas en ella contenidas, por estar conforme a la '
        resultado += 'verdad y a lo pactado. '
        return resultado

    def generar_clausula_banco_compra(self):
        resultado = ''
        resultado += '<b>SEGUNDO: Compra:</b> Que, en consecuencia, acepta la venta de derechos '
        resultado += 'de dominio sobre el inmueble descrito en el ordinal primero de las '
        resultado += 'manifestaciones de <b>EL VENDEDOR.</b> Leída esta escritura pública por los '
        resultado += 'comparecientes y habiéndoles hecho las advertencias sobre las formalidades '
        resultado += 'legales y trámites de rigor, le imparten su aprobación y en constancia la '
        resultado += 'firman ante mí, la notaría que la autoriza. Hasta aquí la minuta.</p>'
        return resultado

    def generar_firma_vendedor(self):
        resultado = ''
        resultado += '<br><b>EL VENDEDOR</b><br><br><br>'
        resultado += '____________________________________'
        resultado += '<br><br>C.C. No. __________ de ______<br>'
        resultado += ''
        resultado += '<br><b>NIT: ____________</b>'
        return resultado

    def generar_firma_locatario(self):
        resultado = ''
        resultado += '<br><br><br><b>EL LOCATARIO</b><br><br><br>'
        resultado += '_________________________________<br>'
        resultado += f'<b>{self.apoderado.nombre.upper()},<br>'
        resultado += f'{self.apoderado.abreviacion_identificacion} '
        resultado += f'{self.apoderado.numero_identificacion} de '
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion}</b><br>'
        resultado += 'En nombre y representación de<br>'
        return resultado

    def generar_firma_poderdante(self):
        resultado = ''
        for index, poderdante in enumerate(self.poderdantes):
            resultado += f'<b>{poderdante.nombre.upper()}</b><br>'
            resultado += f'<b>{poderdante.abreviacion_identificacion} '
            resultado += f'{poderdante.numero_identificacion} de '
            resultado += f'{poderdante.ciudad_expedicion_identificacion}</b><br><br>'
            if index < self.cantidad_poderdantes - 1:
                resultado += 'y <br><br>'
        return resultado

    def generar_firma_comprador(self):
        resultado = 'EL COMPRADOR<br><br><br><br>'
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
        resultado = '<style>'
        resultado += 'div.titulo {text-align: left; font-weight: bold; font-size: 17px; '
        resultado += 'font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.parrafos {text-align: justify; font-size: 16px; list-style: '
        resultado += 'lower-alpha; font-family: Arial, Helvetica, sans-serif;}</style>'
        return resultado
