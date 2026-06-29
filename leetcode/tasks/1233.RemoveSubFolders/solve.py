class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)


        return res 


def test():
    solve = Solution()
    print(solve.removeSubfolders(folder=["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(solve.removeSubfolders(folder=["/a","/a/b/c","/a/b/d"]))
    print(solve.removeSubfolders(folder=["/a/b/c","/a/b/ca","/a/b/d"]))

if __name__ == '__main__':
    test()
