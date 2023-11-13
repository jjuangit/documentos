def strip_dict_or_list(data):
    '''Recortar espacios en blanco'''
    if isinstance(data, str):
        return data.strip()
    if isinstance(data, dict):
        return {key: strip_dict_or_list(value) for key, value in data.items()}
    if isinstance(data, list):
        return [strip_dict_or_list(item) for item in data]
    return data
