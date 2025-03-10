from foo_bar_baz import foo_bar_baz

#Add testcases Here

def test_empty_sequence():
    """Test when n is 0 (edge case)."""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(0) == ""

def test_single_number():
    """Test when n is 1 (edge case)."""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(1) == "1"

def test_sequence_with_foo():
    """Test when there is just foo."""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(3) == "1 2 Foo"

def test_small_sequence():
    """Test a small sequence with foo and bar """
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(7) == "1 2 Foo 4 Bar Foo 7"

def test_sequence_with_baz():
    """Test sequence with foo, bar, and baz"""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_negative_input():
    """Test handling of negative input."""
    from foo_bar_baz import foo_bar_baz
    assert foo_bar_baz(-5) == "" # if i < n, don't return

def test_large_sequence():
    """Test large  sequence."""
    from foo_bar_baz import foo_bar_baz
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"
    assert foo_bar_baz(20) == expected

def test_multiple_baz_occurrences():
    """Test a sequence with multiple Baz"""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(30)
    # for 30, there should be two "Baz" so we need to test that
    assert "Baz" in result
    assert result.count("Baz") == 2  # At 15 and 30

def test_output_format():
    """Test that the output is correctly formatted."""
    result = foo_bar_baz(10)
    # check that there are no double spaces
    assert "  " not in result
    # check that it starts and ends correctly (no leading/trailing spaces)
    assert not result.startswith(" ")
    assert not result.endswith(" ")

def test_foo_replacement():
    """Test foo replacement."""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(12).split()
    assert result[2] == "Foo"  # 3rd element (index 2) should be "Foo" for number 3
    assert result[5] == "Foo"  # 6th element (index 5) should be "Foo" for number 6
    assert result[8] == "Foo"  # 9th element (index 8) should be "Foo" for number 9
    assert result[11] == "Foo"  # 12th element (index 11) should be "Foo" for number 12

def test_bar_replacement():
    """Test bar replacement."""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(20).split()
    assert result[4] == "Bar"  # 5th element (index 4) should be "Bar" for number 5
    assert result[9] == "Bar"  # 10th element (index 9) should be "Bar" for number 10
    assert result[19] == "Bar"  # 20th element (index 19) should be "Bar" for number 20

def test_baz_replacement():
    """Test baz replacement."""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(30).split()
    assert result[14] == "Baz"  # 15th element (index 14) should be "Baz" for number 15
    assert result[29] == "Baz"  # 30th element (index 29) should be "Baz" for number 30

def test_non_replaced_numbers():
    """Make sure other numbers are not replaced."""
    from foo_bar_baz import foo_bar_baz
    result = foo_bar_baz(7).split()
    assert result[0] == "1"
    assert result[1] == "2"
    assert result[3] == "4"
    assert result[6] == "7"