def add_length(str_):
    arr = str_.split()
    for i in range(0,len(arr)):
        size = len(arr[i])
        arr[i] += ' '+str(size)
    return arr
    
