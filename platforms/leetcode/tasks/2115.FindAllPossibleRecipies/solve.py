class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        supplies = set(supplies) # type: ignore
        recipes = dict(zip(recipes, ingredients)) # type: ignore
        made = []

        while True:
            new_recipe_made = False
            for rcp, igs in [*recipes.items()]: # type: ignore
                if not all(i in supplies for i in igs):
                    continue
                made.append(rcp)
                supplies.add(rcp) # type: ignore
                del recipes[rcp]
                new_recipe_made = True

            if not new_recipe_made:
                break
        return made


def main():
    solution = Solution()
    print(solution.findAllRecipes(recipes=["bread"],
        ingredients=[["yeast","flour"]],
        supplies=["yeast","flour","corn"]))
    print(solution.findAllRecipes(recipes=["bread","sandwich"],
        ingredients=[["yeast","flour"],["bread","meat"]],
        supplies=["yeast","flour","meat"]))
    print(solution.findAllRecipes(recipes=["bread","sandwich","burger"],
        ingredients=[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
        supplies=["yeast","flour","meat"]))

main()
