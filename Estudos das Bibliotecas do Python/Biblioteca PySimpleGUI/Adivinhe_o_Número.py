import PySimpleGUI as sg
import random

layout = [
    [sg.Text('Adivinhe o Número!')],
    [sg.Text('Digite a baixo o valor!')],
    [sg.Input(key='num')],
    [sg.Text('',key='Resposta')],
    [sg.Button('Start',key='start')],
    [sg.Button('Sair', key='sair')],
]

window = sg.Window('Jogo', layout=layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'sair':
        break
    
    elif event == 'start':
        num = int(values['num'])
        ran = random.randint(1,99)
        
    
while num != "adivinha":
    if num < ran:
        window['Resposta'].update('O número é muito baixo!')
    elif num > ran:
        window['Resposta'].update('O número é muito alto!')
    else:
        window['Resposta'].update('Parabéns! Você Ganhou!!!')
        break        