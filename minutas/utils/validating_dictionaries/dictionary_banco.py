from utils.validators import Validator

dictionary_validator_banco = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'nit': [
        Validator.validate_numbers_dots_hyphens
    ]
}
