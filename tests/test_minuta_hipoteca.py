from unittest import TestCase

from models.minuta_hipoteca import DocumentoHipoteca
from models.apoderado import ApoderadoHipoteca
from models.poderdantes import Poderdante
from models.inmueble import Inmueble
from models.depositos import Deposito
from models.parqueaderos import Parqueadero
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from models.banco import Banco
from models.prestamo import Prestamo
from models.regimen_propiedad import RegimenPropiedad
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from utils.strip_spaces import strip_dict_or_list

class TestMinutaHipoteca(TestCase):
    """Iniciar Test"""

    def test_init_minuta_hipoteca_success(self):
        """Funcion para imprimir el html de la minuta"""
        diccionario_apoderado= {
                        'nombre': 'CARLOS ALBERTO LOPEZ CEBALLOS',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '1.097.034.456',
                        'ciudad_expedicion_identificacion': 'Quimbaya',
                        'tipo_apoderado': 'General',
                        'fecha_autenticacion_poder': '',
                        'tipo_dependencia_autenticacion': '',
                        'nombre_dependencia': '',
                        'ciudad_dependencia': '',
                        'escritura': 'Escritura Pública No. 1217 del 23 de Agosto del 2023 Notaría Única De Quimbaya Quindío',
                        'genero': 'Masculino'
                    }
        diccionario_poderdantes = [
                    {
                        'nombre': 'JORGE LUIS RESTREPO CARDONA',
                        'tipo_identificacion': 'Cédula de Ciudadanía',
                        'numero_identificacion': '1.004.960.363',
                        'ciudad_expedicion_identificacion': 'Con Montereal',
                        'domicilio': 'SHEERBROOKE - QUEBEC',
                        'estado_civil': 'Soltero sin unión marital de hecho',
                        'genero': 'Masculino'
                    }
                    ]
        diccionario_inmueble = {
                        'nombre': 'APARTAMENTO ',
                        'numero': '903 TORRE 3 ETAPA 2',
                        'direccion': 'PARQUE RESIDENCIAL TACURUMBI P.H. CALLE 21 # 2 - 35',
                        'ciudad_y_o_departamento': 'EN QUIMBAYA QUINDÍO',
                        'matricula': '280-253059 ',
                        'municipio_de_registro_orip': 'Armenia',
                        'tipo_ficha_catastral': 'Mayor Extensión',
                        'numero_ficha_catastral': [
                            {'ficha': '0100000001340001000000000'},
                        ],
                        'numero_chip': '',
                        'linderos_especiales': '"APARTAMENTO 903: Ubicado en el Piso 9 de la torre 3 del Parque Residencia Tacurumbi, al que se accede por entrada común distinguida con la nomenclatura urbana Calle 21 No. 2-35 parque residencial Tacurumbi, del área urbana del municipio de Quimbaya, Departamento del Quindio, con un área privada Construida de 44.88 metros cuadrados, con un área común -muros- de 8.73 metros cuadrados, con un area construida de 53.61 metros cuadrados, con una altura libre de 2.30 metros; consta de una sala, comedor, cocina, zona de ropas, baño, habitación, hall, balcón, habitación con espacio para baño. Sus linderos exclusivos son: #### Del punto 1 al punto 2 en uns longitud de 6.00 metros aproximadamente, con muro común de por medio que lo separa del apartamento 904./ Del punto 2 al punto 3 en una longitud de 7.55 metros aproximadamente, con baranda, muro y ventana común de fachada de por medio que lo separa de vacio sobre zona común del parque residencial. Del punto 3 al punto 4 en una longitud de 6.78 metros aproximadamente con muro común de fachada de por medio que lo separa de vacío sobre zona común del parque residencial. Del punto 4 al punto 5 en una longitud de 1.45 metros aproximadamente, con muro común de por medio que separa del apartamento 902. Del punto: al punto 6 en una longitud de 0.93 metros aproximadamente, con muro comun de por medio que lo separa de zona común de la torre -buitrón-. Del punto 6 al punto 7 en una longitud de 2.40 metros aproximadamente con muro común de por medio que lo separa de zona común de la torre -buitrón-. De punto 7 al punto 8 en una longitud de 0.93 metros aproximadamente, con muro común de por medio que lo separa de zona común de la torre -buitrón-. Del punto 8 al punto en una longitud de 2.90 metros aproximadamente, con muro común de por medio que separa del apartmento 902. Del punto 9 al punto 10 en una longitud de 0.72 metros aproximadamente, con muro común de por medio que lo separa de zona común de circulación de la torre. Del punto 10 al punto 11 en una longitud de 0.15 metros aproximadamente, con muro común de por medio que lo separa de zona común de circulación de la torre. Del punto 11 al punto 1 en una longitud de 0.90 metro aproximadamente, con portón de acceso común de por medio que lo separa de ona común de circulación de la torre, y encierra. POR EL CENIT: Con placa d entrepiso común que lo separa del piso 10. POR EL NADIR: Con placa de entrepiso común que lo separes del piso 8."'
                    }
        diccionario_parqueaderos = [
                    ]
        diccionario_depositos = [
                    ]
        diccionario_apoderado_banco = {
                        'nombre': 'Angy Viviana Gallego',
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
                    'nit': ''
                }
        diccionario_prestamo = {
                        'cantidad_banco_a_hipotecante': 104516544,
                        'cantidad_dada_a_aceptante': 100982168,
                        'gastos_de_gestion': 3534376
                    }
        diccionario_regimen = {
                        'escritura': 'Escritura Pública No. 1566 Del 07 De Junio Del 2019 Notaría Tercera De Armenia y adicionado mediante la Escritura Pública No. 2031 Del 18 De Junio Del 2023 Notaría Tercera De Armenia.'
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
        diccionario_regimen = strip_dict_or_list(diccionario_regimen)

        if diccionario_apoderado is None:
            apoderado = None
        else:
            apoderado = ApoderadoHipoteca(**diccionario_apoderado)
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
        regimen = RegimenPropiedad(**diccionario_regimen)
        minuta_hipoteca = DocumentoHipoteca(apoderado, poderdantes, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco, 
                                 banco, prestamo, regimen
                                 )
        minuta_hipoteca.generate_html()
        print(minuta_hipoteca.html)

# command line for run this test:
# python -m unittest tests.test_minuta_hipoteca.TestMinutaHipoteca.test_init_minuta_hipoteca_success
