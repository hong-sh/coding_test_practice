'''
https://programmers.co.kr/learn/courses/30/lessons/17686

파일명	HEAD	NUMBER	TAIL
foo9.txt	foo	9	.txt
foo010bar020.zip	foo	010	bar020.zip
F-15	F-	15	(빈 문자열)

입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

'''
import re

def solution(files):
    answer = []

    splited_files = []
    for file in files:
        number = re.search("[\d]{1,5}", file).group()
        splited_file = file.split(number)
        head, tail = splited_file[0], splited_file[1]
        splited_files.append((head.lower(), int(number), tail, file))

    splited_files.sort(key= lambda x : (x[0], x[1]))

    for splited_file in splited_files:
        answer.append(splited_file[3])

    return answer


if __name__ == "__main__":
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    # files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    print(solution(files))