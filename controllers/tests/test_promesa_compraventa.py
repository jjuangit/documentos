from unittest import TestCase
from controllers.documentos import DocumentosController

class TestHipoteca(TestCase):

    def test_create_promesa_compraventa(self):
        event = {
                "apoderado": {
                    'nombre': 'DAIRY PAOLA MEJIA PASTRANA',
                    'tipo_identificacion': 'Cédula de Ciudadanía',
                    'numero_identificacion': '1.083.040.935',
                    'ciudad_expedicion_identificacion': 'Santa Marta',
                    'genero': 'Femenino',
                    'tipo_apoderado': 'Especial',
                    'escritura': '',
                    'fecha_autenticacion_poder': '01/11/2023',
                    'tipo_dependencia_autenticacion': 'Consulado',
                    'nombre_dependencia': 'Consulado General Central de Colombia',
                    'ciudad_dependencia': 'New York - Estados Unidos',
                },
                "poderdantes": [{
                    'nombre': 'JORGE ALBEIRO CÁCERES MUNIVE',
                    'tipo_identificacion': 'Cédula de Ciudadanía',
                    'numero_identificacion': '79.409.698',
                    'ciudad_expedicion_identificacion': 'Bogotá',
                    'domicilio': 'NEW ROCHELLE- NEW YORK',
                    'estado_civil': 'Soltero sin unión marital de hecho',
                    'genero': 'Masculino',
                }],
                "inmueble": {
                    'nombre': 'APARTAMENTO',
                    'numero': '207 PISO-2 TORRE-4',
                    'direccion': 'CONJUNTO RESIDENCIAL VENECIA INN CARRERA 34 # 43 - 15',
                    'ciudad_y_o_departamento': 'EN SANTA MARTA MAGDALENA',
                    'matricula': '080-163243',
                    'municipio_de_registro_orip': 'Santa Marta',
                    'tipo_ficha_catastral': 'Mayor Extensión',
                    'numero_ficha_catastral': [
                        {'ficha': '0002000000070001000000000'},
                    ],
                    'numero_chip': ''
                },
                "parqueaderos": [

                ],
                "depositos": [

                ],
                "apoderado_banco": {
                    'nombre': 'Gloria Esperanza Garcia Troncoso',
                    'tipo_identificacion': 'Cédula de Ciudadanía',
                    'numero_identificacion': '1082842113',
                    'ciudad_expedicion_identificacion': 'Santa Marta',
                    'ciudad_residencia': 'Santa Marta',
                    'genero': 'Femenino',
                    'tipo_apoderado': 'General',
                    'tipo_poder': 'Escriturado',
                    'escritura': 'Escritura Pública No. 0020 del 7 de enero de 2022 Notaría Catorce de Cali',
                },
                "representante_banco": {
                    'nombre': 'Héctor Fabio Rodríguez Prado',
                    'tipo_identificacion': 'Cédula de Ciudadanía',
                    'numero_identificacion': '14650246',
                    'ciudad_expedicion_identificacion': 'Ginebra',
                    'ciudad_residencia': 'Cali',
                    'genero': 'Masculino',
                    'tipo_representante': 'Suplente del Presidente',
                },
                "representante_aceptante": {
                    'nombre': 'MILANI ESTHER ESCORCIA SANTIAGO',
                    'tipo_identificacion': 'Cédula de Ciudadanía',
                    'numero_identificacion': '32.706.233',
                    'ciudad_expedicion_identificacion': 'Barranquilla',
                    'ciudad_residencia': 'Barranquilla',
                    'genero': 'Femenino',
                    'tipo_representante': 'Representante Legal'
                },
                "banco": {
                    'nombre': 'Banco unión s.a',
                    'nit': '860006797-9'
                },
                'aceptante': {
                    'nombre': 'CONSTRUCTORA JIMENEZ S.A',
                    'nit': '891.702.877-8',
                    'ciudad_ubicacion': 'Santa Marta',
                    'escritura': 'Escritura Pública Numero 300 de fecha 25 de febrero de 1986',
                    'nombre_notaria': 'Notaria Primera',
                    'ciudad_ubicacion_notaria': 'Santa Marta',
                    'ciudad_ubicacion_camara_comercio': 'Santa Marta'
                },
                'compraventa': {
                    'cantidad_compraventa': 190236667,
                    'cantidad_restante': 131444452,
                    'cuota_inicial': 58792215,
                    'fecha_compraventa': '03/08/2023'
                },
                'organo_autorizador': {
                    'ciudad_ubicacion_camara_comercio': 'Santa Marta',
                    'numero_acta': '00002365 del Libro IX',
                    'fecha_acta': '16/06/2006'
                }
            }
        controller = DocumentosController(event, None)
        response = controller.create_promesa_compraventa()

        self.assertEqual(response['statusCode'], 201)
        self.assertIsNotNone(response['body'])
