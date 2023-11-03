from typing import Optional, Text


class Deposito:
    nombre: Optional[Text]
    numero: Optional[Text]

    def __init__(self,
                 nombre: str,
                 numero: str,
                 ):
        self.nombre = nombre
        self.numero = numero
