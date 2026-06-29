from typing import List 

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        size, offset = 2 * n + 3, n + 1
        tree = [0] * (size + 1)
        answer, balance = 0, 0

        def add(i: int) -> None:
            while i <= size:
                tree[i] += 1
                i += i & -i 

        def query(i: int) -> int:
            total = 0 
            while i > 0:
                total += tree[i]
                i -= i & -i 
            return total 

        add(offset)
        for num in nums:
            balance += 1 if num == target else -1 
            answer += query(balance + offset - 1)
            add(balance + offset)

        return answer 
