class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        answer, last1, last2 = 0, -1, -1

        for L, R in intervals:
            counter = (last1 >= L) + (last2 >= L)
            if counter >= 2: continue
            elif counter == 1:
                if R == last2: add = R - 1
                else: add = R
                last1, last2 = last2, add 
                answer += 1
            else:
                add1, add2 = R - 1, R
                last1, last2 = add1, add2
                answer += 2
        
        return answer
