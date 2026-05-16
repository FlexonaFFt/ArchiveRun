'''class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        spisok, result = [], 1
        for section in bank:
            cnt = section.count("1")
            if cnt > 0:
                spisok.append(cnt)
        print(spisok)
        for num in spisok:
            result *= num
        return result
'''

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = bank[0].count('1')
        result = 0

        for i in range(1,len(bank)):
            curr = bank[i].count('1')
            if curr > 0:
                result += prev * curr
                prev = curr

        return result

def main():
    solve = Solution()
    print(solve.numberOfBeams(["011001","000000","010100","001000"]))
    print(solve.numberOfBeams(["000","111","000"]))

main()
