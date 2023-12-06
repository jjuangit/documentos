import json

from catalogs.catalogos import (aceptantes, apoderados_banco, bancos,
                                representantes_banco)
from models.aceptante import Aceptante
from models.apoderado import Apoderado, ApoderadoPromesaCompraventa
from models.apoderado_banco import ApoderadoBanco
from models.banco import Banco, BancoPoder
from models.compraventa import Compraventa
from models.declaraciones import Declaraciones
from models.depositos import Deposito, DepositoPromesaCompraventa, DepositoPoder
from models.inmueble import Inmueble, InmueblePoder, InmueblePromesaCompraventa
from models.minuta_hipoteca import DocumentoHipoteca
from models.organo_autorizador import OrganoAutorizador
from models.pareja_poderdante import ParejaPoderdante
from models.parqueaderos import Parqueadero, ParqueaderoPromesaCompraventa, ParqueaderoPoder
from models.poder import DocumentoPoder
from models.poderdantes import Poderdante, PoderdantePoder
from models.prestamo import Prestamo
from models.promesa_compraventa import DocumentoPromesaCompraventa
from models.representante_aceptante import RepresentanteAceptante
from models.representante_banco import RepresentanteBanco
from utils.controller import LambdaController, try_catch
from utils.strip_spaces import strip_dict_or_list


class DocumentosController(LambdaController):
    '''Controladores de documentos'''
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
        html = hipoteca.html
        print(html)
        json.dumps({
            "statusCode": 201,
            "body": {"html": html}
        }, ensure_ascii=False)

        self.response["statusCode"] = 201
        self.response["body"] = json.dumps({"html": html})
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

    @try_catch
    def create_poder(self):
        '''Crea el documento del Poder'''
        event = self.body

        apoderado_data = strip_dict_or_list(event.get("apoderado"))
        poderdantes_data = strip_dict_or_list(event.get("poderdantes"))
        pareja_poderdante_data = strip_dict_or_list(
            event.get("pareja_poderdante"))
        parqueaderos_data = strip_dict_or_list(event.get("parqueaderos"))
        depositos_data = strip_dict_or_list(event.get("depositos"))
        inmueble_data = strip_dict_or_list(event.get("inmueble"))
        declaraciones_data = strip_dict_or_list(event.get("declaraciones"))
        banco_data = strip_dict_or_list(event.get("banco"))

        apoderado = Apoderado(**apoderado_data)
        poderdantes = [PoderdantePoder(**poderdante)
                       for poderdante in poderdantes_data]
        if pareja_poderdante_data is None:
            pareja_poderdante = None
        else:
            pareja_poderdante = ParejaPoderdante(**pareja_poderdante_data)
        parqueaderos = [ParqueaderoPoder(
            **parqueadero) for parqueadero in parqueaderos_data]
        depositos = [DepositoPoder(
            **deposito) for deposito in depositos_data]
        inmueble = InmueblePoder(**inmueble_data)
        declaraciones = Declaraciones(**declaraciones_data)
        banco = BancoPoder(**banco_data)
        poder = DocumentoPoder(
            poderdantes,
            pareja_poderdante,
            apoderado,
            inmueble,
            parqueaderos,
            declaraciones,
            banco,
            depositos
        )

        poder.generate_html()
        print(poder.html)
        json.dumps({
            "statusCode": 201,
            "body": {"html": poder.html}
        }, ensure_ascii=False)
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(poder.generate_html())
        return self.response


def create_hipoteca(event, context):
    controller = DocumentosController(event, context)
    response = controller.create_hipoteca()
    return response


def create_promesa_compraventa(event, context):
    controller = DocumentosController(event, context)
    response = controller.create_promesa_compraventa()
    return response


def create_poder(event, context):
    controller = DocumentosController(event, context)
    response = controller.create_poder()
    return response
