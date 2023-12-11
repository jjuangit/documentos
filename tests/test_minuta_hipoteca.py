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
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from utils.strip_spaces import strip_dict_or_list

class TestMinutaHipoteca(TestCase):
    """Iniciar Test"""

    def test_init_minuta_hipoteca_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado= {
                        'nombre': 'LUCELLY VIAFARA CAICEDO',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '31.996.407',
                        'ciudad_expedicion_identificacion': 'Cali',
                        'genero': 'Femenino'
                    }
        diccionario_poderdantes = [
                    {
                        'nombre': 'SANTY ESTEBAN JIMENEZ VIAFARA',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '1.151.959.408',
                        'ciudad_expedicion_identificacion': 'Cali',
                        'domicilio': 'BROOKLYN - NEW YORK',
                        'estado_civil': 'Soltero sin unión marital de hecho',
                        'genero': 'Masculino'
                    }
                    ]
        diccionario_inmueble = {
                        'nombre': 'MANZANA I12 CASA 8B',
                        'numero': 'URBANIZACIÓN MANZANARES CIUDAD DEL VALLE 2',
                        'direccion': 'CALLE 16 # 22B OESTE - 19',
                        'ciudad_y_o_departamento': 'EN CANDELARIA VALLE DEL CAUCA',
                        'matricula': '378-267102',
                        'municipio_de_registro_orip': 'Palmira',
                        'tipo_ficha_catastral': 'Mayor Extensión',
                        'numero_ficha_catastral': [
                            {'ficha': '00100040279000'},
                            {'ficha': '00100040139000'}
                        ],
                        'numero_chip': '',
                        'linderos_especiales': '"MANZANA I12 CASA 8B. A esta casa se accede a través del lote común de uso exclusivo identificado con Calle 16 # 22B Oeste -19 de la actual nomenclatura urbana del Corregimiento de El Carmelo. ÁREA TOTAL PRIVADA CONSTRUIDA: Área=45,37 m2. Discriminadas así: Área privada construida Piso 1=22,31 m2 + Área privada construida Piso 2=23,06 m2. PISO 1: NADIR: 0,00. CENIT: 2,33 metros. ALTURA LIBRE: 2,33 metros (Del piso a la parte inferior de la losa sin contar el acabado). LINDEROS: NORTE: Del punto 1 al punto 2, en línea quebrada, con una distancia de 4,00 metros, colindando con área lote común de uso exclusivo casa 8B. ESTE: Del punto 2 al punto 3, en línea recta, con una distancia de 6,61 metros, colindando con piso 1 casa 8A. SUR: Del punto 3 al punto 4, en línea quebrada, con una distancia de 5,63 metros, colindando con patio común de uso exclusivo casa 8B. OESTE: Del punto 4 al punto 1, en línea recta, con una distancia de 4,99 metros, colindando con piso 1 casa 7A. PISO 2: NADIR: 2,43 metros (Del piso superior de la losa sin contar el acabado). CENIT: 4,65 / 5,41 metros (A la parte inferior de la cubierta en pendiente). ALTURA LIBRE: 2,22 / 2,98 metros. LINDEROS: NORTE: Del punto 5 al punto 6, en línea quebrada, con una distancia de 4,33 metros, colindando con vacío a área lote común de uso exclusivo casa 8B. ESTE: Del punto 6 al punto 7, en línea recta, con una distancia de 6,49 metros, colindando con piso 2 casa 8A. SUR: Del punto 7 al punto 8, en línea quebrada, con una distancia de 5,38 metros, colindando con vacío a patio común de uso exclusivo casa 8B. OESTE: Del punto 8 al punto 5, en línea recta, con una distancia de 5,44 metros, colindando con piso 2 casa 7A. ÁREA TOTAL CONSTRUIDA: 50,33 m2, Discriminada así: ÁREA TOTAL PRIVADA CONSTRUIDA: 45,37 m2 + Área Total Muros Comunes: 4,96 m2. A esta casa se le asigna el uso exclusivo del lote común que se describe a continuación: LOTE COMÚN DE USO EXCLUSIVO: Área= 60,00 m2, discriminada así: Área construida primer Piso=24,40 m2, Área lote común de uso exclusivo= 18,02 m2 + Área patio común de uso exclusivo= 17,58 m2. Comprendido dentro de los siguientes LINDEROS: NORTE: En línea recta, con una distancia de 4,00 metros, colindando con Calle 16. ESTE: En línea recta, con una distancia de 15,00 metros, colindando con lote 8A. SUR: En línea recta, con una distancia de 4,00 metros, colindando con lote 1. OESTE: En línea recta, con una distancia de 15,00 metros, colindando con lote 7A. ARTÍCULO 5.- COEFICIENTES DE COPROPIEDAD: Los coeficientes del LOTE se regirán por lo indicado en el CAPÍTULO VI de la PRIMERA PARTE de este acto. En virtud de lo anterior, se señalan a continuación los coeficientes de propiedad de los bienes de dominio particular que integran el LOTE: BIEN PRIVADO - ÁREA PRIVADA CONSTRUIDA - COEFICIENTE CASA 8B - 45,37 - 50% CASA 8A - 45,37 - 50% TOTAL - 90,74 - 100%"'
                    }
        diccionario_parqueaderos = [
                    ]
        diccionario_depositos = [
                    ]
        diccionario_apoderado_banco = {
                        'nombre': 'Lina Marcela Palau Zea',
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
                                'nombre': 'Héctor Fabio Rodríguez Prado',
                                'tipo_identificacion': '',
                                'numero_identificacion': '',
                                'ciudad_expedicion_identificacion': '',
                                'ciudad_residencia': '',
                                'genero': '',
                                'tipo_representante': ''
                            }
        diccionario_banco = {
                    'nombre': 'Banco unión s.a',
                    'nit': '860.006.797-9'
                }
        diccionario_prestamo = {
                        'cantidad_banco_a_hipotecante': 90000000,
                        'cantidad_dada_a_aceptante': 86956522,
                        'gastos_de_gestion': 3043278
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
