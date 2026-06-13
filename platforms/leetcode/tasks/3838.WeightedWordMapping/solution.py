class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = []

        for curr in words:
            s = 0
            for char in curr:
                s += weights[ord(char) - ord("a")]
            out.append(chr(ord("z") - s % 26))
        return ''.join(out)
