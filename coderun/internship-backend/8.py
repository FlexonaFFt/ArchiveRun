class MySolution:

    def func(self, string: str) -> str: 
        stack, mapp = [], {")": "(", "]": "[", "}": "{"}

        for curr in string:
            if curr in mapp.values():
                stack.append(curr)
            elif curr in mapp:
                if not stack or stack.pop() != mapp[curr]:
                    return 'no'
        
        return 'yes' if not stack else 'no'


    def main(self) -> None:
        input_string = str(input())
        print(self.func(input_string))


if __name__ == '__main__':
    MySolution().main()