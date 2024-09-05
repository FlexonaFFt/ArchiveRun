def find_synonims(n, words, key_word):
    symb_book = {}
    for word1, word2 in words:
        symb_book[word1] = word2
        symb_book[word2] = word1
    return symb_book.get(key_word)

def main():
    n = int(input())
    words = [input().strip().split() for _ in range(n)]
    key_word = input().strip()
    print(find_synonims(n, words, key_word))

if __name__ == '__main__':
    main()
