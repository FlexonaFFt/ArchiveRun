def min_candies(n, list):
    from collections import Counter
    freq = Counter(list)
    if len(freq) == 1:
        return 0
    freq_list = sorted(freq.values(), reverse=True)
    if len(freq_list) == 2:
        return 0
    total_additions = 0
    for i in range(2, len(freq_list)):
        total_additions += freq_list[i]
    return total_additions

def main():
    n = int(input())
    listt = list(map(int, input().split()))
    print(min_candies(n, listt))

if __name__ == '__main__':
    main()
