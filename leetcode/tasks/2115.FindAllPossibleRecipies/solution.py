class Solution:
    def findAllRecipes(self, recepes: list[str], ingridients: list[list[str]],
        supplies: list[str]):
            spisok, result = {}, []
            for recept, ing in zip(recepes, ingridients):
                spisok[recept] = ing

            for key, value in spisok.items():
                main, cnt = len(value), 0
                for val in value:
                    if val in supplies:
                        cnt += 1
                if cnt == main:
                    result.append(key)
                    supplies.append(key)

            return result

# Не прошло 51 тест
def main():
    solution = Solution()
    print(solution.findAllRecipes(recepes=["bread"],
        ingridients=[["yeast","flour"]],
        supplies=["yeast","flour","corn"]))
    print(solution.findAllRecipes(recepes=["bread","sandwich"],
        ingridients=[["yeast","flour"],["bread","meat"]],
        supplies=["yeast","flour","meat"]))
    print(solution.findAllRecipes(recepes=["bread","sandwich","burger"],
        ingridients=[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
        supplies=["yeast","flour","meat"]))

main()
