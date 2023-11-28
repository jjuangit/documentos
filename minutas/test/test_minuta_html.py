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
            'nombre': 'FRANCISCO BUSTAMANTE POSADA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '7.436.307',
            'ciudad_expedicion_identificacion': 'BARRANQUILLA',
            'genero': genero['MASCULINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'LUISA AMELIA HERNANDEZ POSADA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '55.220.020',
            'ciudad_expedicion_identificacion': 'BARRANQUILLA',
            'domicilio': 'HOFFMAN ESTATES - ILLINOIS',
            'estado_civil': estado_civil['CASADO_CON_SOCIEDAD_CONYUGAL_VIGENTE'],
            'genero': genero['FEMENINO'],
        },{
            'nombre': 'WOJCIECH JAROSLAW URBAN',
            'tipo_identificacion': tipos_identificacion_ciudadano['PASAPORTE']['nombre'],
            'numero_identificacion': '520255366',
            'ciudad_expedicion_identificacion': 'ESTADOS UNIDOS DE AMERICA',
            'domicilio': 'HOFFMAN ESTATES - ILLINOIS',
            'estado_civil': estado_civil['CASADO_CON_SOCIEDAD_CONYUGAL_VIGENTE'],
            'genero': genero['MASCULINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '714 PISO 7 TORRE 2 ETAPA 1',
            'direccion': 'CONJUNTO RESIDENCIAL RIVER PALMS CALLE 100 # 64 84',
            'ciudad_y_o_departamento': 'EN RIO ALTO BARRANQUILLA ATLANTICO',
            'matricula': '040-649403',
            'municipio_de_registro_orip': 'Barranquilla',
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '01-03-00-00-0716-0226-0-00-00-0000'}
            ],
            'linderos_especiales': 'TORRE 2 APARTAMENTO N° 714 ubicado en el piso 7 de la Torre número 2 de la etapa 1 del CONJUNTO RESIDENCIAL RIVER PALMS P.H., situada en la ciudad de Barranquilla, en la Calle 100 No. 64 -84 de la nomenclatura urbana, destinado a vivienda, con un área construida total aproximada de 69.05 metros cuadrados, un área privada construida aproximada de 64.61 metros cuadrados, y una altura libre aproximada entre 2.40 - 2.50 metros lineales. Su área y linderos están determinados por el perímetro marcado con los puntos del 133 al 150 y 133 punto de partida, del plano No. PH 9/12 que se protocoliza con el presente reglamento de Propiedad Horizontal; linda por el CENIT, o parte de encima, con losa de concreto que lo separa del piso 8, y por el NADIR, o parte de abajo, con losa de concreto que lo separa del piso 6.'
        }
        diccionario_parqueaderos = [
            {
                "nombre": "GARAJE CON CUARTO UTIL No.",
                "numero": "714 PISO 7 TORRE 2 ETAPA 1",
                "direccion": "CONJUNTO RESIDENCIAL RIVER PALMS CALLE 100 # 64 84, EN RIO ALTO BARRANQUILLA ATLANTICO",
                "matricula": "040-649440",
                "tipo_ficha_catastral": "",
                "numero_ficha_catastral": "",
                "linderos_especiales": "TORRE 2 PARQUEADERO CON CUARTO ÚTIL N° 81, Ubicado en el SOTANO 1 de la torre 2 de la etapa 1 en el CONJUNTO RESIDENCIAL RIVER PALMS P.H., situado en la ciudad de Barranquilla, en la Calle 100 No. 64 - 84 de la nomenclatura urbana, destinado a estacionamiento de un (1) vehículo y a depósito de objetos, con un área privada construida aproximada de 15.2 metros cuadrados y una altura mínima aproximada de 2.5 metros lineales. Su área y linderos están determinados por el perímetro marcado con los puntos 63 al 69 y 63, punto de partida, del plano No. PH 1/12 que se protocoliza con el presente reglamento de Propiedad Horizontal; linda por el CENIT, o parte de encima, con losa de concreto que lo separa del Primer Piso, y por el NADIR, o parte de abajo, con losa de concreto que lo separa del sótano 2."
            }
        ]

        diccionario_depositos = [

        ]

        diccionario_apoderado_banco = {
            'nombre': 'Viviana del Pilar Olaciregui Escalante',
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
            'cantidad_banco_a_hipotecante': 276370742,
            'cantidad_dada_a_aceptante': 267024871,
            'gastos_de_gestion': 9345871
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
