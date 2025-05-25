def find_common_strings_with_least_index_sum(list1: list[str], list2: list[str]) -> list[str]:
    common = set(list1) & set(list2)
    if not common:
        return []
    min_sum = float('inf')
    result = []
    for word in common:
        current_sum = list1.index(word) + list2.index(word)
        if current_sum < min_sum:
            min_sum = current_sum
            result = [word]
        elif current_sum == min_sum:
            result.append(word)
    return result