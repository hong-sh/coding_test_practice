'''
https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
'''

def solution(genres, plays):
    answer = []
    geners_dict = {}
    plays_dict = {}

    for i in range(len(genres)):
        if genres[i] in geners_dict:
            geners_dict[genres[i]] += plays[i]
            plays_dict[genres[i]].append((i, plays[i]))
        else:
            geners_dict[genres[i]] = plays[i]
            plays_dict[genres[i]] = [(i, plays[i])]

    geners_dict = sorted(geners_dict.items(), key= lambda x : x[1], reverse=True)
    for key, value in geners_dict:
        play_list = plays_dict[key]
        play_list.sort(key= lambda x : (-x[1], x[0]))
        cnt = 0
        for play in play_list:
            answer.append(play[0])
            cnt += 1
            if cnt == 2:
                break

    return answer


if __name__ == "__main__":
    geners = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(geners, plays))