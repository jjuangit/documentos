import json
from pathlib import Path
from unittest import TestCase

from models.minutas import DocumentoMinuta
from models.apoderado import Apoderado
from models.poderdantes import Poderdante
from models.banco import Banco
from models.inmueble import InmueblePrincipal
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_especial import ApoderadoEspecial
from models.representante_legal import RepresentanteLegal
from utils.strip_spaces import strip_dict_or_list
from utils.exceptions import GeneracionDeMinutaError


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
            json_banco = cases['banco']
            json_inmueble = cases['inmueble']
            json_parqueaderos = cases['parqueaderos']
            json_depositos = cases['depositos']
            json_apoderado_especial = cases['apoderado_especial']
            json_representante_legal = cases['representante_legal']

            try:
                apoderado = Apoderado(**json_apoderado)
                poderdantes = [Poderdante(**poderdante)
                               for poderdante in json_poderdantes]
                banco = Banco(**json_banco)
                inmueble = InmueblePrincipal(**json_inmueble)
                depositos = [Deposito(**deposito)
                             for deposito in json_depositos]
                parqueaderos = [Parqueadero(**parqueadero)
                                for parqueadero in json_parqueaderos]
                apoderado_especial = ApoderadoEspecial(
                    **json_apoderado_especial)
                representante_legal = RepresentanteLegal(
                    **json_representante_legal)
                minuta = DocumentoMinuta(apoderado, poderdantes, banco, inmueble, depositos,
                                         parqueaderos, apoderado_especial, representante_legal)
            except Exception as error:
                print(f'Error al crear la minuta: {error}')
                raise GeneracionDeMinutaError(
                    'No se pudo generar el html de la minuta') from error

            minuta.generate_html()
            print(minuta.html)

# command line for run this test:
# python -m unittest test.test_minuta_json.TestMinuta.test_init_minuta_success
