from utils.validators import Validator

dictionary_validator_poderdantes = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'tipo_identificacion': [
        Validator.validate_string,
        Validator.validate_special_characters
    ],
    'numero_identificacion': [
        Validator.validate_numeric_string,
        Validator.validate_special_characters
    ],
    'ciudad_expedicion_identificacion': [
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'domicilio': [
        Validator.validate_alphanumeric_with_spaces_and_hyphen
    ],
    'estado_civil': [
        Validator.validate_no_numbers,
        Validator.validate_string,
        Validator.validate_letters_with_spaces
    ],
    'genero': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_only_letters,
    ]
}
