# Libraries
import random
from os import system

# Class
class Minesweeper:
    '''
    columns: columns of the map
    rows: rows of the map
    point: symbol of the point
    bomb: symbol of the bomb
    lost: symbol of the lost
    flag: symbol of the flag
    '''
    def __author__(self):
        return 'Shyrux#0311'

    def __init__(self, params: dict = {
        'columns': 5,
        'rows': 5
        }):
        self.__columns = params.get('columns') or 5
        self.__rows = params.get('rows') or 5
        self.__point = params.get('point') or '•'
        self.__bomb = params.get('bomb') or 'x'
        self.__lost = params.get('lost') or '!'
        self.__flag = params.get('flag') or '⚑'
        self.__base = self.__startBaseMap()
        self.__map = self.__startMap()

    def __startBaseMap(self):
        return [[self.__point for i in range(self.__columns)] for _ in range(self.__rows)]

    def __startMap(self):
        map = [[self.__point for i in range(self.__columns)] for _ in range(self.__rows)]
        return self.__startBombs(map)

    def __startBombs(self, mapa):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if mapa[i][j] == self.__point:
                    if random.randint(0, 4) == 1:
                        mapa[i][j] = self.__bomb
        return mapa

    def __countBombs(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= self.__rows:
                    continue
                if y + j < 0 or y + j >= self.__columns:
                    continue
                if self.__map[x + i][y + j] == self.__bomb:
                    count += 1
        return str(count)

    def __checkPosition(self, x, y):
        if self.__map[x][y] == self.__bomb:
            for i in range(self.__rows):
                for j in range(self.__columns):
                    if self.__map[i][j] == self.__bomb:
                        self.__base[i][j] = self.__bomb
                    self.__map[i][j] = self.__base[i][j]
            self.__map[x][y] = self.__lost
            return True
        else:
            self.__approx(x, y)
            self.__insertPlayer(x, y)
        return False

    def __countAllBombs(self):
        count = 0
        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.__map[i][j] == self.__bomb:
                    count += 1
        return count
    
    def __countAllFlags(self):
        count = 0
        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.__base[i][j] == self.__flag:
                    count += 1
        return count

    def __checkWin(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if (self.__base[i][j] == self.__flag) and (self.__map[i][j] == self.__bomb):
                    if self.__countAllFlags() == self.__countAllBombs():
                        return True
        return False

    def __insertPlayer(self, x , y):
        self.__base[x][y] = self.__countBombs(x, y)

    def __insertFlag(self, x, y):
        self.__base[x][y] = self.__flag

    def __chooseOption(self):
        print('1. Play')
        print('2. Flag')
        return input('Choose option: ')

    def __approx(self, x, y):
        if self.__base[x][y] == self.__point:
            self.__base[x][y] = self.__countBombs(x, y)
            if self.__base[x][y] == '0':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if x + i < 0 or x + i >= self.__rows:
                            continue
                        if y + j < 0 or y + j >= self.__columns:
                            continue
                        self.__approx(x + i, y + j)


    def __printMap(self):
        print(' '*3,' '.join([str(i) for i in range(self.__columns)]))
        print(' '*3 , '-'.join(('-' for i in range(self.__columns))))
        for i in range(self.__rows):
            print(f'{i} |',' '.join(self.__map[i]))

    def __printBaseMap(self):
        print(' '*3,' '.join([str(i) for i in range(self.__columns)]))
        print(' '*3 , '-'.join(('-' for i in range(self.__columns))))
        for i in range(self.__rows):
            print(f'{i} |',' '.join(self.__base[i]))

    def play(self):
        self.__printBaseMap()
        while True:
            if self.__checkWin():
                    system('cls')
                    self.__printBaseMap()
                    print('You won')
                    break
            info = self.__chooseOption()
            system('cls')
            if info == '1':
                self.__printBaseMap()
                x = int(input('Choose row: '))
                y = int(input('Choose column: '))
                system('cls')
                if self.__checkPosition(x, y):
                    self.__printMap()
                    print('You lost')
                    break
                else:
                    self.__printBaseMap()
            elif info == '2':
                self.__printBaseMap()
                x = int(input('Choose row: '))
                y = int(input('Choose column: '))
                system('cls')
                if self.__base[x][y] == self.__point:
                    self.__insertFlag(x, y)
                else:
                    self.__base[x][y] = self.__point
                self.__printBaseMap()