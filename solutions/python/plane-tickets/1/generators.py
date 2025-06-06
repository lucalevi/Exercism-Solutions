"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % len(letters)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats_generated = 0
    row = 1
    while seats_generated < number:
        if row == 13:
            row += 1
            continue

        for letter_index in range(4):
            if seats_generated >= number:
                break

            seat_letter_generator = generate_seat_letters(1)
            seat_letter = next(seat_letter_generator)

            letters = ["A", "B", "C", "D"]
            current_seat_letter = letters[letter_index]

            yield f"{row}{current_seat_letter}"
            seats_generated += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    num_passengers = len(passengers)

    seat_generator = generate_seats(num_passengers)

    return {passenger: next(seat_generator) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        id = seat_number + flight_id
        num_zeros = 12 - len(id)
        yield id + ("0" * num_zeros)
