# Не является решением
def min_candies(n, list):
    sorted_list, min_diff_pairs, result = sorted(list), [], []
    for i in range(len(sorted_list) - 1):
        diff = abs(sorted_list[i] - sorted_list[i - 1])
        min_diff_pairs.append((sorted_list[i], sorted_list[i + 1], diff))
    print(min_diff_pairs)
    min_diff_pairs.sort(key=lambda x: x[2])
    print(min_diff_pairs)
    for pair in min_diff_pairs:
        result.append(pair[0])
    result.append(sorted_list[-1])
    return result

def main():
    n = int(input())
    listt = list(map(int, input().split()))
    print(min_candies(n, listt))

if __name__ == '__main__':
    main()
