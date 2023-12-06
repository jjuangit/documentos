from typing import List

from datetime import datetime
from num2words import num2words
from utils.document import Document
from utils.exceptions import ValidationError
from utils.validators import Validator

from utils.validating_dictionaries.dictionary_poderdantes import dictionary_validator_poderdantes
from utils.validating_dictionaries.dictionary_apoderado import dictionary_validator_apoderado_promesa_compraventa
from utils.validating_dictionaries.dictionary_representante_banco import dictionary_validator_representante_banco
from utils.validating_dictionaries.dictionary_inmueble import dictionary_validator_inmueble_promesa_compraventa
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_parqueaderos_promesa_compraventa
from utils.validating_dictionaries.dictionary_depositos import dictionary_validator_depositos_promesa_compraventa
from utils.validating_dictionaries.dictionary_apoderado_banco import dictionary_validator_apoderado_banco
from utils.validating_dictionaries.dictionary_banco import dictionary_validator_banco
from utils.validating_dictionaries.dictionary_aceptante import dictionary_validator_aceptante
from utils.validating_dictionaries.dictionary_compraventa import dictionary_validator_compraventa
from utils.validating_dictionaries.dictionary_representante_aceptante import dictionary_validator_representante_aceptante
from utils.validating_dictionaries.dictionary_organo_autorizador import dictionary_validator_organo_autorizador

from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.catalogos import aceptantes
from catalogs.fechas import MESES_INGLES_ESPANOL

from .apoderado import ApoderadoPromesaCompraventa
from .apoderado_banco import ApoderadoBanco
from .depositos import DepositoPromesaCompraventa
from .inmueble import InmueblePromesaCompraventa
from .parqueaderos import ParqueaderoPromesaCompraventa
from .poderdantes import Poderdante
from .representante_banco import RepresentanteBanco
from .banco import Banco
from .aceptante import Aceptante
from .compraventa import Compraventa
from .representante_aceptante import RepresentanteAceptante
from .organo_autorizador import OrganoAutorizador


class DocumentoPromesaCompraventa(Document):
    apoderado: ApoderadoPromesaCompraventa
    poderdantes: List[Poderdante]
    inmueble: InmueblePromesaCompraventa
    depositos: List[DepositoPromesaCompraventa]
    parqueaderos: List[ParqueaderoPromesaCompraventa]
    apoderado_banco: ApoderadoBanco
    representante_banco: RepresentanteBanco
    representante_aceptante: RepresentanteAceptante
    banco: Banco
    aceptante: Aceptante
    compraventa: Compraventa
    organo_autorizador: OrganoAutorizador

    generate_html_functions = [
        'generar_titulo_documento',
        'generar_parrafo_datos_apoderado',
        'generar_parrafo_datos_poderdantes',
        'generar_parrafo_datos_apoderado_banco',
        'generar_parrafo_datos_representante_banco',
        'generar_constitucion_banco_union',
        'generar_clausula_antecedentes',
        'generar_parrafo_datos_aceptante',
        'generar_parrafo_datos_inmuebles',
        'generar_matriculas_inmobiliarias',
        'generar_fichas_catastrales',
        'generar_solicitud_credito_a_banco',
        'generar_clausula_objeto',
        'generar_clausula_cesion_instrumentada',
        'generar_clausula_aceptacion',
        'generar_datos_aceptante',
        'generar_fecha_firma',
        'generar_firma_apoderado',
        'generar_firma_poderdantes',
        'generar_firma_apoderado_banco',
        'generar_firma_representante_aceptante',
        'generar_estilos'

    ]

    def __init__(
        self,
        apoderado: ApoderadoPromesaCompraventa,
        poderdantes: List[Poderdante],
        inmueble: InmueblePromesaCompraventa,
        parqueaderos: List[ParqueaderoPromesaCompraventa],
        depositos: List[DepositoPromesaCompraventa],
        apoderado_banco: ApoderadoBanco,
        representante_banco: RepresentanteBanco,
        representante_aceptante: RepresentanteAceptante,
        banco: Banco,
        aceptante: Aceptante,
        compraventa: Compraventa,
        organo_autorizador: OrganoAutorizador
    ):
        self.apoderado = apoderado
        self.poderdantes = poderdantes
        self.inmueble = inmueble
        self.parqueaderos = parqueaderos
        self.depositos = depositos
        self.apoderado_banco = apoderado_banco
        self.representante_banco = representante_banco
        self.representante_aceptante = representante_aceptante
        self.banco = banco
        self.aceptante = aceptante
        self.compraventa = compraventa
        self.organo_autorizador = organo_autorizador
        self.validate_data_cesion_contrato()

    def validate_data_cesion_contrato(self):
        self.validar_apoderado()
        self.validar_poderdantes()
        self.validar_inmueble()
        self.validar_parqueaderos()
        self.validar_depositos()
        self.validar_apoderado_banco()
        self.validar_representante_banco()
        self.validar_representante_aceptante()
        self.validar_banco()
        self.validar_aceptante()
        self.validar_compraventa()
        self.validar_organo_autorizador()

    def validar_apoderado(self):
        atributos_apoderado = self.apoderado.__dict__
        Validator.validate_dict(
            atributos_apoderado, dictionary_validator_apoderado_promesa_compraventa, 'Apoderado')

    def validar_poderdantes(self):
        if self.cantidad_poderdantes == 0 and self.cantidad_poderdantes > 2:
            raise ValidationError(
                'Debe haber al menos un poderdante y no más de dos poderdantes.')

        for poderdante in self.poderdantes:
            atributos_poderdante = poderdante.__dict__
            Validator.validate_dict(
                atributos_poderdante, dictionary_validator_poderdantes, 'Poderdantes')

    def validar_inmueble(self):
        atributos_inmueble = self.inmueble.__dict__
        Validator.validate_dict(
            atributos_inmueble, dictionary_validator_inmueble_promesa_compraventa, 'Inmueble')

    def validar_parqueaderos(self):
        if len(self.parqueaderos) > 2:
            raise ValidationError('No puede haber más de dos "parqueaderos".')

        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                atributos_parqueaderos = parqueadero.__dict__

            Validator.validate_dict(
                atributos_parqueaderos, dictionary_validator_parqueaderos_promesa_compraventa, 'Parqueaderos')

    def validar_depositos(self):
        if len(self.depositos) > 2:
            raise ValidationError('No puede haber más de dos "depósitos".')

        if self.depositos:
            for deposito in self.depositos:
                atributos_depositos = deposito.__dict__

            Validator.validate_dict(
                atributos_depositos, dictionary_validator_depositos_promesa_compraventa, 'Depósitos')

    def validar_apoderado_banco(self):
        if self.apoderado_banco.nombre not in [apoderado['nombre'] for apoderado in apoderados_banco]:
            atributos_apoderado_banco = self.apoderado_banco.__dict__
            Validator.validate_dict(
                atributos_apoderado_banco, dictionary_validator_apoderado_banco, 'Apoderado del banco')

    def validar_representante_banco(self):
        if self.representante_banco.nombre not in [representante['nombre'] for representante in representantes_banco]:
            atributos_representante_banco = self.representante_banco.__dict__
            Validator.validate_dict(
                atributos_representante_banco, dictionary_validator_representante_banco, 'Representante del banco')

    def validar_banco(self):
        if self.banco.nombre not in [banco['nombre'] for banco in bancos]:
            atributos_banco = self.banco.__dict__
            Validator.validate_dict(
                atributos_banco, dictionary_validator_banco, 'Banco')

    def validar_compraventa(self):
        atributos_compraventa = self.compraventa.__dict__
        Validator.validate_dict(
            atributos_compraventa, dictionary_validator_compraventa, 'Compraventa')

    def validar_aceptante(self):
        if self.aceptante.nombre not in [aceptante['nombre'] for aceptante in aceptantes]:
            atributos_aceptante = self.aceptante.__dict__
            Validator.validate_dict(
                atributos_aceptante, dictionary_validator_aceptante, 'Aceptante')

    def validar_representante_aceptante(self):
        atributos_representante_aceptante = self.representante_aceptante.__dict__
        Validator.validate_dict(
            atributos_representante_aceptante, dictionary_validator_representante_aceptante, 'Representante del aceptante')

    def validar_organo_autorizador(self):
        atributos_organo_autorizador = self.organo_autorizador.__dict__
        Validator.validate_dict(
            atributos_organo_autorizador, dictionary_validator_organo_autorizador, 'Organo Autorizador')

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
        resultado = '<title>Cesión del contrato</title>'
        resultado += '<div class="titulo"><p>'
        resultado += '<b>CESIÓN DEL CONTRATO PROMESA DE COMPRAVENTA</b></p></div>'
        return resultado

    def generar_parrafo_datos_apoderado(self):
        resultado = '<div class="parrafos"><p>Entre los suscritos a saber: de una parte, '
        resultado += f'<b><u>{self.apoderado.nombre.upper()},</u></b> mayor de edad, '
        resultado += f'{self.apoderado.identificado} con <b>{self.apoderado.tipo_identificacion} '
        resultado += f'No. <u>{self.apoderado.numero_identificacion}</u> de '
        resultado += f'<u>{self.apoderado.ciudad_expedicion_identificacion},</u></b> hábil para '
        resultado += 'contratar y obligarse, quien actúa en nombre y representación de '
        return resultado

    # TODO Pendiente agregar texto final
    def generar_parrafo_datos_poderdantes(self):
        fecha = datetime.strptime(
            self.apoderado.fecha_autenticacion_poder, "%d/%m/%Y").date()
        dia = fecha.day
        mes = MESES_INGLES_ESPANOL[fecha.strftime('%B')]
        anio = fecha.year
        if len(self.poderdantes) > 1:
            cedentes = 'denominarán <b>LOS CEDENTES</b>'
            quienes = 'quienes'
        elif len(self.poderdantes) == 1:
            quienes = 'quien'
            cedentes = 'denominará <b>El CEDENTE</b>'
        resultado = ''
        for index, poderdante in enumerate(self.poderdantes):

            if index == len(self.poderdantes) - \
                    1 and len(self.poderdantes) > 1:
                resultado += ' y '
            resultado += f'<b><u>{poderdante.nombre.upper()},</u></b> mayor de edad, '
            resultado += f'{poderdante.identificado} con <b><u>{poderdante.tipo_identificacion} '
            resultado += f'No. {poderdante.numero_identificacion}</u> de '
            resultado += f'<u>{poderdante.ciudad_expedicion_identificacion},</u></b> '
            resultado += f'{poderdante.domiciliado} y {poderdante.residenciado} en '
            resultado += f'<b><u>{poderdante.domicilio.upper()},</u></b> de estado civil '
            resultado += f'<b><u>{poderdante.estado_civil_genero.upper()};</u></b> en su calidad '
            resultado += f'de {self.apoderado.apoderado} {self.apoderado.tipo_apoderado}, '
            if self.apoderado.tipo_apoderado == 'Especial':
                resultado += f'según acredita con el Poder {self.apoderado.tipo_apoderado} a '
                resultado += f'{self.apoderado.el} otorgado '
                resultado += f'y debidamente autenticado el día <b><u>{dia} de {mes} del {anio} '
                resultado += f'</u></b>ante {self.apoderado.dependencia} '
                resultado += f'<b><u>{self.apoderado.nombre_dependencia.upper()} de '
                resultado += f'{self.apoderado.ciudad_dependencia.upper()},</u></b> '
            elif self.apoderado.tipo_apoderado == 'General':
                resultado += 'acorde con el Poder General amplio y suficiente, constituido '
                resultado += f'mediante la <b><u>{self.apoderado.escritura}</u></b>'

            resultado += f'{quienes} para todos los efectos se {cedentes}, '
        return resultado

    def generar_parrafo_datos_apoderado_banco(self):
        resultado = f'y de otra parte {self.apoderado_banco.doctor}, <b><u>'
        resultado += f'{self.apoderado_banco.nombre.upper()},</u></b> mayor de edad, '
        resultado += f'{self.apoderado_banco.vecino} de <b><u>{self.apoderado_banco.ciudad_residencia},'
        resultado += f'</b></u> {self.apoderado_banco.identificado} con <b>'
        resultado += f'{self.apoderado_banco.tipo_identificacion} No. '
        resultado += f'<u>{self.apoderado_banco.numero_identificacion}</u> de '
        resultado += f'<u>{self.apoderado_banco.ciudad_expedicion_identificacion},</u></b> '
        resultado += 'quien comparece en este acto en su calidad de '
        resultado += f'{self.apoderado_banco.apoderado} {self.apoderado_banco.tipo_apoderado} de '
        resultado += f'<b>{self.banco.nombre.upper()},</b> acorde con el Poder '
        resultado += f'{self.apoderado_banco.tipo_apoderado}'
        if self.apoderado_banco.tipo_poder == 'Autenticado':
            resultado += f'a {self.apoderado_banco.el} conferido por '
        elif self.apoderado_banco.tipo_poder == 'Escriturado':
            resultado += f' constituido por <b><u>{self.apoderado_banco.escritura},</u></b> '
            resultado += f'a {self.apoderado_banco.el} conferido por '
        return resultado

    def generar_parrafo_datos_representante_banco(self):
        resultado = f'{self.representante_banco.doctor} <u><b>'
        resultado += f'{self.representante_banco.nombre.upper()},</b></u> mayor de edad, '
        resultado += f'{self.representante_banco.vecino} de '
        resultado += f'<u><b>{self.representante_banco.ciudad_residencia},</b></u> '
        resultado += f'{self.representante_banco.identificado} con '
        resultado += f'<u><b>{self.representante_banco.tipo_identificacion}</b></u> No. '
        resultado += f'<u><b>{self.representante_banco.numero_identificacion}</b></u> de '
        resultado += f'<u><b>{self.representante_banco.ciudad_expedicion_identificacion},</b></u> '
        resultado += 'quien compareció en ese acto en nombre y por cuenta en su calidad  '
        resultado += f'de {self.representante_banco.tipo_representante} de '
        return resultado

    def generar_constitucion_banco_union(self):
        resultado = f'<b>{self.banco.nombre.upper()}</b> antes <b>GIROS & FINANZAS COMPAÑÍA DE '
        resultado += 'FINANCIAMIENTO S.A.</b>, sociedad con domicilio principal en Cali, '
        resultado += 'identificada Tributariamente con NIT número 860.006.797-9, sociedad '
        resultado += 'constituida legalmente mediante Escritura Pública No. 5938 del 05 de '
        resultado += 'diciembre de 1963, otorgada en la Notaría Cuarta (04) del Círculo de Bogotá '
        resultado += ', inscrita en la Cámara de Comercio de Cali, el 7 de noviembre de 2000, bajo '
        resultado += 'el número 7516 del Libro IX, sociedad convertida a establecimiento Bancario '
        resultado += 'y modificada su razón social mediante Escritura Pública No. 3140 del 16 de '
        resultado += 'Junio de 2022, otorgada en la Notaría Cuarta del Círculo de Cali, inscrita '
        resultado += 'en la Cámara de Comercio de Cali el 28 de Junio de 2022, bajo el No. 12001 '
        resultado += 'del Libro todo lo cual se acredita con el Certificado de Existencia y '
        resultado += 'Representación Legal expedido por la Cámara de Comercio de Cali y por la '
        resultado += 'Superintendencia Financiera, quien para los efectos del presente contrato se '
        resultado += 'denominará la <b>CESIONARIA,</b> por medio del presente documento convenimos '
        resultado += 'celebrar cesión de contrato de promesa de compraventa que se regirá por las '
        resultado += 'siguientes cláusulas:----------------------------------------------------'
        resultado += '<br><br></p></div>'
        return resultado

    def generar_clausula_antecedentes(self):
        resultado = ''
        resultado += '<div class="center"><b>PRIMERA ANTECEDENTES:</b></div><br>'
        return resultado

    def generar_parrafo_datos_aceptante(self):
        fecha = datetime.strptime(
            self.compraventa.fecha_compraventa, "%d/%m/%Y").date()
        dia = fecha.day
        mes = MESES_INGLES_ESPANOL[fecha.strftime('%B')]
        anio = fecha.year

        if len(self.poderdantes) > 1:
            cedentes = '<b>LOS CEDENTES</b> suscribieron'
        elif len(self.poderdantes) == 1:
            cedentes = '<b>EL CEDENTE</b> suscribió'
        resultado = f'<div class="parrafos"><ol><li>{cedentes} '
        resultado += f'con la sociedad <b><u>{self.aceptante.nombre.upper()},</u></b>'
        resultado += f' identificada tributariamente con NIT <b><u>{self.aceptante.nit},'
        resultado += '</b></u> contrato de promesa de compraventa '
        resultado += f'suscrita el <b><u>{dia} de {mes} de {anio},</u></b> '
        return resultado

    def generar_parrafo_datos_inmuebles(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
        else:
            inmuebles = 'el inmueble'
        resultado = ''
        resultado += f'contrato que versa sobre {inmuebles}: <b><u>{self.inmueble.nombre} '
        resultado += f'{self.inmueble.numero}, '
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f'{parqueadero.nombre} {parqueadero.numero}, '
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'{deposito.nombre} {deposito.numero}, '
        resultado += f'{self.inmueble.direccion}, {self.inmueble.ciudad_y_o_departamento},</u></b> '
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
            inmuebles = 'inmuebles identificados con los folios de matrículas inmobiliarias'
        else:
            inmuebles = 'inmueble identificado con el folio de matrícula inmobiliaria'

        matriculas = [self.inmueble.matricula]
        for parqueadero in self.parqueaderos:
            if self.parqueaderos and parqueadero.matricula:
                matriculas += [parqueadero.matricula]
        for deposito in self.depositos:
            if self.depositos and deposito.matricula:
                matriculas += [deposito.matricula]
        resultado = ''
        resultado += f'{inmuebles} No. <b><u>{", ".join(matriculas)}'
        if matriculas_presentes:
            resultado += '</u></b> respectivamente '

        resultado += '</u></b> de la Oficina de Registro de Instrumentos Públicos de '
        resultado += f'<b><u>{self.inmueble.municipio_de_registro_orip}</u></b>'
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
                resultado += ' En Mayor Extensión.</u></b> '
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

    def generar_solicitud_credito_a_banco(self):
        if len(self.poderdantes) > 1:
            cedentes = '<b>LOS CEDENTES</b> solicitaron'
        elif len(self.poderdantes) == 1:
            cedentes = '<b>EL CEDENTE</b> solicitó'
        resultado = f'<li>{cedentes} a <b>{self.banco.nombre.upper()}</b> crédito de vivienda, '
        resultado += 'para cubrir el pago del precio de la promesa de compraventa '
        resultado += 'descrita en el numeral anterior, el cual le fue aprobado en la '
        resultado += 'modalidad de Leasing Habitacional.</li></ol>'
        return resultado

    def generar_clausula_objeto(self):
        number_to_word_cuota_inicial = num2words(
            self.compraventa.cuota_inicial, lang='es')
        number_format_cuota_inicial = f'{self.compraventa.cuota_inicial:,}'

        fecha = datetime.strptime(
            self.compraventa.fecha_compraventa, "%d/%m/%Y").date()
        dia = fecha.day
        mes = MESES_INGLES_ESPANOL[fecha.strftime('%B')]
        anio = fecha.year

        if len(self.poderdantes) > 1:
            cedentes = 'CEDENTES'
            los = f'<b>LOS {cedentes}</b>'
            de = f'de los <b>{cedentes}</b>'
            realizan = 'realizan'
        elif len(self.poderdantes) == 1:
            cedentes = 'CEDENTE'
            los = f'<b>EL {cedentes}</b>'
            de = f'del <b>{cedentes}</b>'
            realizan = 'realiza'

        resultado = '<p><b>SEGUNDO OBJETO:</b> El objeto del presente contrato es la '
        resultado += f'cesión que {los} {realizan} a favor de la <b>'
        resultado += 'CESIONARIA,</b> de su posición contractual en la promesa de compraventa '
        resultado += f'suscrita con la sociedad <b><u>{self.aceptante.nombre.upper()},</u> '
        resultado += f'identificada tributariamente con NIT <u>{self.aceptante.nit},</u></b> '
        resultado += f'cesión que recae también sobre los recursos entregados por parte {de} '
        resultado += 'a la sociedad vendedora como cuota inicial, dineros pagados en '
        resultado += 'cumplimiento de la promesa de compraventa objeto de la presente '
        resultado += 'cesión, los cuales ascienden a la suma de <b><u>'
        resultado += f'{number_to_word_cuota_inicial.upper()} PESOS MCTE ($'
        resultado += f'{number_format_cuota_inicial}),</u></b> contrato de promesa de '
        resultado += f'compraventa suscrito el <b><u>{dia} de {mes} de {anio},</u></b> '
        resultado += f'{self.generar_parrafo_datos_inmuebles()}'
        resultado += f'{self.generar_matriculas_inmobiliarias()} '
        resultado += f'{self.generar_fichas_catastrales()}</p>'
        return resultado

    def generar_clausula_cesion_instrumentada(self):
        resultado = '<p><b>TERCERO:</b> Que la cesión instrumentada en el presente documento '
        resultado += 'la hace el cedente de su libre y espontánea voluntad y para el '
        resultado += 'cumplimiento de los requisitos exigidos por <b>'
        resultado += f'{self.banco.nombre.upper()},</b> para el desembolso del crédito de '
        resultado += 'vivienda en la modalidad de Leasing Habitacional.</p>'
        return resultado

    def generar_clausula_aceptacion(self):
        if not self.representante_aceptante:
            self.representante_aceptante = RepresentanteAceptante(
                nombre='_________________',
                tipo_identificacion='_______________',
                numero_identificacion='_____________',
                ciudad_expedicion_identificacion='________',
                ciudad_residencia='__________',
                genero='________',
                tipo_representante='_________',
            )
        resultado = ''
        resultado += f'<b>CUARTO: ACEPTACIÓN</b> Presente {self.representante_aceptante.doctor}. '
        resultado += f'<b><u>{self.representante_aceptante.nombre},</b></u> mayor de edad, '
        resultado += f'{self.representante_aceptante.vecino} de <b><u>'
        resultado += f'{self.representante_aceptante.ciudad_residencia},</b></u> '
        resultado += f'{self.representante_aceptante.identificado} con '
        resultado += f'{self.representante_aceptante.tipo_identificacion} No. '
        resultado += f'<b><u>{self.representante_aceptante.numero_identificacion},</u></b> '
        resultado += 'actuando en este acto en nombre y representación legal en su calidad de '
        resultado += f'({self.representante_aceptante.tipo_representante}) de la sociedad '
        return resultado

    def generar_datos_aceptante(self):
        if self.organo_autorizador.fecha_acta:
            fecha = datetime.strptime(
                self.organo_autorizador.fecha_acta, "%d/%m/%Y").date()
            dia = fecha.day
            mes = MESES_INGLES_ESPANOL[fecha.strftime('%B')]
            anio = fecha.year
        else:
            dia = '_____'
            mes = '_____'
            anio = '_____'

        if self.organo_autorizador.numero_acta:
            numero_acta = self.organo_autorizador.numero_acta
        else:
            numero_acta = '_______'

        if len(self.poderdantes) > 1:
            cedentes = 'LOS CEDENTES'
        elif len(self.poderdantes) == 1:
            cedentes = 'EL CEDENTE'
        resultado = ''
        resultado += f'<b><u>{self.aceptante.nombre.upper()},</u></b> identificada tributariamente '
        resultado += f'con NIT <b><u>{self.aceptante.nit},</u></b> sociedad con domicilio en la '
        resultado += f'ciudad de <b>{self.aceptante.ciudad_ubicacion.upper()}</b> constituida '
        resultado += f'por medio de la <b><u>{self.aceptante.escritura},</u></b> otorgada en la '
        resultado += f'<b><u>{self.aceptante.nombre_notaria} de '
        resultado += f'{self.aceptante.ciudad_ubicacion_notaria}</u></b> debidamente inscrita en '
        resultado += 'la <b><u>Cámara de Comercio de '
        resultado += f'{self.aceptante.ciudad_ubicacion_camara_comercio},</b></u> cuya existencia, '
        resultado += 'vigencia y representación legal acreditada con el certificado que para los '
        resultado += 'efectos le ha expedido la <b><u>Camara de Comercio de '
        resultado += f'{self.organo_autorizador.ciudad_ubicacion_camara_comercio}</b></u> '
        resultado += 'debidamente autorizada por la Junta Directiva según consta en el acta '
        resultado += f'No. <b><u>{numero_acta}</b></u> de fecha <b><u>{dia} {mes} de '
        resultado += f'{anio}</u></b> hábil para contratar y obligarse, manifestó que acepta '
        resultado += f'la cesión que por este instrumento hace <b>{cedentes}</b> a la '
        resultado += '<b>CESIONARIA. -----------------</b><br><br><br>'
        return resultado

    def generar_fecha_firma(self):
        resultado = ''
        resultado += 'Para constancia se firma en la ciudad de ________ el  día ________ (_____) '
        resultado += 'de ________ del año dos mil veintitres (2023).<br><br></div>'
        return resultado

    def generar_firma_apoderado(self):
        if len(self.poderdantes) > 1:
            cedentes = 'LOS CEDENTES'
        elif len(self.poderdantes) == 1:
            cedentes = 'EL CEDENTE'
        resultado = ''
        resultado += f'<b>{cedentes}</b><br>'
        resultado += '_________________________________<br>'
        resultado += '_________________________________<br>'
        resultado += '_________________________________<br>'
        resultado += f'<b>{self.apoderado.nombre.upper()},<br>'
        resultado += f'{self.apoderado.abreviacion_identificacion} '
        resultado += f'{self.apoderado.numero_identificacion} de '
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion}</b><br>'
        resultado += 'En nombre y representación de<br>'
        return resultado

    def generar_firma_poderdantes(self):
        resultado = ''
        for index, poderdante in enumerate(self.poderdantes):
            resultado += f'<b>{poderdante.nombre.upper()}</b><br>'
            resultado += f'<b>{poderdante.abreviacion_identificacion} '
            resultado += f' {poderdante.numero_identificacion} de '
            resultado += f'{poderdante.ciudad_expedicion_identificacion}</b><br><br>'
            if index < len(self.poderdantes) - 1:
                resultado += 'y<br><br>'
        return resultado

    def generar_firma_apoderado_banco(self):
        resultado = ''
        resultado += '<b>EL CESIONARIO</b><br><br><br>'
        resultado += '_______________________________________<br>'
        resultado += f'<b>{self.apoderado_banco.nombre.upper()}<br>'
        resultado += f'{self.apoderado_banco.abreviacion_identificacion} '
        resultado += f'{self.apoderado_banco.numero_identificacion} expedida en '
        resultado += f'{self.apoderado_banco.ciudad_expedicion_identificacion}<br> '
        resultado += f'{self.apoderado_banco.apoderado} {self.apoderado_banco.tipo_apoderado} de'
        resultado += f'<br> {self.banco.nombre.upper()}<br>'
        resultado += f'NIT {self.banco.nit}</b>'
        return resultado

    def generar_firma_representante_aceptante(self):
        if not self.representante_aceptante:
            self.representante_aceptante = RepresentanteAceptante(
                nombre='_________________',
                tipo_identificacion='_______________',
                numero_identificacion='_____________',
                ciudad_expedicion_identificacion='________',
                ciudad_residencia='__________',
                genero='________',
                tipo_representante='_________',
            )
        resultado = ''
        resultado += '<br><br><br><b>EL ACEPTANTE</b><br><br><br>'
        resultado += '____________________________________<br>'
        resultado += f'<b>{self.representante_aceptante.nombre}</b><br>'
        resultado += f'<b>{self.representante_aceptante.abreviacion_identificacion} No. '
        resultado += f'{self.representante_aceptante.numero_identificacion} de '
        resultado += self.representante_aceptante.ciudad_expedicion_identificacion
        resultado += '</b><br>Representante legal de<br>'
        resultado += f'<b>{self.aceptante.nombre.upper()}<br>'
        resultado += f'NIT. {self.aceptante.nit}</b>'
        return resultado

    def generar_estilos(self):
        resultado = ''
        resultado += '<style>div.titulo {text-align: center; font-weight: '
        resultado += 'bold; font-size: 17px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif;} div.parrafos {text-align: justify; font-size: '
        resultado += '16px; list-style: lower-alpha; font-family: '
        resultado += 'Arial, Helvetica, sans-serif;} div.center {text-align: center; '
        resultado += 'font-size: 16px; font-family: Arial, Helvetica, sans-serif;}'
        resultado += '</style>'
        return resultado
