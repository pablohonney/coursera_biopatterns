import unittest

datasets = {
    0: [
        "CATGGGCATCGGCCATACGCC",
        "0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2"
    ],
    1: [
        'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCAT'
        'AGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT',
        "0 0 1 0 1 1 2 1 0 1 1 1 1 1 1 1 2 1 0 1 0 -1 -1 0 0 -1 -2 -2 -1 -2 -2 -1 -2 -1 0 0 1 2 1 0 0 -1 0 -1 -2 " \
        "-1 -1 -2 -2 -2 -3 -3 -4 -3 -2 -2 -2 -1 -2 -3 -3 -3 -2 -2 -1 -2 -2 -2 -2 -1 -1 0 1 1 1 2 1 2 2 3 2 2 2 2 " \
        "3 4 4 5 6 6 6 6 5 5 5 5 4 5 4 4 4 4 4 4 3 2 2 3 2 3 2 3 3 3 3 3 2 1 1 0 1 1 1 0 0 1 1 2 1 0 1 1 0 0 0 0"
    ]
}

value_map = {
    'G': 1,
    'C': -1,
    'A': 0,
    'T': 0
}


def skew(Genome):
    size = len(Genome)
    skew = [0] * (size + 1)

    for i in range(1, size + 1):
        skew[i] = skew[i - 1] + value_map[Genome[i - 1]]

    return skew


def HammingDistance(p, q):
    return sum(p[i] != q[i] for i in range(len(p)))


def ApproximatePatternMatching(Pattern, Text, d):
    positions = []
    for i in range(len(Text) - len(Pattern) + 1):
        dist = 0
        for j in range(len(Pattern)):
            dist += Text[i + j] != Pattern[j]
        if dist <= d:
            positions.append(i)

    return positions


def ApproximatePatternCount(Pattern, Text, d):
    seq = ApproximatePatternMatching(Pattern, Text, d)
    return len(seq)


def MaximumSkew(Genome):
    sk = skew(Genome)
    max_value = max(sk)

    return [i for i, j in enumerate(sk) if j == max_value]


class TestCases(unittest.TestCase):
    def test_skew(self):
        given, expected = datasets[1]

        sk = skew(given)
        self.assertEqual(' '.join(map(str, sk)), expected)

    def test_fuzzy_match(self):
        seq = ApproximatePatternMatching(
            'ATTCTGGA', 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', 3
        )
        self.assertEqual(seq, [6, 7, 26, 27])

    def test_fuzzy_pattern_count(self):
        count = ApproximatePatternCount(
            'GAGG', 'TTTAGAGCCTTCAGAGG', 2
        )
        # print(count)
        self.assertEqual(count, 4)

    def test_hamming_distance(self):
        print(HammingDistance(
            "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG",
            "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
        ))

    def test_skew2(self):
        msg = 'CATTCCAGTACTTCGATGATGGCGTGAAGA'
        sk = skew(msg)

        print(len(sk))
        print(len(msg))
        print(MaximumSkew(msg))
