from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        if k <= 0 or k > len(nums): return []
        
        answer: list[int] = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            freq = Counter(window)
            top = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))[:x]
            total = sum(val * cnt for val, cnt in top)
            answer.append(total)
        
        return answer


def test():
    solve = Solution()
    print(solve.findXSum([1,1,2,2,3,4,2,3], 6, 2))
    print(solve.findXSum([3,8,7,8,7,5], 2, 2))

if __name__ == '__main__':
    test()
