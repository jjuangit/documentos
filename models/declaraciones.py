from typing import Optional, Text

class Declaraciones:

    afectar_vivienda_familiar = Optional[Text]
    pareja_hace_parte_de_compraventa = Optional[Text]
    pais_de_firma = Optional[Text]
    municipio_de_firma = Optional[Text]
    departamento_de_firma = Optional[Text]
    fecha_de_firma = Optional[Text]

    def __init__(self,
                 afectar_vivienda_familiar: str, 
                 pareja_hace_parte_de_compraventa: str, 
                 pais_de_firma: str, 
                 municipio_de_firma: str, 
                 departamento_de_firma: str, 
                 fecha_de_firma: str
                 ):
        self.afectar_vivienda_familiar = afectar_vivienda_familiar
        self.pareja_hace_parte_de_compraventa = pareja_hace_parte_de_compraventa
        self.pais_de_firma = pais_de_firma
        self.municipio_de_firma = municipio_de_firma
        self.departamento_de_firma = departamento_de_firma
        self.fecha_de_firma = fecha_de_firma