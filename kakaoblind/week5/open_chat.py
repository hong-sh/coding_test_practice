'''
https://programmers.co.kr/learn/courses/30/lessons/42888

record	result
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
'''

def solution(record):
    answer = []
    
    event_list = []
    id_dict = {}
    for event in record:
        splitted_event = event.split()
        flag, uid = splitted_event[0], splitted_event[1]
        if flag != "Change":
            event_list.append((flag, uid))
    
        if flag != "Leave":
            id_dict[uid] = splitted_event[2]

    for event in event_list:
        if event[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id_dict[event[1]]))
        else:
            answer.append("{}님이 나갔습니다.".format(id_dict[event[1]]))

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))