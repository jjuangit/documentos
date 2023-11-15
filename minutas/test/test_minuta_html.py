from unittest import TestCase

from models.minutas import DocumentoMinuta
from models.apoderado import Apoderado
from models.poderdantes import Poderdante
from models.banco import Banco
from models.inmueble import InmueblePrincipal
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from utils.strip_spaces import strip_dict_or_list


class TestMinuta(TestCase):
    """Iniciar Test"""

    def test_init_minuta_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado = {
            'nombre': 'HENRY BARBOSA ORTIZ',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'tipo_identificacion_abreviacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['abreviacion'],
            'numero_identificacion': '79.708.406',
            'ciudad_expedicion_identificacion': 'Bogotá D.C.',
            'genero': genero['MASCULINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'KATHERINN BARBOSA MARIN',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'tipo_identificacion_abreviacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['abreviacion'],
            'numero_identificacion': '1.022.399.153',
            'ciudad_expedicion_identificacion': 'Bogotá D.C.',
            'domicilio': 'UNIT 2 15 GUESS AVE WOLLI CREEK - AUSTRALIA',
            'estado_civil': estado_civil['SOLTERO_SIN_UNION_MARITAL_DE_HECHO'],
            'genero': genero['FEMENINO'],
        }
        ]

        diccionario_banco = {
            'nombre': 'banco unión s.a',
            'nit': '860.006.797-9',
            'prestamo_banco_a_hipotecante_en_numero': 109844550,
            'cantidad_dada_a_constructora_en_numero': 106130000,
            'gastos_de_gestion_en_numero': 3714550
        }

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '205',
            'direccion': 'TORRE 7 ETAPA II, PRATTO PH. CARRERA 78 #11 C - 58,',
            'ciudad_y_o_departamento': 'NUEVO TECHO BOGOTÁ D.C.',
            'matricula': '50C-2180229',
            'municipio_de_registro_orip': 'Bogotá Zona Centro',
            'tipo_ficha_catastral': 'Individual',
            'numero_ficha_catastral': '006507182000000000',
            'linderos_especiales': 'TORRE 7 - APARTAMENTO 205: Tiene su acceso por la CARRERA 78 # 11 C - 58 de Bogotá D.C. de la actual nomenclatura urbana de Bogotá D.C. El Apartamento está ubicado en el Segundo Piso de la torre. Cuenta con un ÁREA CONSTRUIDA de treinta y siete punto cincuenta y siete metros cuadrados (37,57 M2); de los cuales, el ÁREA PRIVADA es de treinta y tres punto catorce metros cuadrados (33,14 M2) y cuenta con un Área Común de cuatro punto cuarenta y tres metros cuadrados (4,43 M2) que corresponden al área común de muros de fachada, muros divisorios, ductos, pantallas y muros estructurales los cuales aunque se encuentran en el interior de la unidad privada, no se pueden modificar ni demoler dado su carácter estructural. Son comunes los muros de fachada, muros divisorios, ductos, pantallas y muros estructurales de por medio: Partiendo del punto 1 al punto 2 en línea recta y en distancia de cinco punto veintitrés metros (5,23 mts) colinda parte con zona común de vacío interior, parte con el Apartamento 204 de ésta misma torre y parte con vacío sobre zona libre común. Del punto 2 al punto 3 en línea quebrada y en distancias sucesivas de tres punto quince metros (3,15 mts), dos punto cero ocho metros (2,08 mts), cero punto diez metros (0,10 mts), uno punto ochenta y siete metros (1,87 mts), dos punto ochenta y cinco metros (2,85 mts) colinda con vacío sobre zona libre común. Del punto 3 al punto 4 en línea quebrada y en distancias sucesivas de uno punto setenta y cinco metros (1,75 mts), dos punto cero cinco metros (2,05 mts), cero. punto doce metros (0,12 mts), tres punto veintidós metros (3, 22 mts), tres: punto. quince metros (3,15 mts) colinda parte con vacío sobre zona. libre común y circulación y parte con junta sísmica de dilatación contra la torre 6.  Del punto 4 al punto 1 y: cierra en línea: «quebrada y en distancias sucesivas de dos metros (2,00 mts), cero punto cincuenta y cuatro metros (0,54 mts), cero punto cincuenta -metros (0,50 mts), uno punto setenta y un metros (1,71 mts), cero punto quince metros (0,15 mts), dos punto veinticinco metros (2,25 mts), uno punto diecisiete metros (1,17 mts), dos punto veintitres metros (2,23 mts), uno punto cincuenta y cinco metros (1,55 mts), cero punto doce metros (0,12 mts), uno punto cuarenta metros (1,40 mts), uno punto cuarenta y nueve metros (1,49 mts), cero punto cuarenta y dos metros (0,42 mts), cero punto sesenta y dos metros (0,62 mts), dos punto ochenta y ocho metros (2,88 mts) colinda parte con vacío sobre zona libre común y parte con zonas comunes de ductos, escaleras, circulación y acceso al apartamento. LINDEROS VERTICALES APARTAMENTO: NADIR APARTAMENTO. Con placa común que lo separa del primer piso. CENIT APARTAMENTO. - Con placa común que lo separa del tercer piso. DEPENDENCIAS: Salón, Cocina, Ropas, Estudio, Una (1) Alcoba, Un (1) baño.'
        }

        diccionario_parqueaderos = [{
            'nombre': 'parqueadero de uso exclusivo',
            'numero': '123',
            'direccion': 'ETAPA II, PRATTO PH. CARRERA 78 #11 C - 58,',
            'matricula': '50C-45755',
            'tipo_ficha_catastral': 'Individual',
            'numero_ficha_catastral': '0000001111111000000',
            'linderos_especiales': 'PAQUEADERO DE USO EXCLUSIVO 123: tiene su acceso......'
        }
        ]

        diccionario_depositos = [{
            'nombre': 'depósito',
            'numero': '456',
            'direccion': 'ETAPA II, PRATTO PH. CARRERA 78 #11 C - 58,',
            'matricula': '50C-45999',
            'tipo_ficha_catastral': 'Individual',
            'numero_ficha_catastral': '0000003333333000000',
            'linderos_especiales': 'DEPÓSITO 456: tiene su acceso......'
        }
        ]

        diccionario_apoderado_banco = {
            'nombre': 'GERMÁN LEONARDO KALIL MÉNDEZ',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'tipo_apoderado': tipo_apoderado_banco['ESPECIAL'],
            'tipo_identificacion_abreviacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['abreviacion'],
            'numero_identificacion': '79.489.351',
            'ciudad_expedicion_identificacion': 'Bogotá',
            'ciudad_residencia': 'Bogotá',
            'genero': genero['MASCULINO'],
        }

        diccionario_representante_banco = {
            'nombre': 'JUAN PABLO CRUZ LÓPEZ',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '16.724.519',
            'tipo_representante': tipo_representante_banco['LEGAL'],
            'ciudad_expedicion_identificacion': 'Cali',
            'ciudad_residencia': 'Cali',
            'genero': genero['MASCULINO'],
        }

        diccionario_apoderado = strip_dict_or_list(diccionario_apoderado)
        diccionario_poderdantes = strip_dict_or_list(diccionario_poderdantes)
        diccionario_banco = strip_dict_or_list(diccionario_banco)
        diccionario_inmueble = strip_dict_or_list(diccionario_inmueble)
        diccionario_parqueaderos = strip_dict_or_list(diccionario_parqueaderos)
        diccionario_depositos = strip_dict_or_list(diccionario_depositos)
        diccionario_apoderado_banco = strip_dict_or_list(diccionario_apoderado_banco)
        diccionario_representante_banco = strip_dict_or_list(diccionario_representante_banco)

        apoderado = Apoderado(**diccionario_apoderado)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in diccionario_poderdantes]
        banco = Banco(**diccionario_banco)
        inmueble = InmueblePrincipal(**diccionario_inmueble)
        depositos = [Deposito(**deposito)
                     for deposito in diccionario_depositos]
        parqueaderos = [Parqueadero(**parqueadero)
                        for parqueadero in diccionario_parqueaderos]
        apoderado_banco = ApoderadoBanco(
            **diccionario_apoderado_banco)
        representante_banco = RepresentanteBanco(
            **diccionario_representante_banco)
        minuta = DocumentoMinuta(apoderado, poderdantes, banco, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco)
        minuta.generate_html()
        print(minuta.html)

# command line for run this test:
# python -m unittest test.test_minuta_html.TestMinuta.test_init_minuta_success
