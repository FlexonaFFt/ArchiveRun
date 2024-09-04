# Решение превышает лимит времени (id: 19)
def main():
    import re
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    words_counter, rezult = {}, []
    words = re.findall(r'\S+', text)
    for word in words:
        if word in words_counter:
            rezult.append(words_counter[word])
            words_counter[word] += 1
        else:
            rezult.append(0)
            words_counter[word] = 1
    print(' '.join(map(str, rezult)))

if __name__ == '__main__':
    main()
