'''
https://programmers.co.kr/learn/courses/30/lessons/60057

s	result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
'''

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        compress_list = [[1, s[0:i]]]
        for j in range(i, len(s), i):
            if s[j:j+i] == compress_list[-1][1]:
                compress_list[-1][0] += 1
            else:
                compress_list.append([1, s[j:j+i]])
        compressed_str = ""
        for compress in compress_list:
            if compress[0] != 1:
                compressed_str += "{}{}".format(str(compress[0]), compress[1])
            else:
                compressed_str += compress[1]

        answer = min(len(compressed_str), answer)

    return answer


if __name__ == "__main__":
    s = "xababcdcdababcdcd"
    print(solution(s))