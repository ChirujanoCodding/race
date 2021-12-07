from random import randint
from time import sleep
from os import system

cars = ['🚗', '🚕', '🚙']
space = '*'
def gen():
    return [space for i in range(10)]
def update_frame(frame:list, car):
    for i in range(1,11):
        frame[-i],frame[-i+1]= car, space  
        yield frame

def play(route1, route2, route3, cars):  
    win = False
    car1 = cars[0]
    car2 = cars[1]
    car3 = cars[2]
    upframe = update_frame(route1, car1)
    midframe = update_frame(route2, car2)
    downframe = update_frame(route3, car3)
    while not win:
        for i in [upframe, midframe, downframe]:
            if win == True:
                break
            if randint(1,2) == 2:
                print('\n'.join(['-'.join(i) for i in [route1, route2, route3]]))
                print('--------------------')
                sleep(0.5)
                next(i, None)
                for j in [route1, route2, route3]:
                    if j[0] != space:
                        print('Gana el carro {} ({})'.format(j[0], cars.index(j[0])+1))
                        print('\n'.join(['-'.join(i) for i in [route1, route2, route3]]))
                        winner = cars.index(j[0])+1
                        win = True
                        return winner                
cont = 0
while True:
    cont += 1
    route1 = gen()
    route2 = gen()
    route3 = gen()
    a = play(route1, route2, route3, cars)
    input('Presione enter para continuar')
    system('cls')

    
