from utils.validators import Validator

dictionary_validator_banco = {
    'nombre': [
        Validator.validate_string,
        Validator.validate_no_numbers,
        Validator.validate_special_characters
    ],
    'nit': [
        Validator.validate_numbers_dots_hyphens
    ],
    'prestamo_banco_a_hipotecante_en_numero': [
        Validator.validate_number,
    ],
    'cantidad_dada_a_constructora_en_numero': [
        Validator.validate_number,
    ],
    'gastos_de_gestion_en_numero': [
        Validator.validate_number,
    ]
}
