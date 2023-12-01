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
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from catalogs.catalogos import tipo_ficha_catastral
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from utils.strip_spaces import strip_dict_or_list

class TestMinutaHipoteca(TestCase):
    """Iniciar Test"""

    def test_init_minuta_hipoteca_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado = {
            'nombre': 'MARTHA LUCILA ROJAS BETANCOURT',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '31.580.309',
            'ciudad_expedicion_identificacion': 'Cali',
            'genero': genero['FEMENINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'NATHALIA VERGARA HERNANDEZ',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '1.143.871.401',
            'ciudad_expedicion_identificacion': 'Cali',
            'domicilio': 'Barcelona - España',
            'estado_civil': estado_civil['SOLTERO_SIN_UNION_MARITAL_DE_HECHO'],
            'genero': genero['FEMENINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': 'TB-502 TORRE B',
            'direccion': 'CARRERA 23 # 10-15 PORTERIA 1/ CARRERA 23 # 10-73 PORTERIA 2, CONJUNTO RESIDENCIAL ROSETO- APARTAMENTOS',
            'ciudad_y_o_departamento': 'JAMUNDÍ - CALI',
            'matricula': '370-1077247',
            'municipio_de_registro_orip': 'CALI',
            'tipo_ficha_catastral': tipo_ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '763640100000007700049000000000'},
                {'ficha': '763640100000007700001000000000'},
                {'ficha': '763640100000007700002000000000'},
                {'ficha': '763640100000007700051000000000'},
            ],
            'linderos_especiales': '"TORRE B APARTAMENTO TB-502. Carrera 23 No 10-15 Porteria 1/ Carrera 23 No 10-73 Porteria 2. NADIR: 10,20. CENIT: 12,65. ALTURA LIBRE: 2,45 (de losa a losa sin contar el acabado). ÁREA CONSTRUIDA: 44,65 m2. Discriminada así: ÁREA PRIVADA CONSTRUIDA: 40,84 m2. + MUROS COMUNES: 3,81 m2. Comprendido dentro de los siguientes linderos: NORTE: Del punto 1 al punto 2. En línea quebrada. Con una distancia de 8,69 metros. Colindando con vacio a zona de oficios común de uso exclusivo del apartamento TB-102, buitrón y vacío a circulación común. ORIENTE: Del punto 2 al punto 3. En linea quebrada. Con una distancia de 6,44 metros. Colindando con circulación común y apartamento TB- 501. SUR: Del punto 3 al punto 4. En linea quebrada. Con una distancia de 10,18 metros. Colindando con vacio a zona común y buitrón, OCCIDENTE: Del punto 4 al punto 1. En linea recta. Con una distancia de 4,53 metros. Colindando con vacio a zona común."'
        }
        diccionario_parqueaderos = [
            {
                "nombre": "PARQUEADERO",
                "numero": "129",
                "direccion": "CARRERA 23 # 10-15 PORTERIA 1/ CARRERA 23 # 10-73 PORTERIA 2",
                "matricula": "370-1077782",
                "tipo_ficha_catastral": "",
                "numero_ficha_catastral": "",
                "linderos_especiales": "PARQUEADERO 129: Localizado en primer piso. Ubicado en la Carrera 23 No 10-15 Porteria 1 / Carrera 23 No 10-73 Porteria 2. NADIR. 0,00 AREA PRIVADA: 12,00 M2. LINDEROS: NOR-OCCIDENTE: del punto 4 al punto 1 En línea recta. Con una distancia de 5,00 metros. Colindando con zona común. NOR-ORIENTE: del punto 1 al punto 2 En linea recta. Con una distancia de 2,40 metros. Colindando con área de circulación y maniobras. SUR-ORIENTE: del punto 2 al punto 3. En línea recta. Con una distancia de 5,00 metros. Colindando con parqueadero 130. SUR-OCCIDENTE: del punto 3 al punto 4. En línea recta. Con una distancia de 2,40 metros. Colindando con parqueadero 155."
            }
        ]

        diccionario_depositos = [

        ]

        diccionario_apoderado_banco = {
            'nombre': 'Lina Marcela Palau Zea',
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
            'nombre': 'Héctor Fabio Rodríguez Prado',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '',
            'ciudad_expedicion_identificacion': '',
            'ciudad_residencia': '',
            'genero': genero['FEMENINO'],
            'tipo_representante': tipo_representante_banco['SUPLENTE'],
        }

        diccionario_banco = {
            'nombre': 'Banco unión s.a',
            'nit': '',
        }

        diccionario_prestamo = {
            'cantidad_banco_a_hipotecante': 112112000,
            'cantidad_dada_a_aceptante': 108320773,
            'gastos_de_gestion': 3791227
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
