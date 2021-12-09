from random import randint
from time import sleep
from os import system

class RaceTable:
    def __name__(self):
        return 'Tu seleccionaste una pista de {}x{}'.format(self.size, self.max)

    def __init__(self, info:dict = {
        'size': 10,
        'max': 3,
    }):
        '''
        size: size of the sub-list
        max: max numbers of sub-lists
        slot: item in any sublist
        car list: list of cars
        sep: is the separator between sub-lists when is printed
        nicks: nicks of cars
        '''
        self.size = info.get('size') or 10
        self.max = info.get('max') or 3
        self.slot = info.get('slot') or '•'
        self.car_list = info.get('car list') or ['🚗', '🚕', '🚙']
        self.lists = self.__getList()
        for rout in self.lists:
            rout.insert(0,'🏁')
        self.sep = info.get('sep') or '-'
        self.nicks = info.get('nicks') or ['1', '2', '3']
        if self.max > len(self.car_list):
            raise ValueError('car_list must have the same length as the number of sub-lists')

    def __getList(self):
        return [[self.slot for i in range(self.size)]+[self.car_list[j]] for j in range(self.max)]

    def __print_table(self):
        # print the table and the nick names
        print('\n'.join([self.sep.join(route) + ' ' + self.nicks[index] for index, route in enumerate(self.lists)]))
        # print('\n'.join([self.sep.join(li) for li in self.lists]))

    def __move(self):
        win = False
        winner = False
        for index , route in enumerate(self.lists):
            if route[1] != self.slot:
                win, winner = True, self.nicks[self.lists.index(route)]
                return win, winner
            if randint(0,self.max) == index:
                route.pop(1)
                route.append(self.slot)
                return win, winner
        return win, winner

    def play(self, delay:float = 0.1):
        self.__print_table()
        input('\nPress enter to start the game')
        system('cls')
        self.win = False
        while not self.win:
            self.win, winner = self.__move()
            self.__print_table()
            if self.win == True:
                print('------------------------')
                print(f'{winner} Wins!')
                break
            sleep(delay)
            system('cls') 
