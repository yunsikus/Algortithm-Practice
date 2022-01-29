## QuickSort
def quick_sort(arr):
    def sort(low, high):
        if low >= high:
            return
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)
        
    def partition(low, high):
        pivot = arr[(low + high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low
    return sort(0,len(arr)-1)

## MergeSort
def merge_sort(arr):
    # 길이가 1일때 재귀 탈출
    if len(arr)<2:
        return arr
    
    # devide
    mid = len(arr)//2 
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # conquer
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    # low_arr 혹은 high_arr이 비었을 떄 뒤에다 털어준다.
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr

## BubbleSort
# 앞에 있는 데이터가 뒤에 있는 데이터보다 크면 swap
# 한번 루프를 돌때마다 최대값이 맨 앞에 오게 된다. 
# 정렬때마다 제외되는 데이터가 많아진다. 
def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

## InsertionSort
def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        key = my_list[i]
        j = i-1
        while j>=0 and my_list[j] > key:
            my_list[j+1] = my_list[j] # 앞의 값의 인덱스를 올려준다. 
            j -= 1
        my_list[j+1] = key
    return my_list
