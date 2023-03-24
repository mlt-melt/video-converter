from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from converterMain import convert
import tkinter.messagebox as mb

window = Tk()
window.title("Видео-конвертер")


window.geometry('600x400')

text = tk.Label(text="Укажите парамерты для конвертации видео\n-----------------------------------", fg="black")
text.pack(pady=10)

text = tk.Label(text='Укажите таймкоды для обрезки', fg="black")
text.pack()

# text = tk.Label(text='Возможные форматы:\n"секунды"\n"минуты:секунды"\n"часы:минуты:секунды"', fg="black")
# text.pack()

entry = tk.Entry(width=20)
entry.insert(0, '00:00:00')
entry.pack(pady=[5,0])

entry2 = tk.Entry(width=20)
entry2.insert(0, '00:00:00')
entry2.pack(pady=[5,20])

text = tk.Label(text="Выберите формат итогового файла", fg="black")
text.pack()

def startProcess():
  outputvarExt = var.get()
  outputSize = var2.get()
  firstCut = entry.get()
  SecondCut = entry2.get()
  msg = 'Процесс конвертации будет запущен, после нажатия кнопки "OK"! Вы можете следить за ним в окне командной строки рядом. После завершения процесса вам будет показано сообщение об окончании'
  mb.showinfo("Процесс готовов к запуску", msg)
  window.destroy()
  try:
    convert(outputvarExt, outputSize, firstCut, SecondCut)
  except Exception as e:
    msg = f"Обнаружена ошибка - {e}"
    mb.showerror("Ошибка", msg)

days = ('mp4', 'avi', 'mkv')
var = StringVar()
combobox = Combobox(window, textvariable = var)
combobox['values'] = days
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 5, pady=5)


text = tk.Label(text="Выберите разрешение итогового файла", fg="black")
text.pack()

sizes = ('Оставить размер оригинала', '1280:720','1920:1080')
var2 = StringVar()
combobox2 = Combobox(window, textvariable = var2)
combobox2['values'] = sizes
combobox2['state'] = 'readonly'
combobox2.pack(fill='x',padx= 5, pady=5)


button = Button(window, text='Начать конвертацию', command=startProcess)
button.pack(pady=10)

window.mainloop()