class Solution:
    from typing import List
    def func(self, lst: List[int]) -> List[int]:
        answer = []
        value1 = max(lst)
        answer.append(value1)
        lst.remove(value1)
        value2 = max(lst)
        answer.append(value2)
        return answer

def main():
    solve = Solution()
    print(solve.func(lst=[3,1,2]))

if __name__ == '__main__':
    main()
