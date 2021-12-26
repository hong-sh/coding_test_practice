'''
https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer

if __name__ == "__main__":
    phone_book = ["12","123","1235","567","88"]
    print(solution(phone_book))