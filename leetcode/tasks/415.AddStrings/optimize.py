class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result, carry = [], 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 and j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(reversed(result))

'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []  # Список для хранения результата
        carry = 0    # Переменная для хранения переноса
        i = len(num1) - 1  # Индекс для num1 (начинаем с конца)
        j = len(num2) - 1  # Индекс для num2 (начинаем с конца)

        # Пока есть цифры в num1, num2 или есть перенос
        while i >= 0 or j >= 0 or carry:
            # Берем цифру из num1, если она есть
            digit1 = int(num1[i]) if i >= 0 else 0
            # Берем цифру из num2, если она есть
            digit2 = int(num2[j]) if j >= 0 else 0

            # Складываем цифры и перенос
            total = digit1 + digit2 + carry
            # Записываем последнюю цифру результата
            result.append(str(total % 10))
            # Обновляем перенос
            carry = total // 10

            # Переходим к следующим цифрам
            i -= 1
            j -= 1

        # Разворачиваем результат и объединяем в строку
        return ''.join(reversed(result))
'''
