from typing import Optional, Text

class Banco:
    nombre: Optional[Text]
    nit: Optional[Text]
    prestamo_banco_a_hipotecante_en_numero: Optional[Text]
    cantidad_dada_a_constructora_en_numero: Optional[Text]
    gastos_de_gestion_en_numero: Optional[Text]

    def __init__(
        self,
        nombre: str,
        nit: str,
        prestamo_banco_a_hipotecante_en_numero: int,
        cantidad_dada_a_constructora_en_numero: int,
        gastos_de_gestion_en_numero: int
    ):
        self.nombre = nombre
        self.nit = nit
        self.prestamo_banco_a_hipotecante_en_numero = prestamo_banco_a_hipotecante_en_numero
        self.cantidad_dada_a_constructora_en_numero = cantidad_dada_a_constructora_en_numero
        self.gastos_de_gestion_en_numero = gastos_de_gestion_en_numero
