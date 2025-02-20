class Solution:
    from typing import List 
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean_list, intermediate = [], []
        for kid_cand in candies:
            others_candies = candies.copy()
            others_candies.remove(kid_cand)
            for other in others_candies:
                if kid_cand + extraCandies > other:
                    intermediate.append(True)
                else:
                    intermediate.append(False)
            others_candies = candies
            if all(intermediate):
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        return boolean_list

# Выдает неправильный ответ
def main():
    solution = Solution()
    cand_list, extras = [2, 3, 5, 1, 3], 3
    print(solution.kidsWithCandies(candies=cand_list, extraCandies=extras))

if __name__ == '__main__':
    main()
