from typing import List

from datetime import datetime
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
from utils.validating_dictionaries.dictionary_aceptante import dictionary_validator_aceptante
from utils.validating_dictionaries.dictionary_compraventa import dictionary_validator_compraventa

from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.catalogos import aceptantes
from catalogs.fechas import MESES_INGLES_ESPANOL

from .apoderado import Apoderado
from .apoderado_banco import ApoderadoBanco
from .depositos import Deposito
from .inmueble import InmueblePrincipal
from .parqueaderos import Parqueadero
from .poderdantes import Poderdante
from .representante_banco import RepresentanteBanco
from .banco import Banco
from .aceptante import Aceptante
from .compraventa import Compraventa


class DocumentoCompraventaLeasing(Document):
    apoderado: Apoderado
    poderdantes: List[Poderdante]
    inmueble: InmueblePrincipal
    depositos: List[Deposito]
    parqueaderos: List[Parqueadero]
    apoderado_banco: ApoderadoBanco
    representante_banco: RepresentanteBanco
    banco: Banco
    # aceptante: Constructora
    # compraventa: Compraventa

    generate_html_functions = [
        'generar_titulo_documento',
        'generar_datos_inmuebles',
        'generar_matriculas_inmobiliarias',
        'generar_fichas_catastrales'

    ]

    def __init__(
        self,
        apoderado: Apoderado,
        poderdantes: List[Poderdante],
        inmueble: InmueblePrincipal,
        parqueaderos: List[Parqueadero],
        depositos: List[Deposito],
        apoderado_banco: ApoderadoBanco,
        representante_banco: RepresentanteBanco,
        banco: Banco,
        # aceptante: Constructora,
        # compraventa: Compraventa
    ):
        self.apoderado = apoderado
        self.poderdantes = poderdantes
        self.inmueble = inmueble
        self.parqueaderos = parqueaderos
        self.depositos = depositos
        self.apoderado_banco = apoderado_banco
        self.representante_banco = representante_banco
        self.banco = banco
        # self.aceptante = aceptante
        # self.compraventa = compraventa

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
        resultado += 'VEINTITRÉS_______ (2023)<br>***************************<br> OTORGADA '
        resultado += 'ANTE LA NOTARÍA_______ DEL CIRCULO DE ***********************<br>'
        resultado += 'SUPERINTENDENCIA DE NOTARIADO Y REGISTRO<br>FORMATO DE CALIFICACION<br>'
        resultado += 'ACTO O CONTRATO: COMPRAVENTA *****************************<br>'
        resultado += 'PERSONAS QUE INTERVIENEN EN EL ACTO:<br>'
        resultado += 'VENDEDOR: ________________________________________.<br>'
        resultado += 'COMPRADOR:	BANCO UNIÓN********************'
        resultado += ''
        return resultado

    def generar_datos_inmuebles(self):
        resultado = ''
        resultado += f'INMUEBLE: {self.inmueble.nombre.upper()} {self.inmueble.numero}, '
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f'{parqueadero.nombre} {parqueadero.numero}, '
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'{deposito.nombre} {deposito.numero}, '
        resultado += f'{self.inmueble.direccion}</b></p></div>'
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
            matriculas_inmobiliarias = 'MATRÍCULAS INMOBILIARIAS'
        else:
            matriculas_inmobiliarias = 'MATRÍCULA INMOBILIARIA'

        matriculas = [self.inmueble.matricula]
        for parqueadero in self.parqueaderos:
            if self.parqueaderos and parqueadero.matricula:
                matriculas += [parqueadero.matricula]
        for deposito in self.depositos:
            if self.depositos and deposito.matricula:
                matriculas += [deposito.matricula]
        resultado = ''
        resultado += f'<b>{matriculas_inmobiliarias}: <b><u>{", ".join(matriculas)}'
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
                resultado += ', '.join([', '.join(ficha_values.values()) for ficha_values in fichas[:-1]])
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
    
    def generar_cuantia(self):
        resultado +=