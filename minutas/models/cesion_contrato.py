from typing import List

from num2words import num2words
from utils.document import Document
from utils.exceptions import ValidationError
from utils.validators import Validator

from .apoderado import Apoderado
from .apoderado_banco import ApoderadoBanco
from .depositos import Deposito
from .inmueble import InmueblePrincipal
from .parqueaderos import Parqueadero
from .poderdantes import Poderdante
from .representante_banco import RepresentanteBanco
from .banco import Banco
from .prestamo import Prestamo
from .constructora import Constructora
from .compraventa import Compraventa

class DocumentoCesionContrato(Document):
    apoderado: Apoderado
    poderdantes: List[Poderdante]
    inmueble: InmueblePrincipal
    depositos: List[Deposito]
    parqueaderos: List[Parqueadero]
    apoderado_banco: ApoderadoBanco
    representante_banco: RepresentanteBanco
    banco: Banco
    prestamo: Prestamo
    constructora: Constructora
    compraventa: Compraventa

    generate_html_functions = [
        'generar_titulo_documento',
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
        prestamo: Prestamo,
        constructora: Constructora,
        compraventa: Compraventa
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
        self.constructora = constructora
        self.compraventa = compraventa

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
    
    def generar_titulo_documento(self):
        resultado = ''
        resultado += '<title>Cesión del contrato</title>'
        resultado += '<div class="titulo"><p>'
        resultado += '<b>CESIÓN DEL CONTRATO PROMESA DE COMPRAVENTA</b></p></div>'
        return resultado
    
    def generar_datos_apoderado(self):
        resultado = ''
        resultado += '<p>Entre los suscritos a saber: de una parte, '
        resultado += f'<b>{self.apoderado.nombre.upper()},</b> mayor de edad, '
        resultado += f'{self.apoderado.identificado} con <b> {self.apoderado.tipo_identificacion} '
        resultado += f'No. {self.apoderado.numero_identificacion} de '
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion},</b> hábil para '
        resultado += 'contratar y obligarse, quien actúa en nombre y representación de '
        return resultado
    
    def generar_datos_poderdantes(self):
        resultado = ''
        for index, poderdante in enumerate(self.poderdantes):

            if index == len(self.poderdantes) - \
                    1 and len(self.poderdantes) > 1:
                resultado += ' y '
            resultado += f'<b>{poderdante.nombre.upper()},</b> mayor de edad, '
            resultado += f'{poderdante.identificado} con {poderdante.tipo_identificacion} <b>No. '
            resultado += f'{poderdante.numero_identificacion} de '
            resultado += f'{poderdante.ciudad_expedicion_identificacion},</b> '
            resultado += f'{poderdante.domiciliado} {poderdante.residenciado} en '
            resultado += f'<b>{poderdante.domicilio},</b> de estado civil '
            resultado += f'<b>{poderdante.estado_civil_genero};</b> en su calidad de '
        return resultado

    def generar_datos_apoderado_banco(self):
        resultado = ''
        resultado += f'y de otra parte, '
        return resultado
    
    def generar_datos_representante_banco(self):
        resultado = ''
        resultado += ''
        return resultado
    
    def generar_constitucion_banco_union(self):
        resultado = ''
        resultado += f'de <b>{self.banco.nombre.upper()}</b> antes <b>GIROS & FINANZAS COMPAÑÍA DE '
        resultado += 'FINANCIAMIENTO S.A.</b>, sociedad con domicilio principal en Cali, '
        resultado += 'identificada Tributariamente con NIT número 860.006.797-9, sociedad '
        resultado += 'constituida legalmente mediante Escritura Pública No. 5938 del 05 de '
        resultado += 'diciembre de 1963, otorgada en la Notaria Cuarta (04) del Círculo de Bogotá, '
        resultado += 'inscrita en la Cámara de Comercio de Cali, el 7 de noviembre de 2000, bajo el '
        resultado += 'número 7516 del Libro IX, sociedad convertida a establecimiento Bancario y '
        resultado += 'modificada su razón social mediante Escritura Pública No. 3140 del 16 de '
        resultado += 'Junio de 2022, otorgada en la Notaría Cuarta del Círculo de Cali, inscrita en '
        resultado += 'la Cámara de Comercio de Cali el 28 de Junio de 2022, bajo el No. 12001 del '
        resultado += 'Libro todo lo cual se acredita con el Certificado de Existencia y '
        resultado += 'Representación Legal expedido por la Cámara de Comercio de Cali y por la '
        resultado += 'Superintendencia Finaciera, quien para los efectos del presente contraro se '
        resultado += 'denominará la <b>CESIONARIA,</b> por medio del presente documento convenimos '
        resultado += 'celebrar cesión de contrato de promesa de compraventa que se regirá por las '
        resultado += 'siguientes cláusulas:----------------------------------------------------</p>'
        return resultado
    
    def generar_clausula_antecedentes(self):
        resultado = ''
        resultado += '<b>PRIMERA ANTECEDENTES:</b><br><br>'
        return resultado
    
    def generar_datos_constructora(self):
        if len(self.poderdantes) > 1:
            cedentes = '<b>LOS CEDENTES</b> suscribieron'
        elif len(self.poderdantes) == 1:
            cedentes = '<b>EL CEDENTE</b> souscribió'
        resultado = ''
        resultado += f'<ol><li>{cedentes} con la sociedad <b>{self.constructora.nombre.upper()}'
        resultado += f'</b>, identificada tributariamente con NIT <b>{self.constructora.nit},</b> '
        resultado += f'contrato de promesa de compraventa suscrita <b>el {},</b> '
        return resultado
    
    def generar_datos_inmuebles(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
            inmuebles_identifcados = 'inmuebles identificados las matrículas inmobiliarias '
            fichas = 'fichas catastrales'
            individuales = 'Individuales respectivamente'
        else:
            inmuebles = 'el inmueble'
            inmuebles_identifcados = 'inmueble identificado la matrícula inmobiliaria '
            fichas = 'ficha catastral'
            individuales = 'Individual'
        resultado = ''
        resultado += f'contrato que versa sobre {inmuebles}: <b>{self.inmueble.nombre} '
        resultado += f'{self.inmueble.numero}, '
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f'{parqueadero.nombre} {parqueadero.numero}, '
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'{deposito.nombre} {deposito.numero}, '
        resultado += f'{self.inmueble.direccion}, {self.inmueble.ciudad_y_o_departamento},</b> '
        resultado += f'{inmuebles_identifcados}: <b>{self.inmueble.matricula} '
        if self.parqueaderos:
            resultado += f'{parqueadero.matricula},</b> '
        if self.depositos:
            resultado += f'{deposito.matricula},</b> '
        resultado += f'de la Oficina de Registro de Instrumentos Públicos de '
        resultado += f'{self.inmueble.municipio_de_registro_orip} y '
        if self.inmueble.tipo_ficha_catastral == 'Mayor Extensión':
            resultado += f'{fichas} <b>No. {self.inmueble.numero_ficha_catastral} Folio de '
            resultado += 'Mayor Extensión.</b>'
        elif self.inmueble.tipo_ficha_catastral == 'Individual':
            resultado += f'{fichas} <b>No. {self.inmueble.numero_ficha_catastral}</b> '
            if self.parqueaderos:
                resultado += f'<b>{parqueadero.numero_ficha_catastral}</b>'
            if self.depositos:
                resultado += f'<b>{deposito.numero_ficha_catastral}</b>'
            resultado += f'{individuales}'
        return resultado

    def generar_solicitud_credito_a_banco(self):
        if len(self.poderdantes) > 1:
            cedentes = '<b>LOS CEDENTES</b> solicitaron'
        elif len(self.poderdantes) == 1:
            cedentes = '<b>EL CEDENTE</b> solicitó'
        resultado = ''
        resultado += f'<li>{cedentes} a {self.banco.nombre} crédito de vivienda, '
        resultado += 'para cubrir el pago del precio de la promesa de compraventa '
        resultado += 'descrita en el numeral anterior, el cual le fue aprobado en la '
        resultado += 'modalidad de Leasing Habitacional.</li></ol>'

    def generar_clausula_objeto(self):
        if len(self.poderdantes) > 1:
            cedentes = 'LOS CEDENTES'
            realizan = 'realizan'
        elif len(self.poderdantes) == 1:
            cedentes = 'EL CEDENTE'
            realizan = 'realiza'
        
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
        else:
            inmuebles = 'el inmueble'
        resultado = ''
        resultado += '<p><b>SEGUNDO OBJETO:</b> El objeto del presente contrato es la '
        resultado += f'cesión que <b>{cedentes}</b> {realizan} a favor de la <b>'
        resultado += 'CESIONARIA,</b> de su posición contractual en la promesa de '
        resultado += f'compraventa suscrita con la sociedad <b> {self.constructora.nombre} '
        resultado += f', identificada tributariamente con NIT {self.constructora.nit},</b> '
        resultado += 'cesión que recae también sobre los recursos entregados por parte del '
        resultado += 'cumplimiento de la promesa de compraventa objeto de la presente '
        resultado += f'cesión, los cuales ascienden a la suma de {self.compraventa.cuota_inicial} '
        resultado += f'contrato de promesa de compraventa suscrito el {}'
        resultado += f'contratos que versan sobre {inmuebles}: <b>{self.inmueble.nombre} '
        resultado += f'{self.inmueble.numero} '
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f', {parqueadero.nombre} {parqueadero.numero}, '
        if self.depositos:
            for deposito in self.depositos:
                resultado += f', {deposito.nombre} {deposito.numero}, '
        
        resultado += f'{self.inmueble.direccion} {self.inmueble.ciudad_y_o_departamento},</b> '
        return resultado
    
    def generar_matriculas(self):
        resultado = ''
        if self.multiples_inmuebles():
            inmuebles_identificados = 'inmuebles identificados con las matrículas inmobiliarias'
        else:
            inmuebles_identificados = 'inmueble identificado con la matrícula inmobiliaria'
        resultado += f'{inmuebles_identificados}: {self.inmueble.matricula}'
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f', {parqueadero.matricula}'
        if self.depositos:
            for deposito in self.depositos:
                resultado += f', {deposito.matricula} '
        
        resultado += f'de la Oficina de Registro de Instrumentos Púnlicos de Cali, y '
        return resultado
    
    def generar_fichas_catastrales(self):
        if self.multiples_inmuebles():
            fichas = 'fichas catastrales'
        else:
            fichas = '=ficha catastral'
        resultado = ''
        if self.inmueble.tipo_ficha_catastral == 'Mayor Extensión':
            resultado += f'{fichas} <b>No. {self.inmueble.numero_ficha_catastral} '
            resultado += 'Folio de Mayor Extensión</b>'
        elif self.inmueble.tipo_ficha_catastral == 'Individual':
            resultado += f'{fichas} No. {self.inmueble.numero_ficha_catastral} '
            if self.parqueaderos:
                for parqueadero in self.parqueaderos:
                    resultado += f'{parqueadero.numero_ficha_catastral}, '

        