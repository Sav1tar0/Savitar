def count_special_problems(n: int, k: int, arr: list[int]) -> int:
    special = 0
    page = 1
    for chapter in arr:
        problems = range(1, chapter + 1)
        for i in range(0, len(problems), k):
            chunk = problems[i:i+k]
            if page in chunk:
                special += 1
            page += 1
    return special