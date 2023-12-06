from unittest import TestCase

from models.minuta_hipoteca import DocumentoHipoteca
from models.apoderado import Apoderado
from models.poderdantes import Poderdante
from models.inmueble import Inmueble
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from models.banco import Banco
from models.prestamo import Prestamo
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from utils.strip_spaces import strip_dict_or_list

class TestMinutaHipoteca(TestCase):
    """Iniciar Test"""

    def test_init_minuta_hipoteca_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado= None
        diccionario_poderdantes = [
                    {
                        'nombre': 'MARIA DEL PILAR ESCOBAR MAYOR',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '31.165.010',
                        'ciudad_expedicion_identificacion': 'Palmira',
                        'domicilio': 'ELIZABETH - NEW JERSEY',
                        'estado_civil': 'Casado con sociedad conyugal vigente',
                        'genero': 'Femenino'
                    },
                    {
                        'nombre': 'FREDDY HUMBERTO BARANDICA MARTINEZ',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '16.279.472',
                        'ciudad_expedicion_identificacion': 'PENDIENTE',
                        'domicilio': 'ELIZABETH - NEW JERSEY',
                        'estado_civil': 'Casado con sociedad conyugal vigente',
                        'genero': 'Masculino'
                    }
                    ]
        diccionario_inmueble = {
                        'nombre': 'APARTAMENTO',
                        'numero': '1001 TORRE A',
                        'direccion': 'CONJUNTO RESIDENCIAL SENDEROS DE MULI ETAPA 1, CRA. 45 # 26-32',
                        'ciudad_y_o_departamento': 'PALMIRA - VALLE DEL CAUCA',
                        'matricula': '378-257555',
                        'municipio_de_registro_orip': 'PALMIRA',
                        'tipo_ficha_catastral': 'Mayor Extensión',
                        'numero_ficha_catastral': [
                            {'ficha': '765200001000000122281000000000'}
                        ],
                        'numero_chip': '',
                        'linderos_especiales': 'Apartamento 1001. Ubicado en el DECIMO PISO, Torre A del Conjunto Residencial Senderos de Muli, localizado en la Carrera 45 No. 26-32, barrio Santa Bárbara de la actual nomenclatura urbana de la ciudad de Palmira. Niveles altimétricos. Nadir. +24.30 metros. Cenit. +26.88 metros. Altura Libre. 2.58 metros. Area Privada. 81,27 M2. Área construida. 97.00 M2. Conformación: Consta de sala, comedor, terraza, cocina, zona de oficios, baño social, alcoba 2 con closet, Estar o estudio, baño alcobas, alcoba 3 con closet, alcoba principal con Vestier y baño. Este  apartamento tiene asignado por anexidad, funcionabilidad y a perpetuidad como zona común de uso exclusivo una Terraza con área de 3.62 M2 y un balcon con area de 1.43 M2. Linderos especiales. Del punto uno (1) al punto dos (2) en distancia de 8.34 metros, muro y columnas comunes que lo separan de vacío a zona común y terraza común de uso exclusivo apartamento 1001; del punto dos (2) al punto tres (3) en distancia de 31.14 metros, muro y columnas comunes que lo separan de vacío a zona común; del punto tres (3) al punto cuatro (4) en distancia de 13.95 metros, muro y columnas común que lo separan de vacio a zona común, balcón común de uso exclusivo apartamento 1001 de la Torre A y apartamento 1002 Torre A; del punto cuatro (4) al punto uno (1) de partida en distancia de 39,65 metros, muro y columna común que lo separan de apartamento 1002 Torre A y circulación común.'
                    }
        diccionario_parqueaderos = [
                    {
                        "nombre": "PARQUEADERO",
                        "numero": "218 SEMISÓTANO",
                        "direccion": "CONJUNTO RESIDENCIAL SENDEROS DE MULI ETAPA 1, CRA. 45 # 26-32",
                        "matricula": "378-257403",
                        "tipo_ficha_catastral": "Mayor extensión",
                        "numero_ficha_catastral": "765200001000000122281000000000",
                        "linderos_especiales": 'Parqueadero 218. Ubicado en el SEMISOTANO del Conjunto Residencial SENDEROS DE MULI, Localizado en la Carrera 45 No. 26-32, barrio Santa Bárbara de la actual nomenclatura urbana de la ciudad de Palmira. Niveles altimétricos. Nadir. -1.80 metros. Allura Libre. 2.55 metros. Área Privada. 10,35 M2. Linderos especiales. Del punto uno (1) al punto dos (2) en distancia de 6.80 metros, linea común divisoria, que lo separa de zona comun y parqueadero 147, del punto dos (2) al punto de partida (1) en distancia de 6.80 metros. Cenit. + 0.75 metros, linea comun divisoria, que lo separa de parqueadero 219 y circulacion vehicular.'                    
                    }
                    ]
        diccionario_depositos = [
                    {
                        "nombre": "DEPÓSITO",
                        "numero": "167",
                        "direccion": "CONJUNTO RESIDENCIAL SENDEROS DE MULI ETAPA 1, CRA. 45 # 26-32",
                        "matricula": "378-257477",
                        "tipo_ficha_catastral": "Mayor extensión",
                        "numero_ficha_catastral": "765200001000000122281000000000",
                        "linderos_especiales": 'Depósito 167. Ubicado en el SEMISOTANO del Conjunto Residencial SENDEROS DE MULI, Localizado en la Carrera 45 No. 26-32, barrio Santa Bárbara de la actual nomenclatura urbana de la ciudad de Palmira. Niveles altimétricos. Nadir. -1.80 metros. Cenit. + 0.75 metros. Altura Libre. 2.55 metros. Área Privada. 1.56 M2. Linderos especiales. Del punto uno (1) al punto dos (2) en distancia de 2.50 metros, muro y columna comun que lo separa de los depósitos 166 y 129; del punto dos (2) al punto de partida (1) en distancia de 2.50 metros, muro y columna común que lo separa de depósito 168 y circulación común.'                    
                    }
                    ]
        diccionario_apoderado_banco = {
                        'nombre': 'Lina Marcela Palau Zea',
                        'tipo_identificacion': '',
                        'numero_identificacion': '',
                        'ciudad_expedicion_identificacion': '',
                        'ciudad_residencia': '',
                        'genero': '',
                        'tipo_apoderado': '',
                        'tipo_poder': '',
                        'escritura': ''
                    }
        diccionario_representante_banco = {
                                'nombre': 'Héctor Fabio Rodríguez Prado',
                                'tipo_identificacion': '',
                                'numero_identificacion': '',
                                'ciudad_expedicion_identificacion': '',
                                'ciudad_residencia': '',
                                'genero': '',
                                'tipo_representante': ''
                            }
        diccionario_banco = {
                    'nombre': 'banco unión s.a',
                    'nit': '860.006.797-9'
                }
        diccionario_prestamo = {
                        'cantidad_banco_a_hipotecante': 220000000,
                        'cantidad_dada_a_aceptante': 212560386,
                        'gastos_de_gestion': 7439614
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

        if diccionario_apoderado is None:
            apoderado = None
        else:
            apoderado = Apoderado(**diccionario_apoderado)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in diccionario_poderdantes]
        inmueble = Inmueble(**diccionario_inmueble)
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
        minuta_hipoteca = DocumentoHipoteca(apoderado, poderdantes, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco, 
                                 banco, prestamo
                                 )
        minuta_hipoteca.generate_html()
        print(minuta_hipoteca.html)

# command line for run this test:
# python -m unittest tests.test_minuta_hipoteca.TestMinutaHipoteca.test_init_minuta_hipoteca_success
