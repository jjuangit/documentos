from typing import Optional, Text

class RegimenPropiedad:
    escritura: Optional[Text]

    def __init__(
            self,
            escritura
            ):
        self.escritura = escritura
