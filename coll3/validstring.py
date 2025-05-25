def isValidStringSameOccurence(s: str) -> str:
    from collections import Counter
    counts = Counter(s)
    freq = Counter(counts.values())
    if len(freq) == 1:
        return "YES"
    if len(freq) == 2:
        k1, k2 = freq.keys()
        if (freq[k1] == 1 and (k1 == 1 or k1 - k2 == 1)) or (freq[k2] == 1 and (k2 == 1 or k2 - k1 == 1)):
            return "YES"
    return "NO"