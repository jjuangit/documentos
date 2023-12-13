from utils.validators import Validator

dictionary_validator_conjunto_residencial = {
    'nombre': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_special_characters
    ],
    'matricula': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_letters_numbers_dash
    ],
    'municipio_de_registro_orip': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_letters_with_spaces
    ],
    'tipo_ficha_catastral': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_special_characters,
        Validator.validate_no_numbers
    ],
    'numero_ficha_catastral': [
        Validator.required,
        Validator.validate_numbers_dashes_spaces
    ],
    'linderos_generales': [
        Validator.validate_string
    ]
}
