class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute
        # directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # Returns True if coordinates refer to the same point
        return (self.x == Coordinate.getX(other)
                and self.y == Coordinate.getY(other))

    def __repr__(self):
        # Returns a string that looks like a valid Python expression that
        # could be used to recreate an object with the same value
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'


other = Coordinate(5, 1)
other2 = Coordinate(6, 1)
other3 = Coordinate(4, 2)
other4 = Coordinate(5, 2)

print(Coordinate(5, 1) == other)  # True
print(Coordinate(5, 1) == other2)  # False
print(Coordinate(5, 1) == other3)  # False
print(Coordinate(5, 1) == other4)  # False
print(Coordinate(5, 1) == Coordinate(5, 1))  # True
print(Coordinate(5, 1) == Coordinate(6, 2))  # False
print(repr(Coordinate(5, 1)))
