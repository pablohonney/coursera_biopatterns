import unittest

from motifs.count_matrix import get_count


class TestCount(unittest.TestCase):
    def test_count(self):
        motifs = [
            'AACGTA',
            'CCCGTT',
            'CACCTT',
            'GGATTA',
            'TTCCGG',
        ]
        expected = {
            'A': [1, 2, 1, 0, 0, 2],
            'C': [2, 1, 4, 2, 0, 0],
            'G': [1, 1, 0, 2, 1, 1],
            'T': [1, 1, 0, 1, 4, 2]
        }

        count_matrix = get_count(motifs)
        self.assertEqual(expected, count_matrix)
