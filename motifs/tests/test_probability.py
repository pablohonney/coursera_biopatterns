import unittest

from motifs.probability import probability
from motifs.probability import profile_most_probable_pattern


class TestProbability(unittest.TestCase):
    def setUp(self):
        self.profile = {
            'A': [.2, .2, 0, 0, 0, 0, .9, .1, .1, .1, .3, 0],
            'C': [.1, .6, 0, 0, 0, 0, 0, .4, .1, .2, .4, .6],
            'G': [0, 0, 1, 1, .9, .9, .1, 0, 0, 0, 0, 0],
            'T': [.7, .2, 0, 0, .1, .1, 0, .5, .8, .7, .3, .4]
        }

    def test_probability(self):
        baseline = "TCGTGGATTTCC"
        pr = probability(baseline, self.profile)
        self.assertEqual(0E-398, pr)

    def test_probability2(self):
        baseline = "ACGGGGATTACC"
        pr = probability(baseline, self.profile)
        self.assertEqual(0.0008398080000000002, float(pr))


class TestProfileMostProbablePattern(unittest.TestCase):
    def test_profile_most_probable_pattern(self):
        profile = {
            'A': [0.2, 0.2, 0.3, 0.2, 0.3],
            'C': [0.4, 0.3, 0.1, 0.5, 0.1],
            'G': [0.3, 0.3, 0.5, 0.2, 0.4],
            'T': [0.1, 0.2, 0.1, 0.1, 0.2]
        }
        k = 5
        baseline = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
        expected = 'CCGAG'

        first_match = profile_most_probable_pattern(baseline, k, profile)
        self.assertEqual(expected, first_match)
