'''
https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3
'''

from collections import Counter
import re

def compute_jacard(set1:list, set2:list):
    intersection = list((Counter(set1) & Counter(set2)).elements())
    union = list((Counter(set1) | Counter(set2)).elements())

    jacard = 1
    if len(intersection) != 0 or len(union) != 0:
        jacard = len(intersection) / len(union)

    return jacard

if __name__ == "__main__":
    str1 = input().lower()
    str2 = input().lower()

    str1_set = []
    str2_set = []

    for i in range(0, len(str1)):
        subset = str1[i:i+2]
        if re.match("[a-z]{2}", subset) and len(subset) == 2:
            str1_set.append(subset)

    for i in range(0, len(str2)):
        subset = str2[i:i+2]
        if re.match("[a-z]{2}", subset) and len(subset) == 2:
            str2_set.append(subset)

    jacard = compute_jacard(str1_set, str2_set)

    print(int(jacard * 65536))