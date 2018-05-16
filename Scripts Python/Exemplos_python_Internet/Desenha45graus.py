#https://panda.ime.usp.br/pensepy/static/pensepy/genindex.html

import turtle            # permite usar as funções e objetos do módulo turtle
wn = turtle.Screen()     # cria uma janela gráfica
alex = turtle.Turtle()   # cria um turtle chamado alex
alex.forward(150)        # manda o alex se mover 150 unidades para frente
alex.left(90)            # roda de 90 graus para a esquerda
alex.forward(75)         # desenha o segundo lado do retângulo

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")         # define a cor de fundo da janela

tess = turtle.Turtle()
tess.color("blue")               # tess fica azul
tess.pensize(3)                  # define a espessura da caneta

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()
