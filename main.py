import tkinter as tk

import numpy as np
import skfuzzy as fuzz
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def work():
    global m1, m2, m3, ma1, ma2, ma3

    m1 = float(min1.get())
    m2 = float(min2.get())
    m3 = float(min3.get())
    ma1 = float(max1.get())
    ma2 = float(max2.get())
    ma3 = float(max3.get())

    diag1(m1, m2, m3, ma1, ma2, ma3)


def diag1(m1, m2, m3, ma1, ma2, ma3):
    x1 = np.arange(m1, ma1 + 0.05, 0.1)
    x2 = np.arange(m2, ma2 + 0.05, 0.1)
    x3 = np.arange(m3, ma3 + 0.05, 0.1)

    global opp, opp10, opp_2, opp10_2, opp_3, opp10_3

    opp = ((ma1 - m1) / 3)
    opp10 = ((ma1 - m1) / 10)

    opp_2 = ((ma2 - m2) / 3)
    opp10_2 = ((ma2 - m2) / 10)

    opp_3 = ((ma3 - m3) / 3)
    opp10_3 = ((ma3 - m3) / 10)

    grph1 = fuzz.trapmf(x1, [m1 - 999, m1 - 999, (m1 + opp10 * 2), (m1 + opp10 * 3)])
    grph2 = fuzz.trapmf(x1, [(m1 + opp10 * 2), (m1 + opp), (m1 + opp * 2), (m1 + opp10 * 8)])
    grph3 = fuzz.trapmf(x1, [(m1 + opp10 * 7), (m1 + opp10 * 8), ma1 + 999, ma1 + 999])

    grph4 = fuzz.trapmf(x2, [m2 - 999, m2 - 999, (m2 + opp10_2 * 2), (m2 + opp10_2 * 3)])
    grph5 = fuzz.trapmf(x2, [(m2 + opp10_2 * 2), (m2 + opp_2), (m2 + opp_2 * 2), (m2 + opp10_2 * 8)])
    grph6 = fuzz.trapmf(x2, [(m2 + opp10_2 * 7), (m2 + opp10_2 * 8), ma2 + 999, ma2 + 999])

    grph7 = fuzz.trapmf(x3, [m3 - 999, m3 - 999, (m3 + opp10_3 * 2), (m3 + opp10_3 * 3)])
    grph8 = fuzz.trapmf(x3, [(m3 + opp10_3 * 2), (m3 + opp_3), (m3 + opp_3 * 2), (m3 + opp10_3 * 8)])
    grph9 = fuzz.trapmf(x3, [(m3 + opp10_3 * 7), (m3 + opp10_3 * 8), ma3 + 999, ma3 + 999])

    canv(x1, x2, x3, grph1, grph2, grph3, grph4, grph5, grph6, grph7, grph8, grph9)


def canv(x1, x2, x3, grph1, grph2, grph3, grph4, grph5, grph6, grph7, grph8, grph9):
    cl1 = call1.get()
    cl2 = call2.get()
    cl3 = call3.get()

    Framecanv = tk.Frame()

    tk.Label(Framecanv, text=cl1).grid(row=0, column=0)

    fig = Figure(figsize=(2.6, 2.6))
    a = fig.add_subplot(111)
    a.plot(x1, grph1, x1, grph2, x1, grph3, 'k')
    a.set_ylim(0.001, 1.1)
    a.grid()
    canvas = FigureCanvasTkAgg(fig, master=Framecanv)
    canvas.get_tk_widget().grid(row=1, column=0)
    canvas.draw()

    tk.Label(Framecanv, text=cl2).grid(row=0, column=1)

    fig2 = Figure(figsize=(2.6, 2.6))
    a2 = fig2.add_subplot(111)
    a2.plot(x2, grph4, x2, grph5, x2, grph6, 'k')
    a2.set_ylim(0.001, 1.1)
    a2.grid()
    canvas = FigureCanvasTkAgg(fig2, master=Framecanv)
    canvas.get_tk_widget().grid(row=1, column=1)
    canvas.draw()

    tk.Label(Framecanv, text=cl3).grid(row=0, column=2)

    fig3 = Figure(figsize=(2.6, 2.6))
    a3 = fig3.add_subplot(111)
    a3.plot(x3, grph7, x3, grph8, x3, grph9, 'k')
    a3.set_ylim(0.001, 1.1)
    a3.grid()
    canvas = FigureCanvasTkAgg(fig3, master=Framecanv)
    canvas.get_tk_widget().grid(row=1, column=2)
    canvas.draw()

    tk.Label(Framecanv, text=cl3).grid(row=0, column=2)

    Framecanv.pack()

    canv2()


def canv2():
    per_1 = float(e1.get())
    per_2 = float(e2.get())
    per_3 = float(e3.get())

    sr1 = ((ma1 - m1) / 2)
    sr2 = ((ma2 - m2) / 2)
    sr3 = ((ma3 - m3) / 2)

    Framecanv2 = tk.Frame()

    if per_1 < m1 + sr1:
        graphic_1 = Figure(figsize=(2.6, 2.6))
        gr_1 = graphic_1.add_subplot(111)
        xg = [m1 - 999, m1 - 999, (m1 + opp10 * 2), (m1 + opp10 * 3)]
        yg = [0, 0.9, 0.9, 0]
        xg2 = [(m1 + opp10 * 2), (m1 + opp), (m1 + opp * 2), (m1 + opp10 * 8)]
        yg2 = [0, 0.6, 0.6, 0]
        xg3 = [(m1 + opp10 * 7), (m1 + opp10 * 8), ma1 + 999, ma1 + 999]
        yg3 = [0, 0.2, 0.2, 0]
        gr_1.plot(xg, yg, xg2, yg2, xg3, yg3)
        gr_1.set_ylim(0.001, 1.1)
        gr_1.set_xlim(m1 + 0.001, ma1 + 0.1)
        gr_1.grid()
        canvas = FigureCanvasTkAgg(graphic_1, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.draw()
    elif per_1 > m1 + sr1:
        graphic_1 = Figure(figsize=(2.6, 2.6))
        gr_1 = graphic_1.add_subplot(111)
        xg = [m1 - 999, m1 - 999, (m1 + opp10 * 2), (m1 + opp10 * 3)]
        yg = [0, 0.2, 0.2, 0]
        xg2 = [(m1 + opp10 * 2), (m1 + opp), (m1 + opp * 2), (m1 + opp10 * 8)]
        yg2 = [0, 0.6, 0.6, 0]
        xg3 = [(m1 + opp10 * 7), (m1 + opp10 * 8), ma1 + 999, ma1 + 999]
        yg3 = [0, 0.9, 0.9, 0]
        gr_1.plot(xg, yg, xg2, yg2, xg3, yg3)
        gr_1.set_ylim(0.001, 1.1)
        gr_1.set_xlim(m1 + 0.001, ma1 + 0.1)
        gr_1.grid()
        canvas = FigureCanvasTkAgg(graphic_1, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.draw()
    else:
        graphic_1 = Figure(figsize=(2.6, 2.6))
        gr_1 = graphic_1.add_subplot(111)
        xg = [m1 - 999, m1 - 999, (m1 + opp10 * 2), (m1 + opp10 * 3)]
        yg = [0, 0.5, 0.5, 0]
        xg2 = [(m1 + opp10 * 2), (m1 + opp), (m1 + opp * 2), (m1 + opp10 * 8)]
        yg2 = [0, 0.9, 0.9, 0]
        xg3 = [(m1 + opp10 * 7), (m1 + opp10 * 8), ma1 + 999, ma1 + 999]
        yg3 = [0, 0.5, 0.5, 0]
        gr_1.plot(xg, yg, xg2, yg2, xg3, yg3)
        gr_1.set_ylim(0.001, 1.1)
        gr_1.set_xlim(m1 + 0.001, ma1 + 0.1)
        gr_1.grid()
        canvas = FigureCanvasTkAgg(graphic_1, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.draw()

    if per_2 < m2 + sr2:
        graphic_2 = Figure(figsize=(2.6, 2.6))
        gr_2 = graphic_2.add_subplot(111)
        xg_2 = [m2 - 999, m2 - 999, (m2 + opp10_2 * 2), (m2 + opp10_2 * 3)]
        yg_2 = [0, 0.9, 0.9, 0]
        xg2_2 = [(m2 + opp10_2 * 2), (m2 + opp_2), (m2 + opp_2 * 2), (m2 + opp10_2 * 8)]
        yg2_2 = [0, 0.6, 0.6, 0]
        xg3_2 = [(m2 + opp10_2 * 7), (m2 + opp10_2 * 8), ma2 + 999, ma2 + 999]
        yg3_2 = [0, 0.2, 0.2, 0]
        gr_2.plot(xg_2, yg_2, xg2_2, yg2_2, xg3_2, yg3_2)
        gr_2.set_ylim(0.001, 1.1)
        gr_2.set_xlim(m2 + 0.001, ma2 + 0.1)
        gr_2.grid()
        canvas = FigureCanvasTkAgg(graphic_2, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=1)
        canvas.draw()
    elif per_2 > m2 + sr2:
        graphic_2 = Figure(figsize=(2.6, 2.6))
        gr_2 = graphic_2.add_subplot(111)
        xg_2 = [m2 - 999, m2 - 999, (m2 + opp10_2 * 2), (m2 + opp10_2 * 3)]
        yg_2 = [0, 0.2, 0.2, 0]
        xg2_2 = [(m2 + opp10_2 * 2), (m2 + opp_2), (m2 + opp_2 * 2), (m2 + opp10_2 * 8)]
        yg2_2 = [0, 0.6, 0.6, 0]
        xg3_2 = [(m2 + opp10_2 * 7), (m2 + opp10_2 * 8), ma2 + 999, ma2 + 999]
        yg3_2 = [0, 0.9, 0.9, 0]
        gr_2.plot(xg_2, yg_2, xg2_2, yg2_2, xg3_2, yg3_2)
        gr_2.set_ylim(0.001, 1.1)
        gr_2.set_xlim(m2 + 0.001, ma2 + 0.1)
        gr_2.grid()
        canvas = FigureCanvasTkAgg(graphic_2, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=1)
        canvas.draw()
    else:
        graphic_2 = Figure(figsize=(2.6, 2.6))
        gr_2 = graphic_2.add_subplot(111)
        xg_2 = [m2 - 999, m2 - 999, (m2 + opp10_2 * 2), (m2 + opp10_2 * 3)]
        yg_2 = [0, 0.5, 0.5, 0]
        xg2_2 = [(m2 + opp10_2 * 2), (m2 + opp_2), (m2 + opp_2 * 2), (m2 + opp10_2 * 8)]
        yg2_2 = [0, 0.9, 0.9, 0]
        xg3_2 = [(m2 + opp10_2 * 7), (m2 + opp10_2 * 8), ma2 + 999, ma2 + 999]
        yg3_2 = [0, 0.5, 0.5, 0]
        gr_2.plot(xg_2, yg_2, xg2_2, yg2_2, xg3_2, yg3_2)
        gr_2.set_ylim(0.001, 1.1)
        gr_2.set_xlim(m2 + 0.001, ma2 + 0.1)
        gr_2.grid()
        canvas = FigureCanvasTkAgg(graphic_2, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=1)
        canvas.draw()

    if per_3 < m3 + sr3:
        graphic_3 = Figure(figsize=(2.6, 2.6))
        gr_3 = graphic_3.add_subplot(111)
        xg_3 = [m3 - 999, m3 - 999, (m3 + opp10_3 * 2), (m3 + opp10_3 * 3)]
        yg_3 = [0, 0.9, 0.9, 0]
        xg2_3 = [(m3 + opp10_3 * 2), (m3 + opp_3), (m3 + opp_3 * 2), (m3 + opp10_3 * 8)]
        yg2_3 = [0, 0.6, 0.6, 0]
        xg3_3 = [(m3 + opp10_3 * 7), (m3 + opp10_3 * 8), ma3 + 999, ma3 + 999]
        yg3_3 = [0, 0.2, 0.2, 0]
        gr_3.plot(xg_3, yg_3, xg2_3, yg2_3, xg3_3, yg3_3)
        gr_3.set_ylim(0.001, 1.1)
        gr_3.set_xlim(m3 + 0.001, ma3 + 0.1)
        gr_3.grid()
        canvas = FigureCanvasTkAgg(graphic_3, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=2)
        canvas.draw()
    elif per_3 > m3 + sr3:
        graphic_3 = Figure(figsize=(2.6, 2.6))
        gr_3 = graphic_3.add_subplot(111)
        xg_3 = [m3 - 999, m3 - 999, (m3 + opp10_3 * 2), (m3 + opp10_3 * 3)]
        yg_3 = [0, 0.2, 0.2, 0]
        xg2_3 = [(m3 + opp10_3 * 2), (m3 + opp_3), (m3 + opp_3 * 2), (m3 + opp10_3 * 8)]
        yg2_3 = [0, 0.6, 0.6, 0]
        xg3_3 = [(m3 + opp10_3 * 7), (m3 + opp10_3 * 8), ma3 + 999, ma3 + 999]
        yg3_3 = [0, 0.9, 0.9, 0]
        gr_3.plot(xg_3, yg_3, xg2_3, yg2_3, xg3_3, yg3_3)
        gr_3.set_ylim(0.001, 1.1)
        gr_3.set_xlim(m3 + 0.001, ma3 + 0.1)
        gr_3.grid()
        canvas = FigureCanvasTkAgg(graphic_3, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=2)
        canvas.draw()
    else:
        graphic_3 = Figure(figsize=(2.6, 2.6))
        gr_3 = graphic_3.add_subplot(111)
        xg_3 = [m3 - 999, m3 - 999, (m3 + opp10_3 * 2), (m3 + opp10_3 * 3)]
        yg_3 = [0, 0.5, 0.5, 0]
        xg2_3 = [(m3 + opp10_3 * 2), (m3 + opp_3), (m3 + opp_3 * 2), (m3 + opp10_3 * 8)]
        yg2_3 = [0, 0.9, 0.9, 0]
        xg3_3 = [(m3 + opp10_3 * 7), (m3 + opp10_3 * 8), ma3 + 999, ma3 + 999]
        yg3_3 = [0, 0.5, 0.5, 0]
        gr_3.plot(xg_3, yg_3, xg2_3, yg2_3, xg3_3, yg3_3)
        gr_3.set_ylim(0.001, 1.1)
        gr_3.set_xlim(m3 + 0.001, ma3 + 0.1)
        gr_3.grid()
        canvas = FigureCanvasTkAgg(graphic_3, master=Framecanv2)
        canvas.get_tk_widget().grid(row=0, column=2)
        canvas.draw()

    Framecanv2.pack()


root = tk.Tk()
root.geometry('1400x800')
root.title('Made by Devi0let')
root.resizable(False, False)

Frame = tk.Frame()

tk.Label(root, text='Вычисление нечёткой базы (Предпологается использование схемы "Мало, Достаточно, Много")').pack()
tk.Label(Frame, text='Первая переменная: ').grid(row=1, column=0)
tk.Label(Frame, text='Вторая переменная: ').grid(row=1, column=2)
tk.Label(Frame, text='Третья переменная: ').grid(row=1, column=4)
e1 = tk.Entry(Frame, width=4)
e2 = tk.Entry(Frame, width=4)
e3 = tk.Entry(Frame, width=4)
e1.grid(row=1, column=1)
e2.grid(row=1, column=3)
e3.grid(row=1, column=5)
tk.Label(Frame, text='                         ').grid(row=1, column=6)

tk.Label(Frame, text='').grid(row=2)
Frame2 = tk.Frame()
tk.Label(Frame2, text='Поля для своих переменных').grid(row=0, column=0)
tk.Label(Frame2, text='MIN').grid(row=0, column=1)
tk.Label(Frame2, text='MAX').grid(row=0, column=2)

call1 = tk.Entry(Frame2)
call2 = tk.Entry(Frame2)
call3 = tk.Entry(Frame2)
min1 = tk.Entry(Frame2, width=4)
min2 = tk.Entry(Frame2, width=4)
min3 = tk.Entry(Frame2, width=4)
max1 = tk.Entry(Frame2, width=4)
max2 = tk.Entry(Frame2, width=4)
max3 = tk.Entry(Frame2, width=4)
call1.grid(row=1, column=0)
call2.grid(row=2, column=0)
call3.grid(row=3, column=0)
min1.grid(row=1, column=1)
min2.grid(row=2, column=1)
min3.grid(row=3, column=1)
max1.grid(row=1, column=2)
max2.grid(row=2, column=2)
max3.grid(row=3, column=2)

Frame.pack()
Frame2.pack()

tk.Label(text='').pack()
tk.Button(root, text='Вычислить', command=work).pack()

root.mainloop()
