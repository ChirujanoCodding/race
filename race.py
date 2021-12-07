def pist_generator(size:int = 5, max:int= 1, slot:str = '*'):
    return [[slot for spaces in range(size-1)]+['🚗'] for lists in range(max)]

from random import randint
from time import sleep
from os import system

class Table:
    def __init__(self, size:int = 10, max:int= 3, slot:str = '•',car_list:list = ['🚗', '🚕', '🚙'], sep:str = '-', nicks:list = ['1', '2', '3']):
        '''
        size: size of the sub-list
        max: max numbers of sub-lists
        slot: item in any sublist
        car_list: list of cars
        sep: is the separator between sub-lists when is printed
        nicks: list of nicks ( names of cars )
        '''
        self.size = size
        self.max = max
        self.slot = slot
        self.car_list = car_list
        self.lists = [[slot for spaces in range(size-1)]+[car_list[lists]] for lists in range(max)]
        for rout in self.lists:
            rout.insert(0,'🏁')
        self.sep = sep
        self.nicks = nicks
        self.print_table()
        if max > len(car_list):
            raise ValueError('car_list must have the same length as the number of sub-lists')

    def print_table(self):
        # print the table and the nick names
        print('\n'.join([self.sep.join(route) + ' ' + self.nicks[index] for index, route in enumerate(self.lists)]))
        
        # print('\n'.join([self.sep.join(li) for li in self.lists]))

    def move(self):
        win = False
        winner = False
        for route in self.lists:
            if route[1] != self.slot:
                win, winner = True, self.nicks[self.lists.index(route)]
                return win, winner
            if randint(1,self.max) == self.max:
                route.pop(1)
                route.append(self.slot)
                return win, winner
        return win, winner
 

a = Table(size=15, max=5, slot='•', car_list=['🚗', '🚕', '🚙','🚓', '🚑'], sep='-', nicks=['Shyrux#0311', '2', '3', '4', '5'])
sleep(0.5)
input('Press Enter to start')
win = False
while not win:
    win, winner = a.move()
    a.print_table()
    if win == True:
        print('------------------------')
        print(f'{winner} Wins!')
        break
    #sleep(0.5)
    system('cls')
