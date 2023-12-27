import json


def read_json_file(path):
    """
    Функция чтения JSON файла
    :param path: str путь
    :return: list[dict] список со словарями или пустой список
    """
    with open(path) as json_file:
        data = json.load(json_file)
        if isinstance(data, list):
            return data
        else:
            return []