import tkinter as tk #what is this?
from tkinter import messagebox
import pygame

class cube(object): #is the snack 
    rows = 0
    w = 0
    def __init__(self, start, dirx=1, diry=0, colour=(255, 0, 0)):
        pass
    def move(self, dirx, diry):
        pass
    def draw(self, surface, eyes=False):
        pass

class snake(object): #is the snake itself; contains cube object
    def __init__(self, colour, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        #draw line now: 2 per loop.
        #vertical line
        pygame.draw.line(surface, (255, 255, 255), (x, 0) , (x, w))
        #horizontal line
        pygame.draw.line(surface, (255, 255, 255), (0, y) , (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width
    width = 500
    rows = 20 #how many rows: divides 500 evenly
    win = pygame.display.set_mode((width, width))
    #create snake object

    s = snake((255, 0, 0), (10, 10)) #colour: red, position:middle
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) #50 milisecond delay; lower this goes faster
        clock.tick(10) #snake moves 10 blocks/second; lower this goes slower
        redrawWindow(win)
        
    



main()
