class Solution:
    from typing import List
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

# Runtime 3 ms, 22.35 %
# Memory 18.49 mb, 19.99 %
def main():
    solve = Solution()
    test1, test2, test3 = 3, 5, 15
    print(solve.fizzBuzz(test1))
    print(solve.fizzBuzz(test2))
    print(solve.fizzBuzz(test3))

if __name__ == '__main__':
    main()
