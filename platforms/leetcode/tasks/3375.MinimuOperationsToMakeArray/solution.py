class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        hash_map = {}
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                hash_map[i] = hash_map.get(i, 0) + 1
        return len(hash_map)

# Runtime 50 ms, 99.53 %
# Memory 17.68 %, 75.47 %
def main():
    solution = Solution()
    print(solution.minOperations(nums=[5,2,5,4,5], k=2))
    print(solution.minOperations(nums=[2,1,2], k=2))
    print(solution.minOperations(nums=[9,7,5,3], k=1))

if __name__ == '__main__':
    main()
