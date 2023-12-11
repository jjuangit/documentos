from typing import Optional, Type, Text


class ApoderadoBanco:

    nombre: Type[Text]
    tipo_identificacion: Type[Text]
    numero_identificacion: Type[Text]
    ciudad_expedicion_identificacion: Type[Text]
    ciudad_residencia: Type[Text]
    tipo_apoderado: Type[Text]
    tipo_poder: Type[Text]
    escritura: Optional[Text]
    genero: Type[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        tipo_apoderado: str,
        tipo_poder: str,
        escritura: str,
        genero: str
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.ciudad_residencia = ciudad_residencia
        self.tipo_apoderado = tipo_apoderado
        self.tipo_poder = tipo_poder
        self.escritura = escritura
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
    def el(self):
        if self.genero == 'Masculino':
            return 'el'
        elif self.genero == 'Femenino':
            return 'ella'

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


class ApoderadoBancoPromesaCompraventa(ApoderadoBanco):
    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        tipo_apoderado: str,
        tipo_poder: str,
        escritura: str,
        genero: str
    ):

        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            ciudad_residencia,
            tipo_apoderado,
            tipo_poder,
            escritura,
            genero
        )

class ApoderadoBancoCompraventaLeasing(ApoderadoBanco):
    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        tipo_apoderado: str,
        tipo_poder: str,
        escritura: str,
        genero: str,
    ):

        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            ciudad_residencia,
            tipo_apoderado,
            tipo_poder,
            escritura,
            genero
        )
