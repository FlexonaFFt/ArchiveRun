from collections import defaultdict

def solution(n, words):
    # (слово, оригинальный индекс)
    items = [(w, i + 1) for i, w in enumerate(words)]

    # сортируем по длине, потом лексикографически
    items.sort(key=lambda x: (len(x[0]), x[0]))

    used = [False] * (2 * n + 2)          # 1-based
    pairs = []

    i = 0
    while i < 2 * n:
        w1, idx1 = items[i]
        w2, idx2 = items[i + 1]

        if w2.startswith(w1) and len(w1) < len(w2):
            pairs.append((idx1, idx2))
            used[idx1] = used[idx2] = True
            i += 2
        else:
            # значит w1 — длинное, а w2 — его префикс (такого не бывает по условию задачи)
            # но проверим наоборот
            if w1.startswith(w2) and len(w2) < len(w1):
                pairs.append((idx2, idx1))
                used[idx1] = used[idx2] = True
                i += 2
            else:
                # по условию задачи такого не может быть
                raise RuntimeError("invariant violated")

    return pairs


# ---------- тесты ----------
n = 2
words = ["abac", "abacab", "aba", "abaa"]
print(solution(n, words))   # [(3, 4), (1, 2)]
