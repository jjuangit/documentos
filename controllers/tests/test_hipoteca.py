from unittest import TestCase
from controllers.documentos import DocumentosController

class TestHipoteca(TestCase):

    def test_create_documento_hipoteca(self):
        '''Crear documento Hipoteca'''
        event = {
                    'apoderado': {
                        'nombre': 'LUZ EDILMA BOLIVAR VALENCIA',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '24.931.325',
                        'ciudad_expedicion_identificacion': 'PEREIRA',
                        'genero': 'Femenino'
                    },
                    'poderdantes': [{
                        'nombre': 'FERNEY VALENCIA BOLIVAR',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '10.132.073',
                        'ciudad_expedicion_identificacion': 'PEREIRA',
                        'domicilio': 'MALAKOFF - FRANCIA',
                        'estado_civil': 'Casado con sociedad conyugal vigente',
                        'genero': 'Masculino'
                    }],
                    'inmueble': {
                        'nombre': 'APARTAMENTO',
                        'numero': '106 ESQUINERO TIPO 1 TORRE 4,',
                        'direccion': 'CONJUNTO CERRADO MAJESTIC II P.H., TV 35 D G # 2 - 74, SECTOR FRAILES JAPON',
                        'ciudad_y_o_departamento': 'DOSQUEBRADAS RISARALDA',
                        'matricula': '294-103416',
                        'municipio_de_registro_orip': 'DOSQUEBRADAS',
                        'tipo_ficha_catastral': 'Individual',
                        'numero_ficha_catastral': [
                            {'ficha': '0020-000-000-118-07000000000'}
                        ],
                        'numero_chip': '',
                        'linderos_especiales': '"APARTAMENTO 106 ESQUINERO (TIPO 1) TORRE 4: ÁREA PRIVADA APARTAMENTO: 52.84 M2. ÁREA MUROS Y BUITRONES COMUNES: 6.50 M2. ÁREA CONSTRUIDA APARTAMENTO: 59.34 M2. Ubicado en el Piso 1, a nivel de +0.00 m, destinado a vivienda con un área construida de 59.34 M2 aproximadamente, un área privada de 52.84 M2 Aproximadamente y un área común de muros y buitrones de 6.50 M2 aproximadamente, con entrada común Portería al CONJUNTO CERRADO “MAJESTIC II” PROPIEDAD HORIZONTAL, UBICADO en la TV 35 No. DG2-74, SECTOR VIA FRAILES JAPÓN, EN EL ÁREA URBANA DEL MUNICIPIO DE DOSQUEBRADAS, DEPARTAMENTO DE RISARALDA, cuyos linderos y dimensiones referenciados a los Planos 1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12 y 12/12, son los siguientes: ### Partiendo del punto 1, ubicado al lado izquierdo del acceso a este apartamento hasta el punto 2 en dirección Norte en longitud de 6.83 mts, con muro común, que lo separa del apartamento 105 de la Torre 4, del punto 2 en dirección Oriente al punto 3 en Longitud de 2.67 mts, con baranda de balcón, que lo separa del área común zona verde 27, del punto 3 en dirección Sur al punto 4 en longitud de 1.23 mts, con muro común, que lo separa del área común zona verde 27, del punto 4 en dirección Oriente al punto 5 en longitud de 1.15 mts, con muro común, que lo separa del área común zona verde 27, del punto 5 en dirección Sur al punto 6 en longitud de 0.60 mts, con muro común, que lo separa del área común zona verde 27, del punto 6 en dirección Oriente al punto 7 en longitud de 3.25 mts, con muro, ventana, muro, ventana, muro común respectivamente, que lo separa del área común zona verde 27, del punto 7 en dirección Sur al punto 8 en longitud de 0.75 mts, con muro común, que lo separa del área común zona verde 27, del punto 8 en dirección Oriente al punto 9 en longitud de 2.65 mts, con muro, ventana, muro común respectivamente, que lo separa del área común zona verde 27, del punto 9 en dirección Sur al punto 10 en longitud de 4.72 mts, con muro, ventana, muro, ventana de ventilación baño, muro común respectivamente, que lo separa del área común zona verde 27, del punto 10 en dirección Occidente al punto 11 en longitud de 1.00 mts, con muro común, que lo separa del Buitrón común, queda al apartamento 107 de la Torre 4, del punto 11 en dirección Sur al punto 12 en longitud de 0.23 mts, con muro común, que lo separa del Buitrón común, del punto 12 en dirección Occidente al punto 13 en longitud de 1.50 mts, con muro común, que lo separa del apartamento 107 de la Torre 4, del punto 13 en dirección Norte al punto 14 en longitud de 0.80 mts, con muro común y rejilla de ventilación baño, que lo separa del área común de uso exclusivo 107 del apartamento 107 de la Torre 4, del punto 14 en dirección Occidente al punto 15 en longitud de 4.00 mts, con muro, rejilla de ventilación baño, muro, rejilla de ventilación zona de ropas común respectivamente, que lo separa del área común de uso exclusivo 107 del apartamento 107 de la Torre 4, del punto 15 en dirección Sur al punto 16 en longitud de 0.77 mts, con muro común y rejilla de ventilación cocina, que lo separa del área común de uso exclusivo 107 del apartamento 107 de la Torre 4, del punto 16 en dirección Occidente al punto 17 en longitud de 2.10 mts, con muro común, que lo separa del apartamento 107 de la Torre 4, del punto 17 en dirección Norte al punto 18 en longitud de 0.68 mts, con muro común, que lo separa del área común (punto fijo) escaleras, circulación, ascensores, shut de basuras, medidores piso 1, del punto 18 en dirección Occidente al punto 1 de partida, en longitud de 1.15 mts, con muro común y puerta de acceso, que lo separa del área común (punto fijo) escaleras, circulación, asensores, shut de basuras, medidores piso 1. Por el CENIT: En toda su extensión con losa común que lo separa del apartamento 206 de la Torre 4. Por el NADIR: En toda su extensión con losa Común que lo separa del suelo. Este apartamento consta de: Sala - comedor, Alcoba Principal con baño y ducha, Dos alcobas auxiliares, cocina, zona de ropas, baño con ducha y un balcón. Todos los muros y buitrones de este apartamento son comunes y estructurales, por lo tanto, no se pueden alterar ni eliminar."'
                    },
                    'parqueaderos': [

                    ],
                    'depositos': [

                    ],
                    'apoderado_banco': {
                        'nombre': 'Carlos Alberto Agudelo Zapata',
                        'tipo_identificacion': '',
                        'numero_identificacion': '',
                        'ciudad_expedicion_identificacion': '',
                        'ciudad_residencia': '',
                        'genero': '',
                        'tipo_apoderado': '',
                        'tipo_poder': '',
                        'escritura': ''
                    },
                    'representante_banco': {
                        'nombre': 'Juan Pablo Cruz López',
                        'tipo_identificacion': '',
                        'numero_identificacion': '',
                        'ciudad_expedicion_identificacion': '',
                        'ciudad_residencia': '',
                        'genero': '',
                        'tipo_representante': ''
                    },
                    'banco': {
                        'nombre': 'banco unión s.a',
                        'nit': '860.006.797-9'
                    },
                    'prestamo': {
                        'cantidad_banco_a_hipotecante': 98150000,
                        'cantidad_dada_a_aceptante': 94830918,
                        'gastos_de_gestion': 3319082
                    }
                }
        controller = DocumentosController(event, None)
        response = controller.create_hipoteca()

        self.assertEqual(response['statusCode'], 201)
        self.assertIsNotNone(response['body'])
