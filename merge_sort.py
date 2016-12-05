some_arr = [1, 5, 2, 4, 23, 2]

def merge_sort(arr):
    #list is more than just one element
    if len(arr) > 1:
        #break arr into 2 pieces
        mid = len(arr) / 2
        left = arr[:mid]
        right = arr[mid:]
        # make the recursive calls
        merge_sort(left)
        merge_sort(right)
        # At this point left and right will be sorted basically bcs the single
        # element arrays are sorted by default
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
    
print merge_sort(some_arr)
