import sys


def main(stop_words, sentence) -> str:
    if any(word in sentence for word in stop_words):
        return 'DELETE'
    else: return 'KEEP'


def inputer():
    n, m = map(int, input().split())
    stop_words, sentences = [], []
    for _ in range(n):
        word = str(input().strip())
        stop_words.append(word)

    for _ in range(m):
        sentence = str(input().strip())
        sentences.append(sentence)

    for sentence in sentences:
        print(main(stop_words, sentence))


if __name__ == '__main__':
    inputer()
