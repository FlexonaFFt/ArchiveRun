class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        max_length = max(len(v1_parts), len(v2_parts))
        
        for i in range(max_length):
            num1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            num2 = int(v2_parts[i]) if i < len(v2_parts) else 0
            if num1 < num2: return -1
            elif num1 > num2: return 1
        return 0

# Runtime 0 ms, 100 %
# Memory 17.61 mb, 87.98 %
if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.2", "1.10")) 
    print(sol.compareVersion("1.01", "1.001")) 
    print(sol.compareVersion("1.0", "1.0.0.0")) 
