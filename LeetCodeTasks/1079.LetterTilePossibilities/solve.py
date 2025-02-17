class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        def backtrack(counter):
            total = 0
            for letter in counter:
                if counter[letter] > 0:
                    total += 1
                    counter[letter] -= 1
                    total += backtrack(counter)
                    counter[letter] += 1
            return total

        counter = Counter(tiles)
        return backtrack(counter)


def main():
    solution = Solution()
    print(solution.numTilePossibilities("AAB"))
    print(solution.numTilePossibilities("AAABBC"))
    print(solution.numTilePossibilities("V"))

if __name__ == "__main__":
    main()
