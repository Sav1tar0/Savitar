def repeatedString(s: str, n: int) -> int:
    count_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    return count_in_s * full_repeats + s[:remainder].count('a')