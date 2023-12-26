import json

from models.operation import Operation


def get_all_operations(path):
    """
    Функция получения операций из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, encoding="utf=8") as file:
        return json.load(file)


def get_operations_instances(operations):
    """
    Получает список экземпляров класса
    :param operations: список операций
    :return: список экземпляров класса
    """
    operations_instances = []
    for operation in operations:
        if operation:
            operations_instance = Operation(
                pk=operation['id'],
                state=operation['state'],
                date=operation['date'],
                operation_amount=operation['operationAmount'],
                description=operation['description'],
                from_=operation.get('from', ''),
                to=operation['to']
            )
            operations_instances.append(operations_instance)
    return operations_instances
