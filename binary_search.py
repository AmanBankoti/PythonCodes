# Binary Search

def bin_search(arr,x,f,end):
    if(end >= f):
        mid = int((f + end)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return bin_search(arr,x,mid+1,end)
        else:
            return bin_search(arr,x,f,mid-1)
    return False

a = input("Enter numbers: ").split(' ')
num=input("Enter the number to be searched: ")

val=bin_search(a,num,0,len(a)-1)
if val:
    print("Number ",num ,"is present in the aray at index",val)
else:
    print("Number not present")

