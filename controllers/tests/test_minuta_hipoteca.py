from unittest import TestCase
from controllers.minuta_hipoteca import generate_minuta_hipoteca
import json

class TestHipoteca(TestCase):

    def test_generate_minuta_hipoteca_success(self):
        # Crea un evento de prueba con datos simulados
        event = {
            "body": json.dumps(
                 {
                    "apoderado": {
                        "nombre": "LUZ MARIA DURAN RODRIGUEZ",
                        "tipo_identificacion": "Cédula de Ciudadanía",
                        "numero_identificacion": "63.283.505",
                        "ciudad_expedicion_identificacion": "Bucaramanga",
                        "genero": "Femenino"
                    },

                    "poderdantes": [{
                        "nombre": "RAFAEL AUGUSTO DURAN RODRIGUEZ       ",
                        "tipo_identificacion": "Cédula de Ciudadanía",
                        "numero_identificacion": "91.080.630",
                        "ciudad_expedicion_identificacion": "San Gil",
                        "domicilio": "11 DARIEN RD CARMEL-NEW YORK",
                        "estado_civil": "Soltero sin unión marital de hecho",
                        "genero": "Masculino"
                    }
                    ],

                    "inmueble": {
                        "nombre": "APARTAMENTO",
                        "numero": "201 UNIDAD NÚMERO 13",
                        "direccion": "EDIFICIO GALICIA CALLE 5 #5-20,",
                        "ciudad_y_o_departamento": "EN PABLO VI SAN GIL SANTANDER",
                        "matricula": "319-87481",
                        "municipio_de_registro_orip": "San Gil",
                        "tipo_ficha_catastral": "Mayor Extensión",
                        "numero_ficha_catastral": [
                            {"ficha": "686790100000000260005000000000"}
                        ],
                        "linderos_especiales": "UNIDAD NÚMERO TRECE (Apartamento 201). Está ubicado en su totalidad en el segundo Piso de la edificación, su destino es residencial, se identifica en su puerta de entrada con el número CALLE 5 No 5-20, Apartamento 201, de la actual nomenclatura del MUNICIPIO DE SAN GIL; y consta de: tres (3) habitaciones, dos (2) baños, una (1) sala, un (1) comedor, una (1) cocina, un (1) cuarto ropas, 1 balcón, 1 estudio. Esta unidad dispone de un área privada de 83.65 M2 y un coeficiente de copropiedad de 7.37%. Sus linderos son: POR EL ORIENTE: punto 1 a punto 2 sentido norte sur en una extensión de 4.39 ml con calle 5, giro 90 grados, del punto 2 a punto 3 sentido oriente occidente en una extensión de 1.00 ml con calle 5, giro 90 grados, del punto 3 a punto 4 sentido norte sur en una extensión de 1.24 con calle 5, giro 90 grados, del punto 4 a punto 5 sentido occidente oriente en una extensión de 0.80 ml con calle 5, giro 90 grados, de punto 5 a punto 6 sentido norte sur en una extensión de 3.35 con calle 5; POR EL SUR: punto 6 a punto7 sentido oriente occidente en extensión de 5.55 ml con Samuel, giro 90 grados, de punto 7 a punto 8 sentido norte sur en una extensión de 0.07 ml con Samuel, giro 90 grados, de punto 8 a punto 9 sentido oriente occidente en una extensión de 3.53 ml con Samuel; POR EL OCCIDENTE: punto 9 a punto 10 sentido sur norte en extensión de 9.83 ml con zona común, POR EL NORTE: punto 10 a punto 11 sentido occidente oriente en extensión de 2.96 ml con sucesores Fulgencio Gelves, continua de punto 11 a punto 1 sentido occidente a oriente en extensión de 3.35 con sucesores Fulgencio Gelves, POR EL NADIR: con zona común parqueadero; POR EL CENIT: con la placa de entrepiso que lo separa del apartamento 301 de la misma Edificación."
                    },

                    "parqueaderos": [
                    {
                        "nombre": "PARQUEADERO CARRO",
                        "numero": "10",
                        "direccion": "EDIFICIO GALICIA CALLE 5 #5-20, EN PABLO VI SAN GIL SANTANDER",
                        "matricula": "319-87478",
                        "tipo_ficha_catastral": "",
                        "numero_ficha_catastral": "",
                        "linderos_especiales": "UNIDAD NÚMERO DIEZ (PARQUEADERO carro 10). Ubicada en el primer piso o nivel del edificio, con acceso directo a la CALLE 5 a través de una puerta de acceso, se identifica en su puerta de entrada con el número CALLE 5 No 5-18. Le corresponde un área privada de 15.32 metros cuadrados y un coeficiente de copropiedad del 1.35%. Esta unidad se destina para uso parqueadero. Consta de un (1) parqueadero carro. Sus linderos son: POR EL ORIENTE: punto 23 a punto 22 sentido norte sur en una extensión de 6.08 ml con parqueadero carro 9; POR EL SUR: punto 22 a punto 25 sentido oriente occidente en extensión de 2.50 ml con Samuel; POR EL OCCIDENTE: punto 25 a punto 24 sentido sur norte en extensión de 6.18 ml con parqueadero carro 11, POR EL NORTE: punto 24 a punto 23 sentido occidente oriente en extensión de 2.50 ml con zona común, POR EL NADIR: con el terreno donde se levanta la Edificación; POR EL CENIT: con la placa de entrepiso que lo separa del apartamento 203 de la misma Edificación."
                    }
                    ],

                    "depositos": [
                    ],

                    "apoderado_banco": {
                        "nombre": "Nelly Parra Parra",
                        "tipo_identificacion": "Cédula de Ciudadanía",
                        "numero_identificacion": "",
                        "ciudad_expedicion_identificacion": "",
                        "ciudad_residencia": "",
                        "genero": "",
                        "tipo_apoderado": "",
                        "tipo_poder": "",
                        "escritura": ""
                    },

                    "representante_banco": {
                        "nombre": "Héctor Fabio Rodríguez Prado",
                        "tipo_identificacion": "",
                        "numero_identificacion": "",
                        "tipo_representante": "",
                        "ciudad_expedicion_identificacion": "",
                        "ciudad_residencia": "",
                        "genero": ""
                    },

                    "banco": {
                        "nombre": "banco unión s.a",
                        "nit": ""
                    },

                    "prestamo": {
                        "cantidad_banco_a_hipotecante": 150204375,
                        "cantidad_dada_a_aceptante": 145125000,
                        "gastos_de_gestion": 5079375
                    }
                }
            )
            }

        # Llama a la función y verifica la respuesta
        result = generate_minuta_hipoteca(event, None)
        print(result)

        # Verifica que el código de estado sea 200 y que el cuerpo no esté vacío
        self.assertEqual(result["statusCode"], 200)
        self.assertIsNotNone(result["body"])

    def test_generate_minuta_failure(self):
        # Crea un evento de prueba con datos incorrectos o incompletos
        test_event = {'body': '{"poderdantes": [...], ...}'}

        # Llama a la función y verifica la respuesta
        result = generate_minuta_hipoteca(test_event, None)

        # Verifica que el código de estado sea 500 y que el cuerpo indique un error
        self.assertEqual(result["statusCode"], 500)
        self.assertIn("Error", result["body"])

# command line for run this test:
# python -m unittest controllers.tests.test_minuta_hipoteca.TestHipoteca.test_generate_minuta_hipoteca_success