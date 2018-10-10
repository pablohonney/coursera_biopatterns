from motifs import timeit


@timeit
def score(motifs, cons):
    row_count = len(motifs)
    columns_count = len(motifs[0])

    sc = 0
    for column in range(columns_count):
        for row in range(row_count):
            sc += motifs[row][column] != cons[column]

    return sc

