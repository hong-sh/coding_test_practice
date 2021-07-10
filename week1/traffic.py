'''
https://programmers.co.kr/learn/courses/30/lessons/17676
'''

def solution(lines):
    s_e_list = []
    for i in range(len(lines)):
        line = lines[i].split()
        end_time, process_time = line[1], line[2]
        sep_end_time = end_time.split(":")
        end_second = float(sep_end_time[0]) * 3600 + float(sep_end_time[1])*60 + float(sep_end_time[2]) # time to second
        start_second = end_second - float(process_time[:(len(process_time)-1)]) + 0.001 # compute start second
        s_e_list.append((start_second, end_second))

    s_e_list.sort(key=lambda x : x[0])
    max_count = -999
    for i in range(len(s_e_list)):
        s_count = 1
        e_count = 1
        s_second, e_second = s_e_list[i][0], s_e_list[i][1]
        for j in range(len(s_e_list)):
            if i == j : # skip same log
                continue

            comp_s_second, comp_e_second = s_e_list[j][0], s_e_list[j][1]

            if comp_s_second - e_second > 1: # skip log for time complexity
                break
            
            if s_second <= comp_e_second and comp_s_second < s_second + 1: # compare to log start second 
                s_count += 1
            if e_second <= comp_e_second and comp_s_second < e_second + 1: # compare to log end second
                e_count += 1

        max_count = max(max_count, max(s_count, e_count))

    answer = max_count
    return answer

if __name__ == "__main__":
    lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
    ]

    # lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
    # lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(lines))