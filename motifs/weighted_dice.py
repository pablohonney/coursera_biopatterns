from random import uniform


def weighted_dice(probabilities):
    p = uniform(0, 1)
    cum_prob = 0
    kmer = None
    for kmer, prob in probabilities.items():
        if cum_prob <= p < cum_prob + prob:
            break
        cum_prob += prob
    return kmer