from typing import Optional, Type, Text


class ConjuntoResidencial:
    nombre: Type[Text]
    matricula: Type[Text]
    municipio_de_registro_orip: Type[Text]
    tipo_ficha_catastral: Type[Text]
    numero_ficha_catastral: Type[Text]
    linderos_generales: Optional[Text]

    def __init__(
        self,
        nombre: str,
        matricula: str,
        municipio_de_registro_orip: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
        linderos_generales: str,
    ):
        self.nombre = nombre
        self.matricula = matricula
        self.municipio_de_registro_orip = municipio_de_registro_orip
        self.tipo_ficha_catastral = tipo_ficha_catastral
        self.numero_ficha_catastral = numero_ficha_catastral
        self.linderos_generales = linderos_generales
