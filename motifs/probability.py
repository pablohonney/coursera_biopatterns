from motifs import timeit


# @timeit
def probability(baseline, profile):
    product = 1
    for i, letter in enumerate(baseline):
        product *= profile[letter][i]
    return product


@timeit
def profile_most_probable_pattern(text, k, profile):
    best_value = -1
    best_pos = 0

    for i in range(len(text) - k + 1):
        pr = probability(text[i: i + k], profile)
        if pr > best_value:
            best_value = pr
            best_pos = i

    return text[best_pos: best_pos + k]
