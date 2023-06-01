def two_water_jug_problem(x, y, target):
    if target > max(x, y):
        print("No solution exists.")
        return
    
    state = (0, 0)
    print(state)
    
    while True:
        if state[0] == target or state[1] == target:
            if state[0] == target:
                state = (target, 0)
            else:
                state = (0, target)
            print(state)
            return
        elif state[0] == 0:
            state = (x, state[1])
        elif state[1] == y:
            state = (state[0], 0)
        else:
            state = (max(0, state[0] - y + state[1]), min(y, state[0] + state[1]))
        print(state)
        if state == (0, 0):
            print("No solution exists.")
            return
two_water_jug_problem(3, 8, 7)
