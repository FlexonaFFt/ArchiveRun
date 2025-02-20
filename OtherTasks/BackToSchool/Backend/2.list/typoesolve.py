def main(spisok):
    from collections import Counter
    elements_counter = Counter(spisok)
    answer = [element for element in spisok if elements_counter[element] == 1]
    return len(answer)

if __name__ == "__main__":
    n = int(input())
    spisok = list(map(int, input().split()))
    print(main(spisok=spisok))
