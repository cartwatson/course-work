import unittest
import Mandelbrot


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    def test_getColor(self):
        mbrot = Mandelbrot.Mandelbrot()
        self.assertEqual(mbrot.getColor(complex(0, 0)), '#002277')
        self.assertEqual(mbrot.getColor(complex(-0.751, 1.1075)), '#ffe7ae')
        self.assertEqual(mbrot.getColor(complex(-0.2, 1.1075)), '#fff797')
        self.assertEqual(mbrot.getColor(complex(-0.75, 0.1075)), '#95ff51')
        self.assertEqual(mbrot.getColor(complex(-0.748, 0.1075)), '#00f970')
        self.assertEqual(mbrot.getColor(complex(-0.7562500000000001, 0.078125)), '#51ff36')
        self.assertEqual(mbrot.getColor(complex(-0.7562500000000001, -0.234375)), '#fcff8d')
        self.assertEqual(mbrot.getColor(complex(0.3374999999999999, -0.625)), '#fffb94')
        self.assertEqual(mbrot.getColor(complex(-0.6781250000000001, -0.46875)), '#9dff54')
        self.assertEqual(mbrot.getColor(complex(0.4937499999999999, -0.234375)), '#ffeaa8')
        self.assertEqual(mbrot.getColor(complex(0.3374999999999999, 0.546875)), '#ccff6c')


if __name__ == '__main__':
    unittest.main()
