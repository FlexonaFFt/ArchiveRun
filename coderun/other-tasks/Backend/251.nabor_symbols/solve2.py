# Неправильный ответ
def find_podstroka(s, c):
    from collections import Counter
    required_chars = Counter(c)
    required_length = len(required_chars)

    left = 0
    right = 0
    formed = 0
    window_counts = {}
    min_length = float('inf')

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in required_chars and window_counts[char] == required_chars[char]:
            formed += 1
        while left <= right and formed == required_length:
            char = s[left]
            min_length = min(min_length, right - left + 1)
            window_counts[char] -= 1
            if char in required_chars and window_counts[char] < required_chars[char]:
                formed -= 1
            left += 1
        right += 1
    return min_length if min_length != float('inf') else 0

def main():
    string = str(input())
    mnozhestvo = str(input())
    print(find_podstroka(string, mnozhestvo))

if __name__ == '__main__':
    main()
