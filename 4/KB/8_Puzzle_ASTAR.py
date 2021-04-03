"""
I Kadek Agus Ariesta Putra - 05111940000105
Putu Ananda Satria Adi - 05111940000113
Farhan Arifandi - 05111940000061
"""

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

import time as time

def print_puzzle(node):
    print("+ - + - + - +")
    print("| {} | {} | {} |".format(node[0], node[1], node[2]))
    print("+ - + - + - +")
    print("| {} | {} | {} |".format(node[3], node[4], node[5]))
    print("+ - + - + - +")
    print("| {} | {} | {} |".format(node[6], node[7], node[8]))
    print("+ - + - + - +")
    print("DEPTH :", node[9], "| HX :", node[10], "| SEQUENCE :", node[11])
    print()

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
    
    # print(total_cost)
    return total_cost


if __name__ == '__main__':
    startNode = [7,2,4, 5,0,6, 8,3,1]
    goalNode = [0,1,2, 3,4,5, 6,7,8]
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

    # print("Zero loc: ", zero_loc)
    gx = 0

    print("START NODE:")
    hx=Hx(startNode)
    print_puzzle(startNode+[0,hx+gx,0])
    q = Q.PriorityQueue()
    q.put((hx+gx,startNode+[0,hx+gx,0]))

    node_seq=0
    t0 = time.time()

    found = False
    while(not found):
        current_node = q.get()[1].copy()

        for i in range(9):
            if (current_node[i] == 0):
                zero_loc = i
                break

        if(DOWN_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc-3]
            temp[zero_loc-3] = 0
            if(temp[:9] not in visited_node):
                node_seq+=1
                hx=Hx(temp)
                temp[9]+=1
                temp[10]=hx+temp[9]
                temp[11]=node_seq
                # Push to queue
                visited_node.append(temp[:9])
                q.put((temp[10], temp))
                print("DOWN")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True
                    break

        if(UP_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc+3]
            temp[zero_loc+3] = 0
            if(temp[:9] not in visited_node):
                node_seq+=1
                hx=Hx(temp)
                temp[9]+=1
                temp[10]=hx+temp[9]
                temp[11]=node_seq
                # Push to queue
                visited_node.append(temp[:9])
                q.put((temp[10], temp))
                print("UP")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True
                    break

        if(LEFT_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc+1]
            temp[zero_loc+1] = 0
            if(temp[:9] not in visited_node):
                node_seq+=1
                hx=Hx(temp)
                temp[9]+=1
                temp[10]=hx+temp[9]
                temp[11]=node_seq
                # Push to queue
                visited_node.append(temp[:9])
                q.put((temp[10], temp))
                print("LEFT")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True
                    break

        if(RIGHT_ENABLE[zero_loc]):
            temp = current_node.copy()
            temp[zero_loc] = temp[zero_loc-1]
            temp[zero_loc-1] = 0
            if(temp[:9] not in visited_node):
                node_seq+=1
                hx=Hx(temp)
                temp[9]+=1
                temp[10]=hx+temp[9]
                temp[11]=node_seq
                # Push to queue
                visited_node.append(temp[:9])
                q.put((temp[10], temp))
                print("RIGHT")
                print_puzzle(temp)
                if(isFinal(temp)):
                    found = True
                    break

    t1 = time.time()

    print('Time:', t1-t0)
