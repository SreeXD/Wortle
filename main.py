from turtle import *
from random import randint

tracer(False)
colormode(255)

t = Turtle()
t.up()
t.screen.bgcolor(5, 5, 5)

with open('words.txt', 'r') as f:
    words = f.readlines()

answer = words[randint(0, len(words)-1)]
answer = answer.strip('\n')

env = {
    'answer': answer,
    'cell_size': 60,
    'margin': 16,
    'font_size': 28,
    'black': (0, 0, 0),
    'grey': (20, 20, 20),
    'white': (255, 255, 255),
    'green': (65, 125, 65),
    'yellow': (175, 175, 0),
    'cur_row': 0,
    'cur_col': 0,
    'cur_word': '',
    'end': False
}

def draw(i, j, fc):
    x = (j - 2.5) * (env['cell_size']) + (j - 2.0) * env['margin']
    y = (3 - i) * (env['cell_size']) + (2.5 - i) * env['margin']

    t.up()
    t.setposition(x, y)
    t.setheading(0)
    t.down()

    t.color(*env['black'])
    t.fillcolor(*fc)
    t.begin_fill()

    for i in range(4):
        t.forward(env['cell_size'])
        t.right(90)

    t.end_fill()
    t.up()

def write(i, j, c, fc):
    x = (j - 2.5) * (env['cell_size']) + (j - 2.0) * env['margin'] + (0.5 * env['cell_size'] - 0.35 * env['font_size'])
    y = (3 - i) * (env['cell_size']) + (2.5 - i) * env['margin'] - (0.5 * env['cell_size'] + 0.7 * env['font_size'])

    t.setposition(x, y)
    t.down()
    t.color(*fc)
    t.fillcolor(*fc)
    t.begin_fill()
    t.write(c, font=('Ariel', env['font_size'], 'normal'))
    t.end_fill()
    t.up()

def handle_input(c, env):
    if env['end']:
        return

    if env['cur_col'] == 5:
        return 

    write(env['cur_row'], env['cur_col'], c, env['white'])
    env['cur_col'] += 1
    env['cur_word'] += c

def handle_backspace(env):
    if env['end']:
        return

    if env['cur_col'] == 0:
        return 

    env['cur_word'] = env['cur_word'][: -1]
    env['cur_col'] -= 1
    
    draw(env['cur_row'], env['cur_col'], env['grey'])

def handle_enter(env):
    if env['end']:
        return
        
    if env['cur_col'] < 5:
        return 

    for i in range(0, 5):
        if env['cur_word'][i] == env['answer'][i]:
            draw(env['cur_row'], i, env['green'])
            write(env['cur_row'], i, env['cur_word'][i], env['white'])
    
        else:
            if env['cur_word'][i] in env['answer']:
                draw(env['cur_row'], i, env['yellow'])
                write(env['cur_row'], i, env['cur_word'][i], env['white'])
            
    if env['cur_word'] == env['answer']:
        env['end'] = True
        write(6, 1, 'Nice job ;o', env['white'])
        
    else:
        env['cur_col'] = 0
        env['cur_row'] += 1
        env['cur_word'] = ''

        if env['cur_row'] == 6:
            env['end'] = True
            write(6, -0.3, f'the word was {answer} xd :/', env['white'])

write(-1, 1.5, 'Wortle', env['white'])

for i in range(0, 6):
    for j in range(0, 5):
        draw(i, j, env['grey'])

listen()

for i in range(0, 26):
    c = chr(97 + i) 
    onkey(lambda x=c: handle_input(x, env), c)

onkey(lambda: handle_backspace(env), 'BackSpace')
onkey(lambda: handle_enter(env), 'Return')

t.getscreen()._root.mainloop()