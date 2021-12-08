from raceGame.race import Table

info = {
    'size': 10,
    'max': 3,
    'slot': '•',
    'car_list': ['🍌', '👤', '😈'],
    'sep': '-',
    'nicks': ['banana', 'your_mom', 'Kiddie']
}

myT = Table(info)
myT.play(delay=0.5)