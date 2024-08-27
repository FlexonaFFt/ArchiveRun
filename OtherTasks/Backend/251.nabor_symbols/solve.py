def find_podstroka(string, mnozh):
    podstroka = []
    mnozh_list = {}
    for element in mnozh:
        if element in mnozh_list:
            mnozh_list[element] += 1
        else:
            mnozh_list[element] = 1

    counter = 0
    for element in string:
        if element in mnozh_list:
            mnozh_list[element] -= 1
            counter += 1

    return counter

def main():
    string = str(input())
    mnozhestvo = str(input())
    print(find_podstroka(string, mnozhestvo))

if __name__ == '__main__':
    main()
