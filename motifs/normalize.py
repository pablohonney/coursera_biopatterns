def normalize(probabilities):
    size = sum(probabilities.values())
    return {letter: prob/size for letter, prob in probabilities.items()}
