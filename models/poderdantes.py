from typing import Type, Optional, Text

from utils.exceptions import ValorNoEncontrado

class Poderdante:
    nombre: Type[Text]
    tipo_identificacion: Type[Text]
    numero_identificacion: Type[Text]
    ciudad_expedicion_identificacion: Type[Text]
    domicilio: Type[Text]
    estado_civil: Type[Text]
    genero: Type[Text]

    def __init__(
        self,
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
        
    @property
    def estado_civil_genero(self):
        if self.estado_civil == 'Casado con sociedad conyugal vigente':
            if self.genero == "Masculino":
                return "Casado con sociedad conyugal vigente"
            elif self.genero == "Femenino":
                return "Casada con sociedad conyugal vigente"
        elif self.estado_civil == 'Casado sin sociedad conyugal vigente':
            if self.genero == "Masculino":
                return "Casado sin sociedad conyugal vigente"
            elif self.genero == "Femenino":
                return "Casada sin sociedad conyugal vigente"
        elif self.estado_civil == 'Soltero sin unión marital de hecho':
            if self.genero == "Masculino":
                return "Soltero sin unión marital de hecho"
            elif self.genero == "Femenino":
                return "Soltera sin unión marital de hecho"
        elif self.estado_civil == 'Soltero con unión marital de hecho y sociedad patrimonial vigente':
            if self.genero == "Masculino":
                return "Soltero con unión marital de hecho y sociedad patrimonial vigente"
            elif self.genero == "Femenino":
                return "Soltera con unión marital de hecho y sociedad patrimonial vigente"
        elif self.estado_civil == 'Soltero con unión marital de hecho sin sociedad patrimonial vigente':
            if self.genero == "Masculino":
                return "Soltero con unión marital de hecho sin sociedad patrimonial vigente"
            elif self.genero == "Femenino":
                return "Soltera con unión marital de hecho sin sociedad patrimonial vigente"
        raise ValorNoEncontrado(f"El valor <{self.estado_civil}> no se encuentra en el catálogo de estado_civil")

    @property
    def abreviacion_identificacion(self):
        if self.tipo_identificacion == 'Cédula de Ciudadanía':
            return 'C.C.'
        elif self.tipo_identificacion == 'Cédula de Extranjería':
            return 'C.E'
        elif self.tipo_identificacion == 'Pasaporte':
            return 'Pasaporte'

class PoderdantePoder(Poderdante):
    domicilio_pais: Optional[Text]
    domicilio_municipio: Optional[Text]
    domicilio_departamento: Optional[Text]

    def __init__(
        self,
        nombre: str,
        tipo_identificacion: str,
        numero_identificacion: str,
        ciudad_expedicion_identificacion: str,
        estado_civil: str,
        genero: str,
        domicilio_pais: str,
        domicilio_municipio: str,
        domicilio_departamento: str
    ):
        super().__init__(
            nombre,
            tipo_identificacion,
            numero_identificacion,
            ciudad_expedicion_identificacion,
            "",
            estado_civil,
            genero,
        )
        self.domicilio_pais = domicilio_pais
        self.domicilio_municipio = domicilio_municipio
        self.domicilio_departamento = domicilio_departamento