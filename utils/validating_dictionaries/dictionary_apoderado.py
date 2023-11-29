from utils.validators import Validator

dictionary_validator_apoderado = {
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
    'genero': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters,
    ]
}
