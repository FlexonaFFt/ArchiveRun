# Этот код не был дописан 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return false 

        chislo = str(x)
        def around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(chislo) and chislo[left] == chislo[right]:
                left -= 1
                right += 1
            return chislo[left + 1:right]

        for i in range(len(chislo)):
            odd_palindrome = around_center(i, i)
            even_palindrome
