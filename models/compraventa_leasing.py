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
from .inmueble import Inmueble
from .parqueaderos import Parqueadero
from .poderdantes import Poderdante
from .representante_banco import RepresentanteBanco
from .banco import BancoLeasing
from .aceptante import Aceptante
from .compraventa import CompraventaLeasing


class DocumentoCompraventaLeasing(Document):
    apoderado: Apoderado
    poderdantes: List[Poderdante]
    inmueble: Inmueble
    depositos: List[Deposito]
    parqueaderos: List[Parqueadero]
    apoderado_banco: ApoderadoBanco
    representante_banco: RepresentanteBanco
    banco: BancoLeasing
    # aceptante: Constructora
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
        'generar_limitaciones_gravamenes'
    ]

    def __init__(
        self,
        apoderado: Apoderado,
        poderdantes: List[Poderdante],
        inmueble: Inmueble,
        parqueaderos: List[Parqueadero],
        depositos: List[Deposito],
        apoderado_banco: ApoderadoBanco,
        representante_banco: RepresentanteBanco,
        banco: BancoLeasing,
        # aceptante: Constructora,
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
        # self.aceptante = aceptante
        self.compraventa = compraventa

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

    def generar_fichas_catastrales_seccion_inicial(self):
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
        number_to_word_leasing = num2words(
            self.compraventa.cantidad_compraventa, lang='es')
        number_format_leasing = f'{self.compraventa.cantidad_compraventa:,}'
        resultado = ''
        resultado += f'<p><b>CUANTÍA: {number_to_word_leasing} PESOS MCTE '
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

        matriculas = [self.inmueble.matricula]
        for parqueadero in self.parqueaderos:
            if self.parqueaderos and parqueadero.matricula:
                matriculas += [parqueadero.matricula]
        for deposito in self.depositos:
            if self.depositos and deposito.matricula:
                matriculas += [deposito.matricula]
        resultado = f'{inmuebles} No. <b><u>{", ".join(matriculas)}'
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
        resultado = ''
        resultado += '<p><b>SEGUNDO: Tradición del Inmueble:</b> El inmueble objeto del '
        resultado += 'presente estudio fue adquirido por <b>LOS VENDEDORES,</b> a '
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
            resultado += f'{poderdante.ciudad_expedicion_identificacion},</b>'
        resultado += 'quien ostentaba la calidad de promitente comprador, en virtud del '
        resultado += f'del contrato de promesa de compraventa suscrito <b>el {dia} de {mes} '
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
        resultado = ''
        resultado += '<b>CUARTO. - Limitaciones y Gravámenes:</b> Que los derechos de dominio '
        resultado += 'que se transfieren mediante la presente escritura, son de plena y '
        resultado += 'exclusiva propiedad del <b>VENDEDOR,</b> y que no han sido enajenados '
        resultado += 'por acto anterior al presente, que los inmuebles sobre los cuales recaen '
        resultado += 'actualmente los posee de manera regular, pacífica y pública y que dichos '
        resultado += 'inmuebles se hallan libres de censos, anticresis, servidumbres, '
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
        resultado += 'determine el _________________________.'
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
        resultado += f'Presente {self.apoderado_banco.doctor}, '
        resultado += f'<u><b>{self.apoderado_banco.nombre.upper()},</b></u> '
        resultado += f'{self.apoderado_banco.naturaleza}, mayor de edad, '
        resultado += f'{self.apoderado_banco.vecino} de <u><b>'
        resultado += f'{self.apoderado_banco.ciudad_residencia}</b></u> '
        resultado += f'{self.apoderado_banco.identificado} con '
        resultado += f'<u><b>{self.apoderado_banco.tipo_identificacion}</b></u> No. '
        resultado += f'<u><b>{self.apoderado_banco.numero_identificacion}</b></u> de '
        resultado += f'<u><b>{self.apoderado_banco.ciudad_expedicion_identificacion}</b>'
        resultado += '</u> quien comparece en este acto en su calidad de '
        resultado += f'<u><b>{self.apoderado_banco.apoderado} {self.apoderado_banco.tipo_apoderado}'
        resultado += f'</b></u> acorde con el Poder {self.apoderado_banco.tipo_apoderado} '
        if self.apoderado_banco.tipo_poder == 'Autenticado':
            resultado += f'a {self.apoderado_banco.el} conferido por '
        elif self.apoderado_banco.tipo_poder == 'Escriturado':
            resultado += 'constituido por '
            resultado += f'<u><b>{self.apoderado_banco.escritura}</b></u> debidamente '
            resultado += 'inscrito en la Cámara de Comercio de Cali según certificado '
            resultado += 'de la Existencia Representación legal que se protocoliza '
            resultado += 'con este instrumento, conferido por '
        return resultado