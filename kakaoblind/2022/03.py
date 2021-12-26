'''
fees	records	result
[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]


5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600

'''
import math

def time2min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def cal_fee(total_min, fees):
    fee = fees[1]
    if total_min > fees[0]:
            fee += math.ceil((total_min - fees[0]) / fees[2]) * fees[3]
    return fee

def solution(fees, records):
    answer = []
    records_dict = {}
    fees_dict = {}

    for record in records:
        time, number, inout = record.split(' ')
        minute = time2min(time)
        if number not in fees_dict:
            fees_dict[number] = 0

        if number not in records_dict:
            records_dict[number] = []

        records_dict[number].append([minute, inout])

    for key, value in records_dict.items():
        
        if len(value) % 2 != 0:
            value.append([time2min("23:59"), "OUT"])

        total_min = 0
        i = 0
        while i < len(value):
            total_min += value[i+1][0] - value[i][0]
            i += 2
        
        fee = cal_fee(total_min, fees)
        fees_dict[key] = fee

    fee_list = sorted(fees_dict.items(), key= lambda x : x[0])
    for fee in fee_list:
        answer.append(fee[1])

    return answer


if __name__ == "__main__":
    fees = [1, 461, 1, 10]
    records = ["00:00 1234 IN"]
    # [14600, 34400, 5000]
    print(solution(fees, records))