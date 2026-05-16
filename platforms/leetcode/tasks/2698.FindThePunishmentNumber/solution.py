class Solution:
    def punishmentNumber(self, n:int) -> int:
        def is_punishment_number(i):
            square = str(i * i)
            length = len(square)
            def backtrack(index, current_sum):
                if index == length:
                    return current_sum == i
                for j in range(index + 1, length + 1):
                    num = int(square[index:j])
                    if backtrack(j, current_sum + num):
                        return True
                return False
            return backtrack(0, 0)

        total = 0
        for i in range(1, n + 1):
            if is_punishment_number(i):
                total += i * i
        return total

# Runtime 1080 ms, 40.28 %
# Memory 18.03 mb, 19.41 %
def main():
    solution = Solution()
    print(solution.punishmentNumber(10))
    print(solution.punishmentNumber(37))

if __name__ == "__main__":
    main()
