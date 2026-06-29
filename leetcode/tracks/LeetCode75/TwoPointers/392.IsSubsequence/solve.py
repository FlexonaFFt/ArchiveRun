# Мое решение не учитывает порядок элементов, что невероятно важно в этой задаче
class Solution:
    def isSupsecquence(self, string2: str, string1: str) -> bool:
        text_lenght, pattern_length = len(string1), len(string2)
        list, counter = [], 0
        for i in range(pattern_length):
            list.append(string2[i])
        for j in range(text_lenght):
            if string1[j] in list:
                list.remove(string1[j])
                counter += 1
        if counter == pattern_length:
            return True 
        return False 


def main():
    input_ = str(input())
    podstroka = str(input())
    solution = Solution()
    print(solution.isSupsecquence(input_, podstroka))

if __name__ == '__main__':
    main()
