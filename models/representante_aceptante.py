from typing import Optional, Text


class RepresentanteAceptante:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    ciudad_residencia: Optional[Text]
    genero: Optional[Text]
    tipo_representante: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        genero: str,
        tipo_representante: str
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.ciudad_residencia = ciudad_residencia
        self.genero = genero
        self.tipo_representante = tipo_representante

    @property
    def identificado(self):
        if self.genero == 'Masculino':
            return 'identificado'
        elif self.genero == 'Femenino':
            return 'identificada'
        else:
            return 'identificado(a)'

    @property
    def vecino(self):
        if self.genero == 'Masculino':
            return 'vecino'
        elif self.genero == 'Femenino':
            return 'vecina'
        else:
            return 'vecino(a)'
        
    @property
    def doctor(self):
        if self.genero == 'Masculino':
            return 'el Dr'
        elif self.genero == 'Femenino':
            return 'la Dr'
        else:
            return 'el Dr(a)'
        
    @property
    def abreviacion_identificacion(self):
        if self.tipo_identificacion == 'Cédula de Ciudadanía':
            return 'C.C.'
        elif self.tipo_identificacion == 'Cédula de Extranjería':
            return 'C.E'
        elif self.tipo_identificacion == 'Pasaporte':
            return 'Pasaporte'
