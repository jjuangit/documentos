from utils.validators import Validator

dictionary_validator_inmueble = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'numero': [
        Validator.validate_numbers_letters_spaces
    ],
    'direccion': [
        Validator.validate_letters_numbers_comma_dot_hash_dash
    ],
    'ciudad_y_o_departamento': [
        Validator.validate_string,
        Validator.validate_letters_with_accents_dots_and_spaces
    ],
    'matricula': [
        Validator.validate_string,
        Validator.validate_letters_numbers_dash
    ],
    'municipio_de_registro_orip': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_letters_with_spaces
    ],
    'tipo_ficha_catastral': [
        Validator.validate_string,
        Validator.validate_special_characters,
        Validator.validate_no_numbers
    ],
    'numero_ficha_catastral': [
        Validator.validate_numbers_dashes_spaces_and_y
    ],
    'linderos_especiales': [
        Validator.validate_string
    ]
}