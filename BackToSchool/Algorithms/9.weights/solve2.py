def function(n, weights):
    dp = [False] * (n + 1) 
    dp[0] = True 

    for weight in weights:
        for j in range(n, weight - 1, -1):
            if dp[j - weight]:
                dp[j] = True 
        for i in range(n, 0, -1):
            if dp[i] and i + weight <= n:
                dp[i + weight] = True

    return all(dp[1:n+1])

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    if function(n, weights):
        print("Yes") 
    else:
        print("No")

if __name__ == '__main__':
    main()
