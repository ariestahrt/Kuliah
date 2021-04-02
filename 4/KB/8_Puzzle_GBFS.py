try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

def print_puzzle(node):
    print("+ - + - + - +")
    print("| {} | {} | {} |".format(node[0], node[1], node[2]))
    print("+ - + - + - +")
    print("| {} | {} | {} |".format(node[3], node[4], node[5]))
    print("+ - + - + - +")
    print("| {} | {} | {} |".format(node[6], node[7], node[8]))
    print("+ - + - + - +")

def isFinal(node):
    if node[:9] == goalNode:
        print("FINAL FOUND~!")
        return True
    else:
        return False

def Hx(node):
    total_cost=0
    for index in range(0,9):
        data=node[index]
        current_row = int(index/3)
        current_col = index%3
        current_cost = abs(goal_pos[data]['row']-current_row) + abs(goal_pos[data]['col']-current_col)
        total_cost += current_cost
    
    print(total_cost)
    return total_cost


if __name__ == '__main__':
    startNode = [2,8,3, 1,6,4, 7,0,5]
    goalNode = [1,2,3, 8,0,4, 7,6,5]
    goal_pos = [None] * 9

    for index in range(0,9):
        data=goalNode[index]
        current_row = int(index/3)
        current_col = index%3
        goal_pos[data] = {"row":current_row, "col":current_col}

    visited_node = []

    DOWN_ENABLE = [False, False, False, True, True, True, True, True, True]
    UP_ENABLE = [True, True, True, True, True, True, False, False, False]
    LEFT_ENABLE = [True, True, False, True, True, False, True, True, False]
    RIGHT_ENABLE = [False, True, True, False, True, True, False, True, True]

    zero_loc=0
    for i in range(9):
        if (startNode[i] == 0):
            zero_loc = i
            break

    print("Zero loc: ", zero_loc)

    print("START NODE:")
    print_puzzle(startNode)
    q = Q.PriorityQueue()
    q.put((Hx(startNode),startNode))


    found = False
    while(not found):
        current_node = q.get()[1].copy()

        for i in range(9):
            if (current_node[i] == 0):
                zero_loc = i
                break
                
        if(DOWN_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc-3];
            temp[zero_loc-3] = 0;
            if(temp not in visited_node):
                # Push to queue
                q.put((Hx(temp), temp))
                print("DOWN")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True

        if(UP_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc+3];
            temp[zero_loc+3] = 0;
            if(temp not in visited_node):
                # Push to queue
                q.put((Hx(temp), temp))
                print("UP")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True

        if(LEFT_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc+1];
            temp[zero_loc+1] = 0;
            if(temp not in visited_node):
                # Push to queue
                q.put((Hx(temp), temp))
                print("LEFT")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True

        if(RIGHT_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc-1];
            temp[zero_loc-1] = 0;
            if(temp not in visited_node):
                # Push to queue
                q.put((Hx(temp), temp))
                print("RIGHT")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True
