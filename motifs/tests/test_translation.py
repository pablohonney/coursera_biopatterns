import unittest

from motifs.translation import translate


class TestTranslation(unittest.TestCase):
    def test_translate(self):
        expected = 'PRTEIN'
        seqs = [
            'CCGAGGACCGAAAUCAAC',
            # 'CCUCGUACUGAUAUUAAU',
            # 'CCCCGUACGGAGAUGAAA',
            'CCCAGGACUGAGAUCAAU'
        ]

        for i, seq in enumerate(seqs):
            with self.subTest(msg=i):
                result = translate(seq)
                # print(result)
                self.assertEqual(result, expected)
