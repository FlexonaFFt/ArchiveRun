class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = maximum = 0
        for height in gain:
            current += height
            if current > maximum:
                maximum = current
        return maximum
