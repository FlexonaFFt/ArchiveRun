class Solution:
    def minSteps(self, s: str, t: str):
        counter1, counter2, counter = [], [], 0
        for char in s:
            if char not in counter1:
                counter1.append(char)
            else:
                counter1.append(char)

        for char in t:
            if char not in counter2:
                counter2.append(char)
            else:
                counter2.append(char)

        for char in counter1:
            if char not in counter2:
                counter += 1

        for char in counter2:
            if char not in counter1:
                counter += 1

        return counter


def main():
    solution = Solution()
    print(solution.minSteps(s="leetcode", t="coats"))

main()
