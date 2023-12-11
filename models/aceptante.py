from typing import Optional, Text

class Aceptante:
    nombre: Optional[Text]
    nit: Optional[Text]
    ciudad_ubicacion: Optional[Text]
    escritura: Optional[Text]
    nombre_notaria: Optional[Text]
    ciudad_ubicacion_notaria: Optional[Text]
    ciudad_ubicacion_camara_comercio: Optional[Text]

    def __init__(
        self,
        nombre: str,
        nit: str,
        ciudad_ubicacion: str,
        escritura: str,
        nombre_notaria: str,
        ciudad_ubicacion_notaria: str,
        ciudad_ubicacion_camara_comercio: str,
    ):
        self.nombre = nombre
        self.nit = nit
        self.ciudad_ubicacion = ciudad_ubicacion
        self.escritura = escritura
        self.nombre_notaria = nombre_notaria
        self.ciudad_ubicacion_notaria = ciudad_ubicacion_notaria
        self.ciudad_ubicacion_camara_comercio = ciudad_ubicacion_camara_comercio
