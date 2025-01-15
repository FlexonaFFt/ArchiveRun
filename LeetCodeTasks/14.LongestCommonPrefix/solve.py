class Solution:
    from typing import List 
    def longestCommonPrefix(self, string: List[str]) -> str:
        if not string:
            return ''

        default = string[0]
        for str in string[1:]:
            # Пока префикс не является подстрокой текущей строки
            while str[:len(default)] != default:
                default = default[:-1]
                if not default:
                    return ''
        return default

# Runtiem 0ms, Beats 100%
def main():
    strings = ['flower', 'flow', 'flight']
    solution = Solution()
    print(solution.longestCommonPrefix(string=strings))

if __name__ == '__main__':
    main()
