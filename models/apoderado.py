from typing import Optional, Text


class Apoderado:

    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    genero: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        genero: str,
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.genero = genero

    @property
    def el_apoderado(self):
        if self.genero == 'Masculino':
            return 'el Apoderado'
        elif self.genero == 'Femenino':
            return 'la Apoderada'

    @property
    def apoderado(self):
        if self.genero == 'Masculino':
            return 'Apoderado'
        elif self.genero == 'Femenino':
            return 'Apoderada'

    @property
    def el(self):
        if self.genero == 'Masculino':
            return 'el'
        elif self.genero == 'Femenino':
            return 'ella'

    @property
    def identificado(self):
        if self.genero == 'Masculino':
            return 'identificado'
        elif self.genero == 'Femenino':
            return 'identificada'

    @property
    def abreviacion_identificacion(self):
        if self.tipo_identificacion == 'Cédula de Ciudadanía':
            return 'C.C.'
        elif self.tipo_identificacion == 'Cédula de Extranjería':
            return 'C.E'
        elif self.tipo_identificacion == 'Pasaporte':
            return 'Pasaporte'

    @property
    def assignee(self):
        if self.genero == 'Masculino':
            return 'apoderado'
        elif self.genero == 'Femenino':
            return 'apoderada'

    @property
    def facultado(self):
        if self.genero == 'Masculino':
            return 'facultado'
        elif self.genero == 'Femenino':
            return 'facultada'


class ApoderadoPoder(Apoderado):
    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        genero: str,
    ):
        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            genero)


class ApoderadoPromesaCompraventa(Apoderado):
    tipo_apoderado: Optional[Text]
    escritura: Optional[Text]
    fecha_autenticacion_poder: Optional[Text]
    tipo_dependencia_autenticacion: Optional[Text]
    nombre_dependencia: Optional[Text]
    ciudad_dependencia: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        genero: str,
        tipo_apoderado: str,
        escritura: str,
        fecha_autenticacion_poder: str,
        tipo_dependencia_autenticacion: str,
        nombre_dependencia: str,
        ciudad_dependencia: str
    ):
        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            genero)
        self.tipo_apoderado = tipo_apoderado
        self.escritura = escritura
        self.fecha_autenticacion_poder = fecha_autenticacion_poder
        self.tipo_dependencia_autenticacion = tipo_dependencia_autenticacion
        self.nombre_dependencia = nombre_dependencia
        self.ciudad_dependencia = ciudad_dependencia

    @property
    def dependencia(self):
        if self.tipo_dependencia_autenticacion == 'Notaría':
            return 'la'
        elif self.tipo_dependencia_autenticacion == 'Consulado':
            return 'el'

    @property
    def identificado(self):
        if self.genero == 'Masculino':
            return 'identificado'
        elif self.genero == 'Femenino':
            return 'identificada'

    @property
    def assignee(self):
        if self.genero == 'Masculino':
            return 'apoderado'
        elif self.genero == 'Femenino':
            return 'apoderada'

    @property
    def el(self):
        if self.genero == 'Masculino':
            return 'el'
        elif self.genero == 'Femenino':
            return 'la'

    @property
    def ellos(self):
        if self.genero == 'Masculino':
            return 'el'
        elif self.genero == 'Femenino':
            return 'ella'

    @property
    def abreviacion_identificacion(self):
        if self.tipo_identificacion == 'Cédula de Ciudadanía':
            return 'C.C.'
        elif self.tipo_identificacion == 'Cédula de Extranjería':
            return 'C.E'
        elif self.tipo_identificacion == 'Pasaporte':
            return 'Pasaporte'

    @property
    def facultado(self):
        if self.genero == 'Masculino':
            return 'facultado'
        elif self.genero == 'Femenino':
            return 'facultada'
