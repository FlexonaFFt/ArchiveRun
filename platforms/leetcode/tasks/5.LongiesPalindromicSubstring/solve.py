def longestPalindrome(string: str) -> str:
    def around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]

    longiest = ""
    for i in range(len(string)):
        odd_palindrome = around_center(i, i)
        even_palindrome = around_center(i, i + 1)
        longiest = max(longiest, odd_palindrome, even_palindrome, key=len)
    return longiest

def main():
    string = str(input())
    print(longestPalindrome(string=string))

if __name__ == '__main__':
    main()
