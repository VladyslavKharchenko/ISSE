import unittest


class NaturalNumber(object):

    def __init__(self, n):
        if isinstance(n, int) and (n > 0):
            self.n = n
        else:
            raise ValueError('Only natural numbers are allowed')


class DigitalRoot(NaturalNumber):

    def __init__(self, n):
        super(DigitalRoot, self).__init__(n)

    def builtins(self):
        n = self.n
        while n >= 10:
            n = sum([int(e) for e in str(n)])
        return n

    def congruence(self):  # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        return (self.n - 1) % 9 + 1

    def by_digit(self):
        n = self.n
        while len(str(n)) > 1:
            n = sum([int(e) for e in str(n)])
        return n


class TestDigitalRoot(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = {
            1: 1,
            16: 7,
            942: 6,
            2352: 3,
            132189: 6,
            493193: 2,
            999999: 9,
            257520643: 7
        }

    def test_builtins(self):
        for number in self.test_data:
            dr = DigitalRoot(number)
            self.assertEqual(dr.builtins(), self.test_data[number])

    def test_congruence(self):
        for number in self.test_data:
            dr = DigitalRoot(number)
            self.assertEqual(dr.congruence(), self.test_data[number])

    def test_by_digit(self):
        for number in self.test_data:
            dr = DigitalRoot(number)
            self.assertEqual(dr.by_digit(), self.test_data[number])


if __name__ == '__main__':
    unittest.main()

    # number = int(input('Enter a natural number to calculate digital root: '))
    # d = DigitalRoot(number)
    # print(d.congruence(), d.builtins(), d.by_digit())
