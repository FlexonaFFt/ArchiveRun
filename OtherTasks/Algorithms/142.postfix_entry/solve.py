def evaluate_postfix(entry):
    stack, tokens = [], entry.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in '+-*':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    return stack[0]

def main():
    entry = input().strip()
    print(evaluate_postfix(entry))

if __name__ == '__main__':
    main()