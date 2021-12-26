'''
https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3

info	query	result
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	[1,1,1,1,2,4]

'''

def solution(info, query):
    answer = []

    for i in range(len(info)):
        splitted = info[i].split()
        info[i] = (set(splitted[:-1]), int(splitted[-1]))

    for q in query:
        q = q.replace("and", "")
        q = q.replace("-", "")
        splitted = q.split()
        q = (set(splitted[:-1]), int(splitted[-1]))

        cnt = 0
        for i in info:
            inter = q[0].intersection(i[0])
            if len(inter) == len(q[0]) and i[1] >= q[1]:
                cnt +=1
        answer.append(cnt)

    return answer

# import re

# def solution(info, query):
#     answer = []

#     for q in query:
#         lang, _ , job, _ , career, _, food, score = q.split()
#         lang = "\w+" if lang == "-" else lang
#         job = "\w+" if job == "-" else job
#         career = "\w+" if career == "-" else career
#         food = "\w+" if food == "-" else food
#         cnt = 0
#         for i in info:
#             m = re.match('(' + lang + ') (' + job + ') (' + career + ') (' + food + ') (\d)', i)
#             if m != None:
#                 i_ = i.split()
#                 if int(score) <= int(i_[-1]):
#                     cnt += 1
                
#         answer.append(cnt)

#     return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))