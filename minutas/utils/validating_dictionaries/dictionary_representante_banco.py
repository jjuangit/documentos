from utils.validators import Validator

dictionary_validator_representante_banco = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'tipo_identificacion': [
        Validator.validate_string,
        Validator.validate_letters_with_spaces,
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
    'ciudad_residencia': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'genero': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'tipo_representante': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
}
