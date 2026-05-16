class Solution:
    def maximum69Number(self, num: int):
       return int(str(num).replace('6', '9', 1)) 


def test():
    solve = Solution()
    print(solve.maximum69Number(num=9669))


if __name__ == '__main__':
    test()
