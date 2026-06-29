class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losers, winners = {}, {}
        for winner, loser in matches:
            if winner not in winners:
                winners[winner] = 0
            winners[winner] += 1

            if loser not in losers:
                losers[loser] = 0
            losers[loser] += 1

        never_lost = [player for player in winners if player not in losers]
        lost_ones = [player for player, count in losers.items() if count == 1]
        never_lost.sort()
        lost_ones.sort()
        return [never_lost, lost_ones]

# Runtime 168 ms, 21.38 %
# Memory 61.33 mb, 41.41 %
def main():
    solution = Solution()
    print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
    print(solution.findWinners([[2,3],[1,3],[5,4],[6,4]]))

main()
