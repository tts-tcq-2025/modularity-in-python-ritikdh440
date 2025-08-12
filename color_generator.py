from color_coder import get_color_from_pair_number

def print_reference_manual():
    """
    Formats and prints a reference manual of the 25-pair color code.
    """
    print("--- 25-Pair Color Code Reference Manual ---")
    print("{:<12} | {:<12} | {:<12}".format("Pair Number", "Major Color", "Minor Color"))
    print("-" * 40)
    
    for i in range(1, 26):
        major, minor = get_color_from_pair_number(i)
        print("{:<12} | {:<12} | {:<12}".format(i, major, minor))
    print("-" * 40)
