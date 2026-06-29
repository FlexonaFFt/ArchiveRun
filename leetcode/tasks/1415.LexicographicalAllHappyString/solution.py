class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(current, last_char, count):
            if len(current) == n:
                count[0] += 1
                if count[0] == k:
                    return current
                return None

            for char in ['a', 'b', 'c']:
                if char != last_char:
                    result = backtrack(current + char, char, count)
                    if result:
                        return result
            return None

        count = [0]
        return backtrack("", "", count) or ""

# Runtime 3 ms, 82 %
# Memory 17.84 mb, 66 %
def main():
    solution = Solution()
    print(solution.getHappyString(3, 9))

if __name__ == '__main__':
    main()
