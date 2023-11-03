from typing import Optional
from typing import Text

class Apoderado:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    genero: Optional[Text]

    def __init__(self,
                 nombre: str,
                 tipo_identificacion: str,
                 numero_identificacion: str,
                 ciudad_expedicion_identificacion: str,
                 genero: str
                ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.genero = genero
