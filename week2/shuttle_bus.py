'''
https://programmers.co.kr/learn/courses/30/lessons/17678

n	t	m	timetable	answer
1	1	5	["08:00", "08:01", "08:02", "08:03"]	"09:00"
2	10	2	["09:10", "09:09", "08:00"]	"09:09"
2	1	2	["09:00", "09:00", "09:00", "09:00"]	"08:59"
1	1	5	["00:01", "00:01", "00:01", "00:01", "00:01"]	"00:00"
1	1	1	["23:59"]	"09:00"
10	60	45	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	"18:00"
'''

def solution(n, t, m, timetable):
    answer = ''
    timetable_m = []
    shuttle_m = []
    for time in timetable:
        hour, min = int(time[:2]), int(time[3:])
        timetable_m.append(hour*60+min)
    
    timetable_m.sort()

    for i in range(n):
        shuttle_m.append(540 + (i*t))

    idx_list = []
    global_count = 0
    for i in range(len(shuttle_m)):
        local_count = 0

        while (local_count < m and timetable_m[global_count] <= shuttle_m[i]):
            local_count += 1
            global_count += 1

            if global_count == len(timetable_m):
                break


    available_time = 540 + t*(n-1)
    if len(timetable_m) >= global_count and available_time >= timetable_m[global_count-1] and global_count >= m:
        available_time = timetable_m[global_count-1] -1

    available_h = format(available_time // 60, '02') 
    available_m = format(available_time % 60, '02')

    answer = '{}:{}'.format(available_h, available_m)
    return answer

if __name__ == "__main__":
    n, t, m = 1, 1, 5
    timetable = ["08:00", "08:01", "08:02", "08:03"]
    print(solution(n, t, m, timetable))