from typing import List
from typing import Text
from utils.exceptions import GeneracionDeMinutaError

class Document:
    generate_html_functions: List[Text] = []
    html = ""

    def __init__(self, html, name=None):
        self.html = html
        self.name = name

    def generate_html(self):
        try:
            self.html += '<div class="padding">'
            for nombre_function in self.generate_html_functions:
                self.html += getattr(self, nombre_function)()
            self.html += "</div>"
        except GeneracionDeMinutaError as e:
            print(str(e))
            raise GeneracionDeMinutaError('Error al generar el Código html')