import pytest

from foo_bar_baz import foo_bar_baz

# Insert test cases here

# ADD IN MESSAGES SO WE KNOW WHICH TEST IS RUNNING
# Import foo_bar_baz every single time so tests can be individual

# testing empty case so n is 0
def test_empty_sequence():
    """Test 1: n = 0 (edge case)"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(0) == ""

# testing single number so n is 1
def test_single_number():
    """Test 2: n = 1 (edge case)"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(1) == "1"

# testing foo function
def test_sequence_with_foo():
    """Test 3: sequence with just foo"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(4) == "1 2 Foo 4"

# testing bar function
def test_small_sequence():
    """Test 4: small sequence with foo and bar"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"

# testing baz sequence
def test_sequence_with_baz():
    """Test 5: sequence, at least ONE baz"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

# testing negative input
def test_negative_input():
    """Test 6: negative input"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(-5) == "" # i < n so this won't work

# testing multiple baz occurreneces
def test_multiple_baz_occurrences():
    """Test 7: sequence with multiple 'Baz' occurrences"""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(30) 
    # for sequence of 30, there should be two "Baz", 15 and 30
    assert "Baz" in result
    assert result.count("Baz") == 2  # this will check that

# test to make sure format is correct
def test_output_format():
    """Test 8: output is correctly formatted with single spaces"""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(10)
    # check that there are no double spaces
    assert "  " not in result
    # check that it starts and ends correctly (no leading/trailing spaces)
    assert not result.startswith(" ")
    assert not result.endswith(" ")