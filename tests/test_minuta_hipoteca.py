from unittest import TestCase

from models.hipoteca import DocumentoMinutaHipoteca
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
from catalogs.catalogos import ficha_catastral
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from utils.strip_spaces import strip_dict_or_list

class TestMinutaHipoteca(TestCase):
    """Iniciar Test"""

    def test_init_minuta_hipoteca_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado = {
            'nombre': 'NASLY BIBIANA OSPINA RIVERA',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '39.790.848',
            'ciudad_expedicion_identificacion': 'BOGOTÁ D.C.',
            'genero': genero['FEMENINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'MARIA PAULA OSPINA BARACALDO',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '1.015.457.203',
            'ciudad_expedicion_identificacion': 'BOGOTÁ D.C.',
            'domicilio': 'SWIEQI - MALTA',
            'estado_civil': estado_civil['SOLTERO_CON_UNION_MARITAL_Y_SOCIEDAD_PATRIMONIAL_VIGENTE'],
            'genero': genero['FEMENINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '2008-TORRE 3-ETAPA 1',
            'direccion': 'CONJUNTO RESIDENCIAL NATURA LIVING PH CARRERA 74 #152B-70',
            'ciudad_y_o_departamento': 'EN EL PLAN BOGOTÁ D.C.',
            'matricula': '50N-20919524',
            'municipio_de_registro_orip': 'Cali',
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '009128260300000000'}
            ],
            'linderos_especiales': 'TORRE 3 APARTAMENTO 2008. LOCALIZACIÓN: Localizado en el Piso 20 de la TORRE 3, en la ETAPA 1 del Proyecto Natura Living, ubicado en Bogotá. Las Áreas Generales se clasifican como: ÁREA CONSTRUIDA de treinta y siete punto cincuenta y seis metros cuadrados (37.56 m2). ÁREA PRIVADA CONSTRUIDA de treinta y uno punto cuarenta y nueve metros cuadrados (31.49 m2). La diferencia entre el área construida y el área privada es de seis punto cero siete metros cuadrados (6.07 m2). DEPENDENCIAS: Salón comedor, cocina, ropas, alcoba 1, alcoba 2 y baño. LINDEROS HORIZONTALES: Entre los puntos 1 y 2: Línea quebrada, en dimensiones de uno punto dieciséis metros (1.16 m), uno punto treinta y tres metros (1.33 m), cero punto quince metros (0.15 m), un punto tres punto sesenta y nueve metros (3.69 m), cero punto setenta y tres metros (0.73 m), un punto treinta y dos metros (1.32 m), cero punto nueve metros (0.09 m), y cero punto ochenta y ocho metros (0.88 m); con área común libre. Entre los puntos 3 y 4: Línea quebrada, en dimensiones de dos punto treinta y nueve metros (2.39 m), uno punto cuarenta metros (1.40 m), cero punto dieciocho metros (0.18 m), uno punto cincuenta y ocho metros (1.58 m), cero punto cero nueve metros (0.09 m), uno punto veinticinco metros (1.25 m), y tres punto treinta y cuatro metros (3.34 m); parte con área común libre, y parte con área privada construida. Entre los puntos 4 y 1: Línea quebrada, en dimensiones de tres punto cincuenta y seis metros (3.56 m), cero punto noventa y cinco metros (0.95 m), cero punto veintiséis metros (0.26 m), uno punto treinta metros (1.30 m), cero punto cuarenta y ocho metros (0.48 m), cero punto veinte metros (0.20 m), cero punto setenta y tres metros (0.73 m), dos punto sesenta y uno metros (2.61 m), cero punto noventa metros (0.90 m), cero punto dieciséis metros (0.16 m), y uno punto treinta y tres metros (1.33 m); con área común construida. LINDEROS VERTICALES: La altura libre aproximada es de dos punto cuarenta metros (2.40 m). NADIR: Entre piso medio, colindante con Piso 19. CENIT: Entre piso al medio, colindante con Piso 21.'
        }
        diccionario_parqueaderos = [

        ]

        diccionario_depositos = [

        ]

        diccionario_apoderado_banco = {
            'nombre': 'Germán Leonardo Kalil Méndez',
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
            'ciudad_residencia': '',
            'genero': genero['FEMENINO'],
            'tipo_representante': tipo_representante_banco['SUPLENTE'],
        }

        diccionario_banco = {
            'nombre': 'Banco unión s.a',
            'nit': '',
        }

        diccionario_prestamo = {
            'cantidad_banco_a_hipotecante': 97497000,
            'cantidad_dada_a_aceptante': 94200000,
            'gastos_de_gestion': 3297000
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
        minuta_hipoteca = DocumentoMinutaHipoteca(apoderado, poderdantes, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco, 
                                 banco, prestamo
                                 )
        minuta_hipoteca.generate_html()
        print(minuta_hipoteca.html)

# command line for run this test:
# python -m unittest tests.test_minuta_hipoteca.TestMinutaHipoteca.test_init_minuta_hipoteca_success
