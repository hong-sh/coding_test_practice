'''
https://programmers.co.kr/learn/courses/30/lessons/17685

["go","gone","guild"]	7
["abc","def","ghi","jklm"]	4
["word","war","warrior","world"]	15
'''

def find_count(current_node):
    count = 0
    for _, value in current_node.items(): # add count
        if value[0] != 1:
            count += find_count(value[1])
        count += value[0]
    return count

def solution(words):
    answer = 0

    dictionaries = {}
    for word in words: # push N tree words
        i = 0
        current_node = dictionaries
        while i < len(word):
            if word[i] not in current_node:
                new_node = {}
                current_node[word[i]] = [1, new_node]
                current_node = new_node
            else:
                current_node[word[i]][0] += 1
                current_node = current_node[word[i]][1]
            i += 1

    answer = find_count(dictionaries)
    
    return answer



if __name__ == "__main__":
    words = ["go","gone","guild"]
    # words = ["abc","def","ghi","jklm"]
    # words = ["word","war","warrior","world"]
    print(solution(words))