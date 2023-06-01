# Bubble Sort

def bubble_sort(arr,n):
    for i in range(0,n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

a= list(map(int,input("Enter the numbers: ").split(' ')))
num=len(a)-1

sorted=bubble_sort(a,num)
print("The sorted array is: ",sorted)