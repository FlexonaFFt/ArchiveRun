import collections
class Solution:
    from typing import List
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        longest = collections.defaultdict(int)
        max_len = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j], None)
                if i is not None and i < j:
                    longest[j, k] = longest[i, j] + 1
                    max_len = max(max_len, longest[j, k])
        return max_len if max_len >= 3 else 0


def main():
    solution = Solution()
    print(solution.lenLongestFibSubseq(arr=[1,2,3,4,5,6,7,8]))
    print(solution.lenLongestFibSubseq(arr=[1,3,7,11,12,14,18]))

if __name__ == '__main__':
    main()
