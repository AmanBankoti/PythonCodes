# Linear Search

def lin_search(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            print("Number ",x ,"is present in the array at index",i)
            return True
    
    print("Number",x ,"not present in the array")
        
a= input("Enter the numbers: ").split(' ')
num=input("Enter the number to be searched: ")

lin_search(a,num)