incomplete_reverse_dna_code = {
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG'' AGA', 'AGG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'N': ['AAU', 'AAC'],
    'E': ['GAA', 'GAG'],
    'I': ['AUU', 'AUC', 'AUA']
}

dna_code = {}
for letter, codons in incomplete_reverse_dna_code.items():
    for codon in codons:
        dna_code[codon] = letter


def translate(sequence):
    peptide = []
    for i in range(len(sequence) // 3):
        j = 3 * i
        letter = dna_code.get(sequence[j: j + 3], '-')
        peptide.append(letter)
    return ''.join(peptide)

