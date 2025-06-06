def response(hey_bob):
    # 1. Always strip whitespace first
    hey_bob = hey_bob.strip()

    # Determine characteristics of the input
    is_question = hey_bob.endswith('?')
    is_yelling = hey_bob.isupper() and any(c.isalpha() for c in hey_bob) # Check for actual letters, not just symbols/numbers
    is_silent = not hey_bob # True if hey_bob is an empty string

    if is_silent:
        return "Fine. Be that way!"
    elif is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."