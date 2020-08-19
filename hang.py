import random
import subprocess
import os
import time


class Game(object):
    def __init__(self):
        self.max_points = 100
        self.player = Player(self.player_amount())
        self.stage = Stages()
    
    def __re__(self):
        menu = self.menu()
        count = 0
        if menu == 1:
            subprocess.call("clear")
            self.play()
        elif menu == 2:
            try:
                for name in self.player.name:
                    if os.path.isfile(f"{name}.txt"):
                        os.remove(f"{name}.txt")
            except:
                pass
            subprocess.call("clear")
            main()
        elif menu == 3:
            for name in self.player.name:
                count +=1
            if count > 1:
                for name in self.player.name:
                    print(f"{name} [{self.calc_points(name)}] points.")
                time.sleep(3)
                self.__re__()
            else:
                try:
                    with open(f"{self.player.name[0]}.txt","r") as file:
                        print(f"{self.player.name[0]} [{self.calc_points(self.player.name[0])}] points.")
                except:
                    print(f"You have no score {self.player.name[0]}")
                time.sleep(3)
                self.__re__()
        elif menu == 0:
            for name in self.player.name:
                if os.path.isfile(f"{name}.txt"):
                    os.remove(f"{name}.txt")
            exit(0)

        else:
            self.__re__()


    def winner(self,name):
        print(f"{name} win the game!")
        time.sleep(3)
        question = int(input("New Game 1.\nExit 0.\n"))
        if question == 1:
            for name in self.player.name:
                if os.path.isfile(f"{name}.txt"):
                     os.remove(f"{name}.txt")
            main()
        elif question == 0:
            exit(0)
        else:
            exit(0)

        
    def question(self):
        ask = int(input("How many players ? min player 1. max players 8.\nExit 0.\n"))
        return ask
    
    def player_amount(self):
        players_num = self.question()
        player_names = []
        if players_num == 0:
            exit(0)
        elif players_num > 0 and players_num < 9:
            for i in range(players_num):
                j = i+1
                player_input = input(f"Input player {j} name: ")
                player_names.append(player_input)
            return player_names
        else:
            g = Game()
            g.play()
    
    def add_points(self,name):
        with open(f"{name}.txt","a+") as file:
            file.write("Point")
            file.write("\n")
    
    def add_10_points(self,name):
        with open(f"{name}.txt","a+") as file:
            for point in range(0,10):
                file.write("Point")
                file.write("\n")

    def calc_points(self,name):
        point = "Point"
        count = 0
        try:
            with open(f"{name}.txt","r") as file:
                for line in file:
                    if point in line:
                        count += 1
        except:
            pass
        return count


    def menu(self):
        subprocess.call("clear")
        print("Next word 1.")
        print("New game 2.")
        print("Show score 3.")
        print("Exit 0.")
        choice = int(input("your choice: "))
        return choice


    def play(self):
        word = __words__()
        win = False
        wrong = 0
        board = ["__"] * len(word)
        rletters = list(word)
        stage = self.stage.stage1()
        print(f"{len(word)} letters in this word.")
        print(" ".join(board))
        while wrong < len(stage)-1:
            for name in range(len(self.player.name)):
                restart = True
                while restart:
                    char = input(f"{self.player.name[name]}, input letter: ")
                    if char in rletters:
                        cind = rletters.index(char)
                        board[cind] = char
                        rletters[cind] = '$'
                        self.add_points(self.player.name[name])
                        print(f"{self.player.name[name]} got 1 point.")
                        if self.calc_points(self.player.name[name]) >= self.max_points:
                            self.winner(self.player.name[name])
                        print(" ".join(board))
                        if "__" not in board:
                            subprocess.call("clear")
                            self.add_10_points(self.player.name[name])
                            print(f"{self.player.name[name]}, win the round! The word is: ")
                            print(" ".join(board))
                            print(self.calc_points(self.player.name[name]))
                            if self.calc_points(self.player.name[name]) >= self.max_points:
                                self.winner(self.player.name[name])
                            time.sleep(3)
                            self.__re__()
                                
                    else:
                        restart = False
                        print("Wrong letter!\n")
                        wrong += 1
                        i = wrong + 1
                        print(("".join(board)))
                        print("\n".join(stage[name:i]))
                        
        print("You lose the round!\nthe word was: " + word)
        time.sleep(3)
        self.__re__()            
                

class Player:
    def __init__(self,name):
        self.name = name
    

class Stages:
    def __init__(self):
        self.stage1()
    
    def stage1(self):
        stage = [
            " ________",
            "|       ",
            "|   |   ",
            "|   0   ",
            "|  /|\  ",
            "|  / \  ",
            "|       ",
            ]
        return stage

def __words__():
    return(random.choice(open("words.txt").read().splitlines()))

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()

