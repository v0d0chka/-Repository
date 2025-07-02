import pytest

from utils.utils import add_two_numbers


class TestAddTwoNumbers:
    # def test_add_two_numbers_success(self):
    #     number1 = 2
    #     number2 = 3
    #     expected_result = 5
    #     actual_result = add_two_numbers(number1, number2)
    #     assert actual_result == expected_result
    #
    # def test_add_two_strings_success(self):
    #     number1 = "23"
    #     number2 = "23"
    #     expected_result = 46
    #     actual_result = add_two_numbers(number1, number2)
    #     assert actual_result == expected_result

    def test_add_two_strings_fail(self):
        number1 = "dfgjhdfg"
        number2 = "ljkdfghkjdfg"
        with pytest.raises(ValueError):
            add_two_numbers(number1, number2)

    @pytest.mark.parametrize(
        "number1, number2, expected_result",
        [
            (2, 3, 5),
            ("23", "23", 46),
            ("0", 0, 0),
            ("0", 0, 0),
            ("0", 0, 0),
            ("0", 0, 0),
        ],
    )
    def test_success(self, number1, number2, expected_result):
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result
