from motifs.consensus import consensus
from motifs.probability import profile_most_probable_pattern
from motifs.score import score
from motifs.count_matrix import get_count
from motifs import timeit


@timeit
def profile_to_motifs(profile, dna):
    """
    :param profile: profile matrix
    :param dna: DNA strings
    :return: best motifs
    """

    k = len(list(profile.values())[0])
    t = len(dna)
    n = len(dna[0])
    best_motifs = []
    best_score = 0
    for i in range(n - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            motifs.append(profile_most_probable_pattern(dna[j], k, profile))

        if not best_motifs or score(motifs, consensus(get_count(motifs))) < best_score:
            best_motifs = motifs
            best_score = score(best_motifs, consensus(get_count(best_motifs)))

    return best_motifs
