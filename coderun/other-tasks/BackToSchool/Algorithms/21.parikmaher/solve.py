def solve(N, K, values):
    current_sum = sum(values[:K])
    min_sum = current_sum
    
    if K == 0:
        return sum(values)
    for i in range(K, N):
        current_sum += values[i] - values[i - K]
        if current_sum < min_sum:
            min_sum = current_sum
    expected_loss = sum(values) - min_sum
    return expected_loss

def main():
    N = int(input())
    K = int(input())
    values = [float(input()) for _ in range(N)]
    print(solve(N, K, values)) 

if __name__ == '__main__':
    main()
