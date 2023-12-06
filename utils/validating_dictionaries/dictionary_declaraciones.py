from utils.validators import Validator

dictionary_validator_declaraciones = {
    'afectar_vivienda_familiar': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'pareja_hace_parte_compraventa': [
        Validator.required,
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'pais_firma': [
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'municipio_firma': [
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'departamento_firma': [
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'fecha_firma': [
        Validator.validate_string,
        Validator.validate_date_format,
        Validator.validate_date_not_past
    ]
}
