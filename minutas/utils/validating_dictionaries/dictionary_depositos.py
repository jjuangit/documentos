from utils.validators import Validator

dictionary_validator_depositos = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'numero': [
        Validator.validate_only_numbers
    ],
    'linderos_especiales': [
    ]
}
dictionary_validator_direccion = {
    'direccion': [
        Validator.validate_letters_numbers_comma_dot_hash_dash
    ],
}
dictionary_validator_matricula = {
    'matricula': [
        Validator.validate_string,
        Validator.validate_letters_numbers_dash
    ]
}
dictionary_validator_tipo_ficha_catastral = {
    'tipo_ficha_catastral': [
        Validator.validate_string,
        Validator.validate_letters_with_spaces,
        Validator.validate_special_characters
    ]
}
dictionary_validator_numero_ficha_catastral = {
    'numero_ficha_catastral': [
        Validator.validate_numbers_and_hyphens,
        Validator.validate_special_characters
    ]
}
