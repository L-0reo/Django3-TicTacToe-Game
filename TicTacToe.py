countx = 0
counto = 0
count = 0
lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# make sure correct entry when choosing (either 'x' or 'o')
def invalid():
    global lst
    global counto
    global countx
    countx = 0
    counto = 0
    count = 0
    print('    Invalid input')
    les = input('    Choose your mark between X and O: ')
    if les.lower() == 'x':
        counto += 1
        board_l()
        print('    Player 1 is X')
        print('    Player 2 is O')
        print('    Use numpad to place your marks')
        print('                          ')
    elif les.lower() == 'o':
        countx += 1
        board_l()
        print('    Player 1 is O')
        print('    Player 2 is X')
        print('    Use numpad to place your mark')
        print('                          ')
    else:
        invalid()
#ask if player wants to play again in the end
def question():
    global lst
    global counto
    global countx
    countx = 0
    counto = 0
    count = 0
    ques = input('    Would you like to play again? Y/N: ')
    if ques.lower() == 'y':
        lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        les = input('    Choose your mark between X and O: ')
        if les.lower() == 'x':
            counto += 1
        elif les.lower() == 'o':
            countx += 1
            board()
        else:
            invalid()

        steuerbord()
    elif ques.lower() == 'n':
        print('    Thanks for playing')
    else:
        print('    Invalid input')
        question()

#BOARD()
def board():
    print('\n' * 100)
    print('                             |        |        ')
    print('                       {}     |   {}    |   {}   '.format(lst[6], lst[7], lst[8]))
    print('                     --------|--------|--------')
    print('                             |        |        ')
    print('                       {}     |   {}    |   {}   '.format(lst[3], lst[4], lst[5]))
    print('                             |        |        ')
    print('                     --------|--------|--------')
    print('                       {}     |   {}    |   {}   '.format(lst[0], lst[1], lst[2]))
    print('                             |        |        ')

def board_l():
    print('\n' * 100)
    print('                             |        |        ')
    print('                       {}     |   {}    |   {}   '.format(7,8,9))
    print('                     --------|--------|--------')
    print('                             |        |        ')
    print('                       {}     |   {}    |   {}   '.format(4,5,6))
    print('                             |        |        ')
    print('                     --------|--------|--------')
    print('                       {}     |   {}    |   {}   '.format(1,2,3))
    print('                             |        |        ')
    
def board_m():
    
    print('                             |        |        ')
    print('                       {}     |   {}    |   {}   '.format(7,8,9))
    print('                     --------|--------|--------')
    print('                             |        |        ')
    print('                       {}     |   {}    |   {}   '.format(4,5,6))
    print('                             |        |        ')
    print('                     --------|--------|--------')
    print('                       {}     |   {}    |   {}   '.format(1,2,3))
    print('                             |        |        ')

#Input x
def inpx():
    global lst
    global countx
    global count
    while True:
        try:
            pos = int(input("    X's move: "))
            if lst[pos - 1] == ' ':
                lst[pos - 1] = 'X'
                count += 1
                board()
            else:
                print('    That square is already taken')
                inpx()
        except:
            print('    Invalid input')
        else:
            break
#Input o
def inpo():
    global lst
    global counto
    global count
    while True:
        try:#makes sure that position on board is still empty
            pos = int(input("    O's move: "))
            if lst[pos - 1] == ' ':
                lst[pos - 1] = 'O'
                count += 1
                board()
            else:
                print('    That square is already taken')
                inpo()
        except:
            print('    Invalid input')
        else:
            break
#Start
print('\n' * 100)
print('    **********************')
print('    WELCOME TO TIC TAC TOE')
print('    **********************')
print('                          ')
print('                          ')
print('                          ')
print("    TicTacToe is a game for two players using the same computer")
print("    The computer's numpad corresponds to the board's roster")
print('                          ')
board_m()
print('                          ')
print("    Players take turns placing their mark on the board using the numpad")
print('                          ')
pros = input('    Player 1 choose your mark X or O: ')
if pros.lower() == 'x':
    board_l()
    print('    Player 1 is X')
    print('    Player 2 is O')
    print('    Use numpad to place your mark')
    print('                          ')
    inpx()
    countx += 1

elif pros.lower() == 'o':
    board_l()
    print('    Player 1 is O')
    print('    Player 2 is X')
    print('    Use numpad to place your mark')
    print('                          ')
    inpo()
    counto += 1
else:
    invalid()
#game rules
def steuerbord():
        #alternates between putting x and o on the board and checks for win-if player 1 chose x
        global count
        if countx > counto:
            while True:
                if lst[0] == 'X' and lst[1] == 'X' and lst[2] == 'X' or lst[3] == 'X' and lst[4] == 'X' and lst[
                    5] == 'X' or lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X' or lst[0] == 'X' and lst[
                    3] == 'X' and lst[6] == 'X' or lst[0] == 'X' and lst[4] == 'X' and lst[8] == 'X' or lst[
                    6] == 'X' and lst[4] == 'X' and lst[2] == 'X' or lst[1] == 'X' and lst[4] == 'X' and lst[
                    7] == 'X' or lst[2] == 'X' and lst[5] == 'X' and lst[8] == 'X':
                    print('    X won!')
                    count = 0
                    question()
                    break
                elif count >= 9:
                    print("    Draw game!")
                    count = 0
                    question()
                    break
                inpo()
                if lst[0] == 'O' and lst[1] == 'O' and lst[2] == 'O' or lst[3] == 'O' and lst[4] == 'O' and lst[
                    5] == 'O' or lst[6] == 'O' and lst[7] == 'O' and lst[8] == 'O' or lst[0] == 'O' and lst[
                    3] == 'O' and lst[6] == 'O' or lst[0] == 'O' and lst[4] == 'O' and lst[8] == 'O' or lst[
                    6] == 'O' and lst[4] == 'O' and lst[2] == 'O' or lst[1] == 'O' and lst[4] == 'O' and lst[
                    7] == 'O' or lst[2] == 'O' and lst[5] == 'O' and lst[8] == 'O':
                    print('    O won!')
                    count = 0
                    question()
                    break
                elif count >= 9:
                    print("    Draw game!")
                    count = 0
                    question()
                    break
                inpx()
        #alternates between puttin x and o on the board and checks for win-if player 1 chose o
        elif counto > countx:
            while True:
                if lst[0] == 'O' and lst[1] == 'O' and lst[2] == 'O' or lst[3] == 'O' and lst[4] == 'O' and lst[
                    5] == 'O' or lst[6] == 'O' and lst[7] == 'O' and lst[8] == 'O' or lst[0] == 'O' and lst[
                    3] == 'O' and lst[6] == 'O' or lst[0] == 'O' and lst[4] == 'O' and lst[8] == 'O' or lst[
                    6] == 'O' and lst[4] == 'O' and lst[2] == 'O' or lst[1] == 'O' and lst[4] == 'O' and lst[
                    7] == 'O' or lst[2] == 'O' and lst[5] == 'O' and lst[8] == 'O':
                    print('    O won!')
                    count = 0
                    question()
                    break
                elif count >= 9:
                    print("    Draw game!")
                    count = 0
                    question()
                    break
                inpx()
                if lst[0] == 'X' and lst[1] == 'X' and lst[2] == 'X' or lst[3] == 'X' and lst[4] == 'X' and lst[
                    5] == 'X' or lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X' or lst[0] == 'X' and lst[
                    3] == 'X' and lst[6] == 'X' or lst[0] == 'X' and lst[4] == 'X' and lst[8] == 'X' or lst[
                    6] == 'X' and lst[4] == 'X' and lst[2] == 'X' or lst[1] == 'X' and lst[4] == 'X' and lst[
                    7] == 'X' or lst[2] == 'X' and lst[5] == 'X' and lst[8] == 'X':
                    print('    X won!')
                    count = 0
                    question()
                    break
                elif count >= 9:
                    print("    Draw game!")
                    count = 0
                    question()
                    break
                inpo()
steuerbord()