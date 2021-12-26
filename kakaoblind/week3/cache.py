'''
https://programmers.co.kr/learn/courses/30/lessons/17680

캐시크기(cacheSize)	도시이름(cities)	실행시간
3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25
'''

from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache_dict = OrderedDict()
    
    for city in cities:
        city = city.lower()
        if city in cache_dict: # cache hit
            del cache_dict[city]
            cache_dict[city] = ""
            answer += 1
        else: # cache miss
            if len(cache_dict.keys()) < cacheSize:
                cache_dict[city] = ""
            else:
                key = list(cache_dict.keys())[0]
                del cache_dict[key]
                cache_dict[city] = ""
            answer += 5

    return answer


if __name__ == "__main__":
    chacheSize = 2
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
    # cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(chacheSize, cities))