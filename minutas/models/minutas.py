from typing import List

from utils.document import Document
from .apoderado import Apoderado
from .poderdante import Poderdante
from .banco import Banco
from .depositos import Deposito
from .parqueaderos import Parqueadero
from .inmueble import InmueblePrincipal
from . escritura import Escritura


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
        'generar_html_direccion_inmueble',
        'generar_html_datos_inmueble',
        'generar_html_regimen_propiedad_horizontal',
        'generar_html_paragrafo_primero',
        'generar_html_paragrafo_segundo',
        'generar_html_titulo_adquisicion'

    ]

    def __init__(self,
                 apoderado: Apoderado,
                 poderdante: Poderdante,
                 banco: Banco,
                 inmueble: InmueblePrincipal,
                 depositos: List[Deposito],
                 parqueaderos: List[Parqueadero],
                 escrituras: List[Escritura]
                 ):
        self.apoderado = apoderado
        self.poderdante = poderdante
        self.banco = banco
        self.inmueble = inmueble
        self.depositos = depositos
        self.parqueaderos = parqueaderos
        self.escrituras = escrituras

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
        resultado += '<title>Minuta</title>'
        resultado += '<div class="titulo"><p>'
        resultado += '<b>---------------------------------------'
        resultado += 'CONTRATO DE HIPOTECA------------------------------------------</b></p></div>'
        return resultado

    def generar_html_parrafo_apoderado(self):
        resultado = ''
        resultado += f'<p>Presente nuevamente <b>{self.apoderado.nombre},</b> mayor de edad, '
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
        resultado += f'sin límite en su cuantía sobre {t_inmuebles} como cuerpo cierto:</p>'
        return resultado
    
    def generar_html_direccion_inmueble(self):
        resultado = ''
        resultado += f'<b>{self.inmueble.nombre} {self.inmueble.numero} {self.inmueble.direccion}'
        resultado += '</b>'
        return resultado
    
    def generar_html_datos_inmueble(self):
        resultado = ''
        resultado += '<p>Inmueble identificado con el folio de matrícula inmobiliaria No. '
        resultado += f'<b>{self.inmueble.matricula}</b> de la Oficina de Registro de '
        resultado += f'Instrumentos Públicos de <b>{self.inmueble.municipio_de_registro_orip}</b> '
        resultado += f'y ficha catastral No. <b>{self.inmueble.numero_ficha_catastral} '
        resultado += f'{self.inmueble.tipo_ficha_catastral}.</b></p>'
        return resultado

    def generar_html_regimen_propiedad_horizontal(self):
        resultado = ''
        resultado += '<p><b>RÉGIMEN DE PROPIEDAD HORIZONTAL:</b> El inmueble objeto de la '
        resultado += 'presente hipoteca fue sometido al régimen legal de propiedad horizontal, '
        resultado += 'de conformidad con la Ley 675 de agosto 3 de 2001 por medio de la '
        resultado += f'<b>{self.escrituras[0].nombre} No. {self.escrituras[0].numero} Del '
        resultado += f'{self.escrituras[0].fecha}</b> adicionado mediante la '
        resultado += f'<b>{self.escrituras[1].nombre} No. {self.escrituras[1].numero} Del '
        resultado += f'{self.escrituras[1].fecha}</b>, debidamente registrada en el Folio de '
        resultado += f'Matrícula Inmobiliaria No. <b>{self.inmueble.matricula}</b> de la '
        resultado += 'Oficina de Registro de Instrumentos Públicos de '
        resultado += f'<b>{self.inmueble.municipio_de_registro_orip}.</b></p>'
        return resultado
    
    def generar_html_paragrafo_primero(self):
        resultado = ''
        resultado += '<p><b>PARÁGRAFO PRIMERO:</b> La hipoteca se extiende a muebles que por '
        resultado += 'accesión al inmueble hipotecado se reputen inmuebles, a todas las '
        resultado += 'edificaciones, mejoras e instalaciones existentes y a las que llegaren '
        resultado += 'a levantarse o a integrarse a el inmueble en el futuro y se extiende '
        resultado += 'también a las pensiones devengadas por el arrendamiento de los bienes '
        resultado += 'hipotecados y a la indemnización debida por las aseguradoras de este bien, '
        resultado += 'según los artículos 2445 y 2446 del Código Civil. ------<br>'
        return resultado

    def generar_html_paragrafo_segundo(self):
        resultado = ''
        resultado += '<b>PARÁGRAFO SEGUNDO:</b> El producto inicial del mutuo se destinará '
        resultado += 'de conformidad con la ley 546 de 1999 a la adquisición de vivienda nueva o '
        resultado += 'usada, o la construcción de vivienda individual, o al mejoramiento de esta '
        resultado += 'tratándose de vivienda de interés social. ------<br>'
        return resultado
    
    def generar_html_titulo_adquisicion(self):
        resultado = ''
        resultado += '<b>SEGUNDO: TÍTULO DE ADQUISICIÓN:</b> Que el inmueble dado en '
        resultado += 'garantía hipotecaria fue adquirido por la PARTE HIPOTECANTE por medio '
        resultado += 'de la presente escritura pública. ------<br></p>'
        return resultado