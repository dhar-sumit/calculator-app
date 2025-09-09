import unittest
from calc import add, subtract, multiply, divide, modulus, power

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(1, 999), 1000)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(20, 10), 10)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(7, 6), 42)
        self.assertEqual(multiply(1, 100), 100)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 3), 2.3333333333, places=7)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(20, 5), 0)
        self.assertEqual(modulus(7, 7), 0)
        with self.assertRaises(ZeroDivisionError):
            modulus(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(7, 1), 7)
        self.assertEqual(power(10, 2), 100)

if __name__ == '__main__':
    unittest.main()
