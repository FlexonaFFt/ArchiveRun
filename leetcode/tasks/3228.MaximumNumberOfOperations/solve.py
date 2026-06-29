class Solution:
    def maxOperations(self, s: str) -> int:
        ones_so_far = ans = 0
        in_zero_block = False
        for symb in s:
            if symb == '1':
                ones_so_far += 1
                in_zero_block = False
            else:
                if not in_zero_block:
                    ans += ones_so_far
                    in_zero_block = True
        return ans
