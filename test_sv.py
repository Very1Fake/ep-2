from utils import get_tau
import unittest


class SecondVariantTests(unittest.TestCase):
    def test_get_tau(self):
        cases = [[1, 2],[3, 4],[5, 6],[7, 8],[9, 10]]

        answers = [(-0.69315, -0.69315),
	               (-4.15887, -1.38629),
	               (-8.95880, -1.79176),
	               (-14.55608, -2.07944),
	               (-20.72331, -2.30259)]

        for i in range(0, len(cases), 1):
            self.assertEqual(get_tau(*cases[i]), answers[i])


if __name__ == '__main__':
    unittest.main()