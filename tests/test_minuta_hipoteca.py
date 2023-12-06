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
        diccionario_apoderado= {
                    'nombre': 'DANIELA FERNANDA QUICENO COLORADO',
                    'tipo_identificacion': 'Cédula de Ciudadanía',
                    'numero_identificacion': '1.053.799.880',
                    'ciudad_expedicion_identificacion': 'Manizales',
                    'genero': 'Femenino'
                    }
        diccionario_poderdantes = [
                    {
                        'nombre': 'JHONNY ALEJANDRO OSPINA QUICENO',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '1.053.825.607',
                        'ciudad_expedicion_identificacion': 'Manizales',
                        'domicilio': 'TICINIO- BELLINZONA',
                        'estado_civil': 'Soltero sin unión marital de hecho',
                        'genero': 'Masculino'
                    },
                    {
                        'nombre': 'PALOMA ALEJANDRA OSPINA QUICENO',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '1.053.823.744',
                        'ciudad_expedicion_identificacion': 'Manizales',
                        'domicilio': 'TICINIO- BELLINZONA',
                        'estado_civil': 'Soltero sin unión marital de hecho',
                        'genero': 'Femenino'
                    }
                    ]
        diccionario_inmueble = {
                        'nombre': 'APARTAMENTO',
                        'numero': '1104 PISO 11',
                        'direccion': 'EDIFICIO CENTRIKO"P.H. CALLE 11 B # 4 D - 34 BARRIO VILLA PILAR',
                        'ciudad_y_o_departamento': 'EN CHIPRE MANIZALES CALDAS',
                        'matricula': '100-252001',
                        'municipio_de_registro_orip': 'Manizales',
                        'tipo_ficha_catastral': 'Mayor Extensión',
                        'numero_ficha_catastral': [
                            {'ficha': '170010104000003170001000000000'}
                        ],
                        'numero_chip': '',
                        'linderos_especiales': ''
                    }
        diccionario_parqueaderos = [{
                        "nombre": "PARQUEADERO DE CARROS ",
                        "numero": "18 SÓTANO -1",
                        "direccion": 'EDIFICIO CENTRIKO"P.H. CALLE 11 B # 4 D - 34 BARRIO VILLA PILAR, EN CHIPRE MANIZALES CALDAS',
                        "matricula": "100-252091",
                        "tipo_ficha_catastral": "Individual",
                        "numero_ficha_catastral": "170010104000003170001000000000",
                        "linderos_especiales": ""
                    }

                    ]
        diccionario_depositos = [

                    ]
        diccionario_apoderado_banco = {
                        'nombre': 'Alejandra Perez Rodriguez',
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
                                'nombre': 'Juan Pablo Cruz López',
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
                        'cantidad_banco_a_hipotecante': 203770000,
                        'cantidad_dada_a_aceptante': 196879227,
                        'gastos_de_gestion': 6890773
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
