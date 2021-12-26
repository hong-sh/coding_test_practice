import copy 
def name_compare(students:list):
    students.sort(key=lambda x: x[0])
    return students

def math_compare(students:list):
    students.sort(key=lambda x: x[3], reverse=True)
    buf_s = 0
    buf_e = 0
    for i in range(1, len(students)):
        if students[i][3] == students[buf_s][3]:
            buf_e = i
        elif students[i][3] != students[buf_s][3] and buf_s < buf_e:
            students[buf_s:buf_e+1] = name_compare(copy.deepcopy(students[buf_s:buf_e+1]))
            buf_s = i
        else:
            buf_s = i

    if buf_e == len(students) -1:
            students[buf_s:buf_e+1] = name_compare(copy.deepcopy(students[buf_s:buf_e+1]))
    
    return students

def eng_compare(students:list):
    students.sort(key=lambda x: x[2])
    buf_s = 0
    buf_e = 0
    for i in range(1, len(students)):
        if students[i][2] == students[buf_s][2]:
            buf_e = i
        elif students[i][2] != students[buf_s][2] and buf_s < buf_e:
            students[buf_s:buf_e+1] = math_compare(copy.deepcopy(students[buf_s:buf_e+1]))
            buf_s = i
        else:
            buf_s = i

    if buf_e == len(students) -1:
            students[buf_s:buf_e+1] = math_compare(copy.deepcopy(students[buf_s:buf_e+1]))

    return students

def kor_compare(students:list):
    students.sort(key=lambda x: x[1], reverse=True)
    buf_s = 0
    buf_e = 0
    for i in range(1, len(students)):
        if students[i][1] == students[buf_s][1]:
            buf_e = i
        elif students[i][1] != students[buf_s][1] and buf_s < buf_e:
            students[buf_s:buf_e+1] = eng_compare(copy.deepcopy(students[buf_s:buf_e+1]))
            buf_s = i
        else:
            buf_s = i

    if buf_e == len(students) -1:
            students[buf_s:buf_e+1] = eng_compare(copy.deepcopy(students[buf_s:buf_e+1]))
   


if __name__ == "__main__":
    n = int(input())
    students = []
    for _ in range(n):
        student = input().split()
        students.append((student[0], int(student[1]), int(student[2]), int(student[3])))

    kor_compare(students)
    for student in students:
        print(student)