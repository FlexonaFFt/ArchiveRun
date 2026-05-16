def calculate_average(grades):
    if not grades:
        return 0
    total = sum(student['grade'] for student in grades)
    return total / len(grades)

def filter_above_average_students(grades, average):
    return [student for student in grades if student['grade'] > average]

def main():
    import sys
    input_data = sys.stdin.read().splitlines()

    grades = []
    for line in input_data:
        if line.strip():
            name, grade_str = line.strip().split()
            grades.append({'name': name, 'grade': int(grade_str)})

    average_grade = calculate_average(grades)
    above_average = filter_above_average_students(grades, average_grade)
    names = ' '.join(student['name'] for student in above_average)
    print(names)

if __name__ == "__main__":
    main()
