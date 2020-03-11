# sudo python3 -mpip install -U PySimpleGUI
# sudo apt-get install python3-tk 
# sudo apt-get install matplotlib

import matplotlib.pyplot as plt
import PySimpleGUI as sg
import pandas 

# Pontos da Casa
eixo_x = [2,2,1,2,2.5,2.5,4,4,6.5,7.5,6.5,6.5,2]
eixo_y = [2.5,4.5,4.5,6,6,7,7,6,6,4.5,4.5,2.5,2.5]


def Plot(resize):

    plt.plot(eixo_x,eixo_y,color='purple')
    plt.scatter(eixo_x,eixo_y,color='blue')
    plt.show()

sg.theme('DarkBlue3')   

layout = [  
            [sg.Text('Menu')],
            [sg.Button('Adicionar Ponto (X,Y)')],
            [sg.Button('Remover Ponto (X,Y)')],
            [sg.Button('Atualizar Ponto (X,Y)')],
            [sg.Button('Visualizar Pontos')],
            [sg.Button('Sair')],
        ]

window = sg.Window('Computação Gráfica', layout,size=(300,250))
while True:
    event, values = window.read()
    if(event in (None, 'Sair')):
        break
    if(event == "Adicionar Ponto (X,Y)"):
        try:
            eixo_x = int(sg.popup_get_text("Digite o eixo X"))
            if(eixo_x == None):
                eixo_x = int(sg.popup_get_text("Digite o eixo X"))
            eixo_y = int(sg.popup_get_text("Digite o eixo Y"))
            if(eixo_y == None):
                eixo_y = int(sg.popup_get_text("Digite o eixo Y"))
        except TypeError as identifier:
            sg.popup("Entrada inválida")
        
    if(event == "Visualizar Pontos"):
        Plot(1)

window.close()