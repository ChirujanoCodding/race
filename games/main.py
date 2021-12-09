from classes.minesweeper import Minesweeper
from classes.war import BattleArena
config = {
    'columns': 10,
    'rows': 10,
    'bomb': 'x',
    'point': '-',
    'flag':'⚑'
}
m = Minesweeper(config)
m.play()
# arena = BattleArena()



