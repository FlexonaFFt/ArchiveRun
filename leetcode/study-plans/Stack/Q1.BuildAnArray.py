class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer, stack, tracker = [], [], 0
        for element in range(1, n + 1):
            answer.append("Push")
            if tracker < len(target) and element == target[tracker]:
                tracker += 1
                if tracker == len(target):
                    break
            else: answer.append("Pop")
        return answer
