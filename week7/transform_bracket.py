'''
https://programmers.co.kr/learn/courses/30/lessons/60058

p	result
"(()())()"	"(()())()"
")("	"()"
"()))((()"	"()(())()"
'''

def valid_correct(u):
    stack = []
    for ch in u:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True

def divide_uv(v):
    u, open_cnt, close_cnt = "", 0, 0
    for i in range(len(v)):
        if v[i] == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        u += v[i]
        if len(u) % 2 == 0 and open_cnt == close_cnt:
            v = v[i+1:]
            break
    
    return u, v

def create_new(u):
    new_u = ""
    for ch in u[1:len(u)-1]:
        if ch == "(":
            new_u += ")"
        else:
            new_u += "("
    
    return new_u 

def recursive(v):
    if not v:
        return ""

    u, v = divide_uv(v)
    is_correct = valid_correct(u)

    if is_correct:
        return u + recursive(v)
    else:
        return '(' + recursive(v) + ')' + create_new(u)

def solution(p):
    answer = ''

    if valid_correct(p):
        return p

    answer = recursive(p)

    return answer

if __name__ == "__main__":
    p = ")("
    print(solution(p))
