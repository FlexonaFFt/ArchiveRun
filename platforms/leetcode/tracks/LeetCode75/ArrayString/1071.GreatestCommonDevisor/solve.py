# Я не смог самостоятельно придумать алгоритм решения задачи
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b 
            return a 

        def is_divisor(s, t):
            return s == t * (len(s) // len(t))

        len1, len2 = len(str1), len(str2)
        max_len = gcd(len1, len2)
        for i in range(max_len, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                divisor = str1[:i]
                if is_divisor(str1, divisor) and is_divisor(str2, divisor):
                    return divisor
        return ""


# Memory 17.94 mb, 14.03 %
def main():
    solve = Solution()
    string1, string2 = "ABCABC", "ABC"
    print(solve.gcdOfStrings(string1, string2))

if __name__ == '__main__':
    main()
