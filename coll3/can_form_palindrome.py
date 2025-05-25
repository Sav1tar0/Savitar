def can_form_palindrome(s: str) -> str:
    from collections import defaultdict
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return "YES" if odd_count <= 1 else "NO"