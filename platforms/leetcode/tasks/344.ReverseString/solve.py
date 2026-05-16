class Solution:
    from typing import List
    def reverseString(self, s: List[str]):
        s.reverse()
        return s


def main():
    s = ["h","e","l","l","o"]
    s2 = ["H","a","n","n","a","h"]
    solution = Solution()
    print(solution.reverseString(s))
    print(solution.reverseString(s2))

if __name__ == '__main__':
    main()
