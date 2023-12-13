from unittest import TestCase

from models.promesa_compraventa import DocumentoPromesaCompraventa
from models.apoderado import ApoderadoPromesaCompraventa
from models.poderdantes import PoderdantePromesaCompraventa
from models.inmueble import InmueblePromesaCompraventa
from models.depositos import DepositoPromesaCompraventa
from models.parqueaderos import ParqueaderoPromesaCompraventa
from models.apoderado_banco import ApoderadoBancoPromesaCompraventa
from models.representante_banco import RepresentanteBancoPromesaCompraventa
from models.representante_aceptante import RepresentanteAceptantePromesaCompraventa
from models.banco import BancoPromesaCompraventa
from models.aceptante import Aceptante
from models.compraventa import Compraventa
from models.organo_autorizador import OrganoAutorizador
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import tipo_apoderado_banco
from catalogs.catalogos import tipo_representante_banco
from catalogs.catalogos import tipo_ficha_catastral
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.catalogos import aceptantes
from utils.strip_spaces import strip_dict_or_list


class TestPromesaCompraventa(TestCase):
    """Iniciar Test"""

    def test_init_promesa_compraventa_success(self):
        """Funcion para imprimir el html de la cesión de contrato"""
        diccionario_apoderado = {
            'nombre': 'ESPERANZA BOTERO IDÁRRAGA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '31.951.464',
            'ciudad_expedicion_identificacion': 'Cali',
            'tipo_apoderado': 'Especial',
            'fecha_autenticacion_poder': '01/11/2023',
            'tipo_dependencia_autenticacion': 'Notaría',
            'nombre_dependencia': 'Novena',
            'ciudad_dependencia': 'Cali',
            'escritura': '',
            'genero': genero['FEMENINO']
        }

        diccionario_poderdantes = [{
            'nombre': 'MARIA ESPERANZA BETANCOURT',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '31868984',
            'ciudad_expedicion_identificacion': 'Cali',
            'domicilio': 'LONDRES',
            'estado_civil': estado_civil['SOLTERO_SIN_UNION_MARITAL_DE_HECHO'],
            'genero': genero['FEMENINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '107 TORRE A',
            'direccion': 'CONJUNTO RESIDENCIAL ALTEA PH. CARRERA 24 5-269',
            'ciudad_y_o_departamento': 'EN PARQUE NATURA JAMUNDÍ VALLE DEL CAUCA',
            'matricula': '370-1097610',
            'municipio_de_registro_orip': 'Cali',
            'tipo_ficha_catastral': tipo_ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '763640100000007701796000000000'},
            ],
            'numero_chip': ''
        }

        diccionario_parqueaderos = [
            {
                "nombre": "GARAJE NRO",
                "numero": "71",
                "direccion": "CONJUNTO RESIDENCIAL ALTEA PH. CARRERA 24 5-269",
                'ciudad_y_o_departamento': 'EN PARQUE NATURA JAMUNDÍ VALLE DEL CAUCA',
                "matricula": "370-1098010,",
                "tipo_ficha_catastral": "",
                "numero_ficha_catastral": "",
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
            'ciudad_residencia': 'Cali',
            'genero': genero['MASCULINO'],
            'tipo_representante': tipo_representante_banco['SUPLENTE'],
        }

        diccionario_banco = {
            'nombre': 'Banco unión s.a',
            'nit': '',
        }
        diccionario_compraventa = {
            'cuota_inicial': 58792215,
            'fecha_compraventa': '05/07/2023'
        }
        diccionario_aceptante = {
            'nombre': 'CONSTRUCTORA BOLIVAR CALI S.A.',
            'nit': '860037900-4',
            'ciudad_ubicacion': 'Cali',
            'escritura': 'Escritura Pública Numero 3747 de fecha 31 de agosto de 1973',
            'nombre_notaria': 'Catorce',
            'ciudad_ubicacion_notaria': 'Santa Fe de Bogotá',
            'ciudad_ubicacion_camara_comercio': 'Cali'
        }

        diccionario_representante_aceptante = {
            'nombre': 'ANGIE LICETH VALENCIA BACCA',
            'tipo_identificacion': 'Cédula de Ciudadanía',
            'numero_identificacion': '1.007.789.982',
            'ciudad_expedicion_identificacion': 'Cali',
            'ciudad_residencia': 'Cali',
            'tipo_representante': 'Legal',
            'genero': 'Femenino',
        }

        diccionario_organo_autorizador = {
            'ciudad_ubicacion_camara_comercio': 'Cali',
            'numero_acta': '23980',
            'fecha_acta': '25/02/2023'
        }

        diccionario_apoderado = strip_dict_or_list(diccionario_apoderado)
        diccionario_poderdantes = strip_dict_or_list(diccionario_poderdantes)
        diccionario_inmueble = strip_dict_or_list(diccionario_inmueble)
        diccionario_parqueaderos = strip_dict_or_list(diccionario_parqueaderos)
        diccionario_depositos = strip_dict_or_list(diccionario_depositos)
        diccionario_apoderado_banco = strip_dict_or_list(
            diccionario_apoderado_banco)
        diccionario_representante_banco = strip_dict_or_list(
            diccionario_representante_banco)
        diccionario_representante_aceptante = strip_dict_or_list(diccionario_representante_aceptante)
        diccionario_banco = strip_dict_or_list(diccionario_banco)
        diccionario_aceptante = strip_dict_or_list(diccionario_aceptante)
        diccionario_compraventa = strip_dict_or_list(diccionario_compraventa)

        apoderado = ApoderadoPromesaCompraventa(**diccionario_apoderado)
        poderdantes = [PoderdantePromesaCompraventa(**poderdante)
                       for poderdante in diccionario_poderdantes]
        inmueble = InmueblePromesaCompraventa(**diccionario_inmueble)
        depositos = [DepositoPromesaCompraventa(**deposito)
                     for deposito in diccionario_depositos]
        parqueaderos = [ParqueaderoPromesaCompraventa(**parqueadero)
                        for parqueadero in diccionario_parqueaderos]
        for bank_apoderado in apoderados_banco:
            if bank_apoderado['nombre'] == diccionario_apoderado_banco['nombre']:
                apoderado_banco = ApoderadoBancoPromesaCompraventa(**bank_apoderado)
                break
        else:
            apoderado_banco = ApoderadoBancoPromesaCompraventa(
                **diccionario_apoderado_banco)
        for representante in representantes_banco:
            if representante['nombre'] == diccionario_representante_banco['nombre']:
                representante_banco = RepresentanteBancoPromesaCompraventa(**representante)
                break
        else:
            representante_banco = RepresentanteBancoPromesaCompraventa(
                **diccionario_representante_banco)
        if diccionario_representante_aceptante is None:
            representante_aceptante = None
        else:
            representante_aceptante = RepresentanteAceptantePromesaCompraventa(
                **diccionario_representante_aceptante)

        for bank in bancos:
            if bank['nombre'] == diccionario_banco['nombre']:
                banco = BancoPromesaCompraventa(**bank)
                break
        else:
            banco = BancoPromesaCompraventa(**diccionario_banco)
        if diccionario_aceptante is None:
            aceptante = None
        else:
            for aceptador in aceptantes:
                if aceptador['nombre'] == diccionario_aceptante['nombre']:
                    aceptante = Aceptante(**aceptador)
                    break
            else:
                aceptante = Aceptante(**diccionario_aceptante)
        compraventa = Compraventa(**diccionario_compraventa)
        organo_autorizador = OrganoAutorizador(
            **diccionario_organo_autorizador)
        promesa_compraventa = DocumentoPromesaCompraventa(apoderado, poderdantes, inmueble,
                                                  parqueaderos, depositos, apoderado_banco, representante_banco,
                                                  representante_aceptante, banco, aceptante, compraventa, organo_autorizador)
        promesa_compraventa.generate_html()
        print(promesa_compraventa.html)

# command line for run this test:
# python -m unittest tests.test_promesa_compraventa.TestPromesaCompraventa.test_init_promesa_compraventa_success
