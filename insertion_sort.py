# insertion sort

def insert_sort(arr):
    for i in range(1,len(arr)):
        num = arr[i]
        j = i-1
        while j >=0 and num < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] =num
    return arr
a= list(map(int,input("Enter the numbers: ").split(' ')))

sorted=insert_sort(a)
print("The sorted array is: ",sorted)
