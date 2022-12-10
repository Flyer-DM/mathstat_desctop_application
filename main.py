from tkinter import *
from statistics import mean, median


window = Tk()
window.geometry('300x140')
window.title("Добро пожаловать в приложение!")


def EMP():
    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    labelExample = Label(newWindow, text="New Window")
    buttonExample = Button(newWindow, text="New Window button")
    labelExample.pack()
    buttonExample.pack()


def TOUCH_OC():
    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    labelExample = Label(newWindow, text="New Window")
    buttonExample = Button(newWindow, text="New Window button")
    labelExample.pack()
    buttonExample.pack()


def INTERVAL_OC():
    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    labelExample = Label(newWindow, text="New Window")
    buttonExample = Button(newWindow, text="New Window button")
    labelExample.pack()
    buttonExample.pack()


def DOV_INTER():
    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    labelExample = Label(newWindow, text="Выберите доверительный интервал!")
    buttonExample1 = Button(newWindow, text="Рассчитать доверительный интервал для математического ожидания и дисперсии",command = DOV_INTER1)
    labelExample.pack()
    buttonExample1.pack()
    buttonExample2 = Button(newWindow,text="Рассчитать доверительный интервал, если вы ",command=DOV_INTER1)
    buttonExample2.pack()


def DOV_INTER1():
    def get_text():
        res = "Ваша введённая выборка:{}".format(txt.get())
        res2 = "{}".format(txt.get())
        res3 = res2.split()
        res4 = list(map(int, res3))
        Mean_A = mean(res4)  # Поиск среднего значения с помощью библиотеки statistics
        lbl2.configure(text=res)
        lbl3 = Label(newWindow, text="Кол-во элементов выборки = " + str(len(res3)))
        lbl3.grid(column=0, row=1)
        lbl4 = Label(newWindow, text="Среднее арифметическое значение = " + str(round(Mean_A,2)))
        lbl4.grid(column=0, row=2)

    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    lbl = Label(newWindow, text="Введите выборку")
    lbl.grid(column=0, row=0)

    txt = Entry(newWindow, width=10)
    txt.grid(column=1, row=0)

    lbl2 = Label(newWindow, text="Ваша введённая выборка:")
    lbl2.grid(column=3, row=0)

    btn = Button(newWindow, text="Подтвердить", command = get_text)
    btn.grid(column=2, row=0)




def SR_KV():
    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    labelExample = Label(newWindow, text="New Window")
    buttonExample = Button(newWindow, text="New Window button")
    labelExample.pack()
    buttonExample.pack()


def GIP():
    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    labelExample = Label(newWindow, text="New Window")
    buttonExample = Button(newWindow, text="New Window button")
    labelExample.pack()
    buttonExample.pack()


btn1 = Button(window,text = "Эмпирические характеристики",command = EMP)
btn1.pack()
btn2 = Button(window,text = "Точечные оценки",command = TOUCH_OC)
btn2.pack()
btn3 = Button(window,text = "Интервальные оценки",command = INTERVAL_OC)
btn3.pack()
btn4 = Button(window,text = "Доверительные интервалы",command = DOV_INTER)
btn4.pack()
btn5 = Button(window,text = "среднее кв отклонение",command = SR_KV)
btn5.pack()
btn5 = Button(window,text = "Гипотезы",command = GIP)
btn5.pack()


window.mainloop()
