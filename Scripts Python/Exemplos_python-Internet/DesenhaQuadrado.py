#https://panda.ime.usp.br/pensepy/static/pensepy/genindex.html

#Site para aprendizado de pyton
#https://panda.ime.usp.br/pensepy/static/pensepy/05-Funcoes/funcoes.html#index-2

import turtle

def desenhaRetangulo(t, w, h):
    """Faca a tartaruga t desenhar um retangulo de largura w e altura h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def desenhaQuadrado(tx, tam):        # uma nova versao de desenhaQuadrado
    desenhaRetangulo(tx, tam, tam)

#Aqui o Script ganha vida e executa as funções definidas acima no sistem.
wn = turtle.Screen()             # Inicializa a janela
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # cria tess

desenhaQuadrado(tess, 50)

wn.exitonclick()
