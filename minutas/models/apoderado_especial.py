from typing import Optional
from typing import Text


class ApoderadoEspecial:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    tipo_identificacion_abreviacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    ciudad_residencia: Optional[Text]
    genero: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        tipo_identificacion_abreviacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        genero: str
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.tipo_identificacion_abreviacion = tipo_identificacion_abreviacion
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
    def apoderado(self):
        if self.genero == 'Masculino':
            return 'Apoderado'
        elif self.genero == 'Femenino':
            return 'Apoderada'
        
    @property
    def doctor(self):    
        if self.genero == 'Masculino':
            return 'el doctor'
        elif self.genero == 'Femenino':
            return 'la doctora'
        
    @property
    def indole(self):
        if self.genero == 'Masculino':
            return 'varón'
        elif self.genero == 'Femenino':
            return 'mujer'