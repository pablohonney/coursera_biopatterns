from random import randint

from motifs import timeit


@timeit
def random_motifs(dna, k, t):
    string_length = len(dna[0])
    motifs = []

    for string in dna:
        start = randint(0, string_length-k)
        motifs.append(string[start: start+k])
    return motifs
