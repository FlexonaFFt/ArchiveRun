class Solution:
    def find_gcd(self, a: int, b: int) -> int:
        self.a = a
        self.b = b

        while b:
            a, b = b, a % b
        return a

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(1 for x in nums if x == 1)
        if ones > 0:
            return n - ones

        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = self.find_gcd(g, nums[j])  
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        if min_len == float('inf'):
            return -1
        return (min_len - 1) + (n - 1)
