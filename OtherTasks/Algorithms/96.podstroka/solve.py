def find_max_substring(n, k, s):
    char_count = [0] * 26
    left, max_index, start_index = 0, 0, 0

    for right in range(n):
        char_count[ord(s[right]) - ord('a')] += 1
        while char_count[ord(s[right]) - ord('a')] > k:
            char_count[ord(s[left]) - ord('a')] -= 1
            left += 1
        current_lehgth = right - left + 1
        if current_lehgth > max_index:
            max_index = current_lehgth
            start_index = left + 1

    return max_index, start_index

def main():
    n, k = map(int, input().split())
    s = input().strip()
    length, index = find_max_substring(n, k, s)
    print(length, index)

if __name__ == '__main__':
    main()
