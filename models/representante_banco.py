from typing import Type, Text


class RepresentanteBanco:

    nombre: Type[Text]
    tipo_identificacion: Type[Text]
    numero_identificacion: Type[Text]
    ciudad_expedicion_identificacion: Type[Text]
    ciudad_residencia: Type[Text]
    tipo_representante: Type[Text]
    genero: Type[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        tipo_representante: str,
        genero: str,
    ):
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.ciudad_residencia = ciudad_residencia
        self.tipo_representante = tipo_representante,
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

class RepresentanteBancoPromesaCompraventa(RepresentanteBanco):
    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        tipo_representante: str,
        genero: str,
    ):
        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            ciudad_residencia,
            tipo_representante,
            genero,
        )

class RepresentanteBancoCompraventaLeasing(RepresentanteBanco):
    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        ciudad_residencia: str,
        tipo_representante: str,
        genero: str,
    ):
        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            ciudad_residencia,
            tipo_representante,
            genero,
        )
