import os
import pytest
from dictionary import get_word_definition

@pytest.mark.parametrize("word", ['hello', 'world', 'python', 'computer', 'definition'])
def test_output_type(word):
    """Test that get_word_definition() returns a valid string as an output"""
    output = get_word_definition(word)
    assert isinstance(output, str), f"Output for '{word}' should be a string"
    assert len(output) >= 5, f"Output for '{word}' should be at least 5 characters long"


def test_get_word_definition():
    assert get_word_definition("python") == "pī-ˌthän (noun): any of various large constricting snakes; especially"
    assert get_word_definition("frth") == "This word definition doesn't exist in this dictionary"
    assert get_word_definition("") == "An Exception occured!!"
    assert get_word_definition(123) == "This word definition doesn't exist in this dictionary"