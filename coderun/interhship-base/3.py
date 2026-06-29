class Solution:

    def main(self, n: int, nums: list[int]) -> int:
        counter, max_counter = 0, 0 
        for i in range(n):
            if nums[i] == 1:
                counter += 1

                if counter > max_counter: 
                    max_counter = counter 

            else: counter = 0 

        return max_counter 

    def func(self) -> None:
        n = int(input())
        nums = [] 

        for _ in range(n):
            nums.append(int(input()))

        print(self.main(n, nums))


if __name__ == '__main__': 
    Solution().func()