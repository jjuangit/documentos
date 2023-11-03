from typing import Optional
from typing import Text


class Poderdante:
    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    domicilio: Optional[Text]
    estado_civil: Optional[Text]
    genero: Optional[Text]

    def __init__(self,
                 nombre: str,
                 tipo_identificacion: str,
                 numero_identificacion: str,
                 ciudad_expedicion_identificacion: str,
                 domicilio: str,
                 estado_civil: str,
                 genero: str
                 ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.domicilio = domicilio
        self.estado_civil = estado_civil
        self.genero = genero

    @property
    def identificado(self):
        if self.genero == 'Masculino':
            return 'identificado'
        elif self.genero == 'Femenino':
            return 'identificada'

    @property
    def domiciliado(self):
        if self.genero == 'Masculino':
            return 'domiciliado'
        elif self.genero == 'Femenino':
            return 'domiciliada'

    @property
    def residenciado(self):
        if self.genero == 'Masculino':
            return 'residenciado'
        elif self.genero == 'Femenino':
            return 'residenciada'
