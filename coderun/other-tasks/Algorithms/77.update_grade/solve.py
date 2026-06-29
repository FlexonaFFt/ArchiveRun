# Неправильный ответ на закрытом тесте (id: 12)
def find_the_grade_up(a, b, c):
    first_grades, grades, sred_ball, counter = [a, b, c], [], 0, 0
    def find_sred(grades):
        return (sum(map(int, grades)) / len(grades))

    [grades.append('2') for _ in range(first_grades[0]) if first_grades[0] != 0]
    [grades.append('3') for _ in range(first_grades[1]) if first_grades[1] != 0]
    [grades.append('4') for _ in range(first_grades[2]) if first_grades[2] != 0]

    while sred_ball < 3.5:
        grades.append('5')
        sred_ball = find_sred(grades)
        counter += 1

    return counter

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(find_the_grade_up(a, b, c))

if __name__ == '__main__':
    main()
