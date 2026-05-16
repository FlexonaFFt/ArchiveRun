def min_total_difficulty(n, alice, bob, eve):
    # Префиксные минимумы для Алисы
    prefix_min_alice = [float('inf')] * n
    prefix_min_alice[0] = alice[0]
    for i in range(1, n):
        prefix_min_alice[i] = min(prefix_min_alice[i - 1], sum(alice[:i + 1]))

    # Суффиксные минимумы для Евы
    suffix_min_eve = [float('inf')] * n
    suffix_min_eve[-1] = eve[-1]
    for j in range(n - 2, -1, -1):
        suffix_min_eve[j] = min(suffix_min_eve[j + 1], sum(eve[j:]))

    min_difficulty = float('inf')

    # Перебор всех возможных позиций i и j
    for j in range(1, n - 1):
        for i in range(j):
            bob_sum = sum(bob[i + 1:j + 1])
            total_difficulty = prefix_min_alice[i] + bob_sum + suffix_min_eve[j + 1]
            min_difficulty = min(min_difficulty, total_difficulty)

    return min_difficulty

def main():
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    eve = list(map(int, input().split()))
    print(min_total_difficulty(n, alice, bob, eve))

if __name__ == '__main__':
    main()
