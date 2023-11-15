from utils.validators import Validator

dictionary_validator_parqueaderos = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'numero': [
        Validator.validate_only_numbers
    ],
    'direccion': [
        Validator.validate_letters_numbers_comma_dot_hash_dash
    ],
    'matricula': [
        Validator.validate_string,
        Validator.validate_letters_numbers_dash
    ],
    'tipo_ficha_catastral': [
    ],
    'numero_ficha_catastral': [
    ],
    'linderos_especiales': [
    ]
}