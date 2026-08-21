'''
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.
'''

class Solution:
    def rle_func(self, string: str) -> str:
        if not string: return '' 
        updated, counter = [], 1  

        for i in range(1, len(string)):
            if string[i] == string[i - 1]: 
                counter += 1
            else: 
                if counter > 1:
                    updated.append(f'{string[i - 1]}{counter}')
                    counter = 1
                else: updated.append(f'{string[i - 1]}')
        
        updated.append(f'{string[-1]}{counter}' if counter > 1 else string[-1])
        
        return ''.join(updated)