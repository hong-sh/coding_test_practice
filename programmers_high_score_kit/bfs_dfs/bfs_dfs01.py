'''
numbers	target	return
[1, 1, 1, 1, 1]	3	5
'''
def dfs(numbers, idx, target, tmp, count):
    if idx == len(numbers):
        return count + 1 if tmp == target else count
    
    count1 = dfs(numbers, idx + 1, target, tmp + numbers[idx], count)
    count2 = dfs(numbers, idx + 1, target, tmp + (-1 * numbers[idx]), count)
    
    return count1 + count2
    

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, target, 0, 0)
    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))