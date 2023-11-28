from unittest import TestCase

from models.minuta import DocumentoMinuta
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
            'nombre': 'JOSÉ FERNANDO SALAS CALA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '91.219.662',
            'ciudad_expedicion_identificacion': 'Bucaramanga',
            'genero': genero['MASCULINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'YHISELL FERNANDA MORA SALAS',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '1.232.892.499',
            'ciudad_expedicion_identificacion': 'Bucaramanga',
            'domicilio': 'Dacula Georgia',
            'estado_civil': estado_civil['SOLTERO_SIN_UNION_MARITAL_DE_HECHO'],
            'genero': genero['FEMENINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '411 de la Torre 5, piso 4',
            'direccion': 'CONJUNTO RESIDENCIAL NUEVA FORESTA ETAPA V, CARRERA 15 No. 92-164, B/ EL ANGELINO, BUCARAMANGA -SANTANDER',
            'ciudad_y_o_departamento': 'EN SANTA CRUZ DE CURINCA, SANTA MARTA MAGDALENA',
            'matricula': '300-466617',
            'municipio_de_registro_orip': 'BUCARAMANGA',
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '68001010404130005000'}
            ],
            'linderos_especiales': 'APARTAMENTO 411 Torre 5 PISO 4 del conjunto residencial Nueva Foresta etapa V, ubicado en la Carrera 15 No. 92-164 del barrio El Angelino, del Municipio de Bucaramanga, Santander, el cual contiene: sala, comedor, balcón, cocina, ropas, baño 1, baño 2, habitación principal, habitación 2, espacio disponible. El inmueble posee un área total de cincuenta y tres metros cuadrados (53 mts2) de los cuales cuarenta y cinco metros con dieciséis centímetros cuadrados (45,16 mts2) son de área privada construida, seis metros con cuarenta centímetros cuadrados (6,40 mts2) son de área común y un metro con cuarenta y cuatro centímetros (1,44 mts2) son de área común de uso exclusivo. El inmueble está determinado por los siguientes linderos: por el NORTE: Del punto 1 con Foresta - coordenada este= 1105196,35 y coordenada norte= 1275891,06, al punto 2 con coordenada este= 1105188,93 y coordenada norte= 1275888,07 en línea quebrada de 10,75 mts con zona común de la torre; por el SUR: Del punto 3 con coordenada este= 1105191,35 y coordenada norte= 1275882,36, al punto 4 con coordenada este= 1105198,72 y coordenada norte= 1275885,50 en línea quebrada de 13,00 mtl con zona común del conjunto; ORIENTE: Del punto 1 con coordenada este= 1105196,35 y coordenada norte= 1275891,06, al punto 4 con coordenada este= 1105198,72 y coordenada norte= 1275885,50 en línea quebrada de 15,75 mtl con apto 409; por el OCCIDENTE: Del punto 2 con coordenada este= 1105188,93 y coordenada norte= 1275888,07, al punto 3 con coordenada este= 1105191,35 y coordenada norte= 1275882,36 en línea quebrada de 15,60 mtl con apto 413; por el NADIR: con el apto 311; por el CENIT: Con apartamento 511.'
        }
        diccionario_parqueaderos = [
        ]

        diccionario_depositos = [

        ]

        diccionario_apoderado_banco = {
            'nombre': 'ROSANA GUEVARA PLATA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '37.746.531',
            'ciudad_expedicion_identificacion': 'Bucaramanga',
            'ciudad_residencia': 'Bucaramanga',
            'genero': genero['FEMENINO'],
            'tipo_apoderado': tipo_apoderado_banco['GENERAL'],
            'tipo_poder': 'General',
            'escritura': 'Escritura Pública Número 0020 de enero 7 de 2020 de la Notaría Catorce de Cali'
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
            'nombre': 'banco unión s.a',
            'nit': '',
        }

        diccionario_prestamo = {
            'cantidad_banco_a_hipotecante': 102879000,
            'cantidad_dada_a_aceptante': 99400000,
            'gastos_de_gestion': 3479000
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
