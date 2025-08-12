from color_map import MAJOR_COLORS, MINOR_COLORS

TOTAL_PAIRS = len(MAJOR_COLORS) * len(MINOR_COLORS)


def get_pair_number_from_color(major_color, minor_color):

    try:
        major_index = MAJOR_COLORS.index(major_color)
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError as e:
        raise ValueError("Invalid color name provided.") from e
    
    return major_index * len(MINOR_COLORS) + minor_index + 1


def get_color_from_pair_number(pair_number):
 
    if not 1 <= pair_number <= TOTAL_PAIRS:
        raise ValueError(f"Pair number must be between 1 and {TOTAL_PAIRS}.")

    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
