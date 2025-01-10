def find_probs(n, servers):
    error_probs = [(a * b / 10000) for a, b in servers]
    total_error_probs = sum(error_probs)
    # Нормализация всех вычесленных ошибок относительно общей вероятности ошибки
    normilized_probs = [p / total_error_probs for p in error_probs]
    return normilized_probs

def main():
    n = int(input())
    servers = [tuple(map(int, input().split())) for _ in range(n)]
    probs = find_probs(n, servers)
    for p in probs:
        print(f"{p:.12f}")

if __name__ == "__main__":
    main()
