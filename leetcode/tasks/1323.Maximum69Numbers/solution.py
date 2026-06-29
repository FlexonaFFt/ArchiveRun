class Solution:
    def maximum69Number(self, num: int):
        counter, lst = [], []
        counter.append(num)
        for char in str(num):
            lst.append(char)
        
        chislo2 = num: 
        for i in range(len(lst)):
            if lst[i] == '6': lst[i] = '9'
            elif lst[i] == '9': lst[i] = '6'

            chislo = ''.join(lst)
            chislo = int(chislo)
            counter.append(chislo)

        return counter


def test():
    solve = Solution()
    print(solve.maximum69Number(num=9669))


if __name__ == '__main__':
    test()
