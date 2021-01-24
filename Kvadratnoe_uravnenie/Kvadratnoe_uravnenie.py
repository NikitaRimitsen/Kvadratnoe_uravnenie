from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


a_list = []#список с результами корней
vod_list = []#Список водимых значений


def resenie(a,b,c):
    vod_list.append(a)
    vod_list.append(b)
    vod_list.append(c)

    D = b**2 - 4*a*c  # дискриминант
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант равен: %s \n X1 = %s \n X2 = %s \n" % (D, x1, x2)
        a_list.append(x1)
        a_list.append(x2)
       
    else:
        text = "Дискриминант равен: %s \n Нет корней у данного уравнения" % D 
    return text


def inserter(vod):
     #очищает поле для ввода 
    output.delete("0.0","end")
    output.insert("0.0",vod)


def proverka():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(resenie(a_val, b_val, c_val))
    except ValueError:
        inserter("Убедитесь, что вы ввели 3 значения")



def clear(event):
    #Очищает поле ввода
    caller = event.widget
    caller.delete("0", "end")


okno=Tk()
okno.title("Rimitsen Nikita-Решение квадратного уравнения")
okno.geometry("700x400")
frame = Frame(okno) #рабочая область
frame.grid()

a = Entry(frame,width=5)
a.bind("<FocusIn>", clear)
a.grid(row=1, column=1,padx=(10,0)) #grid(). Размещает виджеты на сетке. row/column – строка/столбец в сетке, 

a_lab=Label(frame, text="x**2+").grid(row=1,column=2)

b = Entry(frame, width=5)   # поле для ввода уравнения (b)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)

b_lab = Label(frame, text="x+").grid(row=1, column=4) 
 

c = Entry(frame, width=5)  # поле для ввода уравнения (с)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)

c_lab = Label(frame, text="= 0").grid(row=1, column=6)  



but = Button(frame, text="Решить", command=proverka).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="#98FB98", font="Times_New_Roman 14", width=70, height=25)  # область для вывода решения уравнения

output.grid(row=2, columnspan=10)

okno.mainloop()




def grafik(a,b,c):
    D = b ** 2 - 4 * a * c
    d = D ** 0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    if D > 0:
        return x1, x2
    elif x1 == x2:
        return x1
    else:
        exit('Complex roots')
 
 
k1=vod_list[0]
k2=vod_list[1]
k3=vod_list[2]
 
y0 = 0, 0
 

points = a_list[0], a_list[1]    
  
freq = 100 

xi = np.linspace(a_list[0], a_list[1], freq)
y = [k1 * t * t + k2 * t + k3 for t in xi]       

plt.scatter(points, y0, color='green')
plt.plot(xi, y)

plt.title("График квадратичной функции", fontsize=20, fontweight="bold") # заголовок
plt.xlabel("Ось Х", fontsize=14, fontweight="bold")# метка оси
plt.ylabel("Ось Y", fontsize=14, fontweight="bold")# метка оси



plt.tick_params(axis='both', labelsize=14) #шрифт делений на осях
plt.grid(True)



plt.savefig('sqrt.png')
plt.show()
