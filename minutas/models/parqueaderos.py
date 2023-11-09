from typing import Optional, Text


class Parqueadero:
    nombre: Optional[Text]
    numero: Optional[Text]
    linderos_especiales: Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        linderos_especiales: str
    ):
        self.nombre = nombre
        self.numero = numero
        self.linderos_especiales = linderos_especiales
