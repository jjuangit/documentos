from typing import Optional, Text

class Banco:
    nombre: Optional[Text]
    nit: Optional[Text]

    def __init__(
        self,
        nombre: str,
        nit: str,
    ):
        self.nombre = nombre
        self.nit = nit

