import random
import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe - إكس أوو")

# Global ----
# turn is a varible used to store the last play on the board in order to flip turns
turn = ''
# shown turn is used to to print the turns on screen
shown_turn = ''
winner = ''
check_if_win = False
check_if_tie = False
AI_win = False
# remaining_plays used for the ai loop to store only the remaining spaces in the board
Remaining_plays = []
# used for ai to check the corners
corners = []

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def button_0():
    Play_game(0)
def button_1():
    Play_game(1)
def button_2():
    Play_game(2)
def button_3():
    Play_game(3)
def button_4():
    Play_game(4)
def button_5():
    Play_game(5)
def button_6():
    Play_game(6)
def button_7():
    Play_game(7)
def button_8():
    Play_game(8)

# button_num is the number recived from the gui fuction calls
def Play_game(button_num):
    global error_text, button1, button2, button3, button4, button5, button6, button7, button8, button9
    global turn

    rool = 0
    while rool <= 1:
        rool += 1
        if check_if_win or check_if_tie == True:
            break
        error_text = tk.Label(root, height=1, width=10, bg="#AEC9C7", text="", font=("", 25))
        error_text.place(relx=0.36, rely=0.028)

        check_trun = False
        print_board = board[0] + " | " + board[1] + " | " + board[2] + "\n" + \
                      board[3] + " | " + board[4] + " | " + board[5] + "\n" + \
                      board[6] + " | " + board[7] + " | " + board[8]

        CPU1 = 0
        cpu_play = 0
        Check_Winner()
        check_tie()

        if check_if_win == True:
            error_text["text"] = "Yay " + winner + " won."
            print("Yay " + winner + " won.")
            return
        elif check_if_tie == True:
            error_text["text"] = "Tie :("
            return

        if shown_turn == 'X' or shown_turn == '':

            while check_trun == False:
                if board[button_num] == '-':
                    check_trun = True
                    error_text["text"] = ""

                    board[button_num] = Switch_Turn(turn)
                    if board[0] != '-':
                        button1["text"] = board[0]
                    if board[1] != '-':
                        button2["text"] = board[1]
                    if board[2] != '-':
                        button3["text"] = board[2]
                    if board[3] != '-':
                        button4["text"] = board[3]
                    if board[4] != '-':
                        button5["text"] = board[4]
                    if board[5] != '-':
                        button6["text"] = board[5]
                    if board[6] != '-':
                        button7["text"] = board[6]
                    if board[7] != '-':
                        button8["text"] = board[7]
                    if board[8] != '-':
                        button9["text"] = board[8]


                elif check_trun == False:

                    error_text["text"] = "Used space"
                    return

            # AI turn
        elif shown_turn == 'O' and check_if_win == False:
            CPU1 = biscuit(cpu_play)
            AI_play = CPU1 + 1
            print("AI played on " + str(AI_play) + " slot")

            board[int(CPU1)] = Switch_Turn(turn)
            if board[0] != '-':
                button1["text"] = board[0]
            if board[1] != '-':
                button2["text"] = board[1]
            if board[2] != '-':
                button3["text"] = board[2]
            if board[3] != '-':
                button4["text"] = board[3]
            if board[4] != '-':
                button5["text"] = board[4]
            if board[5] != '-':
                button6["text"] = board[5]
            if board[6] != '-':
                button7["text"] = board[6]
            if board[7] != '-':
                button8["text"] = board[7]
            if board[8] != '-':
                button9["text"] = board[8]
            print(print_board)


# Biscuit is the name for the AI
def biscuit(play):
    global corners
    global Remaining_plays
    board_copy = board[:]
    Remaining_plays = []

    # check for posible losing spot
    ai_play = 0
    for xo in ['O', 'X']:
        loop_number = 0
        board_copy = board[:]

        for i in board_copy:
            if board_copy[loop_number] == '-':
                Remaining_plays.append(loop_number)
            loop_number += 1

        for i in Remaining_plays:
            board_copy = board[:]
            board_copy[i] = xo
            if AI_check_for_win(board_copy):
                ai_play = i
                Remaining_plays = []
                return ai_play

    if board[4] == '-':
        return 4

    corners = []
    for i in [0, 2, 6, 8]:
        if board[i] == '-':
            corners.append(i)
        if len(corners) > 0:
            return random.choice(corners)

    Remaining_plays = []
    loop_number = 0
    for i in board:
        if board[loop_number] == '-':
            Remaining_plays.append(loop_number)
        loop_number += 1
    for i in Remaining_plays:
        if board[i] == '-':
            return i


def Switch_Turn(turn1):
    global turn
    global shown_turn
    if turn1 == 'X':
        turn = 'O'
        shown_turn = 'X'
        return 'O'
    else:
        turn = 'X'
        shown_turn = 'O'
        return 'X'


def Check_Winner():
    global winner
    global check_if_win
    # Rows --
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        check_if_win = True
        return
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        check_if_win = True
        return
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        check_if_win = True
        return
    # Col --
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        check_if_win = True
        return
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        check_if_win = True
        return
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        check_if_win = True
        return
    # digno --
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        check_if_win = True
        return
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        check_if_win = True
        return
    else:
        return


# is a copy loop for the AI to check for a possible win
def AI_check_for_win(c_board):
    # Rows --
    if c_board[0] == c_board[1] == c_board[2] != "-":
        return True
    elif c_board[3] == c_board[4] == c_board[5] != "-":
        return True
    elif c_board[6] == c_board[7] == c_board[8] != "-":
        return True
    # Col --
    if c_board[0] == c_board[3] == c_board[6] != "-":
        return True
    elif c_board[1] == c_board[4] == c_board[7] != "-":
        return True
    elif c_board[2] == c_board[5] == c_board[8] != "-":
        return True
    # digno --
    if c_board[0] == c_board[4] == c_board[8] != "-":
        return True
    elif c_board[2] == c_board[4] == c_board[6] != "-":
        return True
    else:
        return False


# loop throgh boarf if you found '-' break the function a return without reaching Check_if_tie if not change check_if_tie
def check_tie():
    global check_if_tie
    for i in board:
        if i == '-':
            return

    check_if_tie = True


# the main game loop
while check_if_win == False or check_if_tie == False:
    canvas = tk.Canvas(height=700, width=700, bg="#263D42")
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0, relheight=0, relx=0.2, rely=0.1)

    error_text = tk.Label(root, height=1, width=10 ,bg="#D9DAD9", text="", font=("", 25))
    error_text.place(relx=0.36, rely=0.028)

    button1 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_0())
    button1.place(relx=0.1, rely=0.11)

    button2 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_1())
    button2.place(relx=0.375, rely=0.11)

    button3 = tk.Button(root, height=3, width=6 , text="",bg= "#D9DAD9",  font=("", 40), command=lambda: button_2())
    button3.place(relx=0.645, rely=0.11)

    button4 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_3())
    button4.place(relx=0.1, rely=0.38)

    button5 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_4())
    button5.place(relx=0.375, rely=0.38)

    button6 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_5())
    button6.place(relx=0.645, rely=0.38)

    button7 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_6())
    button7.place(relx=0.1, rely=0.655)

    button8 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9", font=("", 40), command=lambda: button_7())
    button8.place(relx=0.375, rely=0.655)

    button9 = tk.Button(root, height=3, width=6, text="",bg= "#D9DAD9",font=("", 40), command=lambda: button_8())
    button9.place(relx=0.645, rely=0.655)

    canvas.pack()
    root.mainloop()
