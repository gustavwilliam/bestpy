from collections import abc
from unittest.mock import Mock
import pytest
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
    best._answers = MOCK_ANSWERS


def teardown_function(_):
    # Restore answers
    best._answers = normal_answers


def test_static():
    assert best.static == "static"


def test_list():
    assert best.list in ["a", "b", "c"]


def test_method():
    mock_method.reset_mock()

    assert best.method == "result"
    mock_method.assert_called_once()


def test_validate_answers():
    """Checks if the normal answers produce errors."""
    best._answers = normal_answers

    for key, real_answer in normal_answers.items():
        answer = getattr(best, key)

        if isinstance(real_answer, abc.Sequence):
            assert answer in real_answer
        elif callable(real_answer):
            pass  # Not sure how to automatically validate the responses of callables
        else:
            assert answer == real_answer


def test_invalid_attribute():
    """Checks if invalid attributes raise `AttributeError`."""
    with pytest.raises(AttributeError):
        _ = best._this_attribute_does_not_exist
