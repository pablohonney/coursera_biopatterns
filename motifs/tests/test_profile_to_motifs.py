import unittest

from motifs.profile_to_motifs import profile_to_motifs


class TestProfileToMatrix(unittest.TestCase):
    def test_0(self):
        profile = {
            'A': [0.8, 0.0, 0.0, 0.2],
            'C': [0.0, 0.6, 0.2, 0.0],
            'G': [0.2, 0.2, 0.8, 0.0],
            'T': [0.0, 0.2, 0.0, 0.8],
        }
        dna = [
            "TTACCTTAAC",
            "GATGTCTGTC",
            "ACGGCGTTAG",
            "CCCTAACGAG",
            "CGTCAGAGGT",
        ]
        expected = [
            "ACCT",
            "ATGT",
            "GCGT",
            "ACGA",
            "AGGT",
        ]
        result = profile_to_motifs(profile, dna)
        self.assertEqual(expected, result)

    def test_1(self):
        profile = {
            "A": [.5, .0, .2, .2],
            "C": [.3, .6, .2, .0],
            "G": [.2, .2, .6, .0],
            "T": [.0, .2, .0, .8],
        }
        dna = [
            "TTACCTTAAC",
            "GATGTCTGTC",
            "ACGGCGTTAG",
            "CCCTAACGAG",
            "CGTCAGAGGT",
        ]
        expected = [
            "ACCT",
            "ATGT",
            "GCGT",
            "ACGA",
            "AGGT",
        ]
        result = profile_to_motifs(profile, dna)
        self.assertEqual(expected, result)
