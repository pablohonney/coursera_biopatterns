from motifs.greedy_motif_search import greedy_motif_search


def greedy_motif_search_with_pseudocounts(dna, k, t):
    return greedy_motif_search(dna, k, t, 1)
