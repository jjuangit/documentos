from typing import List
from datetime import datetime
from utils.document import Document
from utils.exceptions import ValidationError
from utils.validators import Validator
from utils.validating_dictionaries.dictionary_pareja_poderdante import dictionary_validator_pareja_poderdante
from utils.validating_dictionaries.dictionary_poderdantes import dictionary_validator_poderdantes_poder
from utils.validating_dictionaries.dictionary_apoderado import dictionary_validator_apoderado_poder
from utils.validating_dictionaries.dictionary_banco import dictionary_validator_banco_poder
from utils.validating_dictionaries.dictionary_declaraciones import dictionary_validator_declaraciones
from utils.validating_dictionaries.dictionary_depositos import dictionary_validator_depositos_poder
from utils.validating_dictionaries.dictionary_parqueaderos import dictionary_validator_parqueaderos_poder
from utils.validating_dictionaries.dictionary_inmueble import dictionary_validator_inmueble_poder
from catalogs.fechas import MESES_INGLES_ESPANOL

from .poderdantes import PoderdantePoder
from .apoderado import ApoderadoPoder
from .pareja_poderdante import ParejaPoderdante
from .inmueble import InmueblePoder
from .parqueaderos import ParqueaderoPoder
from .depositos import DepositoPoder
from .banco import BancoPoder
from .declaraciones import Declaraciones


class DocumentoPoder(Document):
    poderdantes: List[PoderdantePoder]
    pareja_poderdante: ParejaPoderdante
    apoderado: ApoderadoPoder
    inmueble: InmueblePoder
    parqueaderos: List[ParqueaderoPoder]
    declaraciones: Declaraciones
    banco: BancoPoder
    depositos: List[DepositoPoder]

    generate_html_functions = [
        'generar_html_titulo_documento',
        'generar_html_datos_inmueble',
        'generar_html_datos_parqueaderos',
        'generar_html_datos_depositos',
        'generar_cedula_catastral_mayor_extension',
        'generar_html_parrafo_poderdantes',
        'generar_html_datos_apoderado',
        'generar_html_numerales',
        'generar_html_lugar_y_fecha',
        'generar_html_firmas',
        'generar_estilos'
    ]

    def __init__(
        self,
        poderdantes: List[PoderdantePoder],
        pareja_poderdante: ParejaPoderdante,
        apoderado: ApoderadoPoder,
        inmueble: InmueblePoder,
        parqueaderos: List[ParqueaderoPoder],
        declaraciones: Declaraciones,
        banco: BancoPoder,
        depositos: List[DepositoPoder]
    ):
        self.poderdantes = poderdantes
        self.pareja_poderdante = pareja_poderdante
        self.apoderado = apoderado
        self.inmueble = inmueble
        self.parqueaderos = parqueaderos
        self.declaraciones = declaraciones
        self.banco = banco
        self.depositos = depositos
        self.validate_data()

    def validate_data(self):
        self.validar_apoderado()
        self.validar_poderdantes()
        self.validar_pareja_poderdante()
        self.validar_inmueble()
        self.validar_parqueaderos()
        self.validar_depositos()
        self.validar_banco()
        self.validar_declaraciones()

    def validar_apoderado(self):
        atributos = self.apoderado.__dict__
        Validator.validate_dict(
            atributos, dictionary_validator_apoderado_poder, 'Apoderado'
        )

    def validar_poderdantes(self):
        if self.cantidad_poderdantes == 0 and self.cantidad_poderdantes > 2:
            raise ValidationError(
                'Debe haber al menos un poderdante y no más de dos poderdantes.')

        if self.cantidad_poderdantes == 2 and self.pareja_poderdante:
            raise ValidationError(
                'No puede haber dos poderdantes y pareja poderdante.')

        for poderdante in self.poderdantes:
            atributos_poderdante = poderdante.__dict__
            Validator.validate_dict(
                atributos_poderdante, dictionary_validator_poderdantes_poder, "Poderdante")

    def validar_pareja_poderdante(self):
        if self.pareja_poderdante:
            atributos_pareja_poderdante = self.pareja_poderdante.__dict__
            Validator.validate_dict(
                atributos_pareja_poderdante, dictionary_validator_pareja_poderdante,
                'Pareja Poderdante')

    def validar_inmueble(self):
        atributos_inmueble = self.inmueble.__dict__
        Validator.validate_dict(
            atributos_inmueble, dictionary_validator_inmueble_poder, "Inmueble")

    def validar_parqueaderos(self):
        if len(self.parqueaderos) > 2:
            raise ValidationError('No puede haber más de dos "parqueaderos".')

        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                atributos_parqueaderos = parqueadero.__dict__
                Validator.validate_dict(
                    atributos_parqueaderos, dictionary_validator_parqueaderos_poder, 'Parqueaderos')

    def validar_depositos(self):
        if len(self.depositos) > 2:
            raise ValidationError('No puede haber más de dos "depósitos".')

        if self.depositos:
            for deposito in self.depositos:
                atributos_depositos = deposito.__dict__
                Validator.validate_dict(
                    atributos_depositos, dictionary_validator_depositos_poder, 'Depósitos')

    def validar_banco(self):
        atributos_banco = self.banco.__dict__
        Validator.validate_dict(atributos_banco, dictionary_validator_banco_poder, 'Banco'
                                )

    def validar_declaraciones(self):
        atributos_declaraciones = self.declaraciones.__dict__
        Validator.validate_dict(
            atributos_declaraciones, dictionary_validator_declaraciones, "Declaraciones")

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

    def estado_civil_es_union(self, estado_civil):
        estados_civiles_union = [
            'Casado con sociedad conyugal vigente',
            'Casado sin sociedad conyugal vigente',
            'Soltero con unión marital de hecho y sociedad patrimonial vigente',
            'Soltero con unión marital de hecho sin sociedad patrimonial vigente']
        return estado_civil in estados_civiles_union

    def generar_html_titulo_documento(self):
        resultado = ''
        resultado += '<title>Poder</title><div class="titulo"><p><b>'
        resultado += 'PODER ESPECIAL PARA ADQUISICIÓN DE INMUEBLES Y CONSTITUCIÓN DE HIPOTECA'
        resultado += '</b></p></div>'
        return resultado

    def generar_html_datos_inmueble(self):
        if self.multiples_inmuebles():
            inmuebles = 'DE LOS INMUEBLES'
        else:
            inmuebles = 'DEL INMUEBLE'

        resultado = ''
        resultado += '<div class="datos_inmuebles"><p><b>DATOS DE IDENTIFICACIÓN '
        resultado += f'{inmuebles}</b></p><p><b>DEPARTAMENTO Y CIUDAD DE '
        resultado += f'UBICACIÓN:</b> {self.inmueble.departamento.upper()} '
        resultado += f'{self.inmueble.ciudad.upper()}'
        resultado += '</p><p><b>DIRECCIÓN:</b> '
        resultado += f'{self.inmueble.direccion.upper()}</p>'
        resultado += f'<p><b>APARTAMENTO O CASA:</b> {self.inmueble.nombre.upper()} '
        resultado += f'{self.inmueble.numero}, <b>'
        resultado += f'Matrícula No.</b> {self.inmueble.matricula}'
        if self.inmueble.tipo_ficha_catastral == "Individual":
            resultado += ' <b>Cédula Catastral Individual:</b> '
            fichas = getattr(self.inmueble, 'numero_ficha_catastral')
            if isinstance(fichas, list) and all(isinstance(ficha, dict) for ficha in fichas):
                resultado += ', '.join([', '.join(ficha_values.values())
                                       for ficha_values in fichas[:-1]])
                if len(fichas) > 1:
                    resultado += ' y ' + ', '.join(fichas[-1].values())
                elif len(fichas) == 1:
                    resultado += ', '.join(fichas[-1].values())
        return resultado

    def generar_html_datos_parqueaderos(self):
        resultado = ''
        if self.parqueaderos:
            if len(self.parqueaderos) > 1:
                parqueaderos = '<p><b>PARQUEADEROS:</b></p><ol>'
                parqueadero_apertura_html = '<li><p>'
                parqueadero_cierre_html = '</p></li>'
                ol = '</ol>'
            elif len(self.parqueaderos) == 1:
                parqueaderos = '<p><b>PARQUEADERO:</b></p> '
                parqueadero_apertura_html = '<p>'
                parqueadero_cierre_html = '</p>'
                ol = ''
            resultado += f'{parqueaderos} '
            for parqueadero in self.parqueaderos:
                resultado += f'{parqueadero_apertura_html}{parqueadero.nombre.upper()} No. '
                resultado += f'{parqueadero.numero}, '
                if parqueadero.matricula:
                    resultado += f'<b>Matrícula No.</b> {parqueadero.matricula}, '
                if parqueadero.tipo_ficha_catastral == 'Individual':
                    resultado += '<b>Cédula Catastral Individual:</b>'
                    resultado += f' {parqueadero.numero_ficha_catastral}'
                    resultado += parqueadero_cierre_html
            resultado += ol
        return resultado

    def generar_html_datos_depositos(self):
        resultado = ''
        if self.depositos:
            if len(self.depositos) > 1:
                depositos = '<p><b>DEPÓSITOS:</b></p><ol>'
                deposito_apertura_html = '<li><p>'
                deposito_cierre_html = '</p></li>'
                ol = '</ol>'
            elif len(self.depositos) == 1:
                depositos = '<p><b>DEPÓSITO:</b></p> '
                deposito_apertura_html = '<p>'
                deposito_cierre_html = '</p>'
                ol = ''
            resultado += f'{depositos} '
            for deposito in self.depositos:
                resultado += f'{deposito_apertura_html}{deposito.nombre.upper()} No. '
                resultado += f'{deposito.numero}, '
                if deposito.matricula:
                    resultado += f'<b>Matrícula No.</b> {deposito.matricula}, '
                if deposito.tipo_ficha_catastral == 'Individual':
                    resultado += '<b>Cédula Catastral Individual:</b>'
                    resultado += f' {deposito.numero_ficha_catastral}'
                    resultado += deposito_cierre_html
            resultado += ol
        return resultado

    def generar_cedula_catastral_mayor_extension(self):
        resultado = ''
        if self.inmueble.tipo_ficha_catastral == "Mayor Extensión":
            resultado += '<p><b>CÉDULA CATASTRAL INDIVIDUAL O DE MAYOR EXTENSIÓN:</b> '
            fichas = getattr(self.inmueble, 'numero_ficha_catastral')
            if isinstance(fichas, list) and all(isinstance(ficha, dict) for ficha in fichas):
                resultado += ' y ficha catastral No. <b><u>'
                resultado += ', '.join([', '.join(ficha_values.values())
                                       for ficha_values in fichas[:-1]])
                if len(fichas) > 1:
                    resultado += ' y ' + ', '.join(fichas[-1].values())
                elif len(fichas) == 1:
                    resultado += ', '.join(fichas[-1].values())
        return resultado

    def generar_html_parrafo_poderdantes(self):
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if poderdante.estado_civil == 'Soltero sin unión marital de hecho':
                t_nosotros = 'Yo'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_nosotros = 'Yo'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_nosotros = 'Nosotros'
        elif self.cantidad_poderdantes == 2:
            generos = set(
                [poderdante.genero for poderdante in self.poderdantes])
            if len(generos) == 1 and 'Femenino' in generos:
                t_nosotros = 'Nosotras'
            else:
                t_nosotros = 'Nosotros'

        resultado = ''
        resultado += f'<div class="parrafo_poderdantes"><p>{t_nosotros} '
        for index, poderdante in enumerate(self.poderdantes):

            if index == self.cantidad_poderdantes - \
                    1 and self.cantidad_poderdantes > 1:
                resultado += ' y '

            resultado += f'<b>{poderdante.nombre.upper()}</b>'

            if poderdante.genero == 'Masculino':
                t_identificado = 'identificado'
                t_domiciliado = 'domiciliado'
            elif poderdante.genero == 'Femenino':
                t_identificado = 'identificada'
                t_domiciliado = 'domiciliada'

            resultado += f', mayor de edad, {t_identificado} con '
            resultado += f'<b>{poderdante.tipo_identificacion}</b> No. <b>'
            resultado += f'{poderdante.numero_identificacion}</b> de '
            resultado += f'<b>{poderdante.ciudad_expedicion_identificacion}</b>, de estado civil '
            resultado += f'<b>{poderdante.estado_civil_genero.upper()}</b> y {t_domiciliado} en<b> '
            resultado += f'{poderdante.domicilio_municipio.upper()}, '
            resultado += f'{poderdante.domicilio_departamento.upper()}, '
            resultado += f'{poderdante.domicilio_pais.upper()}</b>'
            if self.cantidad_poderdantes == 1 and self.declaraciones.pareja_hace_parte_compraventa == 'Si'\
                    and self.estado_civil_es_union(poderdante.estado_civil):
                resultado += self.generar_html_datos_pareja_poderdante()

            if index < self.cantidad_poderdantes - 2:
                resultado += ', '
            if index == self.cantidad_poderdantes - \
                    1 and self.cantidad_poderdantes > 1:
                resultado += '; '
            if index < self.cantidad_poderdantes == 1:
                resultado += '; '
        return resultado

    def generar_html_datos_pareja_poderdante(self):
        resultado = ''
        resultado += f' y <b>{self.pareja_poderdante.nombre.upper()}</b>, mayor de edad, '
        resultado += f'{self.pareja_poderdante.identificado} con '
        resultado += f'<b>{self.pareja_poderdante.tipo_identificacion}</b> No. '
        resultado += f'<b>{self.pareja_poderdante.numero_identificacion}</b> de '
        resultado += f'<b>{self.pareja_poderdante.ciudad_expedicion_identificacion.upper()}'
        resultado += '</b>, de estado civil '
        resultado += f'<b>{self.pareja_poderdante.estado_civil_genero_pareja.upper()}</b> '
        resultado += f'y {self.pareja_poderdante.domiciliado} en '
        resultado += f'<b>{self.pareja_poderdante.domicilio_municipio.upper()}, '
        resultado += f'{self.pareja_poderdante.domicilio_departamento.upper()}, '
        resultado += f'{self.pareja_poderdante.domicilio_pais.upper()}</b>'
        return resultado

    def generar_html_datos_apoderado(self):
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if poderdante.estado_civil == 'Soltero sin unión marital de hecho':
                t_conferir = 'confiero'
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_conferir = 'confiero'
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_conferir = 'conferimos'
                t_nuestro = 'nuestro'
        elif self.cantidad_poderdantes == 2:
            t_conferir = 'conferimos'
            t_nuestro = 'nuestro'

        resultado = ''
        resultado += f'mediante el presente escrito, {t_conferir} <b>PODER ESPECIAL, AMPLIO Y '
        resultado += f'SUFICIENTE</b> a <b>{self.apoderado.nombre.upper()}</b>, mayor de edad, '
        resultado += f'{self.apoderado.identificado} con '
        resultado += f'<b>{self.apoderado.tipo_identificacion}</b> No. <b>'
        resultado += f'{self.apoderado.numero_identificacion}</b> de <b>'
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion.upper()},</b> para que, en '
        resultado += f'{t_nuestro} nombre y representación, efectúe los siguientes actos: '
        resultado += '</p></div>'
        return resultado

    def generar_html_adquisicion_de_inmuebles(self):
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if poderdante.estado_civil == 'Soltero sin unión marital de hecho':
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_nuestro = 'nuestro'
        elif self.cantidad_poderdantes == 2:
            t_nuestro = 'nuestro'

        if self.multiples_inmuebles():
            t_inmuebles = 'los bienes inmuebles identificados'
        else:
            t_inmuebles = 'el bien inmueble identificado'
        resultado = ''
        resultado += f'Para que adquiera a {t_nuestro} nombre, por el título y el modo que '
        resultado += f'considere pertinente, {t_inmuebles} en la parte inicial de este '
        resultado += 'documento, con facultades para:<br>'
        resultado += self.generar_html_incisos_seccion_inmuebles()
        return resultado

    def generar_html_facultad_inciso_celebracion_de_contrato(self):
        resultado = ''
        resultado += 'Celebrar el contrato de promesa de compraventa o el encargo fiduciario '
        resultado += 'según el caso, así como modificarlos a través de otrosí.'
        return resultado

    def generar_html_facultad_inciso_firma_de_escritura(self):
        resultado = ''
        resultado += 'Firmar la escritura de compraventa; o transferencia a otro título según '
        resultado += 'el caso, y ratificarla, aclararla o modificarla en caso de requerirse.'
        return resultado

    def generar_html_facultad_inciso_firma_de_acta(self):
        resultado = ''
        if self.multiples_inmuebles():
            t_inmuebles = 'los inmuebles'
        else:
            t_inmuebles = 'el inmueble'
        resultado += f'Recibir {t_inmuebles} y firmar el acta de entrega u otro documento similar '
        resultado += 'en caso de requerirse.'
        return resultado

    def generar_html_suscribir_los_documentos(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'de los inmuebles'
        else:
            t_inmuebles = 'del inmueble'
        resultado = ''
        resultado += 'Suscribir todos los documentos precontractuales y contractuales que se '
        resultado += f'requieran para el perfeccionamiento de la adquisición {t_inmuebles}.'
        resultado += '<br></br>'
        return resultado

    def generar_html_seccion_celebracion_con_el_banco(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'los inmuebles objetos'
        else:
            t_inmuebles = 'el inmueble objeto'
        resultado = ''
        resultado += f'Para que celebre con {self.banco.nombre.upper()} el contrato mutuo para la '
        resultado += f'adquisición de {t_inmuebles} del presente mandato, con facultades para:<br>'
        resultado += self.generar_html_incisos_celebracion()
        return resultado

    def generar_html_inciso_diligenciar_documentos(self):
        resultado = ''
        resultado += 'Diligenciar, suscribir y presentar formularios o documentos para adelantar '
        resultado += 'la solicitud del crédito, tales como la declaración de origen de fondos, la '
        resultado += 'autorización de consulta ante los operadores de la información crediticia, '
        resultado += 'las declaraciones relacionadas con el conocimiento del cliente para la '
        resultado += 'prevención y control del lavado de activos, así como recibir la carta '
        resultado += 'de aprobación del crédito, la proyección de este mismo o cualquier '
        resultado += 'tipo de información relacionada con el crédito.'
        return resultado

    def generar_html_inciso_estipular_interes(self):
        resultado = ''
        resultado += 'Estipular tipo de interés, plazo y demás condiciones del crédito.'
        return resultado

    def generar_html_inciso_seguros_exigidos(self):
        resultado = ''
        resultado += f'Tomar los seguros exigidos por {self.banco.nombre.upper()}, o endosar '
        resultado += 'pólizas a su favor.'
        return resultado

    def generar_html_inciso_firmar_pagare(self):
        resultado = ''
        resultado += 'Firmar pagaré diligenciado y/o en blanco, carta de instrucciones y demás '
        resultado += f'documentos requeridos por {self.banco.nombre.upper()}, incluyendo los '
        resultado += 'documentos necesarios para tramitar subsidios de tasa u otros que ofrezca '
        resultado += 'el Gobierno Nacional.'
        return resultado

    def generar_html_inciso_constituir_hipoteca(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'los inmuebles'
        else:
            t_inmuebles = 'el inmueble'
        resultado = ''
        resultado += 'Constituir hipoteca abierta, de primer grado, sin límite en la cuantía '
        resultado += f'sobre {t_inmuebles} objeto de financiación.'
        return resultado

    def generar_html_inciso_recibir_valor_del_credito(self):
        resultado = ''
        resultado += 'Recibir el valor del crédito o autorizar el giro de este a un tercero.'
        return resultado

    def generar_html_inciso_abrir_cuenta(self):
        resultado = ''
        resultado += 'Abrir cuenta de ahorros para el desembolso del crédito y el pago de las '
        resultado += 'cuotas mensuales de amortización.'
        return resultado

    def generar_html_inciso_suscribir_los_documentos(self):
        resultado = ''
        resultado += 'Suscribir todos los documentos precontractuales y contractuales que se '
        resultado += 'requieran para la adquisición del crédito y la constitución de la '
        resultado += 'garantía hipotecaría.<br></br>'
        return resultado

    def generar_html_seccion_declaracion_del_precio(self):
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if poderdante.estado_civil == 'Soltero sin unión marital de hecho':
                nuestro = 'mi'
                t_declaramos = 'declaro'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                nuestro = 'mi'
                t_declaramos = 'declaro'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_declaramos = 'declaramos'
                if self.apoderado.genero == 'Masculino':
                    nuestro = 'nuestro'
                elif self.apoderado.genero == 'Femenino':
                    nuestro = 'nuestra'
        elif self.cantidad_poderdantes == 2:
            t_declaramos = 'declaramos'
            if self.apoderado.genero == 'Masculino':
                nuestro = 'nuestro'
            elif self.apoderado.genero == 'Femenino':
                nuestro = 'nuestra'

        if self.multiples_inmuebles():
            inmuebles = 'inmuebles'
            t_inmuebles = f'los {inmuebles}'
            los_inmuebles = f'de los {inmuebles}'
        else:
            inmuebles = 'inmueble'
            t_inmuebles = f'el {inmuebles}'
            los_inmuebles = f'del {inmuebles}'

        resultado = ''
        resultado += f'En cumplimiento a lo establecido en la ley, {t_declaramos} bajo la gravedad '
        resultado += 'del juramento que el precio incluido en la escritura pública que '
        resultado += f'{self.apoderado.la} {self.apoderado.assignee} suscribirá en virtud del '
        resultado += 'presente poder es real y no ha sido objeto de pactos privados en los que se '
        resultado += f'señale un valor diferente. En caso de que tales pactos existan, {nuestro} '
        resultado += f'{self.apoderado.assignee} obrando en la calidad indicada, informará al '
        resultado += f'Notario el precio convenido en ellos. {nuestro.capitalize()} '
        resultado += f'{self.apoderado.assignee} queda {self.apoderado.facultado} para transmitir '
        resultado += 'esta declaración juramentada en la escritura pública, e igualmente queda '
        resultado += f'{self.apoderado.facultado} para que en la escritura que suscriba, declare '
        resultado += 'que no existen sumas que se hayan convenido o facturado por fuera de la '
        resultado += 'misma o, de lo contrario,  manifestará su valor. Así mismo, teniendo en '
        resultado += f'cuenta que {t_inmuebles} adquiridos a través de fondos, fiducias, esquemas '
        resultado += 'de promoción inmobiliaria o semejantes se encuentran sometidos a lo previsto '
        resultado += 'en la ley, y que en tales casos los beneficiarios de las unidades '
        resultado += 'inmobiliarias son considerados como adquirentes de los bienes raíces, '
        resultado += f'{nuestro} {self.apoderado.assignee} queda {self.apoderado.facultado} para '
        resultado += f'declarar el valor de mercado {los_inmuebles}.<br></br>'
        return resultado

    def generar_html_seccion_respuesta_a_indagacion(self):
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if poderdante.estado_civil == 'Soltero sin unión marital de hecho':
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                if self.apoderado.genero == 'Masculino':
                    t_nuestro = 'nuestro'
                elif self.apoderado.genero == 'Femenino':
                    t_nuestro = 'nuestra'
        elif self.cantidad_poderdantes == 2:
            if self.apoderado.genero == 'Masculino':
                t_nuestro = 'nuestro'
            elif self.apoderado.genero == 'Femenino':
                t_nuestro = 'nuestra'
        if self.multiples_inmuebles():
            inmuebles = 'de los inmuebles adquiridos y mencionados'
        else:
            inmuebles = 'del inmueble adquirido y mencionado'

        resultado = ''
        resultado += f'{t_nuestro.capitalize()} {self.apoderado.assignee} también se '
        resultado += f'encuentra expresamente {self.apoderado.facultado} para '
        resultado += f'determinar la afectación a vivienda familiar o no {inmuebles} en este '
        resultado += 'documento, en los términos de la Ley 258 de 1996 modificada por la Ley 854 '
        resultado += 'de 2003, y/o la norma que la modifique o reglamente y también se '
        resultado += f'encuentra expresamente {self.apoderado.facultado} para determinar '
        resultado += 'la constitución o no de patrimonio familiar bajo los '
        resultado += 'supuestos legales correspondientes para tal efecto.'

        if self.declaraciones.pareja_hace_parte_compraventa == "Si":
            resultado += '<br></br>'
        if not self.declaraciones.pareja_hace_parte_compraventa:
            resultado += '<br></br>'
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                resultado += self.generar_html_paragrafo()
        return resultado

    def generar_html_paragrafo(self):
        if self.multiples_inmuebles():
            inmuebles = 'inmuebles'
            mencionados = f'los {inmuebles} mencionados'
            señalados = f'los {inmuebles} antes señalados sean afectados'
            anteriores = f'los anteriores bienes {inmuebles}.'
        else:
            inmuebles = 'inmueble'
            mencionados = f'el {inmuebles} mencionado'
            señalados = f'el {inmuebles} antes señalado sea afectado'
            anteriores = f'el anterior bien {inmuebles}.'

        resultado = ''
        resultado += '<div class="paragrafo"><p><b><br>Parágrafo:</b> '
        resultado += f'En los mismos términos, yo, <b>{self.pareja_poderdante.nombre.upper()}'
        resultado += f',</b> {self.pareja_poderdante.identificado} con <b>'
        resultado += f'{self.pareja_poderdante.tipo_identificacion}</b> No. '
        resultado += f'<b>{self.pareja_poderdante.numero_identificacion}</b> de '
        resultado += f'<b>{self.pareja_poderdante.ciudad_expedicion_identificacion.upper()}</b>, '
        resultado += f'de estado civil <b>{self.pareja_poderdante.estado_civil_genero_pareja}</b>'
        resultado += f', en mi calidad de cónyuge o {self.pareja_poderdante.companero} '
        resultado += 'permanente del adquirente otorgo poder especial, amplio y suficiente a '
        resultado += f'<b>{self.apoderado.nombre.upper()},</b> {self.apoderado.identificado} con '
        resultado += f'<b>{self.apoderado.tipo_identificacion}</b> No. <b>'
        resultado += f'{self.apoderado.numero_identificacion}</b> de <b>'
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion.upper()},</b> para que en mi '
        resultado += 'nombre y representación responda acerca de la indagación de qué trata la '
        resultado += 'Ley 258 de 1996 modificada por la Ley 854 de 2003, y/o demás normas '
        resultado += f'concordantes, por lo que <b>{self.declaraciones.afectar_vivienda_familiar}'
        resultado += f'</b> acepto afectar a vivienda familiar {mencionados} en la '
        resultado += f'parte inicial de este documento.</br><br>En caso de que {señalados} a '
        resultado += 'vivienda familiar, declaro aceptar expresamente la hipoteca que '
        resultado += 'se constituye a favor del banco o entidad financiera sobre '
        resultado += f'{anteriores}</br></p></div>'
        return resultado

    def generar_html_seccion_tramites_de_credito_hipotecario(self):
        if self.cantidad_poderdantes == 1:
            poderdante = self.poderdantes[0]
            if poderdante.estado_civil == 'Soltero sin unión marital de hecho':
                t_estuvieramos = 'estuviera presente'
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_estuvieramos = 'estuviera presente'
                t_nuestro = 'mi'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                t_estuvieramos = 'estuviéramos presentes'
                if self.apoderado.genero == 'Masculino':
                    t_nuestro = 'nuestro'
                elif self.apoderado.genero == 'Femenino':
                    t_nuestro = 'nuestra'
        elif self.cantidad_poderdantes == 2:
            t_estuvieramos = 'estuviéramos presentes'
            if self.apoderado.genero == 'Masculino':
                t_nuestro = 'nuestro'
            elif self.apoderado.genero == 'Femenino':
                t_nuestro = 'nuestra'

        if self.multiples_inmuebles():
            t_inmuebles = 'de los inmuebles'
        else:
            t_inmuebles = 'del inmueble'

        resultado = ''
        resultado += f'{t_nuestro.capitalize()} {self.apoderado.assignee} queda '
        resultado += f'{self.apoderado.facultado} para realizar cualquier acto '
        resultado += f'relacionado con el presente mandato, como si {t_estuvieramos}, '
        resultado += 'aunque no se haya enunciado en forma expresa en este poder, de '
        resultado += 'tal forma que no quede sin representación en ninguna actuación'
        resultado += ' que se requiera y que tenga relación directa con la '
        resultado += f'adquisición {t_inmuebles} y los trámites de crédito '
        resultado += f'hipotecario ante {self.banco.nombre.upper()}.'
        return resultado

    def generar_html_incisos_seccion_inmuebles(self):
        resultado = ''
        textos_incisos = [
            self.generar_html_facultad_inciso_celebracion_de_contrato(),
            self.generar_html_facultad_inciso_firma_de_escritura(),
            self.generar_html_facultad_inciso_firma_de_acta(),
            self.generar_html_suscribir_los_documentos()
        ]
        resultado += '<ol class="incisos_seccion_inmuebles">'
        for texto in textos_incisos:
            resultado += f'<li>{texto}</li>'
        resultado += "</ol>"
        return resultado

    def generar_html_numerales(self):
        resultado = ''
        textos_incisos = []
        textos_incisos.append(self.generar_html_adquisicion_de_inmuebles())
        textos_incisos.append(
            self.generar_html_seccion_celebracion_con_el_banco())
        textos_incisos.append(
            self.generar_html_seccion_declaracion_del_precio())
        textos_incisos.append(
            self.generar_html_seccion_respuesta_a_indagacion())
        textos_incisos.append(
            self.generar_html_seccion_tramites_de_credito_hipotecario())

        resultado += '<ol class="seccion_numerales">'
        for texto in textos_incisos:
            resultado += f'<li><p>{texto}</p></li>'
        resultado += "</ol>"
        return resultado

    def generar_html_incisos_celebracion(self):
        resultado = ""
        textos_incisos = [
            self.generar_html_inciso_diligenciar_documentos(),
            self.generar_html_inciso_estipular_interes(),
            self.generar_html_inciso_seguros_exigidos(),
            self.generar_html_inciso_firmar_pagare(),
            self.generar_html_inciso_constituir_hipoteca(),
            self.generar_html_inciso_recibir_valor_del_credito(),
            self.generar_html_inciso_abrir_cuenta(),
            self.generar_html_inciso_suscribir_los_documentos()
        ]
        resultado += '<ol class="incisos_celebracion">'
        for texto in textos_incisos:
            resultado += f'<li>{texto}</li>'
        resultado += "</ol>"
        return resultado

    def generar_html_lugar_y_fecha(self):
        if self.declaraciones.fecha_firma:
            fecha = datetime.strptime(
                self.declaraciones.fecha_firma, "%d/%m/%Y").date()
            dia = fecha.day
            mes = MESES_INGLES_ESPANOL[fecha.strftime('%B')]
            anio = fecha.year
        else:
            dia = "_____"
            mes = "_____"
            anio = "_____"

        if self.declaraciones.municipio_firma and self.declaraciones.departamento_firma and self.declaraciones.pais_firma:
            t_lugar_firma = f"{self.declaraciones.municipio_firma}, {self.declaraciones.departamento_firma}, {self.declaraciones.pais_firma}"
        else:
            t_lugar_firma = "__________________"

        resultado = ""
        resultado += '<div class="lugar_y_fecha_de_firma"><p>'
        resultado += f"Para constancia, se firma en {t_lugar_firma} a los {dia} días "
        resultado += f"del mes de {mes} del {anio}.</p></div>"
        return resultado

    def generar_html_firmas(self):
        resultado = ""
        for poderdante in self.poderdantes:
            resultado += '<div class="firmas_poderdantes">'
            resultado += "_____________________________"
            resultado += f"<br><b>{poderdante.nombre}</b><br>"
            resultado += f"{poderdante.tipo_identificacion} No. {poderdante.numero_identificacion}"
            resultado += '</div><br><br><br>'

        if self.cantidad_poderdantes == 1:
            if self.declaraciones.pareja_hace_parte_compraventa == 'No' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                resultado += ''
                resultado += '<div class="firma_pareja">'
                resultado += '_____________________________'
                resultado += f'<br><b>{self.pareja_poderdante.nombre}</b>'
                resultado += f'<br>{self.pareja_poderdante.tipo_identificacion} No. '
                resultado += f'{self.pareja_poderdante.numero_identificacion}</div>'
                resultado += '<br><br>'
            elif self.declaraciones.pareja_hace_parte_compraventa == 'Si' \
                    and self.estado_civil_es_union(poderdante.estado_civil):
                resultado += ''
                resultado += '<div class="firma_pareja">'
                resultado += '_____________________________'
                resultado += f'<br><b>{self.pareja_poderdante.nombre}</b>'
                resultado += f'<br>{self.pareja_poderdante.tipo_identificacion} No. '
                resultado += f'{self.pareja_poderdante.numero_identificacion}</div>'
                resultado += '<br><br>'

        resultado += '<div class="acepto"><p>Acepto,</p></div>'
        resultado += '<div class="firma_apoderado">'
        resultado += '_____________________________'
        resultado += f'<br><b>{self.apoderado.nombre}</b><br>'
        resultado += f'{self.apoderado.tipo_identificacion} No. '
        resultado += f'{self.apoderado.numero_identificacion}</div>'
        return resultado
    
    def generar_estilos(self):
        resultado = ''
        resultado += '<style>div.titulo {text-align: center; font-weight: bold; font-size: 17px; '
        resultado += 'font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.datos_inmuebles {text-align: left; font-size: 16px; '
        resultado += 'font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.parrafo_poderdantes {text-align: justify; font-size: 16px; '
        resultado += 'font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'ol ::marker {font-weight: bold;}'
        resultado += 'li {text-align: justify;}'
        resultado += 'ol.seccion_numerales {text-align: justify; font-size: 16px; '
        resultado += 'font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'ol.incisos_seccion_inmuebles {text-align: justify; font-size: 16px; '
        resultado += 'list-style: lower-alpha; font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'ol.incisos_celebracion {text-align: justify; font-size: 16px; '
        resultado += 'list-style: lower-alpha; font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.lugar_y_fecha_de_firma {font-size: 16px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif; margin-bottom: 60px;}'
        resultado += 'div.firmas_poderdantes {font-size: 16px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif; margin-top: 20px; line-height: 0.4cm;}'
        resultado += 'div.acepto {font-size: 16px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif; margin-top: 10px; margin-bottom: 60px}'
        resultado += 'div.firma_apoderado {font-size: 16px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif; margin-top: 20px; line-height: 0.4cm;}'
        resultado += 'div.firma_pareja {font-size: 16px; font-family: Arial, Helvetica, '
        resultado += 'sans-serif; margin-top: 20px; line-height: 0.4cm;}'
        resultado += 'div.padding {padding-top: 50px; padding-right: 50px; padding-bottom: '
        resultado += '30px; padding-left: 50px;}</style>'
        return resultado
