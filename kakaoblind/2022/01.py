'''
id_list	report	k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]

'''
def solution(id_list, report, k):
    answer = []
    
    report_dict = {}
    reported_dict = {}

    for id in id_list:
        report_dict[id] = []
        reported_dict[id] = []

    for i in range(len(report)):
        x, y = report[i].split(' ')
        report_dict[x].append(y)
        reported_dict[y].append(x)

    for id in id_list:
        mail_cnt = 0
        for y in report_dict[id]:
            if len(set(reported_dict[y])) >= k:
                mail_cnt += 1
        answer.append(mail_cnt)

    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))