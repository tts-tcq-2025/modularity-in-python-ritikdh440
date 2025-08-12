from color_coder import get_color_from_pair_number, get_pair_number_from_color

def run_tests():
    """Executes all test cases and prints a success message."""
    
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_number_to_pair(25, 'Violet', 'Slate')

    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Red', 'Orange', 7)
    test_pair_to_number('Violet', 'Slate', 25)
    
    print("All tests passed!\n")

def test_number_to_pair(pair_number, expected_major, expected_minor):
    """Tests the conversion from a pair number to colors."""
    major, minor = get_color_from_pair_number(pair_number)
    assert major == expected_major
    assert minor == expected_minor

def test_pair_to_number(major, minor, expected_pair_number):
    """Tests the conversion from a color pair to its number."""
    pair_number = get_pair_number_from_color(major, minor)
    assert pair_number == expected_pair_number
