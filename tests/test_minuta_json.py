import json
from pathlib import Path
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
from utils.strip_spaces import strip_dict_or_list
from utils.exceptions import GeneracionDeMinutaError
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos

class TestMinuta(TestCase):
    def test_init_minuta_success(self):
        for archivo in Path("json_files").glob("*.json"):
            carpeta = 'json_files/'
            carpeta_archivo = carpeta + archivo.name
            with open(carpeta_archivo, encoding="utf-8") as file:
                cases = json.load(file)
                cases = strip_dict_or_list(cases)
            json_apoderado = cases['apoderado']
            json_poderdantes = cases['poderdantes']
            json_inmueble = cases['inmueble']
            json_parqueaderos = cases['parqueaderos']
            json_depositos = cases['depositos']
            json_apoderado_banco = cases['apoderado_banco']
            json_representante_banco = cases['representante_banco']
            json_banco = cases['banco']
            json_prestamo = cases['prestamo']

            try:
                if json_apoderado is None:
                    apoderado = None
                else:
                    apoderado = Apoderado(**json_apoderado)
                poderdantes = [Poderdante(**poderdante)
                               for poderdante in json_poderdantes]
                inmueble = Inmueble(**json_inmueble)
                depositos = [Deposito(**deposito)
                             for deposito in json_depositos]
                parqueaderos = [Parqueadero(**parqueadero)
                                for parqueadero in json_parqueaderos]
                for banck_apoderado in apoderados_banco:
                    if banck_apoderado['nombre'] == json_apoderado_banco['nombre']:
                        apoderado_banco = ApoderadoBanco(**banck_apoderado)
                        break
                else:
                    apoderado_banco = ApoderadoBanco(
                        **json_apoderado_banco)
                for representante in representantes_banco:
                    if representante['nombre'] == json_representante_banco['nombre']:
                        representante_banco = RepresentanteBanco(**representante)
                        break
                else:
                    representante_banco = RepresentanteBanco(
                        **json_representante_banco)
                    
                for bank in bancos:
                    if bank['nombre'] == json_banco['nombre']:
                        banco = Banco(**bank)
                        break
                else:
                    banco = Banco(**json_banco)
                prestamo = Prestamo(**json_prestamo)
                minuta = DocumentoHipoteca(apoderado, poderdantes, inmueble, depositos,
                                         parqueaderos, apoderado_banco, representante_banco, banco, prestamo)
            except Exception as error:
                print(f'Error al crear la minuta: {error}')
                raise GeneracionDeMinutaError(
                    'No se pudo generar el html de la minuta') from error

            minuta.generate_html()
            print(minuta.html)
            print('\n\n')

# command line for run this test:
# python -m unittest test.test_minuta_json.TestMinuta.test_init_minuta_success
