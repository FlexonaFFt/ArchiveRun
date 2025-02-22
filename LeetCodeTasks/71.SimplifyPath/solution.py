class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, components = [], path.split('/')
        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component and component != '.':
                stack.append(component)

        result = '/' + '/'.join(stack)
        return result

# Runtime 0 m, 100 %
# Memory 17.78 mb, 77.10 %
def main():
    solution = Solution()
    print(solution.simplifyPath(path="/home/"))
    print(solution.simplifyPath(path="/home//foo/"))
    print(solution.simplifyPath(path="/home/user/Documents/../Pictures"))
    print(solution.simplifyPath(path="/../"))
    print(solution.simplifyPath(path="/.../a/../b/c/../d/./"))

if __name__ == '__main__':
    main()
