class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        met, ppr, gls, cnt = 0, 0, 0, 0
        for iteration in garbage:
            if cnt == 0:
                met += iteration.count("M")
                ppr += iteration.count("P")
                gls += iteration.count("G")
                print(met, ppr, gls)
            else:
                now_met = iteration.count("M")
                now_ppr = iteration.count("P")
                now_gls = iteration.count("G")

                if now_met > 0:
                    met += now_met + travel[cnt - 1]
                if now_ppr > 0:
                    ppr += now_ppr + travel[cnt - 1]
                if now_gls > 0:
                    gls += now_gls + travel[cnt - 1]
                print(met, ppr, gls)
            cnt += 1

        return met + ppr + gls

# Решение не проходит первый тест, есть ошибка в алгоритме.
# При этом второй тест пройден
def main():
    solution = Solution()
    print(solution.garbageCollection(["G","P","GP","GG"], [2,4,3]))
    print(solution.garbageCollection(["MMM","PGM","GP"], [3,10]))

if __name__ == '__main__':
    main()
