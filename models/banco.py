from typing import Type, Text

class Banco:
    nombre: Type[Text]
    nit: Type[Text]

    def __init__(
        self,
        nombre: str,
        nit: str,
    ):
        self.nombre = nombre
        self.nit = nit

class BancoPromesaCompraventa(Banco):
    def __init__(
        self,
        nombre: str,
        nit: str
    ):
        super().__init__(
            nombre,
            nit
        )

class BancoPoder(Banco):
    def __init__(
        self,
        nombre: str,
    ):
        super().__init__(
            nombre,
            nit=None
        )

class BancoCompraventaLeasing(Banco):
    def __init__(
        self,
        nombre: str,
        nit: str
    ):
        super().__init__(
            nombre,
            nit
        )
