from utils.validators import Validator

dictionary_validator_parqueaderos = {
    'nombre': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'numero': [
        Validator.required,
        Validator.validate_alphanumeric_with_spaces_and_hyphen
    ],
    'direccion': [
        Validator.validate_letters_numbers_comma_dot_hash_dash
    ],
    'matricula': [
        Validator.validate_string,
        Validator.validate_letters_numbers_dash,
        Validator.validate_special_characters
    ],
    'tipo_ficha_catastral': [
        Validator.validate_string,
        Validator.validate_letters_with_spaces,
        Validator.validate_special_characters
    ],
    'numero_ficha_catastral': [
        Validator.validate_numbers_and_hyphens,
        Validator.validate_special_characters
    ],
    'linderos_especiales': [
        Validator.validate_string,
    ],
}
