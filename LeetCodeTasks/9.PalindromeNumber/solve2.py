class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        if x % 10 == 0 and x != 0:
            return False 

        str_x = str(x)
        return str_x == str_x[::-1]

def main():
    chislo = int(input())
    function = Solution()
    print(function.isPalindrome(chislo))

if __name__ == '__main__':
    main()
