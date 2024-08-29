def find_max_profit(n, m, list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2, reverse=True)
    profit, i, j = 0, 0, 0
    while i < n and j < m:
        if sorted_list1[j] >= sorted_list2[i]:
            profit += sorted_list2[j] - sorted_list1[i]
            i += 1
            j += 1
        else:
            j += 1
    return profit

def main():
    n, m = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(find_max_profit(n, m, list1, list2))

if __name__ == '__main__':
    main()
