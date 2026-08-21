'''
Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"
'''


class Solution:

    def func(self, nums: list[int]) -> str:
        if not nums: return ''
        output, otsorted = [], sorted(nums)
        start = prev = otsorted[0]

        for curr in otsorted[1:]:
            if curr == prev + 1: prev = curr  
            else: 
                output.append(str(start) if start == prev else f'{start}-{prev}')
                start = prev = curr 

        output.append(str(start) if start == prev else f'{start}-{prev}')
        return ','.join(output)
