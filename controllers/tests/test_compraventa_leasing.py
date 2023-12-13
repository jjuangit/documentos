from unittest import TestCase
from controllers.documentos import DocumentosController
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from catalogs.catalogos import tipo_ficha_catastral
class TestCompraventaLeasing(TestCase):
    """Iniciar Test"""

    def test_init_compraventa_leasing_success(self):
        """Funcion para imprimir el html de la compraventa leasing"""
        event = {
                    'poderdantes': [{
                        'nombre': 'MARIA ESPERANZA BETANCOURT',
                        'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
                        'numero_identificacion': '31.868.984',
                        'ciudad_expedicion_identificacion': 'Cali',
                        'genero': genero['FEMENINO'],
                    }
                    ],
                    'inmueble': {
                        'nombre': 'APARTAMENTO',
                        'numero': '107 TORRE A',
                        'direccion': 'CARRERA 24 5-269',
                        'ciudad_y_o_departamento': 'EN PARQUE NATURA JAMUNDÍ VALLE DEL CAUCA',
                        'matricula': '370-1097610',
                        'municipio_de_registro_orip': 'Cali',
                        'tipo_ficha_catastral': tipo_ficha_catastral['MAYOR_EXTENSION'],
                        'numero_ficha_catastral': [
                            {'ficha': '763640100000007701796000000000'}
                        ],
                        'numero_chip': '',
                        'linderos_especiales': 'TORRE A APARTAMENTO 107. Identificado con el número Carrera 24 # 5-269 de la actual nomenclatura urbana del municipio de Jamundí, NADIR: 0,00 CENIT 2,45 ALTURA LIBRE: 2,45 (de losa a losa sin contar el acabado). ÁREA CONSTRUIDA: 73,17 m2. Discriminada así: ÁREA PRIVADA CONSTRUIDA: 67.80 m2 + MUROS COMÚNES: 5,37 m2. Comprendido dentro de los siguientes linderos: NOROESTE: Del punto 3 al punto 4 en línea quebrada con una distancia de 12,61 metros. Colindando con buitrón, circulación común, zona común de uso exclusivo del apartamento TA-107, buitrones, y espacio técnico. NORESTE; Del punto 4 al punto 1 en línea recta con una distancia de 7,55 metros. Colindando con zona común. SURESTE: Del punto 1 al punto 2 en línea quebrada con una distancia de 11.62 metros. Colindando con zona común y buitrón. SUROESTE: Del punto 2 al punto 3 en línea recta con una distancia de 8,20 metros. Colindando con apartamento TA-108. A este apartamento se le ha asignado una zona común de uso exclusivo, con un área de 6,51 m2, al cual se accede por la zona de oficios.'
                    },
                    'conjunto_residencial': {
                        'nombre': 'CONJUNTO RESIDENCIAL ALTEA PH.',
                        'matricula': '370-1050808',
                        'municipio_de_registro_orip': 'Cali',
                        'tipo_ficha_catastral': 'Global',
                        'numero_ficha_catastral': '763640100000007701796000000000',
                        'linderos_generales': 'LINDEROS GENERALES: El Conjunto Residencial Altea se desarrolla en un Lote con área total de 18.426,42 m2 localizado en la Carrera 24 No. 5-269 el cual se describe por su cabida y linderos como.se indica a continuación: LOTE M-6A, Globo de terreno con un área de 18.126,12 m2, comprendido por el polígono M6- 1,41, 40, 144, M6-3, M6-2 y M6-1, con los siguientes linderos: NORTE: Del punto 6-1 al punto 40, en línea mixta (recta y curva). Pasando por el punto 41. Con una. longitud total de 141.39 metros. Colindando con calle 8. ESTE: Del punto 40 al punto M6-3, en Línea mixta (curva y recta). Pasando por el punto 144. Con una Longitud total de 169.84 metros. Colindando con carrera 24. SUR: Del punto M5-3 al punio M6-2, en línea recta. Con una distancia de 134.79 metros. Colindando con lote M-68 y lote M.6C. OESTE: Del punto M6-2 al punto M6-1, en línea recta Con una distancia de 97.37 metros. Colindando con lote M-6C.'
                    },
                    'parqueaderos': [
                    {
                        'nombre': 'parqueadero',
                        'numero': '71',
                        'direccion': 'CARRERA 24 5-269',
                        'ciudad_y_o_departamento': 'EN PARQUE NATURA JAMUNDÍ VALLE DEL CAUCA',
                        'matricula': '370-1098010',
                        'tipo_ficha_catastral': 'Mayor Extensión',
                        'numero_ficha_catastral': '763640100000007701796000000000',
                        'linderos_especiales': 'PARQUEADERO 71: Localizado en primer piso. Dirección: CARRERA 24 # 5. 1. NADIR. 0,00 AREA PRIVADA: 10,8 M2. LINDEROS: NORTE: Del punto 4 al punto 1 en línea recta con una distancia de 4,50 metros: Colindando con parqueadero 70. ESTE: Del punto 1 al punto 2 en línea recta con una distancia de 2.40 metros. Colindando con área común de circulación y maniobra, SUR: Del punto 2 al punto 3 en línea recta con una distancia de 4,50 metros. Colindando con el parqueadero 72. OESTE: Del punto 3 al punto 4 en línea recta con una distancia de 2.40 metros. Colindando con zona común.'
                    }
                    ],
                    'depositos': [

                    ],
                    'apoderado_banco': {
                        'nombre': 'Lina Marcela Palau Zea',
                        'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
                        'numero_identificacion': '',
                        'ciudad_expedicion_identificacion': '',
                        'ciudad_residencia': '',
                        'genero': genero['FEMENINO'],
                        'tipo_apoderado': tipo_apoderado_banco['GENERAL'],
                        'tipo_poder': '',
                        'escritura': ''
                    },
                    'representante_banco': {
                        'nombre': 'Héctor Fabio Rodríguez Prado',
                        'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
                        'numero_identificacion': '',
                        'ciudad_expedicion_identificacion': '',
                        'ciudad_residencia': 'Cali',
                        'genero': genero['FEMENINO'],
                        'tipo_representante': tipo_representante_banco['SUPLENTE'],
                    },
                    'banco': {
                        'nombre': 'Banco unión s.a',
                        'nit': '',
                    },
                    'compraventa': {
                        'cantidad_compraventa': 190236667,
                        'cantidad_restante': 131444452,
                        'cuota_inicial': 58792215,
                        'fecha_compraventa': '05/07/2023'
                    }
                }

        controller = DocumentosController(event, None)
        response = controller.create_compraventa_leasing()

        self.assertEqual(response['statusCode'], 201)
        self.assertIsNotNone(response['body'])

# command line for run this test:
# python -m unittest controllers.tests.test_compraventa_leasing