class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        time = hour + minutes / 60
        diff = (11 * time) % 12
        return min(diff, 12 - diff) * 30
