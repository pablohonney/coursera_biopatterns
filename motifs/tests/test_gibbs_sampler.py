import unittest

from motifs.gibbs_sampler import repeated_gibbs_sampler


class TestGibbsSampler(unittest.TestCase):
    def test_0(self):
        dna = [
            "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
            "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
            "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
            "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
            "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
        ]
        k = 8
        t = len(dna)
        n = 100
        expected = [
            "AACGGCCA",
            "AAGTGCCA",
            "TAGTACCG",
            "AAGTTTCA",
            "ACGTGCAA",
        ]

        result = repeated_gibbs_sampler(dna, k, t, n)
        self.assertEqual(expected, result)
