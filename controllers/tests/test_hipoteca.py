from unittest import TestCase
from controllers.hipoteca import DocumentosController

class TestHipoteca(TestCase):

    def test_create_documento_hipoteca(self):
        event = {
                    "apoderado": {
                        "nombre": "LIGIA MILENA ROMERO PARRA",
                        "tipo_identificacion": "Cédula de ciudadanía",
                        "numero_identificacion": "52.823.286",
                        "ciudad_expedicion_identificacion": "Bogotá D.C.",
                        "genero": "Femenino"
                    },
                    "poderdantes": [{
                        "nombre": "CAMILO ROMERO PARRA",
                        "tipo_identificacion": "Cédula de ciudadanía",
                        "numero_identificacion": "1.110.446.328",
                        "ciudad_expedicion_identificacion": "Ibague",
                        "domicilio": "131 SPINDLE RD HICKSVILLE- NEW YORK",
                        "estado_civil": "Casado con sociedad conyugal vigente",
                        "genero": "Masculino"
                    }],
                    "inmueble": {
                        "nombre": "APARTAMENTO",
                        "numero": "208 TORRE 1",
                        "direccion": "CONJUNTO BULEVAR DEL PORTAL PH VIS CARRERA 10 #59-99 SUR",
                        "ciudad_y_o_departamento": "EN PORVENIR BOGOTÁ D.C.",
                        "matricula": "50S-40803060",
                        "municipio_de_registro_orip": "BOGOTÁ ZONA SUR",
                        "tipo_ficha_catastral": "Mayor Extensión",
                        "numero_ficha_catastral": [
                            {"ficha": "2589994300000000"}
                        ],
                        "linderos_especiales": "Apartamento 208, LOCALIZACION: Esté localizado en el piso 2 de Ia torre 7 del conjunto residencial bulervar el portal accesos: acceso vehicular por la carrera 10 No. 59-89 Sur y acceso peatonal por la carrera 10 No, 59-99 Sur en la ciudad de Bogota D.C. DEPENDENGIAS: Sala-comedor cocina, ropas, proyeccién para futuro estar o estudio, dos (2) alcobas, un (1) baño, y proyección futuro baño (por parte del propietario). AREAS: Area construida de cincuenta metros cuadrados con ochenta y dos decimetros Cuadrados (50.82 M2). Area privada de cuarenta y cinco metros cuadrados con treinta y seis decimetros cuadrados (45.36 M2). La diferencia entre el área construida y el área privada es de cinco metros cuadrados con cuarenta y seis decimetros cuadrados (5.46 M2), que corresponden a: muros de fachada común, muros comunes, y ductos comunes, estos elementos y las placas estructurales, ya sean interiores o medianeros con otras unidades privadas, No se pueden demoler ni modificar, dado su carácter estructural y común. ALTURA: La altura libre aproximada es de dos metros con treinta centímetros (2.30 m). LINDEROS: Se encuentra comprendido dentro de los siguientes linderos: Entre los puntos 1 y 2: Línea quebrada, en dimensiones de cuatro metros con sesenta centímetros (4.60 m.), tres metros con cuarenta centímetros (3.40 m.), quince centímetros (0.15 m.), dos metros con diez centímetros (2.10 m.), y dos metros con cuarenta y un centímetros (2.41 m.), muro común al medio, colindante con el partamento 207; ventana y muro de fachada común, colindantes con vacío sobre zona común exterior; y muro común al interior del apartamento. Entre los puntos 2 y 3: Línea quebrada, en dimensiones de dos metros con noventa centímetros (2.90 m.), dos metros con cincuenta y seis centímetros (2.56 m.), quince centímetros (0.15 m.), dos metros con cincuenta y seis centímetros (2.56 m.), un metro con sesenta y cuatro centímetros (1.64 m.), sesenta y nueve centímetros (0.69 m.), veintiún centímetros (0.21 m.), tres centímetros (0.03 m.), y dos metros con noventa y nueve centímetros (2.99 m.), muros, ventanas y baranda de fachada común, colindantes con vacío sobre zona común exterior y con alero común; y muro común al interior del apartamento. Entre los puntos 3 y 4: Línea recta, en dimensión de cuatro metros con cincuenta centímetros (4.50 m.), muro de fachada común, colindante con alero común y con vacío sobre zona común exterior; y muro común al medio, colindante con el apartamento 201. Entre los puntos 4 y 1: Línea quebrada, (entre los cuales se halla el acceso al apartamento), en dimensiones de tres metros con setenta centímetros (3.70m.), un metro con setenta centímetros (1.70 m.), veinte centímetros (0.20 m.), noventa y nueve centímetros (0.99 m.), un metro con veinte centímetros (1.20 m.), noventa y nueve centímetros (0.99 m.), quince centímetros (0.15 m.), dos metros con veinticuatro centímetros (2.24 m.), un metro con veinte centímetros (1.20 m), dos metros con nueve centímetros (2.09 m.), cuarenta y nueve centímetros (0.49 m.), quince centímetros (0.15 m.), sesenta y cuatro centímetros (0.64 m.), tres metros con sesenta y nueve centímetros (3.69 m.), y dos metros con sesenta centímetros (2.60 m.), puerta y muro comunes, colindantes con zona común de circulación peatonal; muro común, colindante con ducto técnico y ascensor; ventanas y muros comunes, colindantes con vacío sobre ducto de ventilación; muros comunes al interior del apartamento; y muro común, colindante con alero común. CENIT: Placa estructural común al medio, colindante con el piso 3. NADIR: Placa estructural común al medio, colindante con el piso 1."
                    },
                    "parqueaderos": [],
                    "depositos": [],
                    "apoderado_banco": {
                        "nombre": "Germán Leonardo Kalil Méndez",
                        "tipo_identificacion": "",
                        "numero_identificacion": "",
                        "ciudad_expedicion_identificacion": "",
                        "ciudad_residencia": "",
                        "genero": "",
                        "tipo_apoderado": "",
                        "tipo_poder": "",
                        "escritura": ""
                    },
                    "representante_banco": {
                        "nombre": "Juan Pablo Cruz López",
                        "tipo_identificacion": "",
                        "numero_identificacion": "",
                        "ciudad_expedicion_identificacion": "",
                        "ciudad_residencia": "",
                        "genero": "",
                        "tipo_representante": ""
                    },
                    "banco": {
                        "nombre": "banco unión s.a",
                        "nit": "860.006.797-9"
                    },
                    "prestamo": {
                        "cantidad_banco_a_hipotecante": 93150000,
                        "cantidad_dada_a_aceptante": 90000000,
                        "gastos_de_gestion": 3150000
                    }
                }
        controller = DocumentosController(event, None)
        response = controller.create_hipoteca()

        self.assertEqual(response['statusCode'], 201)
        self.assertIsNotNone(response['body'])
