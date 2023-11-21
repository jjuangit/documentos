from typing import Optional
from typing import Text

class Compraventa:
    cantidad_compraventa: Optional[Text]
    cantidad_restante: Optional[Text]
    cuota_inicial: Optional[Text]

    def __init__(
        self,
        cantidad_compraventa: int,
        cantidad_restante: int,
        cuota_inicial: int
    ):
        self.cantidad_compraventa = cantidad_compraventa
        self.cantidad_restante = cantidad_restante
        self.cuota_inicial = cuota_inicial
