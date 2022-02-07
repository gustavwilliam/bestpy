from unittest.mock import Mock
from bestpy.best_class import Best
from bestpy.answers import answers as normal_answers

mock_method = Mock(return_value="result")
MOCK_ANSWERS = {
    "static": "static",
    "list": ["a", "b", "c"],
    "method": mock_method
}

# Initialize the mock instance of `Best`
best = Best(MOCK_ANSWERS)


# The reason for these 2 functions is to allow the answer data to change,
# but still allow the tests to pass as long as the Best class works correctly.
# Assuming the format of the answer data does not change,
# if it does the tests should be updated to reflect this.
def setup_function(_):
    # Mock answers
    best.answers = MOCK_ANSWERS


def teardown_function(_):
    # Restore answers
    best.answers = normal_answers


def test_static():
    assert best.static == "static"


def test_list():
    assert best.list in ["a", "b", "c"]


def test_method():
    mock_method.reset_mock()

    assert best.method == "result"
    mock_method.assert_called_once()
