from utils.validators import Validator

dictionary_validator_aceptante = {
    'nombre': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'nit': [
        Validator.required,
        Validator.validate_numbers_dots_hyphens
    ]
}
