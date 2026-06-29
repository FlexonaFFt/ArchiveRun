# Решение прошло тесты
def main():
    from collections import defaultdict
    words_counter = defaultdict(int)

    with open('input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                print(words_counter[word], end=' ')
                words_counter[word] += 1

if __name__ == '__main__':
    main()
