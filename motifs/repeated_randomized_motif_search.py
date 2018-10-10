from motifs.score import score
from motifs.random_motifs import random_motifs
from motifs.consensus import consensus
from motifs.count_matrix import get_count
from motifs.profile_to_motifs import profile_to_motifs
from motifs.pseudocounts import profile_with_pseudocounts


def randomized_motif_search(dna, k, t):
    """
    Runs motifs -> profile -> motif cycle until an optimum score is found

    :param dna: DNA strings
    :param k: kmer size
    :param t: DNA strings count
    :return: best motifs
    """

    motifs = random_motifs(dna, k, t)
    best_motifs = None
    best_score = float('inf')

    while True:
        profile = profile_with_pseudocounts(get_count(motifs))
        motifs = profile_to_motifs(profile, dna)
        current_score = score(motifs, consensus(get_count(motifs)))
        if not best_motifs or current_score < best_score:
            best_motifs = motifs
            best_score = current_score
        else:
            return best_motifs


def repeated_randomized_motif_search(dna, k, t, n):
    """
    Repeats randomized_motif_search multiple times to find the global solution

    :param dna: DNA strings
    :param k: kmer size
    :param t: DNA strings count
    :param n: repeat number
    :return: best motif
    """
    best_score = float('inf')
    best_motifs = []
    for _ in range(n):
        motifs = randomized_motif_search(dna, k, t)
        current_score = score(motifs, consensus(get_count(motifs)))
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs