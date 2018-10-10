import unittest

from motifs.profile_matrix import get_profile
from motifs.count_matrix import get_count


class TestCount(unittest.TestCase):
    def test_profile(self):
        motifs = [
            'AACGTA',
            'CCCGTT',
            'CACCTT',
            'GGATTA',
            'TTCCGG',
        ]
        expected = {
            'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4],
            'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0],
            'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2],
            'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]
        }

        profile = get_profile(get_count(motifs))
        self.assertEqual(profile, expected)
