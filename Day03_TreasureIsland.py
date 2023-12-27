# Treasure Island Project (Treasure Hunt)
# Flow Chart Link - 

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
start = int(input("Press 1 to >>> START the Game: "))

if (start == 1) :
    print("Letttt'sssss Begggiiinnnnnn The GAME >>>>> Booom!!!")
    print("FEW MOMENTS LATER................")
    print("You're at a cross road.")
    response1 = input("Where do you want to go? Type >> 'Left' or 'Right\n")
    if  (response1.lower() == "left") :
        print("Your come to a lake. There is an island in the middle of the lake.")
        response2 = input("Type 'Wait' to wait for a boat OR Type 'Swim' to swim acrossss\n")
        if (response2.lower() == "wait") :
            print("Wohooo!!! You arrive at the island unhamed. Now, there is a house with 3 doors.")
            print("One door of orange colour, one of black colour, one of white colour")
            response3 = input("Which colour do you choose? Type colour name\n")
            if (response3.lower() == "orange") :
                print("WOW....YOU WON!")
            elif (response3.lower() == "black") :
                print("O...O...You ended up meeting a GHOSTTT...GAME OVER!!!")
            elif (response3.lower() == "white") :
                print("Ohhh! You met with an ANGEL....BUT YOU LOST IN HER LOVE!!!")
            else :
                print("You choosed an INVALID COLOUR DOOR...GAME OVER!!!")
        else :
            print("O...O...You were KILLED BY SHARKS...GAME OVER!!!")
    else :
        print("O...O...You choosed a wrong direction and met with an ACCIDENT...GAME OVER!!!")
else :
    print("You don't want to start the game...GET LOST!!!")
