class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                if row not in rows:
                    rows[row] = set()

                rows[row].add(seat)

        ans = n * 2

        for reserved in rows.values():
            left = all(seat not in reserved for seat in (2, 3, 4, 5))
            middle = all(seat not in reserved for seat in (4, 5, 6, 7))
            right = all(seat not in reserved for seat in (6, 7, 8, 9))

            if left and right:
                families = 2
            elif left or middle or right:
                families = 1
            else:
                families = 0

            ans -= 2 - families

        return ans
