'''
진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.

2 ≦ n ≦ 16
0 ＜ t ≦ 1000
2 ≦ m ≦ 100
1 ≦ p ≦ m

n	t	m	p	result
2	4	2	1	"0111"
16	16	2	1	"02468ACE11111111"
16	16	2	2	"13579BDF01234567"
'''

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    number = 0
    converted_num = ""
    while len(converted_num) < t * m:
        converted_num += convert(number, n)
        number += 1

    i = p-1
    while len(answer) < t:
        answer += converted_num[i]
        i = i + m

    return answer

if __name__ == "__main__":
    n = 16
    t = 16
    m = 2
    p = 1
    print(solution(n, t, m, p))