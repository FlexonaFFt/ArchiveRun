class Solution:
    from typing import List
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashTable = {}
        for block in nums1:
            if block[0] not in hashTable:
                hashTable[block[0]] = block[1]
        for block in nums2:
            if block[0] not in hashTable:
                hashTable[block[0]] = block[1]
            else:
                hashTable[block[0]] += block[1]
        result = [[key, value] for key, value in hashTable.items()]
        result.sort()
        return result

# Runtime 0 ms, 100 %
# Memory 17.96 mb, 62.54 %
def main():
    solution = Solution()
    print(solution.mergeArrays(nums1=[[1,2],[2,3],[4,5]], nums2=[[1,4],[3,2],[4,1]]))
    print(solution.mergeArrays(nums1=[[2,4],[3,6],[5,5]], nums2=[[1,3],[4,3]]))

if __name__ == '__main__':
    main()
