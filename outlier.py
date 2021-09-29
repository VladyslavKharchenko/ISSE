import unittest


def find_outlier(input_l: list):
    evens = list(filter(lambda x: x % 2 == 0, input_l))
    if len(evens) > 1:  # Looking for an odd
        for num in evens:  # Remove all even numbers until only one odd number left
            input_l.remove(num)
        return input_l.pop()
    else:  # We're lucky, it's even
        return evens.pop()


class TestOutlierLambda(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [
            [2, 4, 0, 100, 4, 11, 2602, 36],
            [160, 3, 1719, 19, 11, 13, -21]
        ]
        self.correct = [11, 160]

    def test_find_outlier(self):
        for idx, lst in enumerate(self.test_data):
            self.assertEqual(find_outlier(lst), self.correct[idx])


if __name__ == '__main__':
    unittest.main()
