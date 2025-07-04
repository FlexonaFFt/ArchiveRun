def solution(n: int, words: list[str]) -> list[list[int]]:
    result = [[0, 0] for _ in range(n + 1)]

    return result


print(solution(2, ['abac', 'abacab', 'aba', 'abaa']))
