from unittest.mock import Mock
from bestpy import best_class

method_mock = Mock(return_value="result")
MOCK_ANSWERS = {
    "static": "static",
    "list": ["a", "b", "c"],
    "method": method_mock
}
NORMAL_ANSWERS = best_class.answers
best = best_class.Best()


# The reason for these 2 functions is to allow the answer data to change,
# but still allow the tests to pass as long as the Best class works correctly.
# Assuming the format of the answer data does not change,
# if it does the tests should be updated to reflect this.
def setup_function(function):
    # Mock answers
    best_class.answers = MOCK_ANSWERS


def teardown_function(function):
    # Restore answers
    best_class.answers = NORMAL_ANSWERS


def test_static():
    assert best.static == "static"


def test_list():
    assert best.list in ["a", "b", "c"]


def test_method():
    method_mock.reset_mock()

    assert best.method == "result"
    method_mock.assert_called_once()
