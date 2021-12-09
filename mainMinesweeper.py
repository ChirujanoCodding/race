from classes.minesweeper import Minesweeper
config = {
    'columns': 10,
    'rows': 10,
    'bomb': 'x',
    'point': '-',
    'flag':'⚑'
}
m = Minesweeper(config)
m.play()



