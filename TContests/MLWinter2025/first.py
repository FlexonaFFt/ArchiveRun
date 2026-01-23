class Solution:
    def min_number_no_leading_zeros(self, s: str) -> str:
        counts = [0] * 10
        for ch in s:
            counts[ord(ch) - 48] += 1

        first = 0
        for d in range(1, 10):
            if counts[d]:
                first = d
                counts[d] -= 1
                break

        out = [str(first)]
        if counts[0]:
            out.append("0" * counts[0])
        for d in range(1, 10):
            if counts[d]:
                out.append(str(d) * counts[d])

        return "".join(out)


if __name__ == "__main__":
    s = input().strip()
    solver = Solution()
    print(solver.min_number_no_leading_zeros(s))
