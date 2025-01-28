'''
class Solution:
    def findTheDifference(self, s: str, t: str):
        list1, list2 = [], []
        for element in s:
            if element not in list1:
                list1.append(element)
        for char in t:
            if char not in list2:
                list2.append(char)
        diff = set(list2).difference(set(list1))
        return diff'''

class Solution:
    def findTheDifference(self, s: str, t: str):
        charCounter = {}
        for char in s:
            charCounter[char] = charCounter.get(char, 0) + 1
        for char in t:
            if char not in charCounter or charCounter[char] == 0:
                return char
            else:
                charCounter[char] -= 1
        return t[-1]

# Runtime 4 ms, 25 %
# Memory 17.8 mb, 49.93 %
def main():
    s, t = "abcd", "abcde"
    solve = Solution()
    print(solve.findTheDifference(s, t))

if __name__ == '__main__':
    main()
