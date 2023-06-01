j1,j2,g = map(int,input("Enter size of jugs and goal: ").split())

def water_jug(jug1, jug2, goal):
    if goal >max(jug1,jug2):
        print("No solution")
        return

    s_jug = min(jug1, jug2)
    b_jug = max(jug1, jug2)

    c_jug1, c_jug2 = 0, 0
    visited = set()

    while c_jug1 != goal and c_jug2 != goal:
        state = (c_jug1, c_jug2)
        if state in visited:
            print("No solution")
            return
        visited.add(state)

        if not c_jug1:
            c_jug1 = s_jug
            print(f"jug 1 = {c_jug1}, jug 2 = {c_jug2} ")
            continue

        if c_jug2 == b_jug:
            c_jug2 = 0
            print(f"jug 1 = {c_jug1}, jug 2 = {c_jug2} ")
            continue

        r_jug2 = min(abs(b_jug - c_jug2), c_jug1)
        c_jug2 += r_jug2
        c_jug1 -= r_jug2
        print(f"jug 1 = {c_jug1}, jug 2 = {c_jug2} ")

water_jug(j1,j2,g)


