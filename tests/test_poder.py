from unittest import TestCase

from models.poder import DocumentoPoder
from models.apoderado import Apoderado
from models.parqueaderos import ParqueaderoPoder
from models.inmueble import InmueblePoder
from models.depositos import DepositoPoder
from models.poderdantes import PoderdantePoder
from models.banco import BancoPoder
from models.declaraciones import Declaraciones
from models.pareja_poderdante import ParejaPoderdante
from catalogs.catalogos import tipos_identificacion_ciudadano
from catalogs.catalogos import genero
from catalogs.catalogos import estado_civil
from catalogs.catalogos import respuesta


class TestPoder(TestCase):

    def test_init_poder_success(self):
        diccionario_poderdantes = [{
            "nombre": "Addi Anyul Sanchez Rojas",
            "tipo_identificacion": tipos_identificacion_ciudadano["CEDULA_CIUDADANIA"]["nombre"],
            "ciudad_expedicion_identificacion": "Bogotá D.C.",
            "numero_identificacion": "52856754",
            "domicilio_pais": "Estados Unidos",
            "domicilio_municipio": "California",
            "domicilio_departamento": "California",
            "estado_civil": estado_civil["CASADO_CON_SOCIEDAD_CONYUGAL_VIGENTE"],
            "genero": genero["FEMENINO"],
        }, {
            "nombre": "Linda Mayerly Sanchez Rojas",
            "tipo_identificacion": tipos_identificacion_ciudadano["CEDULA_CIUDADANIA"]["nombre"],
            "ciudad_expedicion_identificacion": "Bogotá D.C.",
            "numero_identificacion": "1013663493",
            "domicilio_pais": "Estados Unidos",
            "domicilio_municipio": "California",
            "domicilio_departamento": "San Diego",
            "estado_civil": estado_civil["SOLTERO_SIN_UNION_MARITAL_DE_HECHO"],
            "genero": genero["FEMENINO"],
        }
        ]
        diccionario_pareja_poderdante = None

        diccionario_apoderado = {
            "nombre": "Edna Maritza Gonzalez Beltran",
            "tipo_identificacion": "Cédula de ciudadanía",
            "numero_identificacion": "51855403",
            "ciudad_expedicion_identificacion": "Bogotá D.C",
            "genero": genero["FEMENINO"],
        }

        diccionario_inmueble = {
            "nombre": "Apartamento",
            "numero": "1021 Torre 3",
            "direccion": "CONJUNTO RESIDENCIAL ZAJARI - ZENTRAL, CALLE 16C 78-83",
            "ciudad_y_o_departamento": "Antioquia - Medellin",
            "matricula": "50C-2149874",
            "tipo_ficha_catastral": "Individual",
            "numero_ficha_catastral": "006527452600000000"
        }

        diccionarios_parqueaderos = [
            {
                "nombre": "PARQUEADERO ASIGNADO DE USO EXCLUSIVO",
                "numero": "505",
                "direccion": "CALLE 16C",
                "matricula": "50C-2149874",
                "tipo_ficha_catastral": "Individual",
                "numero_ficha_catastral": "987654321"
            },
            {
                "nombre": "PARQUEADERO ASIGNADO",
                "numero": "600",
                "direccion": "CALLE 16C",
                "matricula": "50C-2149888",
                "tipo_ficha_catastral": "Individual",
                "numero_ficha_catastral": "987654321"
            }
        ]

        diccionarios_depositos = [
            {
                "nombre": "DEPOSITO",
                "numero": "777",
                "direccion": "CALLE 16C",
                "matricula": "50C-2149874",
                "tipo_ficha_catastral": "Individual",
                "numero_ficha_catastral": "987654321"
            }, {
                "nombre": "DEPOSITO",
                "numero": "999",
                "direccion": "CALLE 16C",
                "matricula": "50C-2149888",
                "tipo_ficha_catastral": "Individual",
                "numero_ficha_catastral": "987654321"
            },
        ]

        diccionario_banco = {
            "nombre": "Bancolombia"
        }

        diccionario_declaraciones = {
            "afectar_vivienda_familiar": respuesta["NO"],
            "pareja_hace_parte_compraventa": respuesta["NO"],
            "municipio_firma": "Envigado",
            "departamento_firma": "Antioquia",
            "pais_firma": "Colombia",
            "fecha_firma": "04/12/2023"
        }

        poderdantes = [PoderdantePoder(**poderdante)
                       for poderdante in diccionario_poderdantes]
        if diccionario_pareja_poderdante is None:
            pareja_poderdante = None
        else:
            pareja_poderdante = ParejaPoderdante(**diccionario_pareja_poderdante)
        apoderado = Apoderado(**diccionario_apoderado)
        parqueaderos = [ParqueaderoPoder(
            **parqueadero) for parqueadero in diccionarios_parqueaderos]
        depositos = [DepositoPoder(
            **deposito) for deposito in diccionarios_depositos]
        inmueble = InmueblePoder(**diccionario_inmueble)
        declaraciones = Declaraciones(**diccionario_declaraciones)
        banco = BancoPoder(**diccionario_banco)
        poder = DocumentoPoder(poderdantes, pareja_poderdante, apoderado,
                               inmueble, parqueaderos, declaraciones, banco, depositos)
        poder.generate_html()
        print(poder.html)

# command line for run this test:
# python -m unittest tests.test_poder.TestPoder.test_init_poder_success
