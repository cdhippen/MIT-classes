class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except ValueError:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, x):
        """Returns a new intSet method that returns a new intSet
        containing elements in both sets."""
        newSet = intSet()
        for i in self.vals:
            if i in x.vals:
                newSet.insert(i)
        return newSet

    def __len__(self):
        """Returns the number of elements in s"""
        return len(self.vals)


s1 = intSet()

s1.insert(1)
s1.insert(2)
s1.insert(3)

s2 = intSet()

s2.insert(4)
s2.insert(5)
s2.insert(6)
s2.insert(3)

print(s2)
print(s1)
print(len(s1))
print(s1.intersect(s2))


list1 = [1, 2, 3, 4, 5, 6]

[print(i) for i in list1]
