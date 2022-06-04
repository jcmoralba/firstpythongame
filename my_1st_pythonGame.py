
player = 1
turn = "(X)"
moves = True
moves1 = True
move = 0
move0 = 0
design = "==================="
print("Tic Tac Toe Game")

plot = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9']]




def my_plot():
    print(design)
    print(" " , plot[0][0] ,"|", plot[0][1] ,"|", plot[0][2])
    print(" " , plot[1][0] ,"|", plot[1][1] ,"|", plot[1][2])
    print(" " , plot[2][0] ,"|", plot[2][1] ,"|", plot[2][2])
    print(design)
my_plot()



while moves == True:
    try:
        if player == 1:
            turn = " (X)"
        else:
            turn = " (O)"
        move = int(input("Enter Player " + str(player) + str(turn) + " move: "))
    except ValueError:
        print()


    if move != "X" or "O":
        move0 = str(move)
        move = "move" + str(move)

        # print(str(move))
        # print(move0)

         #line1
        if move0 == plot[0][0]:          
            if player == 1:              
                player += 1                  
                plot[0][0] = "X"             
            else:                            
                plot[0][0] = "O"             
                player -= 1                  
        elif move0 == plot[0][1]:            
            if player == 1:                  
                plot[0][1] = "X"             
                player += 1                  
            else:                            
                plot[0][1] = "O"             
                player -= 1                  
        elif move0 == plot[0][2]:            
            if player == 1:                  
                plot[0][2] = "X"             
                player += 1                  
            else:                            
                plot[0][2] = "O"             
                player -= 1
        #line2
        elif move0 == plot[1][0]:
            if player == 1:
                player += 1
                plot[1][0] = "X"
            else:
                plot[1][0] = "O"
                player -= 1
        elif move0 == plot[1][1]:
            if player == 1:
                plot[1][1] = "X"
                player += 1
            else:
                plot[1][1] = "O"
                player -= 1
        elif move0 == plot[1][2]:
            if player == 1:
                plot[1][2] = "X"
                player += 1
            else:
                plot[1][2] = "O"
                player -= 1
        # line 3
        elif move0 == plot[2][0]:
            if player == 1:
                player += 1
                plot[2][0] = "X"
            else:
                plot[2][0] = "O"
                player -= 1
        elif move0 == plot[2][1]:
            if player == 1:
                plot[2][1] = "X"
                player += 1
            else:
                plot[2][1] = "O"
                player -= 1
        elif move0 == plot[2][2]:
            if player == 1:
                plot[2][2] = "X"
                player += 1
            else:
                plot[2][2] = "O"
                player -= 1

        else:                            
            print("Invalid move Re-Try")     


    my_plot()

    line1 = plot[0][0] + plot[0][1] + plot[0][2]
    line2 = plot[1][0] + plot[1][1] + plot[1][2]
    line3 = plot[2][0] + plot[2][1] + plot[2][2]
    line4 = plot[0][0] + plot[1][0] + plot[2][0]
    line5 = plot[0][1] + plot[1][1] + plot[2][1]
    line6 = plot[0][2] + plot[1][2] + plot[2][2]
    line7 = plot[0][0] + plot[1][1] + plot[2][2]
    line8 = plot[0][2] + plot[1][1] + plot[2][0]

    if line1 == 'XXX' or line2 == "XXX" or line3 == "XXX" or line4 == "XXX" or line5 == "XXX" or line6 == "XXX" or line7 == "XXX" or line8 == "XXX":
        print("Winner! Player1 (X) ")
        moves = False
    elif line1 == 'OOO' or line2 == "OOO" or line3 == "OOO" or line4 == "OOO" or line5 == "OOO" or line6 == "OOO" or line7 == "OOO" or line8 == "OOO":
        print("Winner! Player2 (O) ")
        moves = False
        #checkdraw
    elif plot[0][0] != "1" and plot[0][1] != "2" and plot[0][2] != "3" and plot[1][0] != "4" and plot[1][1] != "5" and plot[1][2] != "6" and plot[2][0] != "7" and plot[2][1] != "8" and plot[2][2] != "9":
        print("Draw!")
        moves = False















