import unittest
from main import reverse

class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_onesymb(self):
        self.assertEqual(reverse('a'), 'a')

    def test_polide(self):
        self.assertEqual(reverse('ada'), 'ada')

    def test_notpolide(self):
        self.assertEqual(reverse('adc'), 'cda')

    def test_wrong_type1(self):
        with self.assertRaises(TypeError):
            reverse([1, 5, 7])

if __name__ == '__main__':
     unittest.main()
