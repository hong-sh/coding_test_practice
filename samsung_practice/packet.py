
import sys
sys.stdin = open("samsung/sample_input.txt", "r")


def dfs(packet_idx, current_t, cpus):
    if packet_idx == N:
        return True
    
    recv_t, process_t = packet[packet_idx]
    diff_t = recv_t - current_t
    
    for c in range(len(cpus)):
        cpus[c] = max(0, cpus[c] - diff_t)
        
    if (packet_idx, tuple(cpus)) in visited:
        return False
    
    visited.add((packet_idx, tuple(cpus)))
    
    for c in range(len(cpus)):
        total_t = cpus[c] + process_t
        if total_t <= 10: # maximum total time is 10
            copy_cpus = cpus[:]
            cpus[c] = total_t
            if dfs(packet_idx + 1, recv_t, cpus):
                return True
            cpus = copy_cpus
    
    return False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    packet = []
    for _ in range(N):
        packet.append(list(map(int, input().split())))
        
    answer = -1
    for i in range(1, 6): #maximum cpu number is 5
        visited = set()
        cpus = [0] * i
        if dfs(0, 0, cpus):
            answer = i
            break
    
    print(f"#{test_case} {answer}")
    