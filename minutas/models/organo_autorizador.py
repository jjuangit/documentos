from typing import Optional
from typing import Text


class OrganoAutorizador:

    ciudad_ubicacion_camara_comercio: Optional[Text]
    numero_acta: Optional[Text]
    fecha: Optional[Text]

    def __init__(
        self,
        ciudad_ubicacion_camara_comercio: str,
        numero_acta: str,
        fecha: str,
    ):
        self.ciudad_ubicacion_camara_comercio = ciudad_ubicacion_camara_comercio
        self.numero_acta = numero_acta
        self.fecha = fecha
