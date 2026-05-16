# Решение по какой-то причине не проходит первый тест
# Хотя я считаю, что задачу решил верно
# Затем я понял в чем моя ошибка. Недочитал условие задачи
class Solution:
    from typing import List  
    def compress(self, string_list: List[int]) -> int:
        main_len, ans_dict = len(string_list), {}
        for num in string_list:
            if num not in ans_dict:
                ans_dict[num] = 1
            else:
                ans_dict[num] += 1
        
        if main_len < 10:
            result_list = []
            for key, value in ans_dict.items():
                result_list.append(key)
                result_list.append(str(value))
            return len(result_list)
        if main_len == 1:
            return 1
        else:
            write_index = 0
            for key, value in ans_dict.items():
                string_list[write_index] = key
                write_index += 1
                if value > 1:
                    for digit in str(value):
                        string_list[write_index] = digit 
                        write_index += 1
            return write_index


def main():
    chars = ["a","a","b","b","c","c","c"]
    solution = Solution()
    print(solution.compress(chars))

if __name__ == '__main__':
    main()
