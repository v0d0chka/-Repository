class TestBank:
    def test_new_bank(self, bank):
        assert bank.name
        assert bank.passive == 0
        assert bank.active == 0
        assert not bank.accounts
