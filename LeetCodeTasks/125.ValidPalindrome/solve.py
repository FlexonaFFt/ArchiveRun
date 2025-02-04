class Solution:
    def isPalindrome(self, s: str):
       punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
       textWithoutPunct = ''.join(char for char in s if char not in punct).lower()
       words = textWithoutPunct.split()
       result = ''.join(words)

       def __palindrome__(string):
           left, right = 0, len(string) - 1
           while left < right:
               if string[left] != string[right]:
                   return False
               left += 1
               right -= 1
           return True

       return __palindrome__(result)

# Runtime 9 ms, 46.17 %
# Memory 19.34 mb, 22.72 %
def main():
    solve = Solution()
    s1 = "A man, a plan, a canal: Panama"
    s2, s3 = "race a car", " "
    print(solve.isPalindrome(s1))
    print(solve.isPalindrome(s2))
    print(solve.isPalindrome(s3))

if __name__ == '__main__':
    main()
