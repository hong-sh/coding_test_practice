'''
https://programmers.co.kr/learn/courses/30/lessons/17676
'''

'''
O(N^2) time complexity
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (96.45ms, 10.4MB)
테스트 3 〉	통과 (159.06ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (3.22ms, 10.2MB)
테스트 6 〉	통과 (3.53ms, 10.3MB)
테스트 7 〉	통과 (86.94ms, 10.4MB)
테스트 8 〉	통과 (86.72ms, 10.4MB)
테스트 9 〉	통과 (1.66ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.09ms, 10.2MB)
테스트 12 〉	통과 (86.66ms, 10.4MB)
테스트 13 〉	통과 (3.27ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (1070.52ms, 10.6MB)
테스트 19 〉	통과 (341.95ms, 10.4MB)
테스트 20 〉	통과 (345.26ms, 10.4MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
테스트 22 〉	통과 (0.02ms, 10.3MB)
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

'''
O(NlogN) time complexity
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (2.66ms, 10.5MB)
테스트 3 〉	통과 (2.59ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.40ms, 10.2MB)
테스트 6 〉	통과 (0.35ms, 10.3MB)
테스트 7 〉	통과 (2.58ms, 10.5MB)
테스트 8 〉	통과 (2.46ms, 10.5MB)
테스트 9 〉	통과 (0.37ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.2MB)
테스트 12 〉	통과 (2.59ms, 10.4MB)
테스트 13 〉	통과 (0.36ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (5.10ms, 10.7MB)
테스트 19 〉	통과 (4.89ms, 10.7MB)
테스트 20 〉	통과 (5.17ms, 10.6MB)
테스트 21 〉	통과 (0.05ms, 10.3MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
'''
def solution2(lines): # solution 2 is n log n time complexity
    time_list = []
    for i in range(len(lines)):
        line = lines[i].split()
        end_time, process_time = line[1], line[2]
        sep_end_time = end_time.split(":")
        end_second = float(sep_end_time[0]) * 3600 + float(sep_end_time[1])*60 + float(sep_end_time[2]) # time to second
        start_second = end_second - float(process_time[:(len(process_time)-1)]) + 0.001 # compute start second
        time_list.append((start_second, "s"))
        time_list.append((end_second+1, "e"))

    time_list.sort(key=lambda x : x[0]) # log n

    max_count = -999
    count = 0
    for time in time_list: # count concurrent process, n
        if time[1] == "s":
            count += 1
        if time[1] == "e":
            count -= 1
        max_count = max(max_count, count)

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
    print(solution2(lines))