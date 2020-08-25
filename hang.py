import random
import subprocess
import time


class Game(object):
    def __init__(self):
        self.max_points = 100
        self.player = Player(self.player_amount())
        self.stage = Stages()
        self.__add_user_to_dict__()
    
    def __add_user_to_dict__(self):
        for name in self.player.name:points.update( {name:0} )

    def __re__(self):
        menu = self.menu()
        if menu == 1:
            subprocess.call("clear")
            self.play()
        elif menu == 2:
            main()
        elif menu == 3:
            self.get_user_score()
            time.sleep(3)
            self.__re__()
        elif menu == 0:
            exit(0)

        else:
            self.__re__()

    def get_user_score(self):
        for name in self.player.name:print(f"{name}, Points: {points[name]}")

    def winner(self,name):
        print(f"{name} win the game!")
        time.sleep(3)
        question = int(input("New Game 1.\nExit 0.\n"))
        if question == 1:
            main()
        elif question == 0:
            exit(0)
        else:
            exit(0)

    def check_score(self):
        for name in self.player.name:
            if int(points.get(name)) >= self.max_points:
                self.winner(name)
        
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
    
 
    def menu(self):
        subprocess.call("clear")
        choice = int(input("Next word 1.\nNew game 2.\nShow score 3.\nExit 0.\nyour choice: "))
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
                        print(f"{self.player.name[name]} + 1 point.")
                        point = int(points.get(self.player.name[name]))
                        point = point + 1
                        points.update( {self.player.name[name]:point} )
                        print(f"{self.player.name[name]}, Points: {int(points.get(self.player.name[name]))}")
                        print(" ".join(board))
                        self.check_score()
                        if "__" not in board:
                            subprocess.call("clear")
                            point = int(points.get(self.player.name[name]))
                            point = point + 10
                            points.update( {self.player.name[name]:point} )
                            print(f"{self.player.name[name]}, win the round! The word is: ")
                            print(" ".join(board))
                            print(int(points.get(self.player.name[name])))
                            self.check_score()
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

points = {}

def __words__():
    return(random.choice(open("words.txt").read().splitlines()))

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()
