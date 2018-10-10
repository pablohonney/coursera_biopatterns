from math import log2

from motifs import timeit

motifs = [
    'tcgggggttttt',
    'ccggtgacttac',
    'acggggattttc',
    'ttggggactttt',
    'aaggggacttcc',
    'ttggggacttcc',
    'tcggggattcat',
    'tcggggattcct',
    'taggggaactac',
    'tcgggtataacc',
]


@timeit
def _get_motif_bags(motifs):
    column_length = len(motifs[0])
    row_length = len(motifs)
    count_matrix = []

    for column in range(column_length):
        count = {}
        for row in range(row_length):
            letter = motifs[row][column]
            if letter not in count:
                count[letter] = 0
            count[letter] += 1
        count_matrix.append(count)

    return count_matrix


def H(ps):
    return -sum(p * log2(p) for p in ps)


def count_matrix_entropy(count_matrix):
    entropy = 0
    for count in count_matrix:
        entropy += H(x / 10. for x in count.values())
    return entropy


def get_most_common(count_matrix):
    commons = []
    for count in count_matrix:
        commons.append(count.most_common(n=1)[0][0])
    return commons


@timeit
def get_count_slow(motifs):
    letters = 'ATGC'
    counts = {x: [] for x in letters}

    for count in _get_motif_bags(motifs):
        for _letter in letters:
            counts[_letter].append(count.get(_letter, 0))

    return counts


@timeit
def get_count_fast(motifs):
    letters = 'ATGC'
    counts = {x: [0] * len(motifs[0]) for x in letters}
    column_length = len(motifs[0])
    row_length = len(motifs)

    for column in range(column_length):
        for row in range(row_length):
            letter = motifs[row][column]
            counts[letter][column] += 1

    return counts

get_count = get_count_fast

if __name__ == '__main__':
    count_matrix = _get_motif_bags(motifs)
    print(count_matrix)
    print(count_matrix_entropy(count_matrix))
    print(get_most_common(count_matrix))
