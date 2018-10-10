import unittest

from motifs.consensus import consensus
from motifs.score import score
from motifs.count_matrix import get_count


class TestCount(unittest.TestCase):
    def test_score(self):
        motifs = [
            'AACGTA',
            'CCCGTT',
            'CACCTT',
            'GGATTA',
            'TTCCGG',
        ]
        expected = 14

        count = get_count(motifs)
        cons = consensus(count)
        sc = score(motifs, cons)
        self.assertEqual(expected, sc)
