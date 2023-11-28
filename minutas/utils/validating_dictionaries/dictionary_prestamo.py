from utils.validators import Validator

dictionary_validator_prestamo = {
    'cantidad_banco_a_hipotecante': [
        Validator.required,
        Validator.validate_number,
    ],
    'cantidad_dada_a_aceptante': [
        Validator.required,
        Validator.validate_number,
    ],
    'gastos_de_gestion': [
        Validator.required,
        Validator.validate_number,
    ]
}
