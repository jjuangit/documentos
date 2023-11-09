from typing import Optional
from typing import Text

class RepresentanteLegal:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    ciudad_residencia: Optional[Text]
    genero: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        genero: str
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.ciudad_residencia = ciudad_residencia
        self.genero = genero

    @property
    def identificado(self):
        if self.genero == 'Masculino':
            return 'identificado'
        elif self.genero == 'Femenino':
            return 'identificada'
        
    @property
    def vecino(self):
        if self.genero == 'Masculino':
            return 'vecino'
        elif self.genero == 'Femenino':
            return 'vecina'
        
    @property
    def doctor(self):
        if self.genero == 'Masculino':
            return 'el doctor'
        elif self.genero == 'Femenino':
            return 'la doctora'