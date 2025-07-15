from collections import defaultdict

def solution(n: int, words: list[str]) -> list[list[int]]:
    # (слово, индекс)
    indexed = [(w, i + 1) for i, w in enumerate(words)]
    # Сортируем по длине
    indexed.sort(key=lambda x: len(x[0]))

    used = set()
    pairs = []

    # Проходим по каждому слову
    for short_word, short_idx in indexed:
        if short_idx in used:
            continue
        # Ищем самое короткое неиспользованное слово, которое начинается с short_word и длиннее
        for long_word, long_idx in indexed:
            if long_idx in used:
                continue
            if len(long_word) > len(short_word) and long_word.startswith(short_word):
                pairs.append([short_idx, long_idx])
                used.add(short_idx)
                used.add(long_idx)
                break

    return pairs

print(solution(2, ["abac", "abacab", "aba", "abaa"]))
