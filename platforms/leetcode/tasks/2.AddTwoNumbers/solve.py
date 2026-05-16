# Этот код не учитывает, что на вход подаются связанные списки
def solve_function(list1, list2):
    reversed_list1 = list1[::-1]
    reversed_list2 = list2[::-1]
    string1 = ''.join(map(str, reversed_list1))
    string2 = ''.join(map(str, reversed_list2))
    sum_result = int(string1) + int(string2)
    string_result = str(sum_result)
    reversed_result = string_result[::-1]
    reversed_list = [int(char) for char in reversed_result]
    return reversed_list


def main():
    list1 = [9, 9, 9, 9, 9, 9, 9]
    list2 = [9, 9, 9, 9]
    print(solve_function(list1, list2))

if __name__ == '__main__':
    main()
