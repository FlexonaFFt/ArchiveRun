from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        answer = 0

        for i in range(k):
            gain = happiness[i] - i
            if gain <= 0: break
            answer += gain
        
        return answer
