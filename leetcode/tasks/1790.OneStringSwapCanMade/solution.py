class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        counter, diff = 0, []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
                diff.append(i)

        if counter == 0:
            return True
        elif counter != 2:
            return False

        i, j = diff
        return s1[i] == s2[j] and s1[j] == s2[i]

# Runtime 0 ms, 100 %
# Memory 17.68 mb, 67.41 %
def main():
    solution = Solution()
    s1, s2 = 'bank', 'kanb'
    s3, s4 = 'attack', 'defend'
    s5, s6 = 'kelb', 'kelb'
    print(solution.areAlmostEqual(s1, s2))
    print(solution.areAlmostEqual(s3, s4))
    print(solution.areAlmostEqual(s5, s6))

if __name__ == '__main__':
    main()
