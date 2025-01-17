class Solution:
    from typing import List  
    def compress(self, string_list: List[int]) -> int:
        write, i = 0, 0
        while i < len(string_list):
            char = string_list[i]
            count = 0
            while i < len(string_list) and string_list[i] == char:
                i += 1
                count += 1
            string_list[write] = char 
            write += 1
            if count != 1:
                for digit in str(count):
                    string_list[write] = digit 
                    write += 1
        return write

# Runtime 0 ms, 100 %
# Memory 18.13 mb, 13.69 %
def main():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    solution = Solution()
    print(solution.compress(chars))

if __name__ == '__main__':
    main()
