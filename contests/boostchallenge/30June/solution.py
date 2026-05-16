def solution(n: int) -> int:
    # Решето Эратосфена
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, val in enumerate(is_prime) if val and i > 2]

    cnt1 = 0
    cnt3 = 0  
    for p in primes:
        if p % 4 == 1:
            cnt1 += 1
        elif p % 4 == 3:
            cnt3 += 1

    return cnt1 * cnt3


def test():
    print(solution(3))
    print(solution(5))
    print(solution(7))


if __name__ == '__main__': test()
