from utils.document import Document
from .apoderado import Apoderado
from .poderdante import Poderdante
from .banco import Banco
from .depositos import Deposito
from .parqueaderos import Parqueadero
from .inmueble import InmueblePrincipal


class DocumentoMinuta(Document):
    apoderado: Apoderado
    poderdante: Poderdante
    banco: Banco
    inmueble: InmueblePrincipal
    depositos: Deposito
    parqueaderos: Parqueadero

    generate_html_functions = [
        'generar_html_titulo_documento',
        'generar_html_parrafo_apoderado',
        'generar_html_parrafo_poderdante',

    ]

    def __init__(self,
                 apoderado,
                 poderdante,
                 banco,
                 inmueble,
                 depositos,
                 parqueaderos
                 ):
        self.apoderado = apoderado
        self.poderdante = poderdante
        self.banco = banco
        self.inmueble = inmueble
        self.depositos = depositos
        self.parqueaderos = parqueaderos

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

    def generar_html_titulo_documento(self):
        resultado = ''
        resultado += '<title>Poder</title>'
        resultado += '<div class="titulo"><p>'
        resultado += '<b>---------------------------------------'
        resultado += 'CONTRATO DE HIPOTECA------------------------------------------</b></p></div>'
        return resultado

    def generar_html_parrafo_apoderado(self):
        resultado = ''
        resultado += f'Presente nuevamente <b>{self.apoderado.nombre},</b> mayor de edad, '
        resultado += f'identificado con <b>{self.apoderado.tipo_identificacion}</b>'
        resultado += f'No. <b>{self.apoderado.numero_identificacion}</b> de '
        resultado += f'<b>{self.apoderado.ciudad_expedicion_identificacion}</b>, quien '
        resultado += 'al Poder General a él otorgado por medio de la Escritura Pública '
        resultado += 'No. 2962 del 16 de diciembre de 2019 Notaría Tercera de Bogotá D.C., '
        resultado += 'el cual se protocoliza con la presente escritura para los fines legales, '
        resultado += 'cuya vigencia, autenticidad y alcance se hace responsable; actúa en nombre y '
        resultado += 'representación de '
        return resultado

    def generar_html_parrafo_poderdante(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'los siguientes inmuebles, los cuales se hipotecan'
        else:
            t_inmuebles = 'el siguiente inmueble, el cual se hipoteca'

        resultado = ''
        resultado += f'<b>{self.poderdante.nombre},</b> mayor de edad, '
        resultado += f'{self.poderdante.identificado} con '
        resultado += f'<b>{self.poderdante.tipo_identificacion}</b> No. '
        resultado += f'<b>{self.poderdante.numero_identificacion}</b> de '
        resultado += f'<b>{self.poderdante.ciudad_expedicion_identificacion},</b> '
        resultado += f'de estado civil <b>{self.poderdante.estado_civil},</b> '
        resultado += f'{self.poderdante.domiciliado} y {self.poderdante.residenciado} en '
        resultado += f'<b>{self.poderdante.domicilio}</b>. Quien en el presente contrato '
        resultado += 'se denominará <b>LA PARTE HIPOTECANTE</b> y manifestó: <b>PRIMERO. '
        resultado += 'CONSTITUCIÓN DE HIPOTECA ABIERTA SIN LÍMITE DE CUANTÍA:</b> Que '
        resultado += '<b>LA PARTE HIPOTECANTE</b> con el propósito de garantizar a '
        resultado += f'<b>“{self.banco.nombre.upper()}”</b>, el pago del crédito de vivienda '
        resultado += 'a largo plazo, que éste le conceda, y ejercitando la facultad prevista '
        resultado += 'en el Artículo 2438 del Código Civil, constituye en favor de '
        resultado += f'<b>“{self.banco.nombre.upper()}”</b>, hipoteca abierta de primer grado '
        resultado += f'sin límite en su cuantía sobre {t_inmuebles} como cuerpo cierto:'
        return resultado

