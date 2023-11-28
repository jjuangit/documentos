from unittest import TestCase

from models.compraventa_leasing import DocumentoCompraventaLeasing
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

class TestCompraventaLeasing(TestCase):
    """Iniciar Test"""

    def test_init_compraventa_leasing_success(self):
        """Funcion para imprimir el html de la compraventa leasing"""
        diccionario_apoderado = {
            'nombre': 'PATRICIA ORTIZ VARON',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '65.766.050',
            'ciudad_expedicion_identificacion': 'Ibague',
            'genero': genero['FEMENINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'SANDRA ISABEL HERRERA NIETO',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '1.126.398.298',
            'ciudad_expedicion_identificacion': 'Con Lisboa Por',
            'domicilio': 'Nyköping - Suecia',
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
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '763640100000007701796000000000'}
            ],
            'linderos_especiales': '"TORRE 4 APARTAMENTO 706. LOCALIZACIÓN: Localizado en el Piso 7 de la TORRE 4 del Proyecto Flora, ubicado en Santa Marta. Las Áreas Generales se clasifican como: ÁREA CONSTRUIDA de cincuenta y ocho punto ochenta y cuatro metros cuadrados (58.84 m2). ÁREA PRIVADA CONSTRUIDA de cuarenta y nueve punto cuarenta y siete metros cuadrados (49.47 m2). Cuenta con una ÁREA PRIVADA CONSTRUIDA de BALCÓN y BALCÓN TÉCNICO de tres punto sesenta y tres metros cuadrados (3.63 m2). La diferencia entre el área construida y el área privada es de cinco punto sesenta y cuatro metros cuadrados (5.74 m2). DEPENDENCIAS: Sala-Comedor, cocina, ropas, disponible, dos (2) alcobas, un (1) baño y espacio para futuro baño. LINDEROS HORIZONTALES: Entre los puntos 1 y 2: Línea recta, en dimensión de cinco punto veinticuatro metros (5.24 m); con área privada construida. Entre los puntos 2 y 3: Línea quebrada, en dimensiones de dos punto ochenta y cinco metros (2.85 m); cero punto veintitrés metros (0.23 m), cero punto treinta y seis metros (0.36 m), cero punto sesenta y seis metros (0.66 m), cero punto diez metros (0.10 m), uno punto cincuenta metros (1.05 m), uno punto ochenta metros (1.80 m), tres punto diez metros (3.10 m), cero punto diez metros (0.10 m), tres punto diez metros (3.10 m), y dos punto cincuenta y cuatro metros (2.54 m); parte con área común libre, y parte con área privada construida de la misma unidad. Entre los puntos 3 y 4: Línea quebrada, en dimensiones de dos punto cuarenta y cinco metros (2.45 m), cero punto dieciocho metros (0.18 m), cero punto cincuenta y cinco metros (0.55 m), uno punto cincuenta y seis metros (1.56 m), cero punto diez metros (0.10 m), tres punto quince metros (3.15 m), y tres punto cincuenta y tres metros (3.53 m); parte con área común libre, y parte con área privada construida de la misma unidad. Entre los puntos 4 y 1: Línea quebrada, en dimensiones de dos punto setenta metros (2.70 m), cero punto cincuenta y uno metros (0.51 m), cero punto diez metros (0.10 m), cero punto cincuenta y uno metros (0.51 m), uno punto treinta y cinco metros (1.35 m), cero punto doce metros (0.12 m), cero punto ochenta metros (0.80 m), uno punto cero nueve metros (1.09 m), dos punto veinticinco metros (2.25 m), uno punto cincuenta y dos metros (1.52 m), cero punto diez metros (0.10 m), uno punto cuarenta y dos metros (1.42 m), uno punto treinta y cinco metros (1.35 m), cero punto veintiséis metros (0.26 m), cero punto ochenta metros (0.80 m), uno punto cero seis metros (1.06 m), uno punto veinte metros (1.20 m), cero punto diez metros (0.10 m), uno punto cero ocho metros (1.08 m), uno punto cero ocho metros (1.08 m), cero punto dieciocho metros (0.18 m), cero punto cincuenta metros (0.50 m), cero punto noventa y dos metros (0.92 m), cero punto dieciocho metros (0.18 m), cero punto noventa metros (0.90 m), uno punto diecisiete metros (1.17 m), cero punto cero ocho metros (0.08 m), cero punto setenta y dos metros (0.72 m), y dos metros (2.00 m); parte con área común construida, y parte con área privada construida. CONTORNOS INTERNOS: COLUMNA O MURO INTERIOR: Entre los puntos 5 y 6: Línea quebrada, en dimensiones de uno punto diez metros (1.10 m), y cero punto diez metros (0.10 m). Entre los puntos 6 y 5: Línea quebrada, en dimensiones de uno punto diez metros (1.10 m), y cero punto diez metros (0.10 m). BALCÓN. Las Áreas Generales se clasifican como: ÁREA PRIVADA CONSTRUIDA de dos punto cuarenta y tres metros cuadrados (2.43 m2). DEPENDENCIAS: Un (1) balcón. LINDEROS HORIZONTALES: Entre los puntos 7 y 8: Línea quebrada, en dimensiones de cero punto setenta y seis metros (0.76 m), y tres punto veinte metros (3.20 m); parte con área común libre, y parte con área privada construida. Entre los puntos 8 y 7: Línea quebrada, en dimensiones de cero punto setenta y seis metros (0.76 m), y tres punto veinte metros (3.20 m); parte con área común libre, y parte con dependencias de la misma unidad. BALCÓN TÉCNICO. Las Áreas Generales se clasifican como: ÁREA PRIVADA CONSTRUIDA de uno punto veinte metros cuadrados (1.20 m2). DEPENDENCIAS: Un (1) balcón técnico. LINDEROS HORIZONTALES: Entre los puntos 9 y 10: Línea quebrada, en dimensiones de cero punto ochenta y siete metros (0.87 m), y uno punto treinta y nueve metros (1.39 m); parte con área común libre, y parte con dependencias de la misma unidad. Entre los puntos 10 y 9: Línea quebrada, en dimensiones de cero punto ochenta y siete metros (0.87 m), y uno punto treinta y nueve metros (1.39 m); parte con área común libre, y parte con dependencias de la misma unidad. LINDEROS VERTICALES: La altura libre aproximada es de dos punto cuarenta metros (2.40 m). NADIR: Placa de entrepiso al medio, colindante con Piso 6. CENIT: Placa de entrepiso al medio, colindante con Piso 8."'
        }
        diccionario_parqueaderos = [
        {
            'nombre': 'GARAJE',
            'numero': 'NRO 71',
            'direccion': '',
            'matricula': '370-1098010',
            'tipo_ficha_catastral': '',
            'numero_ficha_catastral': '',
            'linderos_especiales': ''
        }
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
            'tipo_poder': '',
            'escritura': ''
        }

        diccionario_representante_banco = {
            'nombre': 'Héctor Fabio Rodríguez Prado',
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
            'cantidad_banco_a_hipotecante': 86422500,
            'cantidad_dada_a_aceptante': 83500000,
            'gastos_de_gestion': 2922500
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
        compraventa = DocumentoCompraventaLeasing(apoderado, poderdantes, inmueble, parqueaderos,
                                 depositos, apoderado_banco, representante_banco, banco)
        compraventa.generate_html()
        print(compraventa.html)

# command line for run this test:
# python -m unittest test.test_compraventa_leasing.TestCompraventaLeasing.test_init_compraventa_leasing_success