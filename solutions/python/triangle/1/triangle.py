def isTriangle(sides):
    if ((sides[0] + sides[1]) >= sides[2]) and ((sides[1] + sides[2]) >= sides[0]) and ((sides[0] + sides[2]) >= sides[1]) and ((sides[0] != 0) or (sides[1] != 0) or (sides[2] != 0)):
        return True

    return False


def equilateral(sides):
    if isTriangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if isTriangle(sides):
        return (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])
    return False

def scalene(sides):
    if isTriangle(sides):
        return (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2])
    return False
