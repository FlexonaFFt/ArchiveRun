from typing import List 

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        all_apples, answer = 0, 0
        local_counter_container = 0
        capacity.sort(reverse = True)
        
        for apple in apple: all_apples += apple
        for container in capacity:
            if all_apples > local_counter_container:
                local_counter_container += container
                answer += 1
            else: break 

        return answer
