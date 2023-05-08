def insert_sort(arr):
    n = len(arr) #length of the array is stored in n
    for i in range(n): #loop that will iterate n times
        key = arr[i] # value "key" will be inserted into the sorted portion of the array
        j = i-1 #this variable will be used when looking for the correct position to insert key
        while j >= 0 and key < arr[j]: #as long as j is greater or equal to 0 and key is less than j
            arr[j + 1] = arr[j] #j element gets moved to j+1 position (all elements are shifting 1 position to the right)
            j = j - 1 #by subtracting 1, we iterate backwards through the sorted array, looking for the correct position for key
        arr[j + 1] = key #key is inserted into the correct position in the sorted array
    return arr
#corner cases - algorithm behaves differently than expected
# array = []
# array = [3]
# array = [3, 3, 2, 1]
