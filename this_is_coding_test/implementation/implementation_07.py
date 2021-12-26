def get_best_compress(s:str):
    best_compress = len(s)
    for i in range(1, len(s) // 2 + 1):
        compress = ""
        prev_str = s[0:i]
        count = 1
        
        for j in range(i, len(s), i):
            slicing_str = s[j:j+i]

            if prev_str == slicing_str:
                count += 1
            else:
                if count > 1:
                    compress += str(count) + prev_str
                else:
                    compress += prev_str
                count = 1

            prev_str = slicing_str

        compress += str(count) + prev_str if count >=2 else prev_str
        best_compress = min(best_compress, len(compress))

    return best_compress

if __name__ == "__main__":
    s = input()
    print(get_best_compress(s))