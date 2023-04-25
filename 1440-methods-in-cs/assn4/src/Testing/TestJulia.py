import unittest
import Julia
import FractalInformation


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestJulia(unittest.TestCase):
    def test_getColor(self):
        julia = Julia.Julia()
        self.assertEqual(julia.getColor(complex(0, 0)), '#002277')
        self.assertEqual(julia.getColor(complex(-0.751, 1.1075)), '#ffe4b5')
        self.assertEqual(julia.getColor(complex(-0.2, 1.1075)), '#ffe4b5')
        self.assertEqual(julia.getColor(complex(-0.75, 0.1075)), '#002277')
        self.assertEqual(julia.getColor(complex(-0.748, 0.1075)), '#002277')
        self.assertEqual(julia.getColor(complex(-0.7562500000000001, 0.078125)), '#002277')
        self.assertEqual(julia.getColor(complex(-0.7562500000000001, -0.234375)), '#ffeda4')
        self.assertEqual(julia.getColor(complex(0.3374999999999999, -0.625)), '#ffe7ae')
        self.assertEqual(julia.getColor(complex(-0.6781250000000001, -0.46875)), '#ffe7ae')
        self.assertEqual(julia.getColor(complex(0.4937499999999999, -0.234375)), '#fff797')
        self.assertEqual(julia.getColor(complex(0.3374999999999999, 0.546875)), '#ffe9ab')

    def test_dictionaryGetter(self):
        self.assertEqual('absent' in FractalInformation.julia_images, False)
        self.assertEqual('fulljulia' in FractalInformation.julia_images, True)
        self.assertEqual('' in FractalInformation.julia_images, False)
        self.assertEqual('lakes' in FractalInformation.julia_images, True)
        self.assertEqual('Still Not In Here' in FractalInformation.julia_images, False)
        self.assertEqual('hourglass' in FractalInformation.julia_images, True)


if __name__ == '__main__':
    unittest.main()
