COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def label(colors):
    first_two = colors[:2]
    ohms = [str(COLORS.index(color)) for color in first_two]
    if ohms[0] == "0":
        ohms = ohms[1:]

    if all(digit == "0" for digit in ohms):
        ohms = ["0"]

    zeros = list(COLORS.index(colors[2]) * "0")
    ohms += zeros

    counter = 0
    for i in reversed(ohms):
        if i == "0":
            counter += 1
        if i != "0":
            break

    prefix = ""

    if counter >= 9:
        prefix = "giga"
        ohms = ohms[:len(ohms)-9]
    elif counter >= 6:
        prefix = "mega"
        ohms = ohms[:len(ohms)-6]
    elif counter >= 3:
        prefix = "kilo"
        ohms = ohms[:len(ohms)-3]

    if prefix:
        return "".join(ohms) + " " + prefix + "ohms"
        
    return "".join(ohms) + " ohms"
    
