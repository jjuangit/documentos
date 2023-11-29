from typing import Optional, Text


class Parqueadero:
    nombre: Optional[Text]
    numero: Optional[Text]
    direccion = Optional[Text]
    matricula = Optional[Text]
    tipo_ficha_catastral = Optional[Text]
    numero_ficha_catastral = Optional[Text]
    linderos_especiales: Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        matricula: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
        linderos_especiales: str,
    ):
        self.nombre = nombre
        self.numero = numero
        self.direccion = direccion
        self.matricula = matricula
        self.tipo_ficha_catastral = tipo_ficha_catastral
        self.numero_ficha_catastral = numero_ficha_catastral
        self.linderos_especiales = linderos_especiales


class ParqueaderoPromesaCompraventa(Parqueadero):
    nueva_propiedad: Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        matricula: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
    ):
        super().__init__(
            nombre,
            numero,
            direccion,
            matricula,
            tipo_ficha_catastral,
            numero_ficha_catastral,
            linderos_especiales=None
        )