from unittest import TestCase

from models.cesion_contrato import DocumentoCesionContrato
from models.apoderado import Apoderado
from models.poderdantes import Poderdante
from models.inmueble import InmueblePrincipal
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from models.banco import Banco
from models.constructora import Constructora
from models.compraventa import Compraventa
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from catalogs.catalogos import ficha_catastral
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.catalogos import constructoras
from utils.strip_spaces import strip_dict_or_list


class TestCesionContrato(TestCase):
    """Iniciar Test"""

    def test_init_cesion_contrato_success(self):
        """Funcion para imprimir el html de la cesión de contrato"""
        diccionario_apoderado = {
            'nombre': 'ESPERANZA BOTERO IDÁRRAGA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '31.951.464',
            'ciudad_expedicion_identificacion': 'Cali',
            'genero': genero['FEMENINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'MARIA ESPERANZA BETANCOURT',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '31.868.984',
            'ciudad_expedicion_identificacion': 'Cali',
            'domicilio': 'FLAT 5 262A OLD KENT ROAD SE1 5UB LONDRES',
            'estado_civil': estado_civil['CASADO_CON_SOCIEDAD_CONYUGAL_VIGENTE'],
            'genero': genero['FEMENINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '107 TORRE A',
            'detalle': 'CONJUNTO RESIDENCIAL ALTEA PH.',
            'direccion': 'CARRERA 24 5-269',
            'ciudad_y_o_departamento': 'EN PARQUE NATURA JAMUNDÍ VALLE DEL CAUCA',
            'matricula': '370-1097610',
            'municipio_de_registro_orip': 'Cali',
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '763640100000007701796000000000'},
            ],
            'linderos_especiales': ''
        }

        diccionario_parqueaderos = [{
            'nombre': 'GARAJE',
            'numero': '71',
            'direccion': '',
            'matricula': '370-1098010',
            'tipo_ficha_catastral': ficha_catastral['INDIVIDUAL'],
            'numero_ficha_catastral': '',
            'linderos_especiales': ''
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
            'tipo_poder': ''
        }

        diccionario_representante_banco = {
            'nombre': 'Héctor Fabio Rodríguez Prado',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '',
            'ciudad_expedicion_identificacion': '',
            'ciudad_residencia': 'Cali',
            'genero': genero['MASCULINO'],
            'tipo_representante': tipo_representante_banco['SUPLENTE'],
        }

        diccionario_banco = {
            'nombre': 'banco unión s.a',
            'nit': '',
        }

        diccionario_constructora = {
            'nombre': 'Constructora Bolivar Cali S.A.',
            'nit': '',
            'ciudad_ubicacion': ''
        }

        diccionario_compraventa = {
            'cantidad_compraventa': 190236667,
            'cantidad_restante': 131444452,
            'cuota_inicial': 58792215,
            'fecha_compraventa': '05/06/2023'
        }

        diccionario_apoderado = strip_dict_or_list(diccionario_apoderado)
        diccionario_poderdantes = strip_dict_or_list(diccionario_poderdantes)
        diccionario_inmueble = strip_dict_or_list(diccionario_inmueble)
        diccionario_parqueaderos = strip_dict_or_list(diccionario_parqueaderos)
        diccionario_depositos = strip_dict_or_list(diccionario_depositos)
        diccionario_apoderado_banco = strip_dict_or_list(diccionario_apoderado_banco)
        diccionario_representante_banco = strip_dict_or_list(diccionario_representante_banco)
        diccionario_banco = strip_dict_or_list(diccionario_banco)
        diccionario_constructora = strip_dict_or_list(diccionario_constructora)
        diccionario_compraventa = strip_dict_or_list(diccionario_compraventa)

        apoderado = Apoderado(**diccionario_apoderado)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in diccionario_poderdantes]
        inmueble = InmueblePrincipal(**diccionario_inmueble)
        depositos = [Deposito(**deposito)
                     for deposito in diccionario_depositos]
        parqueaderos = [Parqueadero(**parqueadero)
                        for parqueadero in diccionario_parqueaderos]
        for banck_apoderado in apoderados_banco:
            if banck_apoderado['nombre'] == diccionario_apoderado_banco['nombre']:
                apoderado_banco = ApoderadoBanco(**banck_apoderado)
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
        for builder in constructoras:
            if builder['nombre'] == diccionario_constructora['nombre']:
                constructora = Constructora(**builder)
                break
        else:
            constructora = Constructora(**diccionario_constructora)
        compraventa = Compraventa(**diccionario_compraventa)
        cesion_contrato = DocumentoCesionContrato(apoderado, poderdantes, inmueble, 
                                 parqueaderos, depositos, apoderado_banco, representante_banco, banco, constructora, compraventa)
        cesion_contrato.generate_html()
        print(cesion_contrato.html)

# command line for run this test:
# python -m unittest test.test_cesion_contrato.TestCesionContrato.test_init_cesion_contrato_success
