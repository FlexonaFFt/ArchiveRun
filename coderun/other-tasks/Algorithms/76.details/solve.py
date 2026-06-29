# Превышен лимит времени на закрытом тесте (id: 14)
def find_the_solve(N, K, M):
    total_parts = 0
    while N >= K:
        ingots = N // K
        remaining_metal = N % K
        parts_from_ingots = ingots * (K // M)
        total_parts += parts_from_ingots
        leftover_parts = ingots * (K % M)
        N = remaining_metal + leftover_parts
    return total_parts

def main():
    N, K, M = map(int, input().strip().split())
    print(find_the_solve(N, K, M))

if __name__ == '__main__':
    main()
