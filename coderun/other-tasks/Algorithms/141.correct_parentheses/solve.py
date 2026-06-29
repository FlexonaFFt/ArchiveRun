def is_valid_parentheses(sequence):
    brackets_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in sequence:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or stack[-1] != brackets_map[char]:
                return 'no'
            stack.pop()
    return 'yes' if not stack else 'no'

def main():
    brackets = input().strip()
    print(is_valid_parentheses(brackets))

if __name__ == '__main__':
    main()
