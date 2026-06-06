class Solution:

    def main(self, n: int, t: int, pets) -> int:
        curr, sorted_pets = [], pets.sort()

        for pet in pets: 
            if sum(curr) + pet <= t:
                curr.append(pet)
            else: return len(curr)
        return len(curr)

    def func(self) -> None:
        n, t = map(int, input().split())
        spisok = list(map(int, input().split()))
        print(self.main(n, t, pets=spisok))


if __name__ == '__main__':
    Solution().func()