## Mergesort with recursion
def mergesort(arr):
    print (arr)
    print ('Splitting')
    n = len(arr)
    if n == 1:
        return arr # sorting a single number :) easy!
    else:
        left_sorted = mergesort(arr[:n//2])
        right_sorted = mergesort(arr[n//2:])
        
    return merge(left_sorted, right_sorted) # have to define merge!

def merge(left, right):
    res = [] # store fully sorted array here
    while left and right: # both arrays are not empty
        if left[0] <= right[0]:
            res.append(left.pop(0))  # take first element
        else:                        # and put it to the result
            res.append(right.pop(0))
    res = res + left + right # left or right is empty at this point
    
    print ('Merging')                         # just append the rest, as it is sorted
    print (res)
    return res

alist = [54,26,93,17,77,31,44,55,20]
aa=mergesort(alist)
print(aa)