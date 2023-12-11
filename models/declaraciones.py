from typing import Optional, Text


class Declaraciones:

    afectar_vivienda_familiar: Optional[Text]
    pareja_hace_parte_compraventa: Optional[Text]
    pais_firma: Optional[Text]
    municipio_firma: Optional[Text]
    departamento_firma: Optional[Text]
    fecha_firma: Optional[Text]

    def __init__(self,
                 afectar_vivienda_familiar: str,
                 pareja_hace_parte_compraventa: str,
                 pais_firma: str,
                 municipio_firma: str,
                 departamento_firma: str,
                 fecha_firma: str
                 ):
        self.afectar_vivienda_familiar = afectar_vivienda_familiar
        self.pareja_hace_parte_compraventa = pareja_hace_parte_compraventa
        self.pais_firma = pais_firma
        self.municipio_firma = municipio_firma
        self.departamento_firma = departamento_firma
        self.fecha_firma = fecha_firma
