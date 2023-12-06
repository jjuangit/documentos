from utils.validators import Validator

dictionary_validator_banco = {
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

dictionary_validator_banco_promesa_compraventa = {
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

dictionary_validator_banco_poder = {
    'nombre': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ]
}
