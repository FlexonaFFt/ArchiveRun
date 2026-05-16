class Solution:
    from typing import List
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index):
            if index == len(result):
                return True
            if result[index] != 0:
                return backtrack(index + 1)
            for i in range(n, 0, -1):
                if used[i]:
                    continue
                if i == 1:
                    result[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[1] = False
                elif index + i < len(result) and result[index + i] == 0:
                    result[index] = i
                    result[index + i] = i
                    used[i] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    result[index + i] = 0
                    used[i] = False
            return False

        backtrack(0)
        return result


def main():
    solution = Solution()
    print(solution.constructDistancedSequence(3))
    print(solution.constructDistancedSequence(5))

if __name__ == "__main__":
    main()
