import math
from collections import Counter

def calculate_entropy(passwrod):

    freq = Counter(passwrod)
    length = len(passwrod)
    entropy = 0

    for count in freq.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy