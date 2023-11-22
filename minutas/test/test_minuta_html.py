from unittest import TestCase

from models.minutas import DocumentoMinuta
from models.apoderado import Apoderado
from models.poderdantes import Poderdante
from models.inmueble import InmueblePrincipal
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from models.banco import Banco
from models.prestamo import Prestamo
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from catalogs.catalogos import ficha_catastral
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from utils.strip_spaces import strip_dict_or_list


class TestMinuta(TestCase):
    """Iniciar Test"""

    def test_init_minuta_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado = {
            'nombre': 'HELMUTH GEOFRE RAMOS CALONGE',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '93.391.258',
            'ciudad_expedicion_identificacion': 'Ibague',
            'genero': genero['FEMENINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'OSCAR GARCES HURTADO',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '80.062.545',
            'ciudad_expedicion_identificacion': 'Bogotá D.C.',
            'domicilio': 'CENTEREACH - NEW YORK',
            'estado_civil': estado_civil['CASADO_CON_SOCIEDAD_CONYUGAL_VIGENTE'],
            'genero': genero['MASCULINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '704 TORRE 12,',
            'direccion': 'AGRUPACION RESIDENCIAL AQUALINA ORANGE, TRANSVERSAL 26 # 5A-02(LOTE UTIL 5),',
            'ciudad_y_o_departamento': 'EN AQUALINA GIRARDOT CUNDINAMARCA.',
            'matricula': '307-105408',
            'municipio_de_registro_orip': 'GIRARDOT',
            'tipo_ficha_catastral': ficha_catastral['INDIVIDUAL'],
            'numero_ficha_catastral': [
                {'ficha': '010200062508904'},
            ],
            'linderos_especiales': '"APARTAMENTO NÚMERO 704 (TORRE 12) GENERALIDADES: Se localiza en el SÉPTIMO PISO de la respectiva Torre del Proyecto “AGRUPACIÓN RESIDENCIAL AQUALINA ORANGE”, predio ubicado en la Transversal 26 No. 5A-02 (Lote Útil 5) URBANIZACIÓN AQUALINA (Antes URBANIZACIÓN AQUALINA LOTE 5) de la ciudad de Girardot. Su Coeficiente de Propiedad Horizontal y su altura libre es de dos punto cincuenta metros (2.50m) aproximadamente, con las siguientes áreas de construcción. ÁREAS TOTALES: AREA CONSTRUIDA: SETENTA Y SEIS PUNTO OCHENTA Y CUATRO METROS CUADRADOS (76.84 M2). AREA PRIVADA: SESENTA Y NUEVE PUNTO VEINTITRÉS METROS CUADRADOS (69.23 M2). PÁRRAFO: Dentro del área construida están incluidos MUROS, DUCTOS Y ELEMENTOS ESTRUCTURALES COMUNALES con un área de: SIETE PUNTO CINCUENTA Y UN METROS CUADRADOS (7.51 M2). SESENTA Y UNO METROS CUADRADOS (76.1 M2). ÁREA COMÚN DE USO EXCLUSIVO: Se le asigna un balcón común de uso exclusivo con un área total de siete punto sesenta y dos metros cuadrados (7.62m2). DEPENDENCIAS PRIVADAS. Sala – comedor, dos (2) alcobas (cada una de ellas con espacio disponible para futuro baño), un (1) disponible, un (1) baño, cocina y zona de ropas. LINDEROS: Los linderos con muros de fachada, medianeros, interiores, elementos estructurales, ductos, placas de piso y entrepiso, cubiertas y las demás zonas comunes de uso exclusivo y zonas comunales al medio, son los consignados en los planos de Propiedad Horizontal debidamente sellados y aprobados. Dichos elementos y muros forman parte de la estructura de la edificación, tienen la calidad de bienes comunes esenciales y no pueden ser modificados ni ser demolidos parcial o totalmente pues se pone en peligro la solidez y estabilidad de la construcción. LINDEROS HORIZONTALES Y VERTICALES: Partiendo del punto Número uno (1), localizado a la derecha del acceso, hasta el punto Número dos (2) en línea quebrada y distancias sucesivas de dos punto sesenta y tres metros (2.63m), dos punto ochenta metros (2.80m), cero punto doce metros (0.12m), uno punto cincuenta metros (1.50m), cero punto cero dos metros (0.02m), cero punto noventa y uno metros (0.91m), uno punto trece metros (1.13m), cero punto noventa y uno metros (0.91m), cero punto veintidós metros (0.22m), uno punto treinta y ocho metros (1.38m), cero punto sesenta y tres metros (0.63m), cero punto doce metros (0.12m), cero punto sesenta y tres metros (0.63m), cero punto diez metros (0.10m), cero punto doce metros (0.12m), dos punto cincuenta y uno metros (2.51m), uno punto treinta y siete metros (1.37m), cero punto cincuenta y uno metros (0.51m), cero punto treinta y seis metros (0.36m), dos punto sesenta y dos metros (2.62m) y tres punto treinta y seis metros (3.36m) respectivamente, con condensadores de aire acondicionado y con vacío sobre zona común, Del punto Número dos (2) al Punto Número tres (3) en línea quebrada y distancias sucesivas de dos punto setenta y tres metros (2.73m), cinco punto treinta y ocho metros (5.38m), cero punto quince metros (0.15m), uno punto ochenta y siete metros (1.87m) y tres punto veintinueve metros (3.21m) respectivamente, con vacío sobre zona verde común y área de circulación peatonal. Del punto Número tres (3) al punto Número cuatro (4) en línea quebrada y distancias sucesivas de dos punto setenta y uno metros (2.71m), tres punto treinta y seis metros (3.36m), cero punto ochenta y cinco metros (0.85m), cero punto veinte y cinco metros (0.25m), cero punto noventa y nueve metros (0.99m), cero punto veinte y cinco metros (0.25m), cero punto dieciséis metros (0.16m), cero punto doce metros (0.12m), tres punto cincuenta y nueve metros (3.59m), cero punto doce metros (0.12m), cero punto catorce metros (0.14m), dos punto ochenta y siete metros (2.87m), cero punto doce metros (0.12m), tres punto ochenta y seis metros (3.86m) y dos punto setenta y cuatro metros (2.74m) respectivamente, con balcón común de uso exclusivo del apartamento que se alindera y con vacío sobre zona verde común, área de circulación peatonal y zona verde recreativa. Del punto Número cuatro (4) al punto Número cinco (5) en línea recta y distancia de seis punto treinta y ocho metros (6.38m) con el Apartamento Número 703 de esta misma Torre. Del punto Número cinco (5) al punto Número uno (1) de partida cerrando el polígono, en línea quebrada y distancias sucesivas de uno punto treinta y nueve metros (1.39m), uno punto sesenta y ocho metros (1.68m), uno punto cuarenta y siete metros (1.47m), cero punto veinticuatro metros (0.24m), uno punto treinta y cinco metros (1.35m), cero punto ochenta y siete metros (0.87m), cero punto catorce metros (0.14m), cero punto cincuenta y siete metros (0.57m), cero punto sesenta y dos metros (0.62m), cero punto cero seis metros (0.06m), un metro sesenta y uno metros (1.61m), cero punto cero seis metros (0.06m), un metro sesenta y tres metros (1.63m), cero punto veinticuatro metros (0.24m) y uno punto treinta metros (1.30m) respectivamente, con ducto de ventilación y con vestíbulo de circulación comunal. Cenit: Placa de entrepiso comunal al medio con el OCTAVO PISO de la Torre. Nadir: Placa de entrepiso comunal al medio con el SEXTO PISO del Conjunto. PÁRRAFO: No obstante la mención de las áreas de este apartamento y de la longitud de sus linderos, éstas son aproximadas y se determinan como cuerpos ciertos. En tal calidad se hará su transferencia de dominio a los futuros adquirientes; por lo tanto cualquier eventual diferencia que pueda resultar entre las cabidas de linderos reales y las aquí declaradas, no dará lugar a reclamo por ninguna de las partes."'
        }

        diccionario_parqueaderos = [
            {
                'nombre': 'PARQUEADERO',
                'numero': '665',
                'direccion': 'AGRUPACION RESIDENCIAL AQUALINA ORANGE, TRANSVERSAL 26 # 5A-02(LOTE UTIL 5), EN AQUALINA GIRARDOT CUNDINAMARCA.',
                'linderos_especiales': '"PARQUEADERO NÚMERO 665 GENERALIDADES: Se localiza en la Planta CUBIERTA del EDIFICIO PARQUEADEROS del Proyecto “AGRUPACIÓN RESIDENCIAL AQUALINA ORANGE”, predio ubicado en la Transversal 26 No. 5A-02 (Lote Útil 5) URBANIZACIÓN AQUALINA (Antes URBANIZACIÓN AQUALINA LOTE 5) de la ciudad de Girardot. Su Coeficiente de Copropiedad sobre los bienes comunes es el que se consigna en el Reglamento de Propiedad Horizontal y su altura libre (utilizable) es de dos punto veinte metros (2.20m) aproximadamente. ÁREA PRIVADA: DOCE PUNTO CUARENTA Y OCHO METROS CUADRADOS (12.48 M2). DEPENDENCIAS: Consta de un espacio cubierto (cubierta con teja en acero galvanizado, pre-pintada de espesor 0.36mm) para un (1) estacionamiento vehicular. LINDEROS: Los linderos con elementos estructurales, muros comunales, placas de piso, placas de entrepiso, líneas de demarcación y zonas comunales al medio son los consignados en los planos de Propiedad Horizontal debidamente sellados y aprobados. Dichos elementos y muros estructurales no podrán ser modificados en razón al carácter estructural que prestan. LINDEROS HORIZONTALES Y VERTICALES: Partiendo del punto Número uno (1), localizado a la izquierda del acceso, hasta el punto Número dos (2) en línea recta y distancia de cinco metros (5.00m) con el Parqueadero Número 664. Del punto Número dos (2) al Punto Número tres (3) en línea recta y distancia de dos punto cincuenta metros (2.50m) con vacío sobre zona de cesión. Del punto Número tres (3) al punto Número cuatro (4) en línea quebrada y distancias sucesivas de tres punto setenta y ocho metros (3.78m), cero punto cero cinco metros (0.05m), cero punto quince metros (0.15m), cero punto cero cinco metros (0.05m) y uno punto cero siete metros (1.07m) respectivamente, con el Parqueadero Número 666. Del punto Número cuatro (4) al punto Número uno (1) o punto de partida cerrando el polígono, en línea recta y distancia de dos punto cincuenta metros (2.50m) con acceso y con zona de circulación vehicular comunal. Cenit: Cubierta con teja en acero galvanizado al medio con el vacío o aire común. Nadir: Placa de entrepiso comunal al medio con el PRIMER PISO del Edificio Parqueaderos."',
                'matricula': '307-105760',
                'tipo_ficha_catastral': ficha_catastral['INDIVIDUAL'],
                'numero_ficha_catastral': '10200062863904'
            }
        ]

        diccionario_depositos = [
        ]

        diccionario_apoderado_banco = {
            'nombre': 'Jaime Andres Rodriguez Moreno',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '',
            'ciudad_expedicion_identificacion': '',
            'ciudad_residencia': '',
            'genero': genero['FEMENINO'],
            'tipo_apoderado': tipo_apoderado_banco['GENERAL'],
            'tipo_poder': '',
            'escritura': ''
        }

        diccionario_representante_banco = {
            'nombre': 'Juan Pablo Cruz López',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '',
            'ciudad_expedicion_identificacion': '',
            'ciudad_residencia': 'Cali',
            'genero': genero['FEMENINO'],
            'tipo_representante': tipo_representante_banco['SUPLENTE'],
        }

        diccionario_banco = {
            'nombre': 'banco unión s.a',
            'nit': '',
        }

        diccionario_prestamo = {
            'cantidad_banco_a_hipotecante': 180000000,
            'cantidad_dada_a_constructora': 173913043,
            'gastos_de_gestion': 6086957
        }

        diccionario_apoderado = strip_dict_or_list(diccionario_apoderado)
        diccionario_poderdantes = strip_dict_or_list(diccionario_poderdantes)
        diccionario_inmueble = strip_dict_or_list(diccionario_inmueble)
        diccionario_parqueaderos = strip_dict_or_list(diccionario_parqueaderos)
        diccionario_depositos = strip_dict_or_list(diccionario_depositos)
        diccionario_apoderado_banco = strip_dict_or_list(diccionario_apoderado_banco)
        diccionario_representante_banco = strip_dict_or_list(diccionario_representante_banco)
        diccionario_banco = strip_dict_or_list(diccionario_banco)
        diccionario_prestamo = strip_dict_or_list(diccionario_prestamo)

        apoderado = Apoderado(**diccionario_apoderado)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in diccionario_poderdantes]
        inmueble = InmueblePrincipal(**diccionario_inmueble)
        depositos = [Deposito(**deposito)
                     for deposito in diccionario_depositos]
        parqueaderos = [Parqueadero(**parqueadero)
                        for parqueadero in diccionario_parqueaderos]
        for bank_apoderado in apoderados_banco:
            if bank_apoderado['nombre'] == diccionario_apoderado_banco['nombre']:
                apoderado_banco = ApoderadoBanco(**bank_apoderado)
                break
        else:
            apoderado_banco = ApoderadoBanco(
                **diccionario_apoderado_banco)
        for representante in representantes_banco:
            if representante['nombre'] == diccionario_representante_banco['nombre']:
                representante_banco = RepresentanteBanco(**representante)
                break
        else:
            representante_banco = RepresentanteBanco(
                **diccionario_representante_banco)
                    
        for bank in bancos:
            if bank['nombre'] == diccionario_banco['nombre']:
                banco = Banco(**bank)
                break
        else:
            banco = Banco(**diccionario_banco)
        prestamo = Prestamo(**diccionario_prestamo)
        minuta = DocumentoMinuta(apoderado, poderdantes, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco, banco, prestamo)
        minuta.generate_html()
        print(minuta.html)

# command line for run this test:
# python -m unittest test.test_minuta_html.TestMinuta.test_init_minuta_success
