import unittest

from motifs.normalize import normalize


class TestNormalize(unittest.TestCase):

    def test_0(self):
        probabilities = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
        expected = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}

        result = normalize(probabilities)
        self.assertEqual(expected, result)