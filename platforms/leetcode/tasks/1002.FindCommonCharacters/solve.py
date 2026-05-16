class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        import collections
        result = collections.Counter(words[0])
        for word in words:
            result &= collections.Counter(word)
        return list(result.elements())
