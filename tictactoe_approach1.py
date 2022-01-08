x=[' ']*9
vtab={
    #ai as 1st player
    '         ':'    O    ',
    #1687/9
    'X   O    ':'X  OO    ',
    'X  OOX   ':'XO OOX   ',
    'XO OOX X ':'XOOOOX X ',
    'XOOOOX XX':'XOOOOXOXX',
    'XOOOOXXX ':'XOOOOXXXO',
    #7924/6
    '    O X  ':'O   O X  ',
    'O   O X X':'O   O XOX',
    'OX  O XOX':'OXO O XOX',
    'OXO OXXOX':'OXOOOXXOX',
    'OXOXO XOX':'OXOXOOXOX',
    #3948/2
    '  X O    ':'O X O    ',
    'O X O   X':'O X OO  X',
    'O XXOO  X':'O XXOOO X',
    'OXXXOOO X':'OXXXOOOOX',
    'O XXOOOXX':'OOXXOOOXX',
    #human as first player
    'X        ':'X   O    ',
    ' X       ':' X  O    ',
    '  X      ':'  X O    ',
    '   X     ':'   XO    ',
    '     X   ':'    OX   ',
    '      X  ':'    O X  ',
    '       X ':'    O  X ',
    '        X':'    O   X',
    #52479 tie game
    '    X    ':'O   X    ',
    'OX  X    ':'OX  X  O ',
    'OX XX  O ':'OX XXO O ',
    'OX XXOXO ':'OXOXXOXO ',
    'OXOXXOXOX':'OXOXXOXOX',
    #17683
    'X   O X  ':'X  OO X  ',
    'X  OOXX  ':'XO OOXX  ',
    'XO OOXXX ':'XO OOXXXO',
    'XOXOOXXXO':'XOXOOXXXO',
    #2394
    ' XX O    ':'OXX O    ',
    'OXX O   X':'OXX OO  X',
    'OXXXOO  X':'OXXXOOO X',
    'OXXXOOOXX':'OXXXOOOXX',
    #31867
    '  X      ':'  X O    ',
    'X X O    ':'XOX O    ',
    'XOX O  X ':'XOXOO  X ',
    'XOXOOX X ':'XOXOOX XO',
    'XOXOOX XO':'XOXOOXXXO',
    #41389
    '   X     ':'   XO    ',
    'X  XO    ':'X  XO O  ',
    'X XXO O  ':'XOXXO O  ',
    'XOXXO OX ':'XOXXOOOX ',
    'XOXXOOOXX':'XOXXOOOXX',
    #69724
    '    OX  X':'  O OX  X',
    '  O OXX X':'  O OXXOX',
    ' XO OXXOX':'OXO OXXOX',
    'OXOXOXXOX':'OXOXOXXOX',
}

def display():
    for i in range(0,9,3):
        print(x[i:i+3])
c=0
while True:
    i=int(input('enter position(1-9): '))
    while x[i-1] != ' ': i=int(input('position occupied! enter another position number(1-9): '))
    x[i-1]='X'
    display()
    c+=1
    if c==9:
        print('It\'s a tie')
        break
    x=list(vtab[''.join(x)])
    c+=1
    print('after AI turn...')
    display()
