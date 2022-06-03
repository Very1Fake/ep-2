import unittest
from parsers import parse_sv_tv


class ThirdVariantTests(unittest.TestCase):
    def test_logic(self):
        good_cases = [
            ('0.5', '0.1', '0.01'),
            ('1', '1', '1'),
            ('2', '0.5', '0.1'),
        ]

        for (t1, t2, a) in good_cases:
            self.assertIsInstance(parse_sv_tv(t1, t2, a), tuple)
        
        bad_cases = [
            ('0.4', '0.01', '0.001'),
            ('a', 'a', '1'),
            ('a', '1', 'a'),
            ('1', 'a', 'a'),
        ]

        for (t1, t2, a) in bad_cases:
            self.assertIsInstance(parse_sv_tv(t1, t2, a), str)
