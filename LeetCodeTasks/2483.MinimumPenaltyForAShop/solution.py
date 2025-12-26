class Solution:
    def bestClosingTime(self, customers: str) -> int:
        fine, idx, minPenalty = 0, 0, 0
        for i in range(len(customers)):
            idx += -1 if customers[i] == 'Y' else 1

            if idx < minPenalty:
                fine = i + 1
                minPenalty = idx

        return fine
