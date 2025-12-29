# test_calculator.py
import unittest
from calculator import suma


class TestCalculator(unittest.TestCase):

    def test_suma_correcta(self):
        self.assertEqual(suma(1, 2, 2), 5)

    def test_suma_correcta_otro_caso(self):
        self.assertEqual(suma(2, 2, 1), 5)

    def test_suma_con_float(self):
        self.assertAlmostEqual(suma(1.5, 2.0, 0.5), 4.0)

    def test_suma_lanza_typeerror_si_no_es_numero(self):
        with self.assertRaises(TypeError):
            suma("1", 2, 3)

        with self.assertRaises(TypeError):
            suma(1, None, 3)


if __name__ == "__main__":
    unittest.main()
