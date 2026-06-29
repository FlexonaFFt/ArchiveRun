class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        
        max_value, max_freq = max(nums) + 1, 0
        frequency = [0] * max_value 
        for number in nums:
            frequency[number] += 1

        curr = sum(frequency[:k])
        prev, target, increment = 0, 0, 0
        for target in range(max_value):

            curr -= frequency[target]
            if target < max_value - k: 
                curr += frequency[target - 1]
            if target > 0:
                prev += frequency[target - 1]
            if target > k + 1:
                prev -= frequency[target - (k + 1)]
            increment = min(numOperations, curr + prev)
            max_freq = max(max_freq, frequency[target] + increment)
        
        return max_freq


def test():
    solve = Solution()
    print(solve.maxFrequency([1,4,5], 1, 2))
    print(solve.maxFrequency([5,11,20,20], 5, 1))

if __name__ == '__main__':
    test()
