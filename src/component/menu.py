from src.windows import menu
from src.handlers import handler

def start():
    """ Lanza la ejecucion de la ventana del menu """
    window = loop()
    window.close()

def loop():
    """ Loop de la ventana de menu  que capta los eventos al apretar las opciones """
    window = menu.build()

    while True:
        event, values = window.read()

        if event in ("-exit-"):
            break
        if event == "-data1-":
            handler.dataset1()
        if event == "-data2-":
            handler.dataset2()
    
    return window