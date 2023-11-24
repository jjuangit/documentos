from utils.validators import Validator

dictionary_validator_compraventa = {
    'cantidad_compraventa': [
        Validator.required,
        Validator.validate_number,
    ],
    'cantidad_restante': [
        Validator.required,
        Validator.validate_number,
    ],
    'cuota_inicial': [
        Validator.required,
        Validator.validate_number,
    ]
}
