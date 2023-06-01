x = [int(i) for i in input("Enter Leaf Nodes: ").split()]
turn = int(input("Who will play first,1 for max, 0 for min: "))

while(len(x)!=1):
    if turn:
        y = [max(i) for i in list(zip(x,x[1:]))[0::2]]
        if len(x)%2!=0:
            y.append(x[-1])
        x = y
        turn = 0
        print(f"max {x}")
        continue
    else:
        y = [min(i) for i in list(zip(x,x[1:]))[0::2]]
        if len(x)%2!=0:
            y.append(x[-1])
        x = y
        turn = 1
        print(f"min {x}")
        continue
