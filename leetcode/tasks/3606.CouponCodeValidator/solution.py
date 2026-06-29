from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n, valid_pairs = len(code), []
        
        allowed = {"electronics", "grocery", "pharmacy", "restaurant"}
        priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        code_pattern = re.compile(r'^[A-Za-z0-9_]+$')

        for i in range(n):
            c, b, active = code[i], businessLine[i], isActive[i]
            if not active: continue
            if b not in allowed: continue
            if not c or code_pattern.fullmatch(c) is None: 
                continue

            valid_pairs.append((b, c))
        valid_pairs.sort(key=lambda pair: (priority[pair[0]], pair[1]))
        return [c for _, c in valid_pairs]
