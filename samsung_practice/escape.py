
import sys
sys.stdin = open("samsung/sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def get_max_height(idx, visited, a, b, h):
    if visited == (1 << N) - 1:
        return h
    
    if (idx,h) in dp:
        return dp[(idx,h)]
    
    max_height = h
    for i in range(idx+1, N*6):
        box = boxs[i]
        if visited & (1 << box[3]) != 0:
            continue
        
        if box[0] >= a and box[1] >= b:
            max_height = max(max_height, get_max_height(i, visited | (1 << box[3]), box[0], box[1], h + box[2]))
        
        
    dp[(idx,h)] = max_height
    return max_height

for test_case in range(1, T + 1):
    N = int(input())
    
    boxs = []
    for i in range(N):
        box = list(map(int, input().split()))
        # box = sorted(box, reverse=True)
        boxs.append([box[0], box[1], box[2], i]) # a, b, h, idx
        boxs.append([box[1], box[0], box[2], i])
        boxs.append([box[0], box[2], box[1], i])
        boxs.append([box[2], box[0], box[1], i])
        boxs.append([box[1], box[2], box[0], i])
        boxs.append([box[2], box[1], box[0], i])
        
    boxs.sort(key=lambda x: (x[0]* x[1]))
    visited = 0 
    
    dp = {}
    max_height = 0
    for i in range(N*6):
        box = boxs[i]
        visited = (1 << box[3])
        max_height = max(max_height, get_max_height(i, visited, box[0], box[1], box[2]))
    
    print(f"#{test_case} {max_height}") 
    
    