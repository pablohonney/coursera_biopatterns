from random import randint

from motifs.score import score
from motifs.count_matrix import get_count
from motifs.consensus import consensus
from motifs.random_motifs import random_motifs
from motifs.profile_generated_string import profile_generated_string
from motifs.pseudocounts import profile_with_pseudocounts


def gibbs_sampler(dna, k, t, n):
    best_score = float('inf')
    motifs = random_motifs([string for string in dna], k, t)
    best_motifs = motifs

    for j in range(n):
        skip_index = randint(0, t-1)
        dna_slice = dna[:skip_index] + dna[skip_index+1:]
        profile = profile_with_pseudocounts(get_count(dna_slice))
        motifs[skip_index] = profile_generated_string(motifs[skip_index], profile, k)

        current_score = score(motifs, consensus(get_count(motifs)))
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score

    return best_motifs


def repeated_gibbs_sampler(dna, k, t, n):
    best_score = float('inf')
    best_motifs = []
    for i in range(100):
        motifs = gibbs_sampler(dna, k, t, n)
        current_score = score(motifs, consensus(get_count(motifs)))
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    return best_motifs
