from collections import defaultdict
class Solution:
    from typing import List
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())

# Runtime 11 ms, 89 %
# Memory 20.66 mb, 69 %
def main():
    solve = Solution()
    strings1 = ["eat","tea","tan","ate","nat","bat"]
    strings2, strings3 = [''], ["a"]
    print(solve.groupAnagrams(strings1))
    print(solve.groupAnagrams(strings2))
    print(solve.groupAnagrams(strings3))

if __name__ == '__main__':
    main()
