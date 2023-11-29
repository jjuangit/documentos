from utils.validators import Validator

dictionary_validator_organo_autorizador = {
    'ciudad_ubicacion_camara_comercio': [
        Validator.validate_string,
        Validator.validate_letters_with_accents_dots_and_spaces
    ],
    'numero_acta': [
        Validator.validate_numbers_letters_spaces
    ],
    'fecha_acta': [
        Validator.validate_string,
        Validator.validate_date_format
    ]
}
