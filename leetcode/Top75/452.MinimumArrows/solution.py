from typing import List 

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Сортируем шарики по возрастанию, по координате x_end
        points.sort(key=lambda x: x[1])
        counter, arrow_x = 0, None 

        # Стреляем в конец первого, ещё не лопнувшего шарика
        # Пропускаем все шарики, которые эта стрела задевает
        # Когда встречаем шарик, правее текущей, то это новая стрела
        for start, end in points:
            if arrow_x is None or start > arrow_x:
                counter += 1
                arrow_x = end 

        return counter
