from unittest import main, TestCase

def square(x):
    return x ** 2

class TestSquare(TestCase):
    def test_if_returns_square_of_2(self):
        result = square(2)
        expected = 4

        self.assertEqual(result, expected)

    # simulando um erro
    def test_if_returns_square_of_4(self):
        result = square(4)
        expected = 16 # 4 modificado

        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
