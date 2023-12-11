import PySimpleGUI as sg

layout = [[sg.Text(text='Olá Mundo!',
                   font=('Arial Bold', 20),
                   size=20,
                   expand_x=True,
                   justification='center')],
          ]

Janela = sg.Window('Olá Mundo!', layout, size=(715,250))

while True:
    event, values = Janela.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    
Janela.close()