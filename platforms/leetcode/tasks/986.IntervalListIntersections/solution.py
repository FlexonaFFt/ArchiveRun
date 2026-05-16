class Solution:
    def intervalIntersections(self, firstList: list[list[int]],
        secondList: list[list[int]]) -> list[list[int]]:

        if len(firstList) == 0 or len(secondList) == 0:
            return []
        if len(firstList) == 0 and len(secondList) == 0:
            return []

        i, j, result = 0, 0, []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            if a_start <= b_end and b_start <= a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])

            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return result

# Runtime 8 ms, 29.14 %
# Memory 18.69 mb, 41.89 %
def main():
    solution = Solution()
    print(solution.intervalIntersections([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
    print(solution.intervalIntersections([[0,2],[5,10],[13,23],[24,25]], []))

main()
