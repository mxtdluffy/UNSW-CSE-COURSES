# Written by Jingyun Shen for COMP9021 Lab1

'''
Draws an octagram, the inscribed octagon being
coloured yellow, and the colour of the triangles
alternating red and blue.
'''

from turtle import *

edge_length = 100
angle = 45
vertices = []


def draw_triangle(i, colour):
    penup()
    goto(vertices[(i + 2) % 16])
    pendown()
    color(colour)
    begin_fill()
    goto(vertices[i])
    goto(vertices[i + 1])
    goto(vertices[(i + 2) % 16])
    end_fill()

def draw_octagon(colour):
    penup()
    goto(vertices[0])
    pendown()
    color(colour)
    begin_fill()
    for i in range(9):
        goto(vertices[(2 * i) % 16])
    end_fill()
    

def main():
    penup()
    # Determine the positions of the 12 vertices
    # of the dodecagon by going to each of them.
    for i in range(8):
        left(i * angle)
        forward(edge_length)
        vertices.append(pos())
        left(angle)
        forward(edge_length)
        vertices.append(pos())
        home()
    pendown()

    # Draw the triangles
    for i in range(8):
        colour = 'blue' if i % 2 else 'red'
        draw_triangle(i * 2, colour)
        
    # Draw the octagon
    draw_octagon('yellow')
    home()

    a = input()
    return 0

if __name__ == '__main__':
    main()
