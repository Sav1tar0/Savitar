def acm_team(topic: list[str]) -> list[int]:
    max_topics = 0
    num_teams = 0
    n = len(topic)
    for i in range(n):
        for j in range(i+1, n):
            combined = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if combined > max_topics:
                max_topics = combined
                num_teams = 1
            elif combined == max_topics:
                num_teams += 1
    return [max_topics, num_teams]