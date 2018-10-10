from motifs.profile_matrix import get_profile

from motifs import timeit


@timeit
def add_scalar_to_matrix(scalar, matrix):
    new_matrix = {}
    for letter, row in matrix.items():
        new_row = new_matrix[letter] = []
        for cell in row:
            new_row.append(cell + scalar)
    return new_matrix


@timeit
def profile_with_pseudocounts(count):
    pseudo_count = add_scalar_to_matrix(1, count)
    return get_profile(pseudo_count)
