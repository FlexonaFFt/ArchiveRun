def function(string):
    counter = {}
    for element in string:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    max_counter = max(counter.values())
    max_nums_counter = [x for x, count in counter.items() if count == max_counter]
    return(max(max_nums_counter))

def main():
    n = int(input())
    spisok = list(map(int, input().split()))
    print(function(spisok))

if __name__ == '__main__':
    main()
