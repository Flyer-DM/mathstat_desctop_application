from tkinter import *
from statistics import mean, median
from math import sqrt


window = Tk()
logo = PhotoImage(file='math.png')
window.geometry('370x155')
window.iconphoto(False, logo)
window.config(bg='#E6E6FA')
window.resizable(False, False)
window.title("Типовые задания по мат статистике.")


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
    newWindow.geometry('800x500')
    labelExample = Label(newWindow, text="Выберите доверительный интервал!")
    buttonExample1 = Button(newWindow, text="Рассчитать доверительный интервал для математического ожидания и дисперсии при надёжности оценки 0.98",command = DOV_INTER1)
    labelExample.pack()
    buttonExample1.pack()
    buttonExample2 = Button(newWindow,text="Рассчитать доверительный интервал",command=DOV_INTER2)
    buttonExample2.pack()


def DOV_INTER1():
    def get_text():
        res = "Ваша введённая выборка:{}".format(txt.get())
        res2 = "{}".format(txt.get())
        res3 = res2.split()
        res4 = list(map(int, res3))
        Mean_A = mean(res4)  # Поиск среднего значения с помощью библиотеки statistics
        Sorted_A = sorted(res4)
        Median_A = median(Sorted_A)
        Min_A = Sorted_A[0]
        Max_A = Sorted_A[-1]
        R = Max_A - Min_A  # Поиск размаха
        D = 0
        for i in res4:  # Для каждого элемента в массиве A
            D += ((i - Mean_A) ** 2)  # D = значение массива - среднее значение и всё это в степени 2 и результат прибавляется к D до тех пор пока элементы в выборке не закончатся
        Disper_A = D / len(res4)  # D делим на количество элементов выборки A и находим дисперсию
        KV_A = sqrt(Disper_A)  # С помощью sqrt из библиотеки math, извлекаем корень из дисперсии и находим средне квадратическое отклонение
        Ocen = (2.33 * KV_A) / sqrt(len(res4))  # Находим точность оценки, при надёжности оценки 0.98

        Result1_min = Mean_A - Ocen
        Result1_max = Mean_A + Ocen

        lbl2.configure(text=res)
        lbl3 = Label(newWindow, text="Кол-во элементов выборки = " + str(len(res3)))
        lbl3.grid(column=0, row=1)
        lbl4 = Label(newWindow, text="Среднее арифметическое значение = " + str(round(Mean_A,2)))
        lbl4.grid(column=0, row=2)
        lbl5 = Label(newWindow, text="Медиана = " + str(round(Median_A,2)))
        lbl5.grid(column=0, row=3)
        lbl6 = Label(newWindow, text="Размах = " + str(round(R,2)))
        lbl6.grid(column=0, row=4)
        lbl7 = Label(newWindow, text="Дисперсия = " + str(round(Disper_A,2)))
        lbl7.grid(column=0, row=5)
        lbl8 = Label(newWindow, text="Среднее квадратическое отклонение = " + str(round(KV_A,2)))
        lbl8.grid(column=0, row=6)
        lbl9 = Label(newWindow, text="Доверительный интервал = [" + str(round(Result1_min,2)) + ", " + str(round(Result1_max,2)) + "]")
        lbl9.grid(column=0, row=7)

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

def DOV_INTER2():
    def get_text2():
        res = "Ваша введённая выборка:{}".format(txt.get())
        res2 = "{}".format(txt.get())
        res3 = res2.split()
        res4 = list(map(int, res3))
        Mean_A = mean(res4)  # Поиск среднего значения с помощью библиотеки statistics
        Sorted_A = sorted(res4)
        Median_A = median(Sorted_A)
        Min_A = Sorted_A[0]
        Max_A = Sorted_A[-1]
        R = Max_A - Min_A  # Поиск размаха
        D = 0
        for i in res4:  # Для каждого элемента в массиве A
            D += ((i - Mean_A) ** 2)  # D = значение массива - среднее значение и всё это в степени 2 и результат прибавляется к D до тех пор пока элементы в выборке не закончатся
        Disper_A = D / len(res4)  # D делим на количество элементов выборки A и находим дисперсию
        KV_A = sqrt(Disper_A)  # С помощью sqrt из библиотеки math, извлекаем корень из дисперсии и находим средне квадратическое отклонение


        Result2_min = Median_A - KV_A
        Result2_max = Median_A + KV_A

        lbl2.configure(text=res)
        lbl3 = Label(newWindow, text="Кол-во элементов выборки = " + str(len(res3)))
        lbl3.grid(column=0, row=1)
        lbl4 = Label(newWindow, text="Среднее арифметическое значение = " + str(round(Mean_A,2)))
        lbl4.grid(column=0, row=2)
        lbl5 = Label(newWindow, text="Медиана = " + str(round(Median_A,2)))
        lbl5.grid(column=0, row=3)
        lbl6 = Label(newWindow, text="Размах = " + str(round(R,2)))
        lbl6.grid(column=0, row=4)
        lbl7 = Label(newWindow, text="Дисперсия = " + str(round(Disper_A,2)))
        lbl7.grid(column=0, row=5)
        lbl8 = Label(newWindow, text="Среднее квадратическое отклонение = " + str(round(KV_A,2)))
        lbl8.grid(column=0, row=6)
        lbl9 = Label(newWindow, text="Доверительный интервал = [" + str(round(Result2_min,2)) + ", " + str(round(Result2_max,2))+"]")
        lbl9.grid(column=0, row=7)

    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    lbl = Label(newWindow, text="Введите выборку")
    lbl.grid(column=0, row=0)

    txt = Entry(newWindow, width=10)
    txt.grid(column=1, row=0)

    lbl2 = Label(newWindow, text="Ваша введённая выборка:")
    lbl2.grid(column=3, row=0)

    btn = Button(newWindow, text="Подтвердить", command = get_text2)
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


Button(window, text="Эмпирические характеристики", command=EMP, relief=GROOVE).grid(column=0, row=0, sticky=W)
Button(window, text="Точечные оценки", command=TOUCH_OC, relief=GROOVE).grid(column=0, row=1, sticky=W)
Button(window, text="Интервальные оценки", command=INTERVAL_OC, relief=GROOVE).grid(column=0, row=2, sticky=W)
Button(window, text="Доверительные интервалы", command=DOV_INTER, relief=GROOVE).grid(column=0, row=3, sticky=W)
Button(window, text="Среднее кв. отклонение", command=SR_KV, relief=GROOVE).grid(column=0, row=4, sticky=W)
Button(window, text="Гипотезы", command=GIP, relief=GROOVE).grid(column=0, row=5, sticky=W)


if __name__ == '__main__':
    window.mainloop()
