def solution(n: int, words: list[str]) -> list[list[int]]:
    from collections import defaultdict, deque
    word_info = [(i + 1, w, len(w)) for i, w in enumerate(words)]
    length_groups = defaultdict(list)
    for idx, w, l in word_info:
        length_groups[l].append((idx, w))

    all_lengths = sorted(length_groups.keys())
    min_len = all_lengths[0]
    max_len = all_lengths[-1]

    short_words = []
    long_words = []

    length_count = {l: len(length_groups[l]) for l in length_groups}
    sorted_words = sorted(word_info, key=lambda x: x[2])

    # Берём n самых коротких — короткие, остальные — длинные
    short_words = sorted_words[:n]
    long_words = sorted_words[n:]

    # Для быстрого поиска длинных слов по префиксу
    long_word_map = defaultdict(list)
    for idx, w, l in long_words:
        long_word_map[l].append((idx, w))

    # Для каждого короткого ищем длинное, где короткое — префикс
    used_long = set()
    result = []
    for s_idx, s_word, s_len in short_words:
        found = False
        for l_idx, l_word, l_len in long_words:
            if l_idx in used_long:
                continue
            if l_word.startswith(s_word):
                result.append([s_idx, l_idx])
                used_long.add(l_idx)
                found = True
                break
        if not found:
            # По условию задачи такого не будет
            pass

    return result

