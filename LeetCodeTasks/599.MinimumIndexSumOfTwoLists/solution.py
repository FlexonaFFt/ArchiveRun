class Solution:
    from typing import List
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_map = {rest: idx for idx, rest in enumerate(list1)}
        minSum, res = float('inf'), []
        for idx, rest in enumerate(list2):
            if rest in idx_map:
                currSum = idx_map[rest] + idx
                if currSum < minSum:
                    minSum = currSum
                    res = [rest]
                elif currSum == minSum:
                    res.append(rest)
        return res

# Runtime 4 ms, 90.15 %
# Memory 18.14 mb, 70.02 %
def main():
    solution = Solution()
    print(solution.findRestaurant(list1=["Shogun","Tapioca Express","Burger King","KFC"],
        list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
    print(solution.findRestaurant(list1=["Shogun","Tapioca Express","Burger King","KFC"],
        list2=["KFC","Shogun","Burger King"]))
    print(solution.findRestaurant(list1=["happy","sad","good"],
        list2=["sad","happy","good"]))

if __name__ == '__main__':
    main()
