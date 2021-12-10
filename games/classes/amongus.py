from random import choice
from os import system

class SpaceShip:

    def __author__(self):
        return 'Shyrux#0311'

    def __init__(self , crewmates:int = 10):
        if crewmates < 4:
            print('You need at least 4 crewmates to play Among Us')
            exit()
        self.__crewmates = [crew for crew in range(crewmates)]
        self.__deads = []
        self.__impostor = choice(self.__crewmates)
        self.__judgeds = []
        self.__cmd = 'cls'
    
    def __kill(self, crewmate):
        if crewmate == self.__impostor:
            return True
        else:
            self.__deads.append(crewmate)
        return False

    def __randomKill(self):
        random = choice(self.__crewmates)
        if self.__impostor == random:
            self.__randomKill()
        elif self.__impostor in self.__deads:
            self.__randomKill()
        elif random in self.__judgeds:
            self.__randomKill()
        else:
            self.__kill(random)
            print(f'The impostor killed {random}!')

    def __checkAlive(self, crewmate):
            if crewmate in self.__deads:
                return 'Dead'
            else:
                return 'Alive'

    def __printStatus(self):
        print('Crewmate: \tStatus:')
        print('--------------------------------') 
        for crewmate in self.__crewmates:
            print(f'\t{crewmate} \t\t {self.__checkAlive(crewmate)}')
    
    def play(self):
        while len(self.__deads) < len(self.__crewmates):
            if len(self.__deads)+2 >= len(self.__crewmates):
                self.__printStatus()
                print(f'the impostos always was {self.__impostor}! (You lose)')
                break
            self.__printStatus()
            judged = int(input('Select a crewmate to judge: '))
            system(self.__cmd)
            if judged in self.__deads:
                print('You can\'t judge a dead crewmate')
                input()
                continue
            elif judged == self.__impostor:
                print('You killed the impostor! (You win)')
                break
            elif judged in self.__judgeds:
                print('You can\'t judge a dead crewmate')
                input()
                continue
            else:
                self.__judgeds.append(judged)
                self.__randomKill()
                self.__kill(judged)
        
            