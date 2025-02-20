class Solution:
    def decodeString(self, string: str) -> str:
        stack, current_string, current_num = [], '', 0
        for char in string:
            if char == '[':
                stack.append((current_string, current_num))
                current_string = ''
                current_num = 0
            elif char == ']':
                last_string, num = stack.pop()
                current_string = last_string + current_string * num
            elif char.isdigit():
                current_num = current_num * 10 + int(char)
            else:
                current_string += char
        return current_string

# Runtime 0 ms, 100 %
# Memory 17.94 mb, 8.22 %
def main():
    solve = Solution()
    print(solve.decodeString("3[a]2[bc]"))
    print(solve.decodeString("3[a2[c]]"))
    print(solve.decodeString("2[abc]3[cd]ef"))

if __name__ == '__main__':
    main()
