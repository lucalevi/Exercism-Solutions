def isTriangle(sides):
    a, b, c = sorted(sides)

    # All sides must be greater than 0
    if not (a > 0 and b > 0 and c > 0):
        return False

    # The sum of the lengths of any two sides must be greater than or equal to the length of the third side.
    # With sorted sides, only one check is necessary: the two smallest must be >= the largest.
    if not (a + b >= c):
        return False

    return True


def equilateral(sides):
    if not isTriangle(sides):
        return False
    # If it's a valid triangle, check if all sides are equal.
    # We can use any two sides for comparison since it's a valid triangle.
    return sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides):
    if not isTriangle(sides):
        return False
    # An isosceles triangle has at least two sides the same length.
    # It must NOT be scalene.
    # It includes equilateral triangles as per the problem definition.
    # So, if it's a valid triangle and not scalene, it must be isosceles (or equilateral).
    return (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    if not isTriangle(sides):
        return False
    # A scalene triangle has all sides of different lengths.
    # It must NOT be equilateral, and it must NOT be isosceles.
    return not (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])
    