def reverse_characters_in_words(s: str) -> str:
    return ' '.join(word[::-1] for word in s.split(' '))