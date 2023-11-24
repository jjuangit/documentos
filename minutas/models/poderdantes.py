from typing import Optional
from typing import Text

from utils.exceptions import ValorNoEncontrado

class Poderdante:
    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    domicilio: Optional[Text]
    estado_civil: Optional[Text]
    genero: Optional[Text]

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