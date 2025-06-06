def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    
    # The number of grains on a given square 'n' is 2^(n-1)
    return 2**(number - 1)


def total():
    # The total number of grains on a chessboard (64 squares)
    # is the sum of a geometric series: 2^0 + 2^1 + ... + 2^63
    # This sum simplifies to 2^64 - 1
    return 2**64 - 1