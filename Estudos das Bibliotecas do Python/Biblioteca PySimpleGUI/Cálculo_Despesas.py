import PySimpleGUI as sg

layout = [
    [sg.Text('Salario Bruto')],
    [sg.Input(key='SB')],
    [sg.Text('Despesas Totais')],
    [sg.Input(key='DT')],
    [sg.Button('Calcular')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Cálculo de Despesas', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Calcular':
        SB = values['SB']
        DT = values['DT']
        CalcularDespesas = int(SB) - int(DT)
        Mensagem = window['mensagem'].update(CalcularDespesas)