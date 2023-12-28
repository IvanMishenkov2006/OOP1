from tkinter import *#Импорт всех классов и функций из модуля tkinter
from tkinter import ttk

window = Tk()#Создание экземпляр окна
window.geometry("300x80")#Установка размеров окна

value_var = IntVar()#Создание переменной, которая будет использоваться для связи с полосой прогресса
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate')#Создание полосы прогресса
pb.pack()#Размещениеполосы прогресса

def start():#Запуск анимации полосы прогресса
    pb.start(100)

def stop():# анимация остановки полосы прогресса
    pb.stop()

start_btn = ttk.Button(text="Start", command=start)#Вызов функции start при нажатии
start_btn.pack()#Размещение кнопки "Start"

stop_btn = ttk.Button(text="Stop", command=stop)#Вызов функции stop при нажатии
stop_btn.pack()#Размещение кнопки "Stop"

window.mainloop()#Запуск цикла
