from typing import List

import re
from num2words import num2words
from utils.exceptions import ValidationError

from utils.document import Document
from .apoderado import Apoderado
from .banco import Banco
from .depositos import Deposito
from .inmueble import InmueblePrincipal
from .parqueaderos import Parqueadero
from .poderdantes import Poderdante
from .apoderado_especial import ApoderadoEspecial
from .representante_legal import RepresentanteLegal


class DocumentoMinuta(Document):
    apoderado: Apoderado
    poderdantes: List[Poderdante]
    banco: Banco
    inmueble: InmueblePrincipal
    depositos: List[Deposito]
    parqueaderos: List[Parqueadero]
    apoderado_especial: ApoderadoEspecial
    representante_legal: RepresentanteLegal

    generate_html_functions = [
        'generar_titulo_documento',
        'generar_parrafo_apoderado',
        'generar_parrafo_poderdantes',
        'generar_primero_constitucion_hipoteca',
        'generar_direccion_inmueble',
        'generar_datos_inmueble',
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
        'generar_septimo_costos_y_gastos_judicianles',
        'generar_octavo_secuestre',
        'generar_noveno_vigencia_de_hipoteca',
        'generar_decimo_seguros',
        'generar_decimo_primero_convenio',
        'generar_decimo_segundo_poder',
        'generar_decimo_tercero_inputacion_de_pago',
        'generar_datos_apoderado_especial',
        'generar_datos_representante_legal',
        'generar_banco_union',
        'generar_aprobacion_credito_al_hipotecante',
        'generar_afectacion_vivienda_familiar',
        'generar_lectura_escritura_por_otorgantes',
        'generar_paz_y_salvo',
        'generar_firma_comprador',
        'generar_firma_hipotecante',
        'generar_firma_apoderado_especial',
        'generar_estilos'
    ]

    def __init__(
        self,
        apoderado: Apoderado,
        poderdantes: List[Poderdante],
        banco: Banco,
        inmueble: InmueblePrincipal,
        depositos: List[Deposito],
        parqueaderos: List[Parqueadero],
        apoderado_especial: ApoderadoEspecial,
        representante_legal: RepresentanteLegal
    ):
        self.apoderado = apoderado
        self.poderdantes = poderdantes
        self.banco = banco
        self.inmueble = inmueble
        self.depositos = depositos
        self.parqueaderos = parqueaderos
        self.apoderado_especial = apoderado_especial
        self.representante_legal = representante_legal
        self.validate_data()

    def validate_data(self):
        self.validar_poderdantes()

    def validar_poderdantes(self):
        if self.cantidad_poderdantes == 0 and self.cantidad_poderdantes > 2:
            raise ValidationError(
                'Debe haber al menos un poderdante y no más de dos poderdantes.')
        obligatorios = {
            "nombre": "nombre",
            "tipo_identificacion": "tipo de identificación",
            'tipo_identificacion_abreviacion': 'abreviación de tipo de identificación',
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

        atributos = poderdante.__dict__
        patron = r'[@_!#$%^&*()<>?/\|}{~:]'
        for atributo in atributos:
            if re.search(patron, atributos[atributo]):
                raise ValidationError(
                    f'Error en poderdantes: "{atributos[atributo]}" no puede contener carácteres especiales.')

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

    # TODO Pendiente en relación a la escritura, de momento se queda abierto linea 161
    def generar_parrafo_apoderado(self):
        resultado = ''
        resultado += '<div class="parrafos"><p>'
        resultado += f'Presente nuevamente <b>{self.apoderado.nombre},</b> mayor de edad, '
        resultado += f'identificado con <b>{self.apoderado.tipo_identificacion}</b> '
        resultado += f'No. <b>{self.apoderado.numero_identificacion}</b> de '
        resultado += f'<b>{self.apoderado.ciudad_expedicion_identificacion}</b>, quien '
        resultado += 'al Poder General a él otorgado por medio de la __________________ '
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
            resultado += f'<b>{poderdante.nombre},</b> mayor de edad, '
            resultado += f'{poderdante.identificado} con '
            resultado += f'<b>{poderdante.tipo_identificacion}</b> No. '
            resultado += f'<b>{poderdante.numero_identificacion}</b> de '
            resultado += f'<b>{poderdante.ciudad_expedicion_identificacion},</b> '
            resultado += f'de estado civil <b>{poderdante.estado_civil},</b> '
            resultado += f'{poderdante.domiciliado} y {poderdante.residenciado} en '
            resultado += f'<b>{poderdante.domicilio}</b>. '
        if len(self.poderdantes) == 1:
            resultado += 'Quien en el presente contrato se denominará '
        elif len(self.poderdantes) > 1:
            resultado += 'Quienes en el presente contrato se denominarán '
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
        resultado += f'<b>{self.inmueble.nombre.upper()} {self.inmueble.numero.upper()} '
        resultado += f'{self.inmueble.direccion.upper()} '
        resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}</b>'
        resultado += f'<p>{self.inmueble.linderos_especiales}</p>'
        return resultado

    def generar_direccion_parqueaderos(self):
        resultado = ''
        if self.parqueaderos:
            for parqueadero in self.parqueaderos:
                resultado += f'<b>{parqueadero.nombre.upper()} {parqueadero.numero} '
                resultado += f'{self.inmueble.direccion.upper()} '
                resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}</b>'
                resultado += f'<p>{parqueadero.linderos_especiales}</p>'
        return resultado

    def generar_direccion_depositos(self):
        resultado = ''
        if self.depositos:
            for deposito in self.depositos:
                resultado += f'<b>{deposito.nombre.upper()} {deposito.numero} '
                resultado += f'{self.inmueble.direccion.upper()} '
                resultado += f'{self.inmueble.ciudad_y_o_departamento.upper()}</b>'
                resultado += f'<p>{deposito.linderos_especiales}</p>'
        return resultado

    # TODO refactorizar
    def generar_datos_inmueble(self):
        resultado = ''
        resultado += '<p>Inmueble identificado con el folio de matrícula inmobiliaria No. '
        resultado += f'<b>{self.inmueble.matricula}</b> de la Oficina de Registro de '
        resultado += f'Instrumentos Públicos de <b>{self.inmueble.municipio_de_registro_orip}</b> '
        resultado += f'y ficha catastral No. <b>{self.inmueble.numero_ficha_catastral} '
        resultado += f'{self.inmueble.tipo_ficha_catastral}.</b></p>'
        return resultado

    # TODO pendiente el tema de las escrituras, de momento se queda abierto linea 251
    def generar_regimen_propiedad_horizontal(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'Los inmuebles objeto de la presente hipoteca fueron'
        else:
            t_inmuebles = 'El inmueble objeto de la presente hipoteca fue'
        resultado = ''
        resultado += f'<p><b>RÉGIMEN DE PROPIEDAD HORIZONTAL:</b> {t_inmuebles} al régimen '
        resultado += 'legal de propiedad horizontal, de conformidad con la Ley 675 de '
        resultado += 'agosto 3 de 2001 por medio de _______________________________ , '
        resultado += 'debidamente registrada en el Folio de Matrícula Inmobiliaria No. '
        resultado += f'<b>{self.inmueble.matricula}</b> de la Oficina de Registro '
        resultado += 'de Instrumentos Públicos de <b>'
        resultado += f'{self.inmueble.municipio_de_registro_orip}.</b></p>'
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
            t_inmuebles = 'los inmuebles dados'
        else:
            t_inmuebles = 'el inmueble dado'
        resultado = ''
        resultado += f'<b>SEGUNDO: TÍTULO DE ADQUISICIÓN:</b> Que {t_inmuebles} en '
        resultado += 'garantía hipotecaria fue adquirido por la PARTE HIPOTECANTE por medio '
        resultado += 'de la presente escritura pública. ------<br>'
        return resultado

    def generar_garantia_de_propiedad_y_libertad(self):
        if self.multiples_inmuebles():
            t_inmuebles = 'dichos inmuebles son'
        else:
            t_inmuebles = 'dicho inmueble es'
        resultado = ''
        resultado += '<b>TERCERO: GARANTÍA DE PROPIEDAD Y LIBERTAD:</b> Que garantiza que '
        resultado += f'{t_inmuebles} de su propiedad exclusiva, que no ha sido afectado '
        resultado += 'a vivienda familiar, ni dado en arrendamiento por escritura pública, '
        resultado += 'ni en anticresis y que se halla libre de hipotecas, embargos, censos, '
        resultado += 'condiciones resolutorias, registro por demanda civil, servidumbres '
        resultado += 'pasivas, uso o usufructo y cualquier otra clase de gravámenes o '
        resultado += 'desmembraciones; y que se obliga  a mantenerlo en este estado por todo '
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
        resultado += f'o jurídicas para con <b>{self.banco.nombre.upper()}------</b><br>'
        return resultado

    def generar_paragrafo_primero_aprobacion_de_credito(self):
        number_to_word_hipotecante = num2words(
            self.banco.prestamo_banco_a_hipotecante_en_numero, lang='es')
        number_format_hipotecante = f'{self.banco.prestamo_banco_a_hipotecante_en_numero:,}'

        number_to_word_constructora = num2words(
            self.banco.cantidad_dada_a_constructora_en_numero, lang='es')
        number_format_constructora = f'{self.banco.cantidad_dada_a_constructora_en_numero:,}'

        number_to_word_gastos = num2words(
            self.banco.gastos_de_gestion_en_numero, lang='es')
        number_format_gastos = f'{self.banco.gastos_de_gestion_en_numero:,}'

        if self.multiples_inmuebles():
            t_inmuebles = 'de los bienes inmuebles'
        else:
            t_inmuebles = 'del bien inmueble'
        resultado = ''
        resultado += '<b>PARÁGRAFO PRIMERO:</b> El crédito inicialmente aprobado por '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, en favor de <b>LA PARTE '
        resultado += 'HIPOTECANTE</b> asciende a la cantidad de <b>'
        resultado += f'{number_to_word_hipotecante.upper()} PESOS MCTE ('
        resultado += f'${number_format_hipotecante})</b> de los cuales la '
        resultado += f'suma de <b>{number_to_word_constructora.upper()}PESOS MCTE ('
        resultado += f'${number_format_constructora})</b> corresponden al '
        resultado += f'saldo del precio {t_inmuebles} de esta hipoteca, que desembolsará '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, a la parte vendedora, por cuenta del '
        resultado += 'deudor hipotecante y la diferencia es decir la suma de <b> '
        resultado += f'{number_to_word_gastos.upper()} PESOS MCTE ('
        resultado += f'${number_format_gastos})</b> corresponden a '
        resultado += 'los gastos de gestión y trámite del crédito en el exterior que se '
        resultado += 'giran por instrucción del cliente directamente al Bróker. La garantía '
        resultado += 'cubre también toda clase de obligaciones que <b> LA PARTE HIPOTECANTE '
        resultado += '</b> conjunta o separadamente contraiga en el futuro en favor de <b>'
        resultado += f'{self.banco.nombre}</b>, conforme a lo ya expresado en esta cláusula '
        resultado += 'y a lo establecido en la cláusula séptima y décima de esta hipoteca. '
        resultado += 'Esta liquidación es con el fin de determinar los derechos notariales y '
        resultado += 'de registro de la presente hipoteca. Adicionalmente, para dar '
        resultado += 'cumplimiento a lo ordenado  por el artículo 58 de la ley 788 de 2002, '
        resultado += 'el (los) deudor(es) certifica(n) que a la fecha no ha(n) recibido '
        resultado += 'desembolsos efectivos de créditos que estén garantizados con la '
        resultado += 'presente hipoteca. Es decir, que el desembolso es cero (0). ----------'
        resultado += '</p>'
        return resultado

    def generar_paragrafo_segundo_prestamos(self):
        resultado = ''
        resultado += '<p><b>PARÁGRAFO SEGUNDO:</b> La entrega del (los) préstamo(s) se hará '
        resultado += 'de acuerdo con las disponibilidades de tesorería de <b> '
        resultado += f'{self.banco.nombre.upper()}</b> y el (los) contrato(s) de mutuo '
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
            inmuebles_hipotecados = f'{inmuebles} hipotecados'
            inmuebles_desmejoran = f'{inmuebles} mismos desmejoran o sufren desprecios tales que no lleguen'
            inmuebles_determinan = f'{inmuebles} que se determinan en el presente contrato son gravados'
        else:
            inmuebles = 'el inmueble'
            inmuebles_hipotecados = f'{inmuebles} hipotecado'
            inmuebles_desmejoran = f'{inmuebles} mismo desmejora o sufre despecio tal que no llegue'
            inmuebles_determinan = f'{inmuebles} que e determina en el presente contrato es gravado'

        resultado = ''
        resultado += '<b>QUINTO. ACELERACIÓN DEL PLAZO:</b> Que <b> LA PARTE HIPOTECANTE</b> '
        resultado += f'reconoce y acepta el derecho de <b>{self.banco.nombre.upper()}</b> '
        resultado += 'para declarar por si misma y unilateralmente extinguido el plazo de la '
        resultado += 'deuda y para exigir de inmediato el pago de la totalidad de ella, con '
        resultado += 'intereses, accesorios, costas, gastos y honorarios de cobranzas judicial '
        resultado += 'en los casos en que hubiere lugar, en cualquiera de los casos que siguen: '
        resultado += '1. Si <b>LA PARTE HIPOTECANTE</b> no atiende o incumple las obligaciones '
        resultado += 'que contrae según esta escritura, o las que contraiga conjunta o '
        resultado += f'separadamente a favor de <b>{self.banco.nombre.upper()}</b>, de acuerdo '
        resultado += 'con los documentos o títulos-valores respectivos; o no satisface las '
        resultado += ' cuotas de amortización o los intereses en los términos previstos en los '
        resultado += f'documentos respectivos; 2. Si {inmuebles_hipotecados} es perseguido en '
        resultado += 'todo o en parte por un tercero o en ejercicio de cualquier acción legal; 3. '
        resultado += f'Si {inmuebles_desmejoran} a ser garantía suficiente del crédito, a juicio '
        resultado += f'de un perito que designe <b>{self.banco.nombre.upper()}</b>, 4. Si '
        resultado += f'{inmuebles_determinan} con hipoteca(s) distinta(s) a la(s) constituida(s) '
        resultado += 'mediante esta escritura, sin previo, expreso y escrito consentimiento de '
        resultado += f'<b>{self.banco.nombre.upper()}</b>; 5. Si el hipotecante(s) enajena(n) en '
        resultado += f'todo o en parte {inmuebles} sin consentimiento previo, expreso y escrito de '
        resultado += f'<b>{self.banco.nombre.upper()}</b>; 6. <b>LA PARTE HIPOTECANTE</b> hubiere '
        resultado += 'invertido la suma adeudada en forma diversa a la disposición legal que '
        resultado += 'autoriza la línea de crédito; 7. Por inexactitud o falsedad en los '
        resultado += 'documentos en virtud de los cuales se haya obtenido la adjudicación del '
        resultado += 'crédito. ------<br>'
        resultado += '<b>PARÁGRAFO:</b> En todos los casos y para todos los efectos, será '
        resultado += 'suficiente prueba de incumplimiento el simple dicho al respecto del '
        resultado += f'representante legal de <b>{self.banco.nombre.upper()}</b>, por lo que se '
        resultado += 'puede hacer efectiva la responsabilidad de <b>LA PARTE HIPOTECANTE</b> y la '
        resultado += 'garantía hipotecaria con sólo presentar el o los títulos insolutos que se '
        resultado += 'quieran hacer efectivos y copia de la presente escritura, sin necesidad de '
        resultado += 'requerimiento judicial alguno. ------<br>'
        return resultado

    def generar_sexto_cesion_de_credito(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
        else:
            inmuebles = 'el inmueble'
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

    def generar_septimo_costos_y_gastos_judicianles(self):
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
        resultado += 'seguro de incendio y terremoto se tomará por el valor comercial'
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
        resultado += 'estas operaciones materia de convenio entre las partes, que estarán'
        resultado += 'representadas en documentos separados, que deberán ser firmados para '
        resultado += 'el perfeccionamiento del crédito por <b>LA PARTE HIPOTECANTE</b>, los '
        resultado += 'codeudores y avalistas correspondientes. Como consecuencia de lo '
        resultado += 'anterior, <b>LA PARTE HIPOTECANTE</b> reconoce expresamente que '
        resultado += f'<b>{self.banco.nombre.upper()}</b>, no está obligada a dar o a '
        resultado += 'entregar suma alguna en virtud del presente documento. Si en el '
        resultado += 'lapso entre la aprobación del crédito y su probable perfeccionamiento, '
        resultado += f'<b>{self.banco.nombre.upper()}</b> conoce de hechos sucedidos antes '
        resultado += 'o después de aquella, los cuales la hubieren impedido aprobar el '
        resultado += 'el crédito, podrá darlo por desistido.<br>'
        resultado += '<b>PARÁGRAFO.</b> Con la constitución de la presente hipoteca se '
        resultado += ' garantizan exclusivamente los créditos ya otorgados o los que '
        resultado += f'voluntariamente quiera otorgarle(s) <b>{self.banco.nombre.upper()}'
        resultado += '</b>,comprendiendo además los intereses, costas, gastos, seguros, '
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

    # TODO Agregar datos de escritura linea 555
    def generar_datos_apoderado_especial(self):
        resultado = ''
        resultado += f'Presente {self.apoderado_especial.doctor}, '
        resultado += f'<b>{self.apoderado_especial.nombre.upper()}</b> '
        resultado += f'{self.apoderado_especial.indole}, mayor de edad, '
        resultado += f'{self.apoderado_especial.vecino} de '
        resultado += f'{self.apoderado_especial.ciudad_residencia}, '
        resultado += f'{self.apoderado_especial.identificado} con '
        resultado += f'{self.apoderado_especial.tipo_identificacion} '
        resultado += f'No. <b>{self.apoderado_especial.numero_identificacion}</b> quien '
        resultado += 'comparece en este acto en su calidad de <b>'
        resultado += f'{self.apoderado_especial.apoderado} Especial</b> '
        resultado += 'acorde con el Poder constituido por ______________________________ '
        resultado += 'debidamente inscrito en la Cámara de Comercio de '
        resultado += 'según certificado de la Existencia y Representación legal que '
        resultado += 'se protocoliza con este instrumento, conferido por '
        return resultado

    def generar_datos_representante_legal(self):
        resultado = ''
        resultado += f'{self.representante_legal.doctor} '
        resultado += f'<b>{self.representante_legal.nombre.upper()}</b>, '
        resultado += f'mayor de edad, {self.representante_legal.vecino} de '
        resultado += f'{self.representante_legal.ciudad_residencia}, '
        resultado += f'{self.representante_legal.identificado} con '
        resultado += f'{self.representante_legal.tipo_identificacion} '
        resultado += f'No. <b>{self.representante_legal.numero_identificacion} '
        resultado += f'de {self.representante_legal.ciudad_expedicion_identificacion}</b>, '
        return resultado

    # TODO cambiar nombre de la función
    def generar_banco_union(self):
        resultado = ''
        resultado += 'quien comparece en este acto en calidad de representante legal de '
        resultado += f'<b>{self.banco.nombre.upper()}</b> antes <b>GIROS & FINANZAS COMPAÑÍA DE '
        resultado += 'FINANCIAMIENTO S.A.</b>, sociedad constituida legalmente mediante Escritura '
        resultado += 'Escritura Pública No. 5938 del 05 de diciembre de 1963, otorgada en la '
        resultado += 'Notaria Cuarta (04) del Círculo de Bogotá, inscrita en la Cámara de '
        resultado += 'Comercio de Cali,  el 7 de noviembre de 2000, bajo el número 7516 del Libro '
        resultado += 'IX, sociedad convertida a establecimiento Bancario y modificada su razón '
        resultado += 'social mediante Escritura Pública No. 3140 del 16 de Junio de 2022, otorgada '
        resultado += 'en la Notaría Cuarta del Círculo de Cali, inscrita en la Cámara de Comercio '
        resultado += 'de Cali el 28 de Junio de 2022, bajo el No. 12001 del Libro IX, entidad '
        resultado += 'vigilada por la Superintendencia Financiera, con permiso de funcionamiento '
        resultado += 'otorgado mediante Resolución número 549 del 31 de mayo de 2022, todo lo cual '
        resultado += 'se acredita  con el Certificado de Existencia y Representación Legal '
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
            self.banco.prestamo_banco_a_hipotecante_en_numero, lang='es')
        number_format_hipotecante = f'{self.banco.prestamo_banco_a_hipotecante_en_numero:,}'
        resultado = ''
        resultado += 'Para dar cumplimiento a lo ordenado en la Resolución No. 00536 del 22 de '
        resultado += 'Enero de 2021, aclarada por Resolución 0545 del 25 de Enero de 2021 '
        resultado += 'proferida por la Superintendencia de Notariado y Registro, se adjunta con '
        resultado += f'esta escritura la carta expedida por <b>"{self.banco.nombre.upper()}"</b>, '
        resultado += 'donde aprueba un crédito al Hipotecante por la suma de '
        resultado += f'<b>{number_to_word_hipotecante.upper()} PESOS MCTE '
        resultado += f'(${number_format_hipotecante})</b>, la misma que '
        resultado += 'tomará el Notario para la liquidación de los derechos notariales. ---------'
        resultado += '------------------------------------------------------------------<br>'
        return resultado

    def generar_afectacion_vivienda_familiar(self):
        if self.multiples_inmuebles():
            inmuebles = 'los inmuebles'
        else:
            inmuebles = 'el inmueble'
        resultado = ''
        resultado += '<b>APLICACIÓN A LA LEY 0258 de 1996: AFECTACIÓN A VIVIENDA FAMILIAR:</b> '
        resultado += 'A continuación, el(la) notario(a) interroga bajo juramento a '
        resultado += f'{self.apoderado.apoderado} de <b>LA PARTE HIPOTECANTE</b>, si '
        resultado += f'{inmuebles} que hipotecan por el presente Instrumento se encuentra '
        resultado += 'Afectado al Régimen de Vivienda Familiar, a lo que responde: <b>NO.</b> '
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
        resultado += 'cuyo  incumplimiento causará intereses moratorios por mes o fracción de mes '
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
        resultado += '________.oo, de fecha: ______________,   válido(s) hasta _______________. '
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
        resultado += f'{self.apoderado.tipo_identificacion_abreviacion} '
        resultado += f'{self.apoderado.numero_identificacion} de '
        resultado += f'{self.apoderado.ciudad_expedicion_identificacion}</b><br>'
        resultado += 'En representación de<br>'
        return resultado

    def generar_firma_hipotecante(self):
        resultado = ''
        for poderdante in self.poderdantes:
            resultado += f'<b>{poderdante.nombre.upper()}</b><br>'
            resultado += f'<b>{poderdante.tipo_identificacion_abreviacion}'
            resultado += f'{poderdante.numero_identificacion} de '
            resultado += f'{poderdante.ciudad_expedicion_identificacion}</b><br><br>'
        return resultado

    def generar_firma_apoderado_especial(self):
        resultado = ''
        resultado += 'EL ACREEDOR,<br><br><br><br>'
        resultado += '____________________________<br>'
        resultado += f'<b>{self.apoderado_especial.nombre.upper()}<br>'
        resultado += f'{self.apoderado_especial.tipo_identificacion_abreviacion} '
        resultado += f'{self.apoderado_especial.numero_identificacion} expedida en '
        resultado += f'{self.apoderado_especial.ciudad_expedicion_identificacion}</b><br>'
        resultado += f'{self.apoderado_especial.apoderado} Especial de<br>'
        resultado += f'<b>{self.banco.nombre.upper()}<br>'
        resultado += f'NIT. {self.banco.nit}</b><br><br><br><br>'
        resultado += 'LA NOTARÍA.<br><br><br><br>____________________</div>'
        return resultado

    def generar_estilos(self):
        resultado = ''
        resultado += '<style>'
        resultado += 'div.titulo {text-align: center; font-weight: bold; font-size: 17px; font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.parrafos {text-align: justify; font-size: 16px; list-style: lower-alpha; font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.seccion_firmas {font-size: 16px; font-family: Arial, Helvetica, sans-serif;}'
        resultado += 'div.padding {padding-top: 50px; padding-right: 50px; padding-bottom: 30px; padding-left: 50px;}</style>'
        return resultado
