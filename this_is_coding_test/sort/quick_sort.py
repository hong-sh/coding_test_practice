
arr = [38, 27, 43, 3, 9, 82, 43, 10]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    pivot = arr[mid]
    left_arr, eqaul_arr, right_arr = [], [], []
    
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            eqaul_arr.append(num)
            
    return quick_sort(left_arr) +eqaul_arr+ quick_sort(right_arr)


print(quick_sort(arr))