import unittest
from collections import Counter

from motifs.profile_generated_string import profile_generated_string


class TestProfileGeneratedString(unittest.TestCase):
    def test_0(self):
        text = 'AAACCCAAACCC'
        profile = {
            'A': [0.5, 0.1],
            'C': [0.3, 0.2],
            'G': [0.2, 0.4],
            'T': [0.0, 0.3]
        }
        k = 2
        expected = 'AC'

        results = []
        for _ in range(100):
            results.append(profile_generated_string(text, profile, k))

        most_common_result = Counter(results).most_common(n=1)[0][0]
        self.assertEqual(expected, most_common_result)

