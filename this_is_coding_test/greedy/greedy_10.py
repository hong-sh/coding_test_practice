import sys
input = sys.stdin.readline

accumulation={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334} 
flowers = int(input())
flower_days = []
for i in range(flowers):
    s_mon, s_day, e_mon, e_day = map(int, input().split())
    flower_days.append((accumulation[s_mon]+s_day, accumulation[e_mon]+e_day))

flower_days.sort()

end_max, x, flower_count = 0, 0, 0
start_day, end_day = 60, 335

while start_day < end_day:
    changed = False
    while x < flowers:
        if flower_days[x][0] > start_day:
            break

        if end_max < flower_days[x][1]:
            end_max = flower_days[x][1]

        changed = True
        x += 1

    if changed:
        flower_count += 1
        start_day = end_max
    else:
        print(0)
        exit(0)

    start_day += 1

print(flower_count)