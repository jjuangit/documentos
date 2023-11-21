from unittest import TestCase

from models.minutas import DocumentoMinuta
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
            'nombre': 'LUZ MARIA DURAN RODRIGUEZ',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '63.283.505',
            'ciudad_expedicion_identificacion': 'Bucaramanga',
            'genero': genero['FEMENINO'],
        }

        diccionario_poderdantes = [{
            'nombre': 'RAFAEL AUGUSTO DURAN RODRIGUEZ',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '91.080.630',
            'ciudad_expedicion_identificacion': 'San Gil',
            'domicilio': '11 DARIEN RD CARMEL-NEW YORK',
            'estado_civil': estado_civil['SOLTERO_SIN_UNION_MARITAL_DE_HECHO'],
            'genero': genero['MASCULINO'],
        }
        ]

        diccionario_inmueble = {
            'nombre': 'APARTAMENTO',
            'numero': '201 UNIDAD NÚMERO 13',
            'direccion': 'EDIFICIO GALICIA CALLE 5 #5-20,',
            'ciudad_y_o_departamento': 'EN PABLO VI SAN GIL SANTANDER',
            'matricula': '319-87481',
            'municipio_de_registro_orip': 'San Gil',
            'tipo_ficha_catastral': ficha_catastral['MAYOR_EXTENSION'],
            'numero_ficha_catastral': [
                {'ficha': '686790100000000260005000000000'},
            ],
            'linderos_especiales': 'UNIDAD NÚMERO TRECE (Apartamento 201). Está ubicado en su totalidad en el segundo Piso de la edificación, su destino es residencial, se identifica en su puerta de entrada con el número CALLE 5 No 5-20, Apartamento 201, de la actual nomenclatura del MUNICIPIO DE SAN GIL; y consta de: tres (3) habitaciones, dos (2) baños, una (1) sala, un (1) comedor, una (1) cocina, un (1) cuarto ropas, 1 balcón, 1 estudio. Esta unidad dispone de un área privada de 83.65 M2 y un coeficiente de copropiedad de 7.37%. Sus linderos son: POR EL ORIENTE: punto 1 a punto 2 sentido norte sur en una extensión de 4.39 ml con calle 5, giro 90 grados, del punto 2 a punto 3 sentido oriente occidente en una extensión de 1.00 ml con calle 5, giro 90 grados, del punto 3 a punto 4 sentido norte sur en una extensión de 1.24 con calle 5, giro 90 grados, del punto 4 a punto 5 sentido occidente oriente en una extensión de 0.80 ml con calle 5, giro 90 grados, de punto 5 a punto 6 sentido norte sur en una extensión de 3.35 con calle 5; POR EL SUR: punto 6 a punto7 sentido oriente occidente en extensión de 5.55 ml con Samuel, giro 90 grados, de punto 7 a punto 8 sentido norte sur en una extensión de 0.07 ml con Samuel, giro 90 grados, de punto 8 a punto 9 sentido oriente occidente en una extensión de 3.53 ml con Samuel; POR EL OCCIDENTE: punto 9 a punto 10 sentido sur norte en extensión de 9.83 ml con zona común, POR EL NORTE: punto 10 a punto 11 sentido occidente oriente en extensión de 2.96 ml con sucesores Fulgencio Gelves, continua de punto 11 a punto 1 sentido occidente a oriente en extensión de 3.35 con sucesores Fulgencio Gelves, POR EL NADIR: con zona común parqueadero; POR EL CENIT: con la placa de entrepiso que lo separa del apartamento 301 de la misma Edificación.'
        }

        diccionario_parqueaderos = [{
            'nombre': 'PARQUEADERO CARRO',
            'numero': '10',
            'direccion': 'EDIFICIO GALICIA CALLE 5 #5-20, EN PABLO VI SAN GIL SANTANDER',
            'matricula': '319-87478',
            'tipo_ficha_catastral': ficha_catastral['INDIVIDUAL'],
            'numero_ficha_catastral': '',
            'linderos_especiales': 'UNIDAD NÚMERO DIEZ (PARQUEADERO carro 10). Ubicada en el primer piso o nivel del edificio, con acceso directo a la CALLE 5 a través de una puerta de acceso, se identifica en su puerta de entrada con el número CALLE 5 No 5-18. Le corresponde un área privada de 15.32 metros cuadrados y un coeficiente de copropiedad del 1.35%. Esta unidad se destina para uso parqueadero. Consta de un (1) parqueadero carro. Sus linderos son: POR EL ORIENTE: punto 23 a punto 22 sentido norte sur en una extensión de 6.08 ml con parqueadero carro 9; POR EL SUR: punto 22 a punto 25 sentido oriente occidente en extensión de 2.50 ml con Samuel; POR EL OCCIDENTE: punto 25 a punto 24 sentido sur norte en extensión de 6.18 ml con parqueadero carro 11, POR EL NORTE: punto 24 a punto 23 sentido occidente oriente en extensión de 2.50 ml con zona común, POR EL NADIR: con el terreno donde se levanta la Edificación; POR EL CENIT: con la placa de entrepiso que lo separa del apartamento 203 de la misma Edificación.'
        }
        ]

        diccionario_depositos = [
        ]

        diccionario_apoderado_banco = {
            'nombre': 'Carlos Alberto Agudelo Zapata',
            'tipo_identificacion': tipos_identificacion_ciudadano['CEDULA_CIUDADANIA']['nombre'],
            'numero_identificacion': '63.450.000',
            'ciudad_expedicion_identificacion': 'Floridablanca',
            'ciudad_residencia': 'Bucaramanga',
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

        diccionario_prestamo = {
            'cantidad_banco_a_hipotecante': 150204375,
            'cantidad_dada_a_constructora': 145125000,
            'gastos_de_gestion': 5079375
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
        prestamo = Prestamo(**diccionario_prestamo)
        minuta = DocumentoMinuta(apoderado, poderdantes, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco, banco, prestamo)
        minuta.generate_html()
        print(minuta.html)

# command line for run this test:
# python -m unittest test.test_minuta_html.TestMinuta.test_init_minuta_success
