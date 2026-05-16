# WA: закрытый тест (id: 15)

def function(s, c):
    C, n = set(c), len(s)
    left, char_counter = 0, {}
    min_length, required_chars = float("inf"), len(C) 

    for right in range(n):
        char = s[right]
        if char in C:
            char_counter[char] = char_counter.get(char, 0) + 1

        while len(char_counter) == required_chars:
            current_length = right - left + 1
            min_length = min(min_length, current_length) 
            left_char = s[left]
            if left_char in C:
                char_counter[left_char] -= 1
                if char_counter[left_char] == 0:
                    del char_counter[left_char]
            left += 1
    return min_length if min_length != float("inf") else 0

def main():
    s = input().strip()
    c = input().strip()
    result = function(s, c) 
    print(result)

if __name__ == '__main__':
    main()
