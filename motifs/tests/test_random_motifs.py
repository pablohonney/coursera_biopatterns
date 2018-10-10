import unittest

from motifs.random_motifs import random_motifs


class TestRandomMotifs(unittest.TestCase):
    def test_0(self):
        dna = [
            "TTACCTTAAC",
            "GATGTCTGTC",
            "ACGGCGTTAG",
            "CCCTAACGAG",
            "CGTCAGAGGT",
        ]
        k = 3
        t = len(dna)
        expected = [
            "TTA",
            "ATG",
            "GGC",
            "GAG",
            "CGT",
        ]
        result = random_motifs(dna, k, t)
        print(result)
        # self.assertEqual(expected, result)  # random, connot check
