import re
from datetime import datetime

from utils.exceptions import ValidationError


class Validator:
    '''Validación de datos'''

    @staticmethod
    def validate_only_letters(value, key=None):
        '''Solo letras son permitidas'''
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'"{key}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_string(value, key=None):
        '''Validar que sea tipo de dato string'''
        if value:
            if not isinstance(value, str):
                raise ValidationError(
                    f'"{key}" no es una cadena de texto.')
            return True
        else:
            return True

    @staticmethod
    def validate_number(value, key=None):
        '''Solo números enteros son permitidos'''
        if value:
            if not isinstance(value, int):
                raise ValidationError(
                    f'"{key}" no es un número entero.')
            return True
        else:
            return True

    @staticmethod
    def validate_no_numbers(value, key=None):
        '''No se permiten números'''
        if value:
            pattern = r'^[^0-9]+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f'"{key}" contiene números y no está permitido.')
            return True
        else:
            return True

    @staticmethod
    def validate_only_numbers(value, key=None):
        '''Solo se permiten números'''
        if value:
            pattern = r'^\d+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f'"{key}" no contiene solo números.')
            return True
        else:
            return True

    @staticmethod
    def validate_letters_numbers(value, key=None):
        '''Valida si la cadena contiene solo letras y números'''
        if value:
            pattern = r'^[a-zA-Z0-9]+$'
            if not re.match(pattern, value):
                raise ValueError(f'"{key}" contiene caracteres no permitidos.')
            return True
        else:
            return True

    @staticmethod
    def validate_letters_with_spaces(value, key=None):
        '''Solo se permiten letras y espacios intermedios'''
        if value:
            pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f'"{key}" contiene carácteres no permitidos.')
            return True
        else:
            return True

    @staticmethod
    def validate_letters_with_accents_dots_and_spaces(value, key=None):
        '''Solo se permiten letras incluyendo tildes y puntos(.)'''
        pattern = r'^[a-zA-ZáéíóúüÁÉÍÓÚÜñÑ.,\s-]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'"{key}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_alphanumeric_with_spaces_and_hyphen(value, key=None):
        '''Solo se permiten letras,espacios intermedios y guión(-)'''
        pattern = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜöñÑ\s-]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'"{key}" contiene carácteres no permitidos.')
        return True

    @staticmethod
    def validate_numeric_string(value, key=None):
        '''Solo se permiten números y punto(.)'''
        if value:
            pattern = r'^[0-9.]+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f'"{key}" no es una cadena numérica válida.')
            return True
        else:
            return True

    @staticmethod
    def validate_special_characters(value, key=None):
        '''No se permiten los carácteres especiales definidos en el pattern'''
        if value:
            pattern = r'[@_!#$%^&*()<>?/\|}{~:]'
            if re.search(pattern, value):
                raise ValidationError(
                    f'"{key}" contiene carácteres especiales no permitidos.')
            return True
        else:
            return True

    @staticmethod
    def validate_letters_numbers_comma_dot_hash_dash(value, key=None):
        '''Solo se permiten letras, números, almohadilla(#) y guion(-)'''
        if value:
            pattern = r'^[a-zA-Z0-9,.\#\-\s\'"áéíóúÁÉÍÓÚüÜñÑ()/]+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f'"{key}" contiene carácteres no permitidos.')
            return True
        else:
            return True

    @staticmethod
    def validate_letters_numbers_dash(value, key=None):
        '''Solo se permiten letras, números y guion(-)'''
        if value:
            pattern = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚüÜ\s,-]+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f'"{key}" contiene carácteres no permitidos.')
            return True
        else:
            return True

    @staticmethod
    def validate_numbers_dots_hyphens(value, key=None):
        '''Solo se permiten numeros, puntos(.) y guión(-)'''
        pattern = r'^[\d\.-]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f'"{key}" contiene caracteres no permitidos.')
        return True

    @staticmethod
    def validate_numbers_letters_spaces(value, key=None):
        '''Solo se permiten numeros, letras, tildes y espacios'''
        if value:
            pattern = r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜ]+$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f"{key} contiene caracteres no permitidos.")
            return True
        else:
            return True

    @staticmethod
    def validate_numbers_dashes_spaces(value, key=None):
        '''Solo se permiten números, guiones(-), espacios intermedios'''
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            value = ' '.join(str(v) for item in value for v in item.values())
        pattern = r'^[0-9\s\-]+$'
        if not re.match(pattern, value):
            raise ValidationError(
                f"{key} contiene caracteres no permitidos.")
        return True

    @staticmethod
    def validate_numbers_and_hyphens(value, key=None):
        '''Solo se permiten números y guines(-)'''
        if value:
            pattern = r'^[0-9]+(-[0-9]+)*$'
            if not re.match(pattern, value):
                raise ValidationError(
                    f"{key} contiene caracteres no permitidos.")
            return True
        else:
            return True

    @staticmethod
    def validate_date_format(value, key=None):
        '''Solo se permite fecha con el siguiente formato (dd/mm/yyyy)'''
        if value:
            pattern = r'^\d{2}/\d{2}/\d{4}$'

            if not re.match(pattern, value):
                raise ValueError(
                    f'Error: La fecha "{key}" no tiene el formato correcto (dd/mm/yyyy).')

            return True
        else:
            return True

    @staticmethod
    def required(value, key=None):
        '''Valida si el valor es requerido (no es None ni cadena vacía)'''
        if value is None or (isinstance(value, str) and value.strip() == ''):
            raise ValidationError(f'"{key}" es un campo es requerido.')
        return True

    @staticmethod
    def validate_date_not_past(value, key=None):
        '''Valida que la fecha no sea menor a la fecha actual'''
        if value:
            input_date = datetime.strptime(value, '%d/%m/%Y').date()
            current_date = datetime.now().date()
            if input_date < current_date:
                raise ValidationError(f'"{key}" no puede ser una fecha pasada.')
            return True
            
        else:
            return True
        
    @staticmethod
    def validate_dict(dictionary, dictionary_validator, dictionary_name):
        '''Validación de diccionarios'''
        try:
            for key, validators in dictionary_validator.items():
                for validator in validators:
                    validator(dictionary[key], key)
            return True
        except ValidationError as error:
            raise ValidationError(
                f'Error en la validación de {dictionary_name}: {str(error)}')
