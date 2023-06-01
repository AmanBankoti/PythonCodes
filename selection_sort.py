# Selection sort

def select_sort(arr,n):
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

a= list(map(int,input("Enter the numbers: ").split(' ')))
num=len(a)
sorted=select_sort(a,num)
print("The sorted array is: ",sorted)