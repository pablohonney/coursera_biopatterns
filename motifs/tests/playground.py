from motifs.normalize import normalize
from motifs.repeated_randomized_motif_search import randomized_motif_search

probs = map(float, "0.22 0.54 0.58 0.36 0.3".split())
dummy_lettered = {i: p for i, p in enumerate(probs)}
normed_probes = normalize(dummy_lettered)
print(list(normed_probes.values()))

dna = [
    "TGACGTTC",
    "TAAGAGTT",
    "GGACGAAA",
    "CTGTTCGC",
]

# r = randomized_motif_search(dna, 3, len(dna))
# print(r)

print(sum([0.11, 0.27, 0.29, 0.18, 0.15]))