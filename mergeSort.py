def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_arr = arr[0:middle]
        right_arr = arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge depth
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(left_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [16, 27, 77, 71, 70, 75, 48, 19, 110]
merge_sort(arr_test)
print(arr_test)
