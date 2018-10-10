from motifs import timeit


@timeit
def get_profile(counts):
    size = sum(list(zip(*counts.values()))[0])

    profile = {}
    for letter, count in counts.items():
        profile[letter] = [x / (size) for x in count]
    return profile
