# Tests the NumberSet Class

import unittest
import NumberSet


class TestNumberSet(unittest.TestCase):
    def setUp(self):
        self.numberSet = NumberSet.NumberSet(18)
        self.numberSet1 = NumberSet.NumberSet(0)

    def test_getSize(self):
        self.assertIsNotNone(self.numberSet)
        self.assertIsNotNone(self.numberSet1)
        self.assertEqual(self.numberSet.getSize(), 18)
        self.assertEqual(self.numberSet1.getSize(), 0)

    def test_get(self):
        self.assertEqual(self.numberSet.get(0), 1)
        self.assertEqual(self.numberSet.get(17), 18)
        self.assertIsNone(self.numberSet1.get(0))

    def test_getNext(self):
        for i in range(1, 19):
            self.assertEqual(self.numberSet.getNext(), i)
        self.assertIsNone(self.numberSet1.getNext())


if __name__ == '__main__':
    unittest.main()
