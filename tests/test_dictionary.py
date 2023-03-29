import os
import pytest
from dictionary import get_word_definition


@pytest.mark.parametrize("word", ['hello', 'world', 'python', 'computer', 'definition'])
def test_output_type(word):
    """Test that get_word_definition() returns a valid string as an output"""
    output = get_word_definition(word)
    assert isinstance(output, str), f"Output for '{word}' should be a string"
    assert len(output) >= 5, f"Output for '{word}' should be at least 5 characters long"


