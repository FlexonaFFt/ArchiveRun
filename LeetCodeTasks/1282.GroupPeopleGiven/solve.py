from collections import defaultdict
class Solution:
    from typing import List
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result, groups = [], defaultdict(list)
        for pid, groupSize in enumerate(groupSizes):
            groups[groupSize].append(pid)
            if len(groups[groupSize]) == groupSize:
                result.append(groups.pop(groupSize))
        return result


def main():
    solve = Solution()
    print(solve.groupThePeople([3,3,3,3,3,1,3]))
    print(solve.groupThePeople([2,1,3,3,3,2]))

if __name__ == '__main__':
    main()
