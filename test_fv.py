import unittest
from utils import checkMonteKarloTable, getQuantityOfListElements


class TestFirstVar(unittest.TestCase):

    def test_getQuantityOfListElements(self):
        list1 = [1, 2, 3, 4, 5, 6]
        list2 = [[123, 9], 345]
        list3 = [[], [1, 2], 3]
        list4 = [[], []]
        list5 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

        answers = [6, 3, 3, 0, 9]
        lists = [list1, list2, list3, list4, list5]
        for i in range[0, len(lists), 1]:
            self.assertEqual(getQuantityOfListElements(lists[i]), answers[i])

    def test_checkMonteKarloTableFalse(self):
        list1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        list2 = [[1, 2, 3], [9, 10]]
        list3 = [[1, 45], [1, 2], 3]
        list4 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
        list5 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]

        lists = [list1, list2, list3, list4, list5]
        strNums = [3, 3, 4, 5, 3]
        for i in range(0, len(lists), 1):
            self.assertFalse(checkMonteKarloTable(lists[i], strNums[i]))

    def test_checkMonteKarloTableTrue(self):
        list1 = [[1, 'First<br>Second', 0.1955, 0.4192, 0.4139, '<br>0.6218', '<br>0.9072', '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [2, 'First<br>Second', 0.9588, 0.1126, 0.6397, '<br>0.2526', '<br>0.4972',
                     '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [None, None, None, None, None, None, '(stop)', None, None, 'P<sub>1</sub> = 1', 'P<sub>2</sub> = 1', 'P = 1', 'P* = 1.0', '|P-P*| = 0.0']]
        list2 = [[1, 'First<br>Second', 0.1173, 0.7633, 0.9326, '<br>0.6759', '<br>0.1079', '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [2, 'First<br>Second', 0.5798, 0.4849, 0.4461, '<br>0.1944', '<br>0.6787',
                     '-<br>', '+<br>', '+<br>', '<br>+', '<br>-', '+<br>+', '+'],
                 [3, 'First<br>Second', 0.3681, 0.1053, 0.0095, '<br>0.7844', '<br>0.4815',
                     '-<br>', '+<br>', '+<br>', '<br>+', '<br>-', '+<br>+', '+'],
                 [None, None, None, None, None, None, '(stop)', None, None, 'P<sub>1</sub> = 1.0', 'P<sub>2</sub> = 0.96', 'P = 0.96', 'P* = 1.0', '|P-P*| = 0.04']]
        list3 = [[1, 'First<br>Second', 0.9481, 0.6329, 0.373, '<br>0.2762', '<br>0.7689', '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [2, 'First<br>Second', 0.1962, 0.1621, 0.5811, '<br>0.7181', '<br>0.3765',
                     '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [3, 'First<br>Second', 0.814, 0.8684, 0.4098, '<br>0.4353', '<br>0.1952',
                     '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [4, 'First<br>Second', 0.7403, 0.4122, 0.0396, '<br>0.7105', '<br>0.9071',
                     '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [None, None, None, None, None, None, '(stop)', None, None, 'P<sub>1</sub> = 1', 'P<sub>2</sub> = 1', 'P = 1', 'P* = 1.0', '|P-P*| = 0.0']]
        list4 = [[1, 'First<br>Second', 0.1704, 0.4947, 0.8383, '<br>0.0303', '<br>0.0129', '+<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [2, 'First<br>Second', 0.7988, 0.4824, 0.8798, '<br>0.8099', '<br>0.8371',
                     '-<br>', '+<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [3, 'First<br>Second', 0.2739, 0.7275, 0.4371, '<br>0.7224', '<br>0.0331',
                     '+<br>', '-<br>', '+<br>', '<br>+', '<br>+', '+<br>+', '+'],
                 [None, None, None, None, None, None, '(stop)', None, None, 'P<sub>1</sub> = 1.0', 'P<sub>2</sub> = 1', 'P = 1.0', 'P* = 1.0', '|P-P*| = 0.0']]
        list5 = [[1, 'First<br>Second', 0.0498, 0.4063, 0.3043, '<br>0.6227', '<br>0.3959', '+<br>', '-<br>', '+<br>', '<br>-', '<br>+', '+<br>+', '+'],
                 [None, None, None, None, None, None, '(stop)', None, None, 'P<sub>1</sub> = 1.0', 'P<sub>2</sub> = 0.88', 'P = 0.88', 'P* = 1.0', '|P-P*| = 0.12']]

        lists = [list1, list2, list3, list4, list5]
        strNums = [3, 4, 5, 4, 2]
        for i in range(0, len(lists), 1):
            self.assertTrue(checkMonteKarloTable(lists[i], strNums[i]))


if __name__ == '__main__':
    unittest.main()
