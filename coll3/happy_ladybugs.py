def happyLadybugs(b: str) -> str:
    from collections import Counter
    count = Counter(b)
    if '_' in count:
        for key, val in count.items():
            if key != '_' and val == 1:
                return "NO"
    else:
        for i in range(len(b)):
            if (i == 0 or b[i] != b[i-1]) and (i == len(b)-1 or b[i] != b[i+1]):
                return "NO"
    return "YES"