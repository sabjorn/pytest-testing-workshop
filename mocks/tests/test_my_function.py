import pytest

from my_function import function_under_test


@pytest.fixture
def requests_mock(mocker):
    return mocker.patch("my_function.requests", return_value=mocker.Mock())


def test_function_under_test(requests_mock):
    requests_mock.get.return_value.json.return_value = {
        "name": "some name",
        "author": "some author",
        "colors": ["0x00FF00", "0xFFFFFF"],
    }

    actual = function_under_test(palette_name="palette_name")

    requests_mock.get.assert_called_with(
        f"https://Lospec.com/palette-list/palette_name"
    )

    assert actual.name == "some name"
    assert actual.author == "some author"
    assert actual.colors == ["0x00FF00", "0xFFFFFF"]
