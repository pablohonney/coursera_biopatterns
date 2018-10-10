from motifs.consensus import consensus
from motifs.probability import profile_most_probable_pattern
from motifs.profile_matrix import get_profile
from motifs.pseudocounts import add_scalar_to_matrix
from motifs.score import score
from motifs.count_matrix import get_count

from motifs import timeit


@timeit
def greedy_motif_search(dna, k, t, pseudo=0):
    """
    :param dna: DNA strings
    :param k: kmer size
    :param t: number of kmers in the DNA
    :param pseudo: pseudocount
    :return: best motif
    """

    n = len(dna[0])
    best_motifs = []
    best_score = 0
    for i in range(n - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            profile = get_profile(get_count(motifs[0:j]))
            if pseudo:
                profile = add_scalar_to_matrix(pseudo, profile)
            motifs.append(profile_most_probable_pattern(dna[j], k, profile))

        current_score = score(motifs, consensus(get_count(motifs)))
        if not best_motifs or current_score < best_score:
            best_motifs = motifs
            best_score = current_score

    return best_motifs
