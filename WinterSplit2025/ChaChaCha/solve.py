def solve(string):
    latin_alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

    summ, counter = 0, 0
    for char in latin_alphabet:
        if char in latin_alphabet:
            summ += latin_alphabet[char]
            counter += 1

    if counter == 0:
        return 0
    else: 
        average = summ / counter 
        return average 

def main():
    string = input()
    print(solve(string))

if __name__ == '__main__':
    main()
