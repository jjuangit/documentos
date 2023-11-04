from typing import Optional, Text


class InmueblePrincipal:
    nombre: Optional[Text]
    numero: Optional[Text]
    direccion: Optional[Text]
    matricula: Optional[Text]
    municipio_de_registro_orip: Optional[Text]
    tipo_ficha_catastral: Optional[Text]
    numero_ficha_catastral: Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        matricula: str,
        municipio_de_registro_orip: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str
    ):
        self.nombre = nombre
        self.numero = numero
        self.direccion = direccion
        self.matricula = matricula
        self.municipio_de_registro_orip = municipio_de_registro_orip
        self.tipo_ficha_catastral = tipo_ficha_catastral
        self.numero_ficha_catastral = numero_ficha_catastral
