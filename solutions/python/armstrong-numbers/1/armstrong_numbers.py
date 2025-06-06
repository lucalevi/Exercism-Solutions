def is_armstrong_number(number):
    number_string = str(number)
    number_length = len(number_string)
    return number == sum(int(digit) ** number_length for digit in number_string)
    