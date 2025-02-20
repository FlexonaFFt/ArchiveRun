def min_total_difficulty(n, alice, bob, eve):

    # Нахождение префиксных сумм (нифига не понял)
    prefix_alice = [0] * (n + 1)
    prefix_bob = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_alice[i] = prefix_alice[i - 1] + alice[i - 1]
        prefix_bob[i] = prefix_bob[i - 1] + bob[i - 1]

    # Находим суффиксные суммы для челиксов
    suffix_bob = [0] * (n + 2)
    suffix_eve = [0] * (n + 2)
    for j in range(n, 0, -1):
        suffix_bob[j] = suffix_bob[j + 1] + bob[j - 1]
        suffix_eve[j] = suffix_eve[j + 1] + eve[j - 1]

    min_difficulty = float('inf')
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            current_difficulty = prefix_alice[i] + (prefix_bob[j] - prefix_bob[i]) + suffix_eve[j + 1]
            min_difficulty = min(min_difficulty, current_difficulty)
    return min_difficulty

def main():
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    eve = list(map(int, input().split()))
    print(min_total_difficulty(n, alice, bob, eve))

if __name__ == '__main__':
    main()
