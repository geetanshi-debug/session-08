import unittest
from discount import discount_rate, final_price

class TestDiscount(unittest.TestCase):
    def test_negative_total(self):
        with self.assertRaises(ValueError):
            discount_rate(-1)

    def test_discount_boundaries(self):
        self.assertEqual(discount_rate(49.99), 0.00)
        self.assertEqual(discount_rate(50), 0.05)
        self.assertEqual(discount_rate(99.99), 0.05)
        self.assertEqual(discount_rate(100), 0.10)
        self.assertEqual(discount_rate(199.99), 0.10)
        self.assertEqual(discount_rate(200), 0.15)

    def test_vip_bonus(self):
        self.assertEqual(discount_rate(100, True), 0.15)

    def test_cap(self):
        self.assertEqual(discount_rate(200, True), 0.20)

    def test_final_price(self):
        self.assertAlmostEqual(final_price(100), 90.0)
        self.assertAlmostEqual(final_price(100, True), 85.0)

    def test_small_order(self):
        self.assertAlmostEqual(final_price(25), 25.0)

if __name__ == "__main__":
    unittest.main()
