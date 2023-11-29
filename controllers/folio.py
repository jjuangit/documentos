from models.folio import Folio
from utils.controller import LambdaController
from utils.controller import try_catch
import json

class FolioController(LambdaController):

    @try_catch
    def create_hipoteca(self):
        folio = Folio(**self.body)
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(folio.generate_html())
        return self.response
    
    @try_catch
    def create_promesa_compraventa(self):
        folio = Folio(**self.body)
        self.response["statusCode"] = 201
        self.response["body"] = json.dumps(folio.generate_html())
        return self.response
    
def create_hipoteca(event, context):
    controller = FolioController(event, context)
    response = controller.create_hipoteca()
    return response
    
def create_promesa_compraventa(event, context):
    controller = FolioController(event, context)
    response = controller.create_promesa_compraventa()
    return response