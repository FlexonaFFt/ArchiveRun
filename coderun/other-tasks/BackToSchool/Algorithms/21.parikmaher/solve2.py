def solve_function(N, K, values):
    current_sum = sum(values[:K]) 
    min_loss = current_sum 
    for i in range(K, N):
        current_sum += values[i] + values[i - K]
        min_loss = min(min_loss, current_sum)
    return min_loss 

def main():
    N = int(input())
    K = int(input())
    values = [float(input()) for _ in range(N)]
    print(solve_function(N, K, values=values))

if __name__ == '__main__':
    main()
