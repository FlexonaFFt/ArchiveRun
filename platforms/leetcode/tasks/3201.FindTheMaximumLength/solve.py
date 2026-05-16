class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        even_cnt = sum(1 for x in nums if x % 2 == 0)
        odd_cnt = sum(1 for x in nums if x % 2 == 1)

        max_alt_even, last = 0, None 
        for x in nums:
            if last is None:
                if x % 2 == 0:
                    last = x % 2
                    max_alt_even += 1

            else: 
                if x % 2 != last:
                    last = x % 2
                    max_alt_even += 1

        max_alt_odd, last = 0, None 
        for x in nums:
            if last is None:
                if x % 2 == 1:
                    last = x % 2
                    max_alt_odd += 1

            else: 
                if x % 2 != last:
                    last = x % 2
                    max_alt_odd += 1

        return max(even_cnt, odd_cnt, max_alt_even, max_alt_odd)


def test():
    solve = Solution()
    print(solve.maximumLength([1,2,3,4]))           
    print(solve.maximumLength([1,2,1,1,2,1,2]))     
    print(solve.maximumLength([1,3]))  

if __name__ == '__main__':
    test()
