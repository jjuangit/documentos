from typing import Optional
from typing import Text

class Compraventa:
    cantidad_compraventa: Optional[Text]
    cantidad_restante: Optional[Text]
    cuota_inicial: Optional[Text]
    fecha_compraventa: Optional[Text]

    def __init__(
        self,
        cantidad_compraventa: int,
        cantidad_restante: int,
        cuota_inicial: int,
        fecha_compraventa: str
    ):
        self.cantidad_compraventa = cantidad_compraventa
        self.cantidad_restante = cantidad_restante
        self.cuota_inicial = cuota_inicial
        self.fecha_compraventa = fecha_compraventa

class CompraventaLeasing:
    cantidad_compraventa: Optional[Text]
    cantidad_restante: Optional[Text]
    cuota_inicial: Optional[Text]
    fecha_compraventa: Optional[Text]

    def __init__(
        self,
        cantidad_compraventa: int,
        cantidad_restante: int,
        cuota_inicial: int,
        fecha_compraventa: str
    ):
        self.cantidad_compraventa = cantidad_compraventa
        self.cantidad_restante = cantidad_restante
        self.cuota_inicial = cuota_inicial
        self.fecha_compraventa = fecha_compraventa
