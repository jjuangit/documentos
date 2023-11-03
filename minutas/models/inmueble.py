from typing import Optional, Text


class InmueblePrincipal:
    nombre: Optional[Text]
    numero: Optional[Text]
    direccion: Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str
    ):
        self.nombre = nombre
        self.numero = numero
        self.direccion = direccion
