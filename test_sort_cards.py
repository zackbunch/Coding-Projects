import unittest
from sort_cards import sortCards

class TestCardSort(unittest.TestCase):

    # Test cards are properly sorted
    def test_valid_sort(self):
        unsorted =  ["3c", "Js", "2d", "10h", "Kh", "8s", "Ac", "4h", "Qh", "Qc"]
        sorted_cards = ['2d', '8s', 'Js', '3c', 'Qc', 'Ac', '4h', '10h', 'Qh', 'Kh']
        self.assertEqual(sortCards(unsorted), sorted_cards)

    # Test that the function returns a Key error if card rank is not valid rank (1-10)
    # Raises KeyError if rank is out of range
    def test_invalid_rank(self):
        unsorted =  ["3c", "Js", "2d", "110h", "Kh", "8s", "Ac", "4h", "Qh", "Qc"]
        with self.assertRaises(KeyError) as context:
            sortCards(unsorted)

    # Test that an invalid rank returns a KeyError
    # Rank is only valid if equal to d,s,c,h
    def test_invalid_suit(self):
        unsorted = ["3c", "JJ", "2d", "110h", "Kh", "8s", "AC", "4h", "Qh", "Qc"]
        with self.assertRaises(KeyError) as context:
            sortCards(unsorted)

    # Test Edge case would be if a suit is capitalized, function will raise KeyError
    def test_lower_case_rank(self):
        unsorted = ["3C", "JS", "2d", "10h", "Kh", "8s", "Ac", "4h", "Qh", "Qc"]
        with self.assertRaises(KeyError) as context:
            sortCards(unsorted)

if __name__ == '__main__':
    unittest.main()