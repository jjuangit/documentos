from typing import Optional, Text

class Escritura:
    nombre: Optional[Text]
    numero: Optional[Text]
    fecha: Optional[Text]
    
    def __init__(
                self,
                nombre: str,
                numero: str,
                fecha: str
                ):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha