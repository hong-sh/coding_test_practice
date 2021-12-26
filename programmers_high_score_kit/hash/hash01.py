'''
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

'''

def solution(participant, completion):
    answer = ''

    completion_dict = {}
    for i in range(len(completion)):
        name = completion[i]
        if name in completion_dict:
            completion_dict[name] += 1
        else:
            completion_dict[name] = 1

    for i in range(len(participant)):
        name = participant[i]
        if name in completion_dict:
            completion_dict[name] -= 1
            if completion_dict[name] < 0:
                return name
        else:
            return name

    return answer

if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution(participant, completion))