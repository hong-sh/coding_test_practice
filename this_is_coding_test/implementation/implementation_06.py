import re


def re_sort_list(input_list:list):
    char_list = re.findall("[A-Z]", input_list)
    int_list = re.findall("[0-9]", input_list)
    char_list.sort()
    int_sum = 0
    for integer in int_list:
        int_sum += int(integer)
    
    string = ""
    for char in char_list:
        string += char
    
    string += str(int_sum)
    return string

if __name__ == "__main__":
    input_list = input()
    print(re_sort_list(input_list))