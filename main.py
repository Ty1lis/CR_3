from models.operation import read_json_file
from models.views import show_last_five_operations
from settings import OPERATION_PATH


def main() -> None:
    data = read_json_file(OPERATION_PATH)

    transactions = show_last_five_operations(data)

    for transaction in transactions:
        print(
            f"{transaction['date']} {transaction['description']}\n"
            f"{transaction.get('from', 'нет информации счет/карта')} -> {transaction['to']}\n"
            f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n"
        )


if __name__ == "__main__":
    main()