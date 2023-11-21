from typing import Optional, Text


class Constructora:
    nombre: Optional[Text]
    nit: Optional[Text]
    ciudad_ubicacion: Optional[Text]

    def __init__(
        self,
        nombre: str,
        nit: str,
        ciudad_ubicacion: str
    ):
        self.nombre = nombre
        self.nit = nit
        self.ciudad_ubicacion = ciudad_ubicacion
