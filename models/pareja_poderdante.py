from typing import Optional, Text


class ParejaPoderdante:
    nombre: Optional[Text]
    tipo_identificacion: Optional[Text]
    ciudad_expedicion_identificacion: Optional[Text]
    numero_identificacion: Optional[Text]
    domicilio_pais: Optional[Text]
    domicilio_municipio: Optional[Text]
    domicilio_departamento: Optional[Text]
    estado_civil: Optional[Text]
    genero: Optional[Text]

    def __init__(self,
                 nombre: str,
                 tipo_identificacion: str,
                 ciudad_expedicion_identificacion: str,
                 numero_identificacion: str,
                 domicilio_pais: str,
                 domicilio_municipio: str,
                 domicilio_departamento: str,
                 estado_civil: str,
                 genero: str
                 ):
        
        self.nombre = nombre
        self.tipo_identificacion = tipo_identificacion
        self.ciudad_expedicion_identificacion = ciudad_expedicion_identificacion
        self.numero_identificacion = numero_identificacion
        self.domicilio_pais = domicilio_pais
        self.domicilio_municipio = domicilio_municipio
        self.domicilio_departamento = domicilio_departamento
        self.estado_civil = estado_civil
        self.genero = genero

    @property
    def estado_civil_genero_pareja(self):
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
    def companero(self):
        if self.genero == 'Masculino':
            return 'compañero'
        elif self.genero == 'Femenino':
            return 'compañera'
        
