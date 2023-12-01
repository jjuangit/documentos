import json
from utils.controller import LambdaController
from utils.strip_spaces import strip_dict_or_list
from utils.controller import try_catch
from models.apoderado import Apoderado
from models.apoderado import ApoderadoPromesaCompraventa
from models.poderdantes import Poderdante
from models.inmueble import Inmueble
from models.inmueble import InmueblePromesaCompraventa
from models.depositos import Deposito
from models.depositos import DepositoPromesaCompraventa
from models.parqueaderos import Parqueadero
from models.parqueaderos import ParqueaderoPromesaCompraventa
from models.apoderado_banco import ApoderadoBanco
from models.representante_banco import RepresentanteBanco
from models.representante_aceptante import RepresentanteAceptante
from models.banco import Banco
from models.prestamo import Prestamo
from models.compraventa import Compraventa
from models.aceptante import Aceptante
from models.minuta_hipoteca import DocumentoHipoteca
from models.promesa_compraventa import DocumentoPromesaCompraventa
from models.organo_autorizador import OrganoAutorizador
from catalogs.catalogos import apoderados_banco
from catalogs.catalogos import representantes_banco
from catalogs.catalogos import bancos
from catalogs.catalogos import aceptantes


class DocumentosController(LambdaController):

    @try_catch
    def create_hipoteca(self):
        '''Crea el documento de la minuta de hipoteca'''
        event = self.body

        apoderado_data = strip_dict_or_list(event.get("apoderado"))
        poderdantes_data = strip_dict_or_list(event.get("poderdantes"))
        inmueble_data = strip_dict_or_list(event.get("inmueble"))
        parqueaderos_data = strip_dict_or_list(event.get("parqueaderos"))
        depositos_data = strip_dict_or_list(event.get("depositos"))
        apoderado_banco_data = strip_dict_or_list(event.get("apoderado_banco"))
        representante_banco_data = strip_dict_or_list(
            event.get("representante_banco"))
        banco_data = strip_dict_or_list(event.get("banco"))
        prestamo_data = strip_dict_or_list(event.get("prestamo"))

        if apoderado_data is None:
            apoderado = None
        else:
            apoderado = Apoderado(**apoderado_data)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in poderdantes_data]
        inmueble = Inmueble(**inmueble_data)
        depositos = [Deposito(**deposito)
                     for deposito in depositos_data]
        parqueaderos = [Parqueadero(**parqueadero)
                        for parqueadero in parqueaderos_data]
        for bank_apoderado in apoderados_banco:
            if bank_apoderado['nombre'] == apoderado_banco_data['nombre']:
                apoderado_banco = ApoderadoBanco(**bank_apoderado)
                break
        else:
            apoderado_banco = ApoderadoBanco(
                **apoderado_banco_data)
        for representante in representantes_banco:
            if representante['nombre'] == representante_banco_data['nombre']:
                representante_banco = RepresentanteBanco(**representante)
                break
        else:
            representante_banco = RepresentanteBanco(
                **representante_banco_data)

        for bank in bancos:
            if bank['nombre'] == banco_data['nombre']:
                banco = Banco(**bank)
                break
        else:
            banco = Banco(**banco_data)
        prestamo = Prestamo(**prestamo_data)

        hipoteca = DocumentoHipoteca(
            apoderado,
            poderdantes,
            inmueble,
            depositos,
            parqueaderos,
            apoderado_banco,
            representante_banco,
            banco,
            prestamo
        )

        hipoteca.generate_html()
        print(json.dumps({
            "statusCode": 201,
            "body": {"html": hipoteca.html}
        }, ensure_ascii=False))
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(hipoteca.generate_html())
        return self.response

    @try_catch
    def create_promesa_compraventa(self):
        '''Crea el documento de la minuta de Cesión del contrato de Promesa Compraventa'''
        event = self.body

        apoderado_data = strip_dict_or_list(event.get("apoderado"))
        poderdantes_data = strip_dict_or_list(event.get("poderdantes"))
        inmueble_data = strip_dict_or_list(event.get("inmueble"))
        parqueaderos_data = strip_dict_or_list(event.get("parqueaderos"))
        depositos_data = strip_dict_or_list(event.get("depositos"))
        apoderado_banco_data = strip_dict_or_list(event.get("apoderado_banco"))
        representante_banco_data = strip_dict_or_list(
            event.get("representante_banco"))
        representante_aceptante_data = strip_dict_or_list(
            event.get("representante_aceptante"))
        banco_data = strip_dict_or_list(event.get("banco"))
        aceptante_data = strip_dict_or_list(event.get("aceptante"))
        compraventa_data = strip_dict_or_list(event.get("compraventa"))
        organo_autorizador_data = strip_dict_or_list(
            event.get("organo_autorizador"))

        apoderado = ApoderadoPromesaCompraventa(**apoderado_data)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in poderdantes_data]
        inmueble = InmueblePromesaCompraventa(**inmueble_data)
        depositos = [DepositoPromesaCompraventa(**deposito)
                     for deposito in depositos_data]
        parqueaderos = [ParqueaderoPromesaCompraventa(**parqueadero)
                        for parqueadero in parqueaderos_data]
        for banck_apoderado in apoderados_banco:
            if banck_apoderado['nombre'] == apoderado_banco_data['nombre']:
                apoderado_banco = ApoderadoBanco(**banck_apoderado)
                break
        else:
            apoderado_banco = ApoderadoBanco(
                **apoderado_banco_data)
        for representante in representantes_banco:
            if representante['nombre'] == representante_banco_data['nombre']:
                representante_banco = RepresentanteBanco(**representante)
                break
        else:
            representante_banco = RepresentanteBanco(
                **representante_banco_data)
        representante_aceptante = RepresentanteAceptante(
            **representante_aceptante_data)

        for bank in bancos:
            if bank['nombre'] == banco_data['nombre']:
                banco = Banco(**bank)
                break
        else:
            banco = Banco(**banco_data)
        for builder in aceptantes:
            if builder['nombre'] == aceptante_data['nombre']:
                aceptante = Aceptante(**builder)
                break
        else:
            aceptante = Aceptante(**aceptante_data)
        compraventa = Compraventa(**compraventa_data)
        organo_autorizador = OrganoAutorizador(
            **organo_autorizador_data)

        promesa_compraventa = DocumentoPromesaCompraventa(
            apoderado,
            poderdantes,
            inmueble,
            parqueaderos,
            depositos,
            apoderado_banco,
            representante_banco,
            representante_aceptante,
            banco,
            aceptante,
            compraventa,
            organo_autorizador
        )

        promesa_compraventa.generate_html()
        print(json.dumps({
            "statusCode": 201,
            "body": {"html": promesa_compraventa.html}
        }, ensure_ascii=False))
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(promesa_compraventa.generate_html())
        return self.response


def create_hipoteca(event, context):
    controller = DocumentosController(event, context)
    response = controller.create_hipoteca()
    return response


def create_promesa_compraventa(event, context):
    controller = DocumentosController(event, context)
    response = controller.create_promesa_compraventa()
    return response
