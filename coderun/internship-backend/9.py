class Solution:

    def mainFunc(self, string: list[int], k: int) -> int:
        answer = 0 

        for target in 'abcdefghijklmnopqrstuvwxyz':
            left, replacements = 0, 0

            for right in range(len(string)):
                if string[right] != target:
                    replacements += 1

                while replacements > k:
                    if string[left] != target:
                        replacements -= 1
                    left += 1

                answer = max(answer, right - left + 1)

        return answer 


    def inputer(self) -> None: 
        n = int(input())
        string = str(input())
        print(self.mainFunc(string, n))


if __name__ == '__main__':
    Solution().inputer()