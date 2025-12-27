import math
from collections import Counter

def calculate_entropy(domain):
    # A high entropy means randomly generated domains 

    if not domain:
        return 0

    # Count the frequency of each character in the domain
    char_counts = Counter(domain)

    # Total length of the domain
    length = len(domain)

    entropy = 0
    for count in char_counts.values():
        # The probability of each character
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy 