import unittest

from motifs.weighted_dice import weighted_dice


class TestWeightedDie(unittest.TestCase):
    def test_0(self):
        probabilities = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}

        for i in range(5):
            print(weighted_dice(probabilities))
