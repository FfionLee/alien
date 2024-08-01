import pgzrun
import random

WIDTH=400
HEIGHT=400

alien=Actor('alien')
alien.pos=200,200

text=''
score=0


def draw():
    screen.fill('skyblue')
    alien.draw()
    screen.draw.text(text,center=(330,10),fontsize=30)
    screen.draw.text(str(score),center=(10,10),fontsize=30,color='midnightblue')
    if score<0:
        screen.fill('red')
        screen.draw.text('Game Over',center=(200,200),fontsize=50,color='black')

def on_mouse_down(pos):
    global text, score
    if alien.collidepoint(pos):
        alien.pos=random.randint(20,380),random.randint(20,380)
        text='Good Shot!'
        score=score+1
    else:
        text='You missed :('
        score=score-1
pgzrun.go()