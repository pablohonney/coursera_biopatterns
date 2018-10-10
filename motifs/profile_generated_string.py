from motifs.probability import probability
from motifs.normalize import normalize
from motifs.weighted_dice import weighted_dice


def profile_generated_string(text, profile, k):

    n = len(text)
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[text[i:i + k]] = probability(text[i:i + k], profile)

    normalized_probabilities = normalize(probabilities)
    return weighted_dice(normalized_probabilities)