from typing import Optional
from typing import Text


class ApoderadoBanco:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    ciudad_residencia: Optional[Text]
    genero: Optional[Text]
    tipo_apoderado: Optional[Text]
    tipo_poder: Optional[Text]
    poder_autenticado: bool = False

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        genero: str,
        tipo_apoderado: str,
        tipo_poder: str,
        escritura: str
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.ciudad_residencia = ciudad_residencia
        self.genero = genero
        self.tipo_apoderado = tipo_apoderado
        self.tipo_poder = tipo_poder
        self.escritura = escritura

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
    def naturaleza(self):
        if self.genero == 'Masculino':
            return 'varón'
        elif self.genero == 'Femenino':
            return 'mujer'
        
    @property
    def abreviacion_identificacion(self):
        if self.tipo_identificacion == 'Cédula de Ciudadanía':
            return 'C.C.'
        elif self.tipo_identificacion == 'Cédula de Extranjería':
            return 'C.E'
        elif self.tipo_identificacion == 'Pasaporte':
            return 'Pasaporte'