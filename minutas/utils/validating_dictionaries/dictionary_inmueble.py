from utils.validators import Validator

dictionary_validator_inmueble = {
    'nombre': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'numero': [
        Validator.required,
        Validator.validate_letters_numbers_dash
    ],
    'direccion': [
        Validator.required,
        Validator.validate_letters_numbers_comma_dot_hash_dash
    ],
    'ciudad_y_o_departamento': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_letters_with_accents_dots_and_spaces
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
    'linderos_especiales': [
        Validator.validate_string
    ]
}
