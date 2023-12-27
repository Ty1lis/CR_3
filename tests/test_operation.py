import pytest

from models.operation import get_mask_the_bankcard, get_mask_the_bank_account, get_mask_bankcard_account, convert_date


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361 5", "Не верный номер карты"),
    ("70007922896063615", "Не верный номер карты")
])
def test_get_mask_the_bankcard(card_number: str, expected: str) -> None:
    """
    Тесты для функции get_mask_the_bankcard
    :param card_number: Номер карты
    :param expected: Замаскированный номер карты
    :return:
    """
    assert get_mask_the_bankcard(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("736 541084 301358 74305", "**4305"),
    ("73654108430135874305 4", "Не верный номер счета")
])
def test_get_mask_the_bank_account(account_number: str, expected: str) -> None:
    """
    Тесты для функции get_mask_the_bank_account
    :param account_number: Номер счета
    :param expected: Замаскированный номер счета
    :return:
    """
    assert get_mask_the_bank_account(account_number) == expected


@pytest.mark.parametrize("number_name, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Maestro 15968378687051995", "Maestro Не верный номер карты"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_get_mask_bankcard_account(number_name: str, expected: str) -> None:
    """
    Тест для функции get_mask_bankcard_account
    :param number_name: Номер счета/карты
    :param expected: Замаскированный номер счета/карты
    :return:
    """
    assert get_mask_bankcard_account(number_name) == expected


def test_convert_date() -> None:
    """
    Тест для функции convert_date
    :return: None
    """
    result = convert_date("2018-07-11T02:26:18.671407")
    assert result == "11.07.2018"
    