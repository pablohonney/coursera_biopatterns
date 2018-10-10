from motifs import timeit


@timeit
def consensus(count):
    columns_count = len(list(count.values())[0])
    consensus_list = []

    for column in range(columns_count):
        max_value = -1
        max_letter = None
        for letter in sorted(count):  # outcome is ACGT order dependent
            if count[letter][column] > max_value:
                max_value = count[letter][column]
                max_letter = letter

        consensus_list.append(max_letter)

    return ''.join(consensus_list)
