


arr = [1, 5, 2, 3, 2, 7, 4]
len_arr = len(arr)

for i in range(len_arr):
    for j in range(i, len_arr):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

print(arr)
            