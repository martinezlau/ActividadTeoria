import PySimpleGUI as sg

def build():
    """ Construye la ventana del menu """
    layout = [
        [sg.Text("Que datos analizamos ?")],
        [sg.Button('Datos De Poblacion', size=(50, 2), key="-data1-")],
        [sg.Button('Datos De Gastos En Educacion', size=(50, 2), key="-data2-")],
        [sg.Button('Salir', size=(50, 2), key="-exit-")]
    ]

    board = sg.Window('Actividad Teoria').Layout(layout)

    return board