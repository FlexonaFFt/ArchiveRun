class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counter, result = {}, []
        for integer in arr1:
            if integer not in counter:
                counter[integer] = 1
            else:
                counter[integer] += 1

        for element in arr2:
            result.extend([element] * counter.get(element, 0))

        remaining = sorted([num for num in arr1 if num not in arr2])
        result.extend(remaining)
        return result


def test():
    solution = Solution()
    print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
    print(solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))

if __name__ == '__main__':
    test()
