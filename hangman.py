import subprocess
import random
import time


def multi_player_mode(word,points1,points2,player1,player2):
    word = _word()
    p1wrong = 0
    p2wrong = 0
    stages = _stages()
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    subprocess.call("clear")
        
    print(f"{player1}, {points1} Points. \n{player2}, {points2} Points.")
    print(f"{player1} starting the game ")
    print(str(len(word))+ " letters in this word.")
    while not win:
        while p1wrong < len(stages) - 1:
            restart = True
            while restart:
                char = input(f"{player1}, Input letter: ")

                if char in rletters:
                    cind = rletters.index(char)
                    board[cind] = char
                    rletters[cind] = '@'
                    print(("".join(board)))

                    if "__" not in board:
                        subprocess.call("clear")
                        print(f"{player1} win the round! The word was:")
                        print(("".join(board)))
                        win = True
                        pp1 = points1 + 10
                        pp2 = rletters.count('$')
                        p2 = pp2 + points2
                        check_points(player1,pp1,player2,p2)
                                        
                else:  
                    restart = False
                    print("Wrong letter!")
                    p1wrong += 1
                    e1 = p1wrong + 1
                    print("\n".join(stages[0: e1]))
                    print(e1)

                    if e1 == len(stages) or e1 > len(stages):
                        print(f"{player1} lose the round!")
                        pp1 = rletters.count('@')
                        p1 = points1 + pp1
                        pp2 = rletters.count('$')
                        p2 = pp2 + points2
                        check_points(player1,p1,player2,p2)
            break

        while p2wrong < len(stages) - 1:
            restart = True
            while restart:
                char1 = input(f"{player2}, input letter: ")

                if char1 in rletters:
                    cind1 = rletters.index(char1)
                    board[cind1] = char1
                    rletters[cind1] = '$'
                    print("char in :")
                    print(("".join(board)))

                    if "__" not in board:
                        subprocess.call("clear")
                        print(f"{player2} win the round! The word was:")
                        print("".join(board))
                        win = True
                        pp1 = rletters.count('@')
                        p1 = pp1 + points1
                        pp2 = points2 + 10
                        check_points(player2,pp2,player1,p1)
                        

                else:
                    restart = False
                    print("Wrong letter!")
                    p2wrong += 1
                    e2 = p2wrong + 1
                    print("\n".join(stages[0: e2]))
                    print(e2)

                    if e2 == len(stages) or e2 > len(stages):
                        print(f"{player2} lose the round!")
                        p1 = rletters.count('@')
                        pp1 = p1 + points1
                        pp2 = rletters.count('$')
                        p2 = pp2 + points2
                        check_points(player2,pp2,player1,pp1)
                        
            break

def single_player_mode():
    subprocess.call("clear")
    word = _word()
    stages = _stages()
    wrong = 0
    rletters = list(word)
    board = ["__"] * len(word)
    print("Welcome to execution single mode!")
    print(str(len(word))+ " letters in this word.")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("input letter: ")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            subprocess.call("clear")
            print("You win! The word was: ")
            print("".join(board))
            win = True
            time.sleep(3)
            main()

    if not win:
        print("\n".join(stages[0: wrong]))
        print ("you lose! the word was:{}.".format(word))
    

def names():
    players_names = []
    player1 = input("enter first player name: ")
    player2 = input("enter second player name: ")
    players_names.append(player1)
    players_names.append(player2)
    return players_names

def menu(points1,points2,player1,player2):
    print(f"\nScore board: \n{player1}: {points1}.\n{player2}: {points2}.")
    retry = int(input("\nDo you want to play again ?\nYes: 1.\nNo: 2.\n"))
    try:   
        if retry == 1:
            subprocess.call("clear")
            inp = int(input("same players ?\nYes: 1.\nNo: 2.\n"))

            if inp == 1:
                multi_player_mode(_word,points1,points2,player1,player2)

            if inp == 2:
                players_names = names()
                multi_player_mode(_word,0,0,players_names[0],players_names[1])

        if retry == 2:
            subprocess.call("clear")
            print("Bye.")
            exit(0)
        else:
            menu(player1,points1,player2,points2) 

    except ValueError:
        print("Only integers!")

def check_points(player1,points1,player2,points2):
    max_points = 50
    if points1 == max_points or points1 > max_points:
        sleep(3)
        subprocess.call("clear")
        print(f"{player1} Win the Game!")
        exit(0)
    elif points2 == max_points or points2 > max_points:
        sleep(3)
        subprocess.call("clear")
        print(f"{player2} Win the Game!")
        exit(0)
    else:
        menu(points1,points2,player1,player2)

        
def asking():
    ask = int(input("Single player press 1.\nMulti player press 2.\npress 0 for exit.\n"))
    return ask 

def _stages():
    stages = ["",
            "________",
            "|       ",
            "|   |   ",
            "|   0   ",
            "|  /|\  ",
            "|  / \  ",
            "|       ",
            ]
    return stages

def _word():
    """words= ["cat","main","game","power","python","programming","letter","menu","hotel",\
            "visual","studio","code","fast","car","break","illusion","mastering","popcorn",\
            "fantasy","random","word","english","russian","master"]"""
    words = ["cat"]
    rand = random.choice(words)
    return rand

def main():
    subprocess.call("clear")
    print("##### Welcome to execution game #####\n")
    ask = asking()
    if ask == 2:
        player_name = names()
        multi_player_mode(_word,0,0,player_name[0],player_name[1])

    if ask == 1:
        single_player_mode()

    if ask == 0:
        exit(0)

if __name__ == "__main__":
    main()
