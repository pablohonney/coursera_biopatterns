import unittest

from motifs.count_matrix import get_count
from motifs.pseudocounts import add_scalar_to_matrix
from motifs.pseudocounts import profile_with_pseudocounts


class TestPseudocounts_1(unittest.TestCase):
    def setUp(self):
        self.motifs = [
            "AACGTA",
            "CCCGTT",
            "CACCTT",
            "GGATTA",
            "TTCCGG",
        ]

    def test_count_with_pseudocounts(self):
        expected = {
            'T': [2, 2, 1, 2, 5, 3],
            'A': [2, 3, 2, 1, 1, 3],
            'C': [3, 2, 5, 3, 1, 1],
            'G': [2, 2, 1, 3, 2, 2]
        }
        count = get_count(self.motifs)
        result = add_scalar_to_matrix(1, count)

        self.assertEqual(expected, result)

    def test_profile_with_pseudocounts(self):
        expected = {
            'A': [
                0.2222222222222222,
                0.3333333333333333,
                0.2222222222222222,
                0.1111111111111111,
                0.1111111111111111,
                0.3333333333333333
            ],
            'C': [
                0.3333333333333333,
                0.2222222222222222,
                0.5555555555555556,
                0.3333333333333333,
                0.1111111111111111,
                0.1111111111111111
            ],
            'G': [
                0.2222222222222222,
                0.2222222222222222,
                0.1111111111111111,
                0.3333333333333333,
                0.2222222222222222,
                0.2222222222222222
            ],
            'T': [
                0.2222222222222222,
                0.2222222222222222,
                0.1111111111111111,
                0.2222222222222222,
                0.5555555555555556,
                0.3333333333333333
            ]
        }

        result = profile_with_pseudocounts(self.motifs)
        self.assertEqual(expected, result)


class TestPseudocounts_2(unittest.TestCase):
    def setUp(self):
        self.motifs = [
            "GTACAACTGT",
            "CAACTATGAA",
            "TCCTACAGGA",
            "AAGCAAGGGT",
            "GCGTACGACC",
            "TCGTCAGCGT",
            "AACAAGGTCA",
            "CTCAGGCGTC",
            "GGATCCAGGT",
            "GGCAAGTACC",
        ]

    def test_count_with_pseudocounts(self):
        expected = {
            'A': [3, 4, 4, 4, 7, 5, 3, 3, 2, 4],
            'C': [3, 4, 5, 4, 3, 4, 3, 2, 4, 4],
            'T': [3, 3, 1, 5, 2, 1, 3, 3, 2, 5],
            'G': [5, 3, 4, 1, 2, 4, 5, 6, 6, 1]
        }
        count = get_count(self.motifs)
        result = add_scalar_to_matrix(1, count)

        self.assertEqual(expected, result)

    def test_profile_with_pseudocounts(self):
        expected = {
            'A': [
                0.21428571428571427,
                0.2857142857142857,
                0.2857142857142857,
                0.2857142857142857,
                0.5,
                0.35714285714285715,
                0.21428571428571427,
                0.21428571428571427,
                0.14285714285714285,
                0.2857142857142857
            ],
            'C': [
                0.21428571428571427,
                0.2857142857142857,
                0.35714285714285715,
                0.2857142857142857,
                0.21428571428571427,
                0.2857142857142857,
                0.21428571428571427,
                0.14285714285714285,
                0.2857142857142857,
                0.2857142857142857
            ],
            'G': [
                0.35714285714285715,
                0.21428571428571427,
                0.2857142857142857,
                0.07142857142857142,
                0.14285714285714285,
                0.2857142857142857,
                0.35714285714285715,
                0.42857142857142855,
                0.42857142857142855,
                0.07142857142857142
            ],
            'T': [
                0.21428571428571427,
                0.21428571428571427,
                0.07142857142857142,
                0.35714285714285715,
                0.14285714285714285,
                0.07142857142857142,
                0.21428571428571427,
                0.21428571428571427,
                0.14285714285714285,
                0.35714285714285715
            ]
        }
        result = profile_with_pseudocounts(self.motifs)
        self.assertEqual(expected, result)