x_size = 7
y_size = 6

def display(field):
    for x in range(x_size):
        print(" {}".format(x),end="")
    print()

    for y in range(y_size):
        for x in range(x_size):
            print("|{}".format(field[x][y]),end="")
        print("|")

def put(field, x, y):
    check = 0
    for i in range(y_size):
        if field[x][y-check] == " ":
            return check
        else:
            check += 1

def check_win(field, symbol, player, lx, ly):   
    if lx < 4 and field[lx][ly] == symbol and field[lx+1][ly] == symbol and field[lx+2][ly] == symbol and field[lx+3][ly] == symbol:
        return 1
    elif lx > 2 and field[lx][ly] == symbol and field[lx-1][ly] == symbol and field[lx-2][ly] == symbol and field[lx-3][ly] == symbol:
        return 1
    elif lx > 0 and lx < 5 and field[lx][ly] == symbol and field[lx+1][ly] == symbol and field[lx+2][ly] == symbol and field[lx-1][ly] == symbol:
        return 1
    elif lx > 1 and lx < 4 and field[lx][ly] == symbol and field[lx-1][ly] == symbol and field[lx-2][ly] == symbol and field[lx+1][ly] == symbol:
        return 1
    
    elif ly < 3 and field[lx][ly] == symbol and field[lx][ly+1] == symbol and field[lx][ly+2] == symbol and field[lx][ly+3] == symbol:
        return 1
    elif ly > 2 and field[lx][ly] == symbol and field[lx][ly-1] == symbol and field[lx][ly-2] == symbol and field[lx][ly-3] == symbol:
        return 1
    elif ly > 0 and ly < 4 and field[lx][ly] == symbol and field[lx][ly+1] == symbol and field[lx][ly+2] == symbol and field[lx][ly-1] == symbol:
        return 1
    elif ly > 1 and ly < 3 and field[lx][ly] == symbol and field[lx][ly+1] == symbol and field[lx][ly-2] == symbol and field[lx][ly-1] == symbol:
        return 1

    elif lx < 4 and ly < 3 and field[lx][ly] == symbol and field[lx+1][ly+1] == symbol and field[lx+2][ly+2] == symbol and field[lx+3][ly+3] == symbol:
        return 1
    elif lx > 2 and ly > 2 and field[lx][ly] == symbol and field[lx-1][ly-1] == symbol and field[lx-2][ly-2] == symbol and field[lx-3][ly-3] == symbol:
        return 1
    elif lx > 0 and lx < 5 and ly > 0 and ly < 4 and field[lx][ly] == symbol and field[lx+1][ly+1] == symbol and field[lx+2][ly+2] == symbol and field[lx-1][ly-1] == symbol:
        return 1
    elif lx > 1 and lx < 4 and ly > 1 and ly < 3 and field[lx][ly] == symbol and field[lx+1][ly+1] == symbol and field[lx-2][ly-2] == symbol and field[lx-1][ly-1] == symbol:
        return 1

    elif lx > 2 and ly < 3 and field[lx][ly] == symbol and field[lx-1][ly+1] == symbol and field[lx-2][ly+2] == symbol and field[lx-3][ly+3] == symbol:
        return 1
    elif lx < 4 and ly > 2 and field[lx][ly] == symbol and field[lx+1][ly-1] == symbol and field[lx+2][ly-2] == symbol and field[lx+3][ly-3] == symbol:
        return 1
    elif lx > 1 and lx < 6 and ly > 0 and ly < 4 and field[lx][ly] == symbol and field[lx-1][ly+1] == symbol and field[lx-2][ly+2] == symbol and field[lx+1][ly-1] == symbol:
        return 1
    elif lx > 0 and lx < 5 and ly > 1 and ly < 3 and field[lx][ly] == symbol and field[lx-1][ly+1] == symbol and field[lx+2][ly-2] == symbol and field[lx+1][ly-1] == symbol:
        return 1
    else:
        return 0

count = 0
player = 1
symbol = "x"

name1 = input("Player 1, what's your name? ")
name2 = input("Player 2, what's your name? ")

actual_player = name1

playing_field = [[" " for i in range(y_size)] for j in range(x_size)] 
display(playing_field)

# Main loop
while True:
    x_in = int(input("{}, enter where you want to put your symbol >>>".format(actual_player)))
    y_in = 5

    if x_in > x_size or x_in < 0:
        print("This field doesn't exist, please try again.")
        continue
    elif not playing_field[x_in][y_in] == " ":
        y_in -= put(playing_field, x_in, y_in)
        playing_field[x_in][y_in] = symbol
        count += 1
    else:
        playing_field[x_in][y_in] = symbol
        count += 1

    display(playing_field)

    if check_win(playing_field, symbol, player, x_in, y_in) == 1:
        print("Congratulations, {}, you won!".format(actual_player))
        break
    elif count == x_size * y_size:
        print("Draw! Play another round!")
        break

    if player == 1:
        player = 2
        symbol = "o"
        actual_player = name2
    else:
        player = 1
        symbol = "x"
        actual_player = name1
