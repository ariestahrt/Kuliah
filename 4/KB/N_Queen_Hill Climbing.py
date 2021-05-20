"""
I Kadek Agus Ariesta Putra - 05111940000105
Putu Ananda Satria Adi - 05111940000113
Farhan Arifandi - 05111940000061
"""
import random, copy

petak_size = 8

def print_board(board):
    for row in range(0,petak_size):
        print("+", end="")
        for col in range(0,petak_size):
            print(" - +", end="")
        print()
        print("|", end="")
        for col in range(0,petak_size):
            print(" {} |".format(board[row][col]), end="")
        print()
    print("+", end="")
    for col in range(0,petak_size):
        print(" - +", end="")
    print()

def generate_state():
    board = []
    for row in range(0,petak_size):
        new_row = []
        for col in range(0,petak_size):
            new_row.append(" ")
        board.append(new_row)

    for row in range(0,petak_size):
        rand = random.randint(0,petak_size-1)
        board[row][rand] = "Q"
    return board

def sum_hx(board):
    attacking = 0

    position = []
    for row in range(0,petak_size):
        for col in range(0,petak_size):
            if(board[row][col] == "Q"):
                position.append({"row":row, "col":col})

    # Memoisasi
    counted = []
    for row in range(0,petak_size):
        new_row = []
        for col in range(0,petak_size):
            new_row.append(False)
        counted.append(new_row)

    # Cek setiap Queen apakah saling menyerang
    for i in range(0,petak_size):
        for j in range(0,petak_size):
            if(i == j or counted[i][j] or counted[j][i]):
                continue
            queen_a = position[i]
            queen_b = position[j]

            # Apakah saling menyerang
            if(queen_a["col"] == queen_b["col"] or abs(queen_a["col"] - queen_b["col"]) == abs(queen_a["row"] - queen_b["row"])):
                attacking += 1
                counted[i][j] = True
                counted[j][i] = True
                continue

    return attacking

def start_the_thing():
    board = generate_state()
    print_board(board)

    current_hx = 9999999
    new_hx = sum_hx(board)
    current_board = board.copy()
    
    while(current_hx > new_hx):
        current_hx = new_hx

        # Evaluate
        for row in range(0,petak_size):
            temp_board = copy.deepcopy(current_board)
            for i in range(0,petak_size):
                temp_board[row][i] = " "
            for col in range(0,petak_size):
                temp_board[row][col] = "Q"
                temp_hx = sum_hx(temp_board)
                if(temp_hx < new_hx):
                    print("New hx found :", temp_hx)
                    print("CURRENT BOARD : ")
                    print_board(temp_board)
                    current_board = copy.deepcopy(temp_board)
                    new_hx = temp_hx
                temp_board[row][col] = " "
    
    if(current_hx > 0):
        return False
    
    return True
if __name__ == '__main__':
    petak_size = int(input("Masukkan ukuran papan catur :: "))
    status = start_the_thing()
    while(status == False):
        status = start_the_thing()
    print("LOOP SELESAI")
    exit()
