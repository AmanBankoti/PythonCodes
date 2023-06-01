def min(a, n, setIndex):
    smallest = a[setIndex][0]
    for i in range(1, n):
        if smallest > a[setIndex][i]:
            smallest = a[setIndex][i]
    return smallest

def max(a, n, setIndex):
    greatest = a[setIndex][0]
    for i in range(1, n):
        if greatest < a[setIndex][i]:
            greatest = a[setIndex][i]
    return greatest

n = int(input("Enter the no. of nodes in each subtree: "))
set = [[0 for j in range(n)] for i in range(n)]
print("Enter the utility values: ")
for i in range(n):
    row = input().split()
    for j in range(n):
        set[i][j] = int(row[j])

max_arr = [0 for i in range(n)]
print("The min values returned are: ", end="")
for i in range(n):
    max_arr[i] = min(set, n, i)
    print(max_arr[i], end=" ")

maxValue = max([max_arr], n, 0)
print("\nThe Max Value is", maxValue)

