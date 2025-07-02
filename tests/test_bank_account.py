class TestBankAccount:
    def test_bank_account(self, bank_account, person):
        assert bank_account.balance == 0
        assert bank_account.client == person

    def test_deposit(self, bank_account, bank):
        bank_account.deposit(3000)
        assert bank_account.balance == 3000
        assert bank.passive == 3000
        assert bank.active == 0

    def test_withdraw(self, bank_account2, bank):
        bank_account2.withdraw(2000)
        assert bank_account2.balance == -2000
        assert bank.passive == 3000
        assert bank.active == -2000

    def test_transfer(self, bank_account, bank_account2):
        bank_account.transfer(bank_account2, 50)
        assert bank_account.balance == 3000 - 50
        assert bank_account2.balance == -2000 + 50
