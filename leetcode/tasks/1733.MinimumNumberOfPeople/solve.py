class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        user_langs, need_teach = [set(langs) for langs in languages], set()
        
        for one, two in friendships:
            one, two = one - 1, two - 1
            if user_langs[one] & user_langs[two]:
                continue
            need_teach.add(one)
            need_teach.add(two)
        if not need_teach: return 0
            
        min_to_teach = float('inf')
        for lang in range(1, n + 1):
            counter = 0
            for user in need_teach:
                if lang not in user_langs[user]: counter += 1
            min_to_teach = min(min_to_teach, counter)
        
        return min_to_teach
        

def test():
    solve = Solution()
    print(solve.minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))
    print(solve.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]])) 

if __name__ == '__main__':
    test()       