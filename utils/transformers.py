class Transformers:
    @staticmethod
    def delete_dot(value, key=None):
        '''Elimina los puntos de un valor de entrada'''
        if value:
            return value.replace('.', '')
        else:
            return None
        
    @staticmethod
    def delete_hypen(value, key=None):
        '''Elimina los guionrd de un valor de entrada'''
        if value:
            return value.replace('-', '')
        else:
            return None
        
    @staticmethod
    def delete_comma(value, key=None):
        '''Elimina los guionrd de un valor de entrada'''
        if value:
            return value.replace(',', '')
        else:
            return None