import pytest

from my_function import function_under_test


@pytest.fixture()
def process_numbers_mock(mocker):
    def mock_return(values: list[int]) -> list[int]:
        for v in values:
            assert type(v) is int
        return [value + 1 for value in values]

    return mocker.patch(
        "my_function.process_numbers",
        side_effect=mock_return,
    )


@pytest.mark.parametrize(
    "input_values, expected",
    [
        (
            {"a": [1]}, [1 + 1]
        ),
        (
            {"a": [1], "b": [2, 3]},
            [1 + 1, 2 + 1, 3 + 1]
        ),
        (
            {"a": [1], "b": [2, 3], "c": [4, 5, 6]},
            [1 + 1, 2 + 1, 3 + 1, 4 + 1, 5 + 1, 6 + 1]
        ),
    ],
)
def test_function_under_test(
    process_numbers_mock,
    input_values,
    expected,
):
    actual = function_under_test(input_values)

    assert actual == expected
    assert process_numbers_mock.called
