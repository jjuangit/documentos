import json

from catalogs.catalogos import (aceptantes, apoderados_banco, bancos,
                                representantes_banco)
from models.aceptante import Aceptante
from models.apoderado import ApoderadoHipoteca, ApoderadoPromesaCompraventa, ApoderadoPoder
from models.apoderado_banco import ApoderadoBanco, ApoderadoBancoPromesaCompraventa, ApoderadoBancoCompraventaLeasing
from models.banco import Banco, BancoPoder, BancoPromesaCompraventa, BancoCompraventaLeasing
from models.compraventa import Compraventa, CompraventaLeasing
from models.declaraciones import Declaraciones
from models.depositos import Deposito, DepositoPromesaCompraventa, DepositoPoder, DepositoCompraventaLeasing
from models.inmueble import Inmueble, InmueblePoder, InmueblePromesaCompraventa, InmuebleCompraventaLeasing
from models.minuta_hipoteca import DocumentoHipoteca
from models.organo_autorizador import OrganoAutorizador
from models.pareja_poderdante import ParejaPoderdante
from models.parqueaderos import Parqueadero, ParqueaderoPromesaCompraventa, ParqueaderoPoder, ParqueaderoCompraventaLeasing
from models.poder import DocumentoPoder
from models.poderdantes import Poderdante, PoderdantePromesaCompraventa, PoderdantePoder, PoderdanteCompraventaLeasing
from models.prestamo import Prestamo
from models.promesa_compraventa import DocumentoPromesaCompraventa
from models.compraventa_leasing import DocumentoCompraventaLeasing
from models.representante_aceptante import RepresentanteAceptante
from models.representante_banco import RepresentanteBanco, RepresentanteBancoPromesaCompraventa, RepresentanteBancoCompraventaLeasing
from models.regimen_propiedad import RegimenPropiedad
from models.conjunto_residencial import ConjuntoResidencial
from utils.controller import LambdaController, try_catch
from utils.strip_spaces import strip_dict_or_list
from utils.cleaner import Cleaner

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
        regimen_data = strip_dict_or_list(event.get("regimen"))

        apoderado_data['numero_identificacion'] = Cleaner.delete_dot(
            apoderado_data['numero_identificacion'])

        for poderdante_data in poderdantes_data:
            poderdante_data['numero_identificacion'] = Cleaner.delete_dot(
                poderdante_data['numero_identificacion'])

        for ficha_catastral in inmueble_data['numero_ficha_catastral']:
            ficha_catastral['ficha'] = Cleaner.delete_hypen(
                ficha_catastral['ficha'])

        for parqueadero_data in parqueaderos_data:
            parqueadero_data['numero_ficha_catastral'] = Cleaner.delete_hypen(
                parqueadero_data['numero_ficha_catastral'])

        for deposito_data in depositos_data:
            deposito_data['numero_ficha_catastral'] = Cleaner.delete_hypen(
                deposito_data['numero_ficha_catastral'])

        if apoderado_data is None:
            apoderado = None
        else:
            apoderado = ApoderadoHipoteca(**apoderado_data)
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
        regimen = RegimenPropiedad(**regimen_data)

        hipoteca = DocumentoHipoteca(
            apoderado,
            poderdantes,
            inmueble,
            depositos,
            parqueaderos,
            apoderado_banco,
            representante_banco,
            banco,
            prestamo,
            regimen
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
        '''Crea el documento de la minuta de Cesión del Contrato de Promesa Compraventa'''
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
        poderdantes = [PoderdantePromesaCompraventa(**poderdante)
                       for poderdante in poderdantes_data]
        inmueble = InmueblePromesaCompraventa(**inmueble_data)
        depositos = [DepositoPromesaCompraventa(**deposito)
                     for deposito in depositos_data]
        parqueaderos = [ParqueaderoPromesaCompraventa(**parqueadero)
                        for parqueadero in parqueaderos_data]
        for bank_apoderado in apoderados_banco:
            if bank_apoderado['nombre'] == apoderado_banco_data['nombre']:
                apoderado_banco = ApoderadoBancoPromesaCompraventa(
                    **bank_apoderado)
                break
        else:
            apoderado_banco = ApoderadoBancoPromesaCompraventa(
                **apoderado_banco_data)
        for representante in representantes_banco:
            if representante['nombre'] == representante_banco_data['nombre']:
                representante_banco = RepresentanteBancoPromesaCompraventa(
                    **representante)
                break
        else:
            representante_banco = RepresentanteBancoPromesaCompraventa(
                **representante_banco_data)

        if representante_aceptante_data is None:
            representante_aceptante = None
        else:
            representante_aceptante = RepresentanteAceptante(
                **representante_aceptante_data)

        for bank in bancos:
            if bank['nombre'] == banco_data['nombre']:
                banco = BancoPromesaCompraventa(**bank)
                break
        else:
            banco = BancoPromesaCompraventa(**banco_data)

        if aceptante_data is None:
            aceptante = None
        else:
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
        print(promesa_compraventa.html)
        json.dumps({
            "statusCode": 201,
            "body": {"html": promesa_compraventa.html}
        }, ensure_ascii=False)
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(promesa_compraventa.generate_html())
        return self.response

    @try_catch
    def create_compraventa_leasing(self):
        '''Crea el documento de Compraventa Leasing'''
        event = self.body

        poderdantes_data = strip_dict_or_list(event.get('poderdantes'))
        inmueble_data = strip_dict_or_list(event.get('inmueble'))
        parqueaderos_data = strip_dict_or_list(event.get('parqueaderos'))
        depositos_data = strip_dict_or_list(event.get('depositos'))
        apoderado_banco_data = strip_dict_or_list(event.get('apoderado_banco'))
        representante_banco_data = strip_dict_or_list(
            event.get('representante_banco'))
        banco_data = strip_dict_or_list(event.get('banco'))
        compraventa_data = strip_dict_or_list(event.get('compraventa'))
        conjunto_residencial_data = strip_dict_or_list(event.get('conjunto_residencial'))

        poderdantes = [PoderdanteCompraventaLeasing(**poderdante)
                       for poderdante in poderdantes_data]
        inmueble = InmuebleCompraventaLeasing(**inmueble_data)
        if conjunto_residencial_data is None:
            conjunto_residencial = None
        else:
            conjunto_residencial = ConjuntoResidencial(**conjunto_residencial_data)
        depositos = [DepositoCompraventaLeasing(**deposito)
                     for deposito in depositos_data]
        parqueaderos = [ParqueaderoCompraventaLeasing(**parqueadero)
                        for parqueadero in parqueaderos_data]
        for bank_apoderado in apoderados_banco:
            if bank_apoderado['nombre'] == apoderado_banco_data['nombre']:
                apoderado_banco = ApoderadoBancoCompraventaLeasing(
                    **bank_apoderado)
                break
        else:
            apoderado_banco = ApoderadoBancoCompraventaLeasing(
                **apoderado_banco_data)
        for representante in representantes_banco:
            if representante['nombre'] == representante_banco_data['nombre']:
                representante_banco = RepresentanteBancoCompraventaLeasing(
                    **representante)
                break
        else:
            representante_banco = RepresentanteBancoCompraventaLeasing(
                **representante_banco_data)

        for bank in bancos:
            if bank['nombre'] == banco_data['nombre']:
                banco = BancoCompraventaLeasing(**bank)
                break
        else:
            banco = BancoCompraventaLeasing(**banco_data)
        compraventa = CompraventaLeasing(**compraventa_data)
           
        compraventa_leasing = DocumentoCompraventaLeasing(poderdantes, inmueble,
                                                          conjunto_residencial, parqueaderos,
                                                          depositos, apoderado_banco,
                                                          representante_banco,
                                                          banco, compraventa)
        compraventa_leasing.generate_html()
        print(compraventa_leasing.html)
        json.dumps({
            "statusCode": 201,
            "body": {"html": compraventa_leasing.html}
        }, ensure_ascii=False)
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(compraventa_leasing.generate_html())
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

        apoderado = ApoderadoPoder(**apoderado_data)
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


def create_compraventa_leasing(event, context):
    controller = DocumentosController(event, context)
    response = controller.create_compraventa_leasing()
    return response
