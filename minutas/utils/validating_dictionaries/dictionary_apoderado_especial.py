from utils.validators import Validator

dictionary_validator_apoderado_especial = {
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
    'ciudad_residencia': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'genero': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ]
}
