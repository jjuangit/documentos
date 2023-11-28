from typing import Optional
from typing import Text


class OrganoAutorizador:

    ciudad_ubicacion_camara_comercio: Optional[Text]
    numero_acta: Optional[Text]
    fecha_acta: Optional[Text]

    def __init__(
        self,
        ciudad_ubicacion_camara_comercio: str,
        numero_acta: str,
        fecha_acta: str,
    ):
        self.ciudad_ubicacion_camara_comercio = ciudad_ubicacion_camara_comercio
        self.numero_acta = numero_acta
        self.fecha_acta = fecha_acta
