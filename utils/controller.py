import json

class APIController:

    allowed_methods = []

    def __init__(self, event, context):
        self.event = event
        self.context = context
        self.body = json.loads(event['body'])
        self.path = event['requestContext']['http']['path']
        self.method = event['requestContext']['http']['method']
        self.query_string_parameters = event['rawQueryString']
        # self.path_parameters = event['pathParameters']
        self.headers = event['headers']
        # self.stage_variables = event['stageVariables']
        self.request_context = event['requestContext']
        # self.resource = event['resource']
        self.is_base64_encoded = event['isBase64Encoded']
        self.response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
                "Content-Type": "application/json",
            },
            "body": None,
        }

    def response_error(self, error, status_code=500):
        self.response["statusCode"] = status_code
        self.response["body"] = json.dumps({
            "error": error,
        })
        return self.response

    def run(self):
        try:
            if self.method not in self.allowed_methods:
                return self.response_error(
                    f"Method {self.method} not allowed",
                    403
                )
            method = getattr(self, self.method.lower())
            return method()
        except Exception as error:
            print(error)
            return self.response_error(
                str(error),
                500
            )


def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            return {
                "statusCode": 500,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Credentials": True,
                    "Content-Type": "application/json",
                },
                "body": json.dumps({
                    "error": f"Error al obtener {str(error)}",
                }),
            }
        except Exception as error:
            print(error)
            return {
                "statusCode": 500,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Credentials": True,
                    "Content-Type": "application/json",
                },
                "body": json.dumps({
                    "error": str(error),
                }),
            }
    return wrapper


class LambdaController:

    allowed_methods = []

    def __init__(self, event, context=None):
        self.body = event
        self.response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
                "Content-Type": "application/json",
            },
            "body": None,
        }

    def response_error(self, error, status_code=500):
        self.response["statusCode"] = status_code
        self.response["body"] = json.dumps({
            "error": error,
        })
        return self.response
