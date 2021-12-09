from random import randint
from time import sleep
from os import system

class Table:
    def __name__(self):
        return 'Tu seleccionaste una pista de {}x{}'.format(self.size, self.max)

    def __init__(self, info:dict = {
        'size': 10,
        'max': 3,
        'slot': '•',
        'car_list': ['🚗', '🚕', '🚙'],
        'sep': '-',
        'nicks': ['1', '2', '3']
    }):
        '''
        size: size of the sub-list
        max: max numbers of sub-lists
        slot: item in any sublist
        car_list: list of cars
        sep: is the separator between sub-lists when is printed
        nicks: nicks of cars
        '''
        self.size = info['size']
        self.max = info['max']
        self.slot = info['slot']
        self.car_list = info['car_list']
        self.lists = [[info['slot'] for spaces in range(info['size']-1)]+[info['car_list'][lists]] for lists in range(info['max'])]
        for rout in self.lists:
            rout.insert(0,'🏁')
        self.sep = info['sep']
        self.nicks = info['nicks']
        if info['max'] > len(info['car_list']):
            raise ValueError('car_list must have the same length as the number of sub-lists') 

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