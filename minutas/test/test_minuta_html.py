from unittest import TestCase

from models.minutas import DocumentoMinuta
from models.apoderado import Apoderado
from models.poderdante import Poderdante
from models.banco import Banco
from models.inmueble import InmueblePrincipal
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil


class TestMinuta(TestCase):
    """Iniciar Test"""
    def test_init_minuta_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado = {
            "nombre": "HENRY BARBOSA ORTIZ",
            "tipo_identificacion": tipos_identificacion_ciudadano["CEDULA_CIUDADANIA"]["nombre"],
            "numero_identificacion": "79.708.406",
            "ciudad_expedicion_identificacion": "Bogotá D.C.",
            "genero": genero["MASCULINO"],
        }

        diccionario_poderdante = {
            "nombre": "KATHERINN BARBOSA MARIN",
            "tipo_identificacion": tipos_identificacion_ciudadano["CEDULA_CIUDADANIA"]["nombre"],
            "numero_identificacion": "1.022.399.153",
            "ciudad_expedicion_identificacion": "Bogotá D.C.",
            "domicilio": "UNIT 2 15 GUESS AVE WOLLI CREEK - AUSTRALIA",
            "estado_civil": estado_civil["SOLTERO_SIN_UNION_MARITAL_DE_HECHO"],
            "genero": genero["FEMENINO"],
        }

        diccionario_banco = {
            "nombre": "banco unión s.a",
            "nit": "precio_hipoteca_inmueble",
            "precio_hipoteca_inmueble": "precio_hipoteca_inmueble"
        }

        diccionario_inmueble = {
            "nombre": "APARTAMENTO",
            "numero": "205",
            "direccion": "TORRE 7 ETAPA II, PRATTO PH. CARRERA 78 #11 C - 58"
        }

        diccionario_depositos = [

        ]

        diccionario_parqueaderos = [

        ]

        apoderado = Apoderado(**diccionario_apoderado)
        poderdante = Poderdante(**diccionario_poderdante)
        banco = Banco(**diccionario_banco)
        inmueble = InmueblePrincipal(**diccionario_inmueble)
        depositos = [Deposito(**deposito) for deposito in diccionario_depositos]
        parqueaderos = [Parqueadero(**parqueadero) for parqueadero in diccionario_parqueaderos]
        minuta = DocumentoMinuta(apoderado, poderdante, banco, inmueble, depositos, parqueaderos)
        minuta.generate_html()
        print(minuta.html)

# command line for run this test:
# python -m unittest test.test_minuta_html.TestMinuta.test_init_minuta_success