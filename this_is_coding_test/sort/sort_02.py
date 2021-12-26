def increase(students:list):
    students.sort(key=lambda x: x[1])
    return students

if __name__ == "__main__":
    n = int(input())
    students = []
    for _ in range(n):
        name, score = input().split()
        students.append((name, int(score)))

    increase(students)
    for student in students:
        print(student[0])