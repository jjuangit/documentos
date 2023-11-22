from utils.validators import Validator

dictionary_validator_poderdantes = {
    'nombre': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'tipo_identificacion': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_special_characters
    ],
    'numero_identificacion': [
        Validator.required,
        Validator.validate_numeric_string,
        Validator.validate_special_characters
    ],
    'ciudad_expedicion_identificacion': [
        Validator.required,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'domicilio': [
        Validator.required,
        Validator.validate_alphanumeric_with_spaces_and_hyphen
    ],
    'estado_civil': [
        Validator.required,
        Validator.validate_no_numbers,
        Validator.validate_string,
        Validator.validate_letters_with_spaces
    ],
    'genero': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters,
    ]
}
