def solve(grades):
    numeric_grades = [ord(grade) - ord('A') + 1 for grade in grades]
    worst_grade = max(numeric_grades)
    average = sum(numeric_grades) / len(numeric_grades)
    rounded = round(average)
    final_grade = worst_grade - 1
    return chr(final_grade + ord('A') - 1)

def main():
    grades = input().strip()
    print(solve(grades))

if __name__ == '__main__':
    main()