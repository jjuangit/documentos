from flask import Flask, request
from pydantic import BaseModel

from controllers.config import config
from models.apoderado import Apoderado
from models.apoderado_banco import ApoderadoBanco
from models.poderdantes import Poderdante
from models.representante_banco import RepresentanteBanco
from models.inmueble import InmueblePrincipal
from models.parqueaderos import Parqueadero
from models.depositos import Deposito
from models.banco import Banco
from models.prestamo import Prestamo
from models.minuta import DocumentoMinuta
from utils.strip_spaces import strip_dict_or_list
from utils.exceptions import GeneracionDeMinutaError

app_flask = Flask(__name__)


class MinutaBM(BaseModel):
    json_apoderado: dict
    json_poderdantes: list
    json_banco: dict
    json_inmueble: dict
    json_parqueaderos: list
    json_depositos: list
    json_apoderado_banco: dict
    json_representante_banco: dict


@app_flask.route('/minuta/create/flask', methods=['POST'])
def create_minuta_html():
    try:
        request_data = request.get_json()
        request_data = strip_dict_or_list(request_data)
        json_apoderado = request_data['apoderado']
        json_poderdantes = request_data['poderdantes']
        json_inmueble = request_data['inmueble']
        json_parqueaderos = request_data['parqueaderos']
        json_depositos = request_data['depositos']
        json_apoderado_banco = request_data['apoderado_banco']
        json_representante_banco = request_data['representante_banco']
        json_banco = request_data['banco']
        json_prestamo = request_data['prestamo']

        apoderado = Apoderado(**json_apoderado)
        poderdantes = [Poderdante(**poderdante)
                       for poderdante in json_poderdantes]
        inmueble = InmueblePrincipal(**json_inmueble)
        depositos = [Deposito(**deposito)
                     for deposito in json_depositos]
        parqueaderos = [Parqueadero(**parqueadero)
                        for parqueadero in json_parqueaderos]
        apoderado_banco = ApoderadoBanco(
            **json_apoderado_banco)
        representante_banco = RepresentanteBanco(
            **json_representante_banco)
        banco = Banco(**json_banco)
        prestamo = Prestamo(**json_prestamo)
        minuta = DocumentoMinuta(apoderado, poderdantes, inmueble, depositos,
                                 parqueaderos, apoderado_banco, representante_banco, 
                                 banco, prestamo)
        minuta.generate_html()
        print(minuta.html)
        return minuta.html
    except Exception as error:
        print(f'Error al crear la minuta: {error}')
        raise GeneracionDeMinutaError(
            'No se pudo generar el html de la minuta') from error


app_flask.config.from_object(config['development'])
app_flask.run()
