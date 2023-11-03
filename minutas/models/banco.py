from typing import Optional, Text

class Banco:
    nombre: Optional[Text]
    nit: Optional[Text]
    precio_hipoteca_inmueble: Optional[Text]

    def __init__(self, nombre: str, nit, precio_hipoteca_inmueble):
        self.nombre = nombre
        self.nit = nit
        self.precio_hipoteca_inmueble = precio_hipoteca_inmueble