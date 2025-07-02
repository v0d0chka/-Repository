import pytest

from models import Bank, BankAccount, Person


# @pytest.fixture(scope='function')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
@pytest.fixture(scope="session")
def person() -> Person:
    print(111111111)
    oleg = Person("Oleg")
    return oleg


@pytest.fixture(scope="session")
def another_person() -> Person:
    oleg = Person("Oleg")
    return oleg


@pytest.fixture(scope="session")
def bank() -> Bank:
    b = Bank("Mono")
    return b


@pytest.fixture(scope="session")
def bank2() -> Bank:
    b = Bank("Privat")
    return b


@pytest.fixture(scope="session")
def bank_account(bank, person) -> BankAccount:
    account = bank.open_account(person)
    return account


@pytest.fixture(scope="session")
def bank_account2(bank, another_person) -> BankAccount:
    account = bank.open_account(another_person)
    return account
