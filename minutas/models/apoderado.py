from typing import Optional, Text


class Apoderado:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    tipo_identificacion_abreviacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    genero: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        tipo_identificacion_abreviacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        genero: str
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.tipo_identificacion_abreviacion = tipo_identificacion_abreviacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.genero = genero

    @property
    def apoderado(self):
        if self.genero == 'Masculino':
            return 'el Apoderado'
        elif self.genero == 'Femenino':
            return 'la Apoderada'
