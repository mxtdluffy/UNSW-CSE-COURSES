# Written by Jingyun Shen for COMP9021 Lab1

'''
Draws an hexagram that is centred horizontally in the
window that displays it, with the colour of the tips
alternating red and blue.
'''

from turtle import *


edge_length = 60


def draw_angle(colour):
    color(colour)
    forward(edge_length)
    right(120)
    forward(edge_length)
    left(60)

def teleport(distance):
    penup()      
    forward(distance)
    pendown()

def main():

    teleport(- edge_length)
    left(120)
    draw_angle('blue')
    draw_angle('red')
    draw_angle('blue')
    draw_angle('red')
    draw_angle('blue')
    draw_angle('red')
    

if __name__ == '__main__':
    main()
