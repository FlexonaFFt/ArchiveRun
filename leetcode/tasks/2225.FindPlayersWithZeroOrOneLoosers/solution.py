class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loosers, winners = [], []
        for item in matches:
            if item[0] not in winners:
                winners.append(item[0])

            if item[1] not in loosers:
                loosers.append(item[1])

        lsrs, wnns = [], []
        for lsr, wnr in zip(loosers, winners):
            if lsr not in wnr:
                lsrs.append(lsr)
            if wnr not in lsr:
                wnns.append(wnr)

        return [wnns, lsrs]

# Я не доработал это решение
def main():
    solution = Solution()
    print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
    print(solution.findWinners([[2,3],[1,3],[5,4],[6,4]]))

main()
