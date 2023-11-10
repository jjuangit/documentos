from typing import Optional, Text


class Parqueadero:
    nombre: Optional[Text]
    numero: Optional[Text]
    direccion = Optional[Text]
    linderos_especiales: Optional[Text]
    matricula = Optional[Text]
    tipo_ficha_catastral = Optional[Text]
    numero_ficha_catastral = Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        linderos_especiales: str,
        matricula: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str
    ):
        self.nombre = nombre
        self.numero = numero
        self.direccion = direccion
        self.linderos_especiales = linderos_especiales
        self.matricula = matricula
        self.tipo_ficha_catastral = tipo_ficha_catastral
        self.numero_ficha_catastral = numero_ficha_catastral
