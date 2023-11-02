def letter_to_number(letter):
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A')
    elif 'a' <= letter <= 'z':
        return ord(letter) - ord('a')
    elif '0' <= letter <= '9':
        return ord(letter) - ord('0') + 26
    else:
        return ord(letter) - ord('A') + 36

def transform_text(plain_text):
    # Create a list with a filler 'x' between empty spaces
    result = []
    is_previous_space = False  # Flag to track if the previous character was a space

    for letter in plain_text:
        if letter.isspace():
            if not is_previous_space:
                result.append('x')  # Add a filler 'x' between empty spaces
            is_previous_space = True
        else:
            result.append(letter)
            is_previous_space = False

    # Convert to numbers using the custom mapping
    numbers = [letter_to_number(letter) for letter in result]
    return numbers

def denormalize_and_convert_back(reproduced_values):
    def number_to_letter(number):
        if 0 <= number <= 25:
            return chr(number + ord('A'))
        elif 26 <= number <= 35:
            return chr(number - 26 + ord('0'))
        elif 36 <= number <= 61:
            return chr(number - 36 + ord('a'))
        else:
            return 'x'  # Filler for spaces

    denormalized_text = [number_to_letter(int(round(value * 61)) if value < 1 else 61) for value in reproduced_values]
    return ''.join(denormalized_text)