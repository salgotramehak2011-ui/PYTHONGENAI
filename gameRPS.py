print("GAME BEGIN! ROCK PAPER SCISSOR!")
count = 0
user_win = 0
comp_win = 0
match_draw = 0
while True:
    rps=("Rock","Paper","Scissor")
    user=input("Enter the user hand gesture: ")
    if user in rps:
        print(user)
    else:
        print("Invalid String")
    import random 
    comp = ["Rock","Paper","Scissor"]
    choice = random.choice(comp)
    print(choice)
    if user == "Rock" and choice == "Scissor":
        print("User is winner.")
        user_win += 1
    elif user == "Rock" and choice == "Paper":
        print("Computer  is winner.")
        comp_win += 1
    elif user == "Rock" and choice == "Rock":
        print("Match Draw.")
        match_draw += 1
    elif user == "Scissor" and choice == "Paper":
        print("User is winner.")
        user_win += 1
    elif user == "Scissor" and choice == "Scissor":
        print("Match Draw.")
        match_draw += 1
    elif user == "Scissor" and choice == "Rock":
        print("Computer is winner.")
        comp_win += 1
    elif user == "Paper" and choice == "Scissor":
        print("Computer is winner.")
        comp_win += 1
    elif user == "Paper" and choice == "Rock":
        print("User is winner.")
        user_win += 1
    elif user == "Paper" and choice == "Paper":
        print("Match Draw.")
        match_draw += 1
    

    play = input("Do you want to play again(yes/no)?: ")
    count += 1
    if play == "no":
        print("How many times game are run: ",count)
        print("User is winner: ",user_win)
        print("Computer is winner: ",comp_win)
        print("Match Draw: ",match_draw)
        print("Now Game is Ended!")
        final_result = f" How many times game are run: {count}\n  User is winner: {user_win}\n  Computer is winner: {comp_win}\n  Match Draw: {match_draw}\n  GAME IS ENDED!"
        break
    
        

f = open("file_sh.txt","w") 
f.write(final_result)
f.close()





