'''
https://programmers.co.kr/learn/courses/30/lessons/72414

play_time	adv_time	logs	result
"02:03:55"	"00:14:15"	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	"01:30:59"
"99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	"01:00:00"
"50:00:00"	"50:00:00"	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	"00:00:00"

'''
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s



# def s_to_time(s):
#     h = s // 3600
#     s -= h * 3600
#     m = s // 60
#     s -= m * 60

#     h = str(h).zfill(2)
#     m = str(m).zfill(2)
#     s = str(s).zfill(2)

#     time = h + ":" + m + ":" + s
#     return time

# def time_to_s(time):
#     h, m, s = time.split(":")
#     time_s = int(h) * 3600 + int(m) * 60 + int(s)

#     return time_s


# def solution(play_time, adv_time, logs):
#     answer = ''

#     play_s = time_to_s(play_time)
#     adv_s = time_to_s(adv_time)

#     time_line = [0] * play_s
#     for log in logs:
#         log_start , log_end = log.split("-")
        
#         log_start_s = time_to_s(log_start)
#         log_end_s = time_to_s(log_end)

#         for i in range(log_start_s, log_end_s):
#             time_line[i] += 1

#     max_sum = -999
#     max_idx = 0
#     for i in range(0, len(time_line)):
#         adv_sum = sum(time_line[i:i+adv_s])
#         if max_sum < adv_sum:
#             max_sum = adv_sum
#             max_idx = i

#     return s_to_time(max_idx)



# def solution(play_time, adv_time, logs):
#     answer = ''
#     answer_s = 0
#     play_h, play_m, play_s = play_time.split(":")
#     play_time_s = int(play_h) * 3600 + int(play_m) * 60 + int(play_s)
    
#     adv_h, adv_m, adv_s = adv_time.split(":")
#     adv_time_s = int(adv_h) * 3600 + int(adv_m) * 60 + int(adv_s)

#     logs_s = []
#     for log in logs:
#         log_start , log_end = log.split("-")
        
#         log_start_h, log_start_m, log_start_s = log_start.split(":")
#         log_end_h, log_end_m, log_end_s = log_end.split(":")

#         log_start_time_s = int(log_start_h) * 3600 + int(log_start_m) * 60 + int(log_start_s)
#         log_end_time_s = int(log_end_h) * 3600 + int(log_end_m) * 60 + int(log_end_s)
#         log_adv_start_time_s = log_start_time_s + adv_time_s
#         log_adv_end_time_s = log_end_time_s + adv_time_s

#         # if log_start_time_s + adv_time_s < log_end_time_s:
#         #     log_end_time_s = log_start_time_s + adv_time_s

#         logs_s.append((log_start_time_s, "s"))
#         logs_s.append((log_end_time_s, "e"))
#         logs_s.append((log_adv_start_time_s, "a"))
#         logs_s.append((log_adv_end_time_s, "a"))

#     logs_s.sort(key=lambda x : x[0])

#     if (play_time_s - adv_time_s) < logs_s[0][0]:
#         answer_s = play_time_s - adv_time_s

#     max_cnt, local_cnt = -999, 0
#     for log_s in logs_s:
#         if log_s[1] == "a":
#             local_cnt -= 1
#             if max_cnt < local_cnt:
#                 max_cnt = local_cnt
#                 answer_s = log_s[0] - adv_time_s

#         elif log_s[1] == "s":
#             local_cnt += 1
#         elif log_s[1] == "e":
#             local_cnt += 1

#     return s_to_time(answer_s)


if __name__ == "__main__":
    # "02:03:55"	"00:14:15"	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	"01:30:59"
    # "99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	"01:00:00"
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

    print(solution(play_time, adv_time, logs))