from color_coder import get_color_from_pair_number, get_pair_number_from_color

def print_reference_manual():
    """
    Formats and prints a reference manual of the 25-pair color code.
    The output is a table mapping pair numbers to their color combinations.
    """
    print("--- 25-Pair Color Code Reference Manual ---")
    print("{:<12} | {:<12} | {:<12}".format("Pair Number", "Major Color", "Minor Color"))
    print("-" * 40)
    
    for i in range(1, 26):
        major, minor = get_color_from_pair_number(i)
        print("{:<12} | {:<12} | {:<12}".format(i, major, minor))
    print("-" * 40)


def test_number_to_pair(pair_number, expected_major, expected_minor):
    """Tests the conversion from a pair number to colors."""
    major, minor = get_color_from_pair_number(pair_number)
    assert major == expected_major
    assert minor == expected_minor


def test_pair_to_number(major, minor, expected_pair_number):
    """Tests the conversion from a color pair to its number."""
    pair_number = get_pair_number_from_color(major, minor)
    assert pair_number == expected_pair_number


if __name__ == '__main__':
    # --- Run Tests ---
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print("All tests passed!\n")

    print_reference_manual()
