lookup_tables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',\
     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def solution(msg):
    answer = []
    i = 0
    while i < len(msg):
        key = ""
        for j in range(len(lookup_tables)-1, -1, -1): # find longest word in lookup tables
            key = lookup_tables[j]
            if msg[i:i+len(key)] == key: # split msg for match length key
                answer.append(j+1)
                break

        lookup_tables.append(msg[i:i+len(key)+1]) # append key + 1 in lookup tables
        i += len(key)

    return answer

if __name__ == "__main__":
    msg = "TOBEORNOTTOBEORTOBEORNOT"
    print(solution(msg))