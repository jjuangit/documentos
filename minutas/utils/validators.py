import re

from utils.exceptions import ValidationError


class Validator:
    '''Validación de datos'''

    @staticmethod
    def validate_only_letters(value, dictionary_name):
        '''Solo letras son permitidas'''
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_string(value, dictionary_name):
        '''Solo cadenas de texto son permitidas'''
        if not isinstance(value, str):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" no es una cadena de texto.')
        return True

    @staticmethod
    def validate_number(value, dictionary_name):
        '''Solo números enteros son permitidos'''
        if not isinstance(value, int):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" no es un número entero.')
        return True

    @staticmethod
    def validate_no_numbers(value, dictionary_name):
        '''No se permiten números'''
        pattern = r'^[^0-9]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" contiene números y no está permitido.')
        return True

    @staticmethod
    def validate_only_numbers(value, dictionary_name):
        '''Solo se permiten números'''
        pattern = r'^\d+$'
        if not re.match(pattern, value):
            raise ValueError(
                f'Error en {dictionary_name}: "{value}" no contiene solo números.')
        return True

    @staticmethod
    def validate_letters_with_spaces(value, dictionary_name):
        '''Solo se permiten letras y espacios intermedios'''
        pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$'
        if not re.match(pattern, value):
            raise ValueError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_letters_with_accents_dots_and_spaces(value, dictionary_name):
        '''Solo se permiten letras incluyendo tildes y puntos(.)'''
        pattern = r'^[a-zA-ZáéíóúüÁÉÍÓÚÜ.\s]+$'
        if not re.match(pattern, value):
            raise ValueError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_alphanumeric_with_spaces_and_hyphen(value, dictionary_name):
        '''Solo se permiten letras,espacios intermedios y guión(-)'''
        pattern = r'^[a-zA-Z0-9\s-]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_numeric_string(value, dictionary_name):
        '''Solo se permiten números y punto(.)'''
        pattern = r'^[0-9.]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" no es una cadena numérica válida.')
        return True

    @staticmethod
    def validate_special_characters(value, dictionary_name):
        '''No se permiten los carácteres especiales definidos en el pattern'''
        pattern = r'[@_!#$%^&*()<>?/\|}{~:]'
        if re.search(pattern, value):
            raise ValidationError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres especiales no permitidos.')
        return True

    @staticmethod
    def validate_letters_numbers_comma_dot_hash_dash(value, dictionary_name):
        '''Solo se permiten letras, números, almohadilla(#) y guion(-)'''
        pattern = r'^[a-zA-Z0-9,.\#\-\s]+$'
        if not re.match(pattern, value):
            raise ValueError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_letters_numbers_dash(value, dictionary_name):
        '''Solo se permiten letras, números y guion(-)'''
        pattern = r'^[a-zA-Z0-9\-]+$'
        if not re.match(pattern, value):
            raise ValueError(
                f'Error en {dictionary_name}: "{value}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_numbers_dots_hyphens(value, dictionary_name):
        '''Solo se permiten numeros, puntos(.) y guión(-)'''
        pattern = r'^[\d\.-]+$'
        if not re.match(pattern, value):
            raise ValueError(
                f'Error en {dictionary_name}: "{value}" contiene caracteres no permitidos.')
        return True

    @staticmethod
    def validate_dict(dictionary, dictionary_validator, dictionary_name):
        '''Validación de diccionario'''
        for key, validators in dictionary_validator.items():
            for validator in validators:
                validator(dictionary[key], dictionary_name)
        return True
