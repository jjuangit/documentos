from typing import Optional, Type, Text


class Inmueble:
    nombre: Type[Text]
    numero: Type[Text]
    direccion: Type[Text]
    ciudad_y_o_departamento: Type[Text]
    matricula: Type[Text]
    municipio_de_registro_orip: Type[Text]
    tipo_ficha_catastral: Type[Text]
    numero_ficha_catastral: Type[Text]
    numero_chip: Optional[Text]
    linderos_especiales: Optional[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        ciudad_y_o_departamento: str,
        matricula: str,
        municipio_de_registro_orip: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
        numero_chip: str,
        linderos_especiales: str,
    ):
        self.nombre = nombre
        self.numero = numero
        self.direccion = direccion
        self.ciudad_y_o_departamento = ciudad_y_o_departamento
        self.matricula = matricula
        self.municipio_de_registro_orip = municipio_de_registro_orip
        self.tipo_ficha_catastral = tipo_ficha_catastral
        self.numero_ficha_catastral = numero_ficha_catastral
        self.numero_chip = numero_chip
        self.linderos_especiales = linderos_especiales

class InmueblePromesaCompraventa(Inmueble):

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        ciudad_y_o_departamento: str,
        matricula: str,
        municipio_de_registro_orip: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
        numero_chip: str
    ):
        super().__init__(
            nombre,
            numero,
            direccion,
            ciudad_y_o_departamento,
            matricula,
            municipio_de_registro_orip,
            tipo_ficha_catastral,
            numero_ficha_catastral,
            numero_chip,
            linderos_especiales=None
        )

class InmuebleCompraventaLeasing(Inmueble):

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        ciudad_y_o_departamento: str,
        matricula: str,
        municipio_de_registro_orip: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
        numero_chip: str,
        linderos_especiales: str
    ):
        super().__init__(
            nombre,
            numero,
            direccion,
            ciudad_y_o_departamento,
            matricula,
            municipio_de_registro_orip,
            tipo_ficha_catastral,
            numero_ficha_catastral,
            numero_chip,
            linderos_especiales
        )

class InmueblePoder(Inmueble):
    departamento: Type[Text]
    ciudad: Type[Text]

    def __init__(
        self,
        nombre: str,
        numero: str,
        direccion: str,
        departamento: str,
        ciudad: str,
        matricula: str,
        tipo_ficha_catastral: str,
        numero_ficha_catastral: str,
    ):
        super().__init__(
            nombre,
            numero,
            direccion,
            '',
            matricula,
            '',
            tipo_ficha_catastral,
            numero_ficha_catastral,
            '',
            '',
        )
        self.departamento = departamento
        self.ciudad = ciudad
