import unittest
from calculator import suma


class TestCalculator(unittest.TestCase):

    def test_suma_correcta(self):
        self.assertEqual(suma(1, 2, 2), 5)

    def test_suma_falla(self):
        # Este test está diseñado para FALLAR
        self.assertEqual(suma(2, 2, 1), 6)


if __name__ == "__main__":
    unittest.main()
