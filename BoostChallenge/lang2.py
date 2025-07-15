from collections import defaultdict

def solution(n, words):
    # слово -> список индексов (1-based)
    buckets = defaultdict(list)
    for idx, w in enumerate(words, 1):
        buckets[w].append(idx)

    # все (слово, индекс)
    items = [(w, idx) for w, idxs in buckets.items() for idx in idxs]

    # сортируем по длине, потом лексикографически
    items.sort(key=lambda x: (len(x[0]), x[0]))

    used = set()
    pairs = []

    # словарь: префикс -> список (слово, индекс) с этим префиксом
    pref_map = defaultdict(list)

    # проходим слева-направо
    for w, idx in items:
        if idx in used:
            continue

        # ищем в pref_map по всем своим префиксам
        found = None
        for l in range(1, len(w)):
            pref = w[:l]
            if pref in pref_map:
                # берём первый свободный
                while pref_map[pref]:
                    cand_w, cand_idx = pref_map[pref][0]
                    if cand_idx in used:
                        pref_map[pref].pop(0)
                        continue
                    found = (cand_idx, idx)   # короткое -> длинное
                    break
                if found:
                    break

        if found:
            pairs.append(found)
            used.update(found)
            continue

        # если не нашли — добавляем само слово в pref_map
        # (кому-то оно будет префиксом)
        pref_map[w].append((w, idx))

    # гарантируется, что все пары найдены
    return pairs


# ---------- тесты ----------
n = 2
words = ["abac", "abacab", "aba", "abaa"]
print(solution(n, words))   # [(3, 4), (1, 2)]

n = 10
words = [
    "a", "ab", "abc", "abcd", "abcde",
    "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij",
    "ax", "abxx", "abcxx", "abcdxx", "abcdexx",
    "abcdefxx", "abcdefgxx", "abcdefghxx", "abcdefghiixx", "abcdefghijxx"
]
print(solution(n, words))


n = 10
words = [
    "a",       #1 короткое
    "ab",      #2 короткое
    "abc",     #3 короткое
    "abcd",    #4 короткое
    "abcde",   #5 короткое
    "abcdef",  #6 короткое
    "abcdefg", #7 короткое
    "abcdefgh",#8 короткое
    "abcdefghi",#9 короткое
    "abcdefghij",#10 короткое

    "ax",      #11 длинное, не префикс от коротких
    "abxx",    #12 длинное, префикс "ab"
    "abcxx",   #13 длинное, префикс "abc"
    "abcdxx",  #14 длинное, префикс "abcd"
    "abcdexx", #15 длинное, префикс "abcde"
    "abcdefxx",#16 длинное, префикс "abcdef"
    "abcdefgxx",#17 длинное, префикс "abcdefg"
    "abcdefghxx",#18 длинное, префикс "abcdefgh"
    "abcdefghiixx",#19 длинное, префикс "abcdefghi"
    "abcdefghijxx" #20 длинное, префикс "abcdefghij"
]


print(solution(n, words))
