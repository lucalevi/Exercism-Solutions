def commands(binary_str):
    secret_shake = []

    for i, digit in enumerate(reversed(binary_str)):
        if digit == "1":
            if i == 0:
                secret_shake.append("wink")
            if i == 1:
                secret_shake.append("double blink")
            if i == 2:
                secret_shake.append("close your eyes")
            if i == 3:
                secret_shake.append("jump")
            if i == 4:
                secret_shake = secret_shake[::-1]

    return secret_shake
