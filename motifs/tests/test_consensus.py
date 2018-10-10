import unittest

from motifs.consensus import consensus
from motifs.count_matrix import get_count


class TestCount(unittest.TestCase):
    def test_consensus(self):
        motifs = [
            'AACGTA',
            'CCCGTT',
            'CACCTT',
            'GGATTA',
            'TTCCGG',
        ]
        expected = 'CACCTA'

        count_matrix = get_count(motifs)
        cons_string = consensus(count_matrix)
        self.assertEqual(expected, cons_string)
