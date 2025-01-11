def can_weigh_all_masses(n, weights):
    dp = [False] * (n + 1)
    dp[0] = True

    for weight in weights:
        for i in range(n, weight - 1, -1):
            if dp[i - weight]:
                dp[i] = True 

    for i in range(1, n + 1):
        if not dp[i]:
            return 'No'
    
    return 'Yes'

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    print(can_weigh_all_masses(n, weights))

if __name__ == '__main__':
    main()
