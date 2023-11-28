from unittest import TestCase

from models.cesion_contrato import DocumentoCesionContrato
from models.apoderado import ApoderadoCesionContrato
from models.poderdantes import Poderdante
from models.inmueble import InmueblePrincipal
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from models.representante_aceptante import RepresentanteAceptante
from models.banco import Banco
from models.aceptante import Aceptante
from models.compraventa import Compraventa
from models.organo_autorizador import OrganoAutorizador
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from catalogs.catalogos import ficha_catastral
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.catalogos import aceptantes
from utils.strip_spaces import strip_dict_or_list


class TestCesionContrato(TestCase):
    """Iniciar Test"""

    def test_init_cesion_contrato_success(self):
        """Funcion para imprimir el html de la cesión de contrato"""
        diccionario_apoderado = {
            'nombre': 'DAIRY PAOLA MEJIA PASTRANA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '1.083.040.935',
            'ciudad_expedicion_identificacion': 'Santa Marta',
            'genero': genero['FEMENINO'],
            'tipo_apoderado': 'Especial',
            'escritura': '',
            'fecha_autenticacion_poder': '01/11/2023',
            'tipo_dependencia_autenticacion': 'Consulado',
            'nombre_dependencia': 'Consulado General Central de Colombia',
            'ciudad_dependencia': 'New York - Estados Unidos',
        }

        diccionario_poderdantes = [{
            'nombre': 'JORGE ALBEIRO CÁCERES MUNIVE',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '79.409.698',
            'ciudad_expedicion_identificacion': 'Bogotá',
            'domicilio': 'NEW ROCHELLE- NEW YORK',
            'estado_civil': estado_civil['SOLTERO_SIN_UNION_MARITAL_DE_HECHO'],
            'genero': genero['MASCULINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '207 PISO-2 TORRE-4',
            'direccion': 'CONJUNTO RESIDENCIAL VENECIA INN CARRERA 34 # 43 - 15',
            'ciudad_y_o_departamento': 'EN SANTA MARTA MAGDALENA',
            'matricula': '080-163243',
            'municipio_de_registro_orip': 'Santa Marta',
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '0002000000070001000000000'},
            ],
            'linderos_especiales': ''
        }

        diccionario_parqueaderos = [
        ]

        diccionario_depositos = [
        ]

        diccionario_apoderado_banco = {
            'nombre': 'Gloria Esperanza Garcia Troncoso',
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

        diccionario_representante_aceptante = {
            'nombre': 'MILANI ESTHER ESCORCIA SANTIAGO',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '32.706.233',
            'ciudad_expedicion_identificacion': 'Barranquilla',
            'ciudad_residencia': 'Barranquilla',
            'genero': genero['FEMENINO'],
            'tipo_representante': 'Representante Legal'
        }
        diccionario_banco = {
            'nombre': 'banco unión s.a',
            'nit': '',
        }

        diccionario_aceptante = {
            'nombre': 'CONSTRUCTORA JIMENEZ S.A',
            'nit': '891.702.877-8',
            'ciudad_ubicacion': 'Santa Marta',
            'escritura': 'Escritura Pública Numero 300 de fecha 25 de febrero de 1986',
            'nombre_notaria': 'Notaria Primera',
            'ciudad_ubicacion_notaria': 'Santa Marta',
            'ciudad_ubicacion_camara_comercio': 'Santa Marta'

        }

        diccionario_compraventa = {
            'cantidad_compraventa': 190236667,
            'cantidad_restante': 131444452,
            'cuota_inicial': 58792215,
            'fecha_compraventa': '05/07/2023'
        }

        diccionario_organo_autorizador = {
            'ciudad_ubicacion_camara_comercio': 'Santa Marta',
            'numero_acta': '00002365 del Libro IX',
            'fecha_acta': '16/06/2006'
        }

        diccionario_apoderado = strip_dict_or_list(diccionario_apoderado)
        diccionario_poderdantes = strip_dict_or_list(diccionario_poderdantes)
        diccionario_inmueble = strip_dict_or_list(diccionario_inmueble)
        diccionario_parqueaderos = strip_dict_or_list(diccionario_parqueaderos)
        diccionario_depositos = strip_dict_or_list(diccionario_depositos)
        diccionario_apoderado_banco = strip_dict_or_list(diccionario_apoderado_banco)
        diccionario_representante_banco = strip_dict_or_list(diccionario_representante_banco)
        diccionario_banco = strip_dict_or_list(diccionario_banco)
        diccionario_aceptante = strip_dict_or_list(diccionario_aceptante)
        diccionario_compraventa = strip_dict_or_list(diccionario_compraventa)

        apoderado = ApoderadoCesionContrato(**diccionario_apoderado)
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
        representante_aceptante = RepresentanteAceptante(
            **diccionario_representante_aceptante)
                    
        for bank in bancos:
            if bank['nombre'] == diccionario_banco['nombre']:
                banco = Banco(**bank)
                break
        else:
            banco = Banco(**diccionario_banco)
        for builder in aceptantes:
            if builder['nombre'] == diccionario_aceptante['nombre']:
                aceptante = Aceptante(**builder)
                break
        else:
            aceptante = Aceptante(**diccionario_aceptante)
        compraventa = Compraventa(**diccionario_compraventa)
        organo_autorizador = OrganoAutorizador(**diccionario_organo_autorizador)
        cesion_contrato = DocumentoCesionContrato(apoderado, poderdantes, inmueble, 
                                 parqueaderos, depositos, apoderado_banco, representante_banco, 
                                 representante_aceptante, banco, aceptante, compraventa, organo_autorizador)
        cesion_contrato.generate_html()
        print(cesion_contrato.html)

# command line for run this test:
# python -m unittest test.test_cesion_contrato.TestCesionContrato.test_init_cesion_contrato_success
