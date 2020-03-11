# sudo python3 -mpip install -U PySimpleGUI
# sudo apt-get install python3-tk 
# pip3 install matplotlib

import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
import math

pontos = np.array([
    [2,2,1,2,2.5,2.5,4,4,6.5,7.5,6.5,6.5,2], # X
    [2.5,4.5,4.5,6,6,7,7,6,6,4.5,4.5,2.5,2.5] # Y
])

def Plot():
    plt.plot(pontos[0],pontos[1],color='purple')
    plt.scatter(pontos[0],pontos[1],color='blue')
    plt.show()

sg.theme('DarkBlue3')   

layout = [  
            [sg.Text('Menu')],
            [sg.Button('Translação - mover o objeto no eixo X e/ou em Y')],
            [sg.Button('Escala - alterar escala do objeto em X e/ou Y')],
            [sg.Button('Rotação - rotacionar objeto no sentido horário e/ou anti-horário')],
            [sg.Button('Espelhamento - espelhar o polígono em X e/ou Y')],
            [sg.Button('Cisalhamento - aplicar deformação em X e/ou Y')],
            [sg.Button('Visualizar Pontos')],
            [sg.Button('Sair')],
        ]

window = sg.Window('Computação Gráfica', layout,size=(500,300))
while True:
    event, values = window.read()
    if(event in (None, 'Sair')):
        break

    if(event == "Translação - mover o objeto no eixo X e/ou em Y"):
        quantidade = ''
        eixo = ''    
        try:
            quantidade = sg.PopupGetText("Digite a quantidade de passos")
            eixo = sg.PopupGetText("Digite o Eixo\nX\nY\nXY",title="Trabalho Louco do Casseb")
            if(str(eixo).upper() == "X"):
                for i in range(len(pontos[0])):
                    pontos[0][i] += int(quantidade)
            if(str(eixo).upper() == "Y"):
                for j in range(len(pontos[1])):
                    pontos[1][j] += int(quantidade)
            if(str(eixo).upper() == "XY"):
                for k in range(len(pontos[0])):
                    pontos[0][k] += int(quantidade)
                    pontos[1][k] += int(quantidade)
            Plot()
        
        except TypeError as identifier:
            pass

    if(event == "Escala - alterar escala do objeto em X e/ou Y"):
        multiplo = ''
        eixo = ''    
        try:
            multiplo = sg.PopupGetText("Digite o Múltiplo Escalar")
            eixo = sg.PopupGetText("Digite o Eixo\nX\nY\nXY",title="Trabalho Louco do Casseb")
            if(str(eixo).upper() == "X"):
                for i in range(len(pontos[0])):
                    pontos[0][i] *= int(multiplo)
            if(str(eixo).upper() == "Y"):
                for j in range(len(pontos[1])):
                    pontos[1][j] *= int(multiplo)
            if(str(eixo).upper() == "XY"):
                for k in range(len(pontos[0])):
                    pontos[0][k] *= int(multiplo)
                    pontos[1][k] *= int(multiplo)
            Plot()
        
        except TypeError as identifier:
            pass

    if(event == "Espelhamento - espelhar o polígono em X e/ou Y"):
        eixo = ''    
        try:
            eixo = sg.PopupGetText("Digite o Eixo\nX\nY\nXY",title="Trabalho Louco do Casseb")
            if(str(eixo).upper() == "X"):
                for i in range(len(pontos[0])):
                    pontos[0][i] *= -1;
            if(str(eixo).upper() == "Y"):
                for j in range(len(pontos[1])):
                    pontos[1][j] *= -1;
            if(str(eixo).upper() == "XY"):
                for k in range(len(pontos[0])):
                    pontos[0][k] *= -1;
                    pontos[1][k] *= -1;
            Plot()
        
        except TypeError as identifier:
            pass

    if(event == "Rotação - rotacionar objeto no sentido horário e/ou anti-horário"):
        sentido = ''    
        try:
            eixo = sg.PopupGetText("Digite o Sentido da Rotação",title="Trabalho Louco do Casseb")
            grau = sg.PopupGetText("Graus",title="Trabalho Louco do Casseb")
            if(str(eixo).upper() == "H"):
                for i in range(len(pontos[0])):
                    pontos[0][i] = float(pontos[0][i]) * math.cos(float(grau)) + float(pontos[1][i]) * math.sin(float(grau))
                Plot()
            if(str(eixo).upper() == "AH"):
                for i in range(len(pontos[1])):
                    pontos[0][i] = float(pontos[0][i]) * math.cos(float(grau)) - float(pontos[1][i]) * math.sin(float(grau))
                Plot()
            
        except TypeError as identifier:
            pass
    
    if(event == "Visualizar Pontos"):
        Plot()

window.close()