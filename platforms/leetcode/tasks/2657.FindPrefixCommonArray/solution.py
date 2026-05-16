class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        if len(A) != len(B): return []

        answer, common = [], 0
        seen = [0] * (len(A) + 1)
        for i in range(len(A)):
            if seen[A[i]] == 0:
                seen[A[i]] = 1
            elif seen[A[i]] == 1:
                common += 1

            if seen[B[i]] == 0:
                seen[B[i]] = 1
            elif seen[B[i]] == 1:
                common += 1

            answer.append(common)

        return answer

# Runtime 6 ms, 71 %
# Memory 17.81 mb, 41.36 %
def main():
    solution = Solution()
    print(solution.findThePrefixCommonArray(A=[1,3,2,4], B=[3,1,2,4]))
    print(solution.findThePrefixCommonArray(A=[2,3,1], B=[3,1,2]))

main()
