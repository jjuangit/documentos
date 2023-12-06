from unittest import TestCase
from controllers.documentos import DocumentosController


class TestPoder(TestCase):
    def test_create_documento_poder(self):
        '''Crear documento Poder'''

        event = {
            "poderdantes": [{
                "nombre": "Addi Anyul Sanchez Rojas",
                "tipo_identificacion": "Cédula de ciudadanía",
                "ciudad_expedicion_identificacion": "Bogotá D.C.",
                "numero_identificacion": "52856754",
                "domicilio_pais": "Estados Unidos",
                "domicilio_municipio": "California",
                "domicilio_departamento": "California",
                "estado_civil": "Soltero sin unión marital de hecho",
                "genero": "Femenino"
            }, {
                "nombre": "Linda Mayerly Sanchez Rojas",
                "tipo_identificacion": "Cédula de ciudadanía",
                "ciudad_expedicion_identificacion": "Bogotá D.C.",
                "numero_identificacion": "1013663493",
                "domicilio_pais": "Estados Unidos",
                "domicilio_municipio": "California",
                "domicilio_departamento": "San Diego",
                "estado_civil": "Casado sin sociedad conyugal vigente",
                "genero": "Femenino"
            }
            ],

            "pareja_poderdante": None,

            "apoderado": {
                "nombre": "Edna Maritza Gonzalez Beltran",
                "tipo_identificacion": "Cédula de ciudadanía",
                "numero_identificacion": "51855403",
                "ciudad_expedicion_identificacion": "Bogotá D.C",
                "genero": "Femenino"
            },

            "inmueble": {
                "nombre": "Apartamento",
                "numero": "1021 Torre 3",
                "direccion": "CONJUNTO RESIDENCIAL ZAJARI - ZENTRAL, CALLE 16C 78-83",
                "departamento": "Antioquia",
                "ciudad": "Medellin",
                "matricula": "50C-2149874",
                "tipo_ficha_catastral": "Individual",
                "numero_ficha_catastral": "006527452600000000"
            },

            "parqueaderos": [
                {
                    "nombre": "PARQUEADERO",
                    "numero": "555",
                    "direccion": "CALLE 16C",
                    "matricula": "123123213",
                    "tipo_ficha_catastral": "Individual",
                    "numero_ficha_catastral": "987654321"
                }, {
                    "nombre": "PARQUEADERO DE USO EXCLUSIVO",
                    "numero": "666",
                    "direccion": "CALLE 16C",
                    "matricula": "333123213",
                    "tipo_ficha_catastral": "Individual",
                    "numero_ficha_catastral": "9007654321"
                }
            ],

            "depositos": [
                {
                    "nombre": "DEPÓSITO",
                    "numero": "505",
                    "direccion": "CALLE 16C",
                    "matricula": "343434",
                    "tipo_ficha_catastral": "Individual",
                    "numero_ficha_catastral": "123456789"
                }, {
                    "nombre": "DEPÓSITO",
                    "numero": "999",
                    "direccion": "CALLE 16C",
                    "matricula": "00343434",
                    "tipo_ficha_catastral": "Individual",
                    "numero_ficha_catastral": "00123456789"
                }
            ],

            "banco": {
                "nombre": "Bancolombia"
            },

            "declaraciones": {
                "afectar_vivienda_familiar": "No",
                "pareja_hace_parte_compraventa": "No",
                "municipio_firma": "",
                "departamento_firma": "",
                "pais_firma": "",
                "fecha_firma": ""
            }
        }
        controller = DocumentosController(event, None)
        response = controller.create_poder()

        self.assertEqual(response['statusCode'], 201)
        self.assertIsNotNone(response['body'])

# command line for run this test:
# python -m unittest controllers.tests.test_poder
