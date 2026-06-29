class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int: 
        players.sort()
        trainers.sort()
        i = j = counter = 0
        n, m = len(players), len(trainers)

        while i < n and j < m:
            if players[i] <= trainers[j]:
                counter += 1
                i += 1
                j += 1
            else: j += 1

        return counter 


def test():
    solve = Solution()
    print(solve.matchPlayersAndTrainers([4,7,9], [8,2,5,8]))
    print(solve.matchPlayersAndTrainers([1,1,1], [10]))

if __name__ == '__main__':
    test()
