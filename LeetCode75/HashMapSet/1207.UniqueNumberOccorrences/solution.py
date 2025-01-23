class Solution:
    from typing import List
    def uniqueOccurrences(self, array: List[int]) -> bool:
        counter_list = {}
        for element in array:
            if element not in counter_list:
                counter_list[element] = 1
            counter_list[element] += 1
        occurrences = set()
        for count in counter_list.values():
            if count in occurrences:
                return False
            occurrences.add(count)
        return True

# Runtime 0 ms, 100 %
# Memory 17.80 mb, 56,54 %
def main():
    array1, array2 = [1,2,2,1,1,3], [1,2]
    array3 = [-3,0,1,-3,1,1,1,-3,10,0]
    solution = Solution()
    print(solution.uniqueOccurrences(array1))
    print(solution.uniqueOccurrences(array2))
    print(solution.uniqueOccurrences(array3))

if __name__ == "__main__":
    main()
