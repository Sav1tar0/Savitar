def alternate(s: str) -> int:
    unique_chars = set(s)
    max_len = 0
    for a in unique_chars:
        for b in unique_chars:
            if a == b:
                continue
            filtered = [c for c in s if c == a or c == b]
            if all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1)):
                max_len = max(max_len, len(filtered))
    return max_len