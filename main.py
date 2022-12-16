from tkinter import *
from statistics import mean, median
from math import sqrt
from os import remove
import matplotlib.pyplot as plt
import numpy as np

window = Tk()
logo = PhotoImage(file='math.png')
window.geometry('700x155')
window.iconphoto(False, logo)
window.config(bg='#E6E6FA')
window.resizable(False, False)
window.title("Типовые задания по мат статистике.")


def EMP():
    def get_text():
        y1 = int("{}".format(ytxt.get()))  # Получение всех Y
        y2 = int("{}".format(ytxt2.get()))
        y3 = int("{}".format(ytxt3.get()))
        n1 = int("{}".format(txt.get()))  # Получение всех значений
        n2 = int("{}".format(txt1.get()))
        n3 = int("{}".format(txt2.get()))
        n4 = int("{}".format(txt3.get()))
        n5 = int("{}".format(txt4.get()))
        n6 = int("{}".format(txt5.get()))
        n7 = int("{}".format(txt6.get()))
        n8 = int("{}".format(txt7.get()))
        n9 = int("{}".format(txt8.get()))
        n10 = int("{}".format(txt9.get()))
        n11 = int("{}".format(txt10.get()))
        n12 = int("{}".format(txt11.get()))
        x1 = int("{}".format(xtxt.get()))  # Получение всех X
        x2 = int("{}".format(xtxt2.get()))
        x3 = int("{}".format(xtxt3.get()))
        x4 = int("{}".format(xtxt4.get()))
        N = int("{}".format(ntxt.get()))  # Получение N
        x1_all = n1 + n2 + n3  # Сумма колонки x1
        x2_all = n4 + n5 + n6  # Сумма колонки x2
        x3_all = n7 + n8 + n9  # Сумма колонки x3
        x4_all = n10 + n11 + n12  # Сумма колонки x4
        y1_all = n1 + n4 + n7 + n10  # Сумма колонки y1
        y2_all = n2 + n5 + n8 + n11  # Сумма колонки y2
        y3_all = n3 + n6 + n9 + n12  # Сумма колонки y3
        sr_x = (1 / N) * (x1 * x1_all + x2 * x2_all + x3 * x3_all + x4 * x4_all)  # Среднее значение X
        D_x = (1 / N) * (
                (((x1 - sr_x) ** 2) * x1_all) + (((x2 - sr_x) ** 2) * x2_all) + (((x3 - sr_x) ** 2) * x3_all) + (
                ((x4 - sr_x) ** 2) * x4_all))  # Эмпирическая дисперсия X
        sr_y = (1 / N) * (y1 * y1_all + y2 * y2_all + y3 * y3_all)  # Среднее значение Y
        D_y = (1 / N) * ((((y1 - sr_y) ** 2) * y1_all) + (((y2 - sr_y) ** 2) * y2_all) + (
                ((y3 - sr_y) ** 2) * y3_all))  # Эмпирическая дисперсия Y
        COV = (((x1 - sr_x) * (y1 - sr_y) * n1) + ((x2 - sr_x) * (y1 - sr_y) * n4) + (
                (x3 - sr_x) * (y1 - sr_y) * n7) + ((x4 - sr_x) * (y1 - sr_y) * n10) + (
                       (x1 - sr_x) * (y2 - sr_y) * n2) + ((x2 - sr_x) * (y2 - sr_y) * n5) + (
                       (x3 - sr_x) * (y2 - sr_y) * n8) + ((x4 - sr_x) * (y2 - sr_y) * n11) + (
                       (x1 - sr_x) * (y3 - sr_y) * n3) + ((x2 - sr_x) * (y3 - sr_y) * n6) + (
                       (x3 - sr_x) * (y3 - sr_y) * n9) + ((x4 - sr_x) * (y3 - sr_y) * n12)) / N  # Ковариация
        p = COV / sqrt(D_x * D_y)  # Эмпирический коэффициент корреляции

        lbl = Label(newWindow, text="Значение X:")  # Частотные распределения признаков X
        lbl.grid(column=0, row=5)
        lbl2 = Label(newWindow, text=str(x1))
        lbl2.grid(column=1, row=5)
        lbl3 = Label(newWindow, text=str(x2))
        lbl3.grid(column=2, row=5)
        lbl4 = Label(newWindow, text=str(x3))
        lbl4.grid(column=3, row=5)
        lbl5 = Label(newWindow, text=str(x4))
        lbl5.grid(column=4, row=5)
        lbl6 = Label(newWindow, text="Частота:")
        lbl6.grid(column=0, row=6)
        lbl7 = Label(newWindow, text=str(x1_all))
        lbl7.grid(column=1, row=6)
        lbl8 = Label(newWindow, text=str(x2_all))
        lbl8.grid(column=2, row=6)
        lbl9 = Label(newWindow, text=str(x3_all))
        lbl9.grid(column=3, row=6)
        lbl10 = Label(newWindow, text=str(x4_all))
        lbl10.grid(column=4, row=6)

        lbl_empty = Label(newWindow, text="")  # Пустая строчка для разделения частотных признаков между собой
        lbl_empty.grid(column=0, row=7)

        lbl11 = Label(newWindow, text="Значение Y:")  # Частотные распределения признаков Y
        lbl11.grid(column=0, row=8)
        lbl12 = Label(newWindow, text=str(y1))
        lbl12.grid(column=1, row=8)
        lbl13 = Label(newWindow, text=str(y2))
        lbl13.grid(column=2, row=8)
        lbl14 = Label(newWindow, text=str(y3))
        lbl14.grid(column=3, row=8)
        lbl15 = Label(newWindow, text="Частота:")
        lbl15.grid(column=0, row=9)
        lbl16 = Label(newWindow, text=str(y1_all))
        lbl16.grid(column=1, row=9)
        lbl17 = Label(newWindow, text=str(y2_all))
        lbl17.grid(column=2, row=9)
        lbl18 = Label(newWindow, text=str(y3_all))
        lbl18.grid(column=3, row=9)

        lbl_empty2 = Label(newWindow,
                           text="")  # Пустая строчка для разделения частотных признаков и эмпирических характеристик
        lbl_empty2.grid(column=0, row=10)

        lbl19 = Label(newWindow, text="ср. x = " + str(sr_x))  # Среднее значение X
        lbl19.grid(column=0, row=11)
        lbl20 = Label(newWindow, text="ср. y = " + str(sr_y))  # Среднее значение Y
        lbl20.grid(column=0, row=12)
        lbl21 = Label(newWindow, text="D(X) = " + str(D_x))  # Эмпирическая дисперсия по X
        lbl21.grid(column=0, row=13)
        lbl22 = Label(newWindow, text="D(Y) = " + str(D_y))  # Эмпирическая дисперсия по Y
        lbl22.grid(column=0, row=14)
        lbl23 = Label(newWindow, text="COV(X,Y) = " + str(COV))  # Эмпирическая ковариация
        lbl23.grid(column=0, row=15)
        lbl24 = Label(newWindow, text="p(X,Y) = " + str(p))  # Эмпирический коэффициент корреляции
        lbl24.grid(column=0, row=16)

        lbl_empty3 = Label(newWindow, text="")  # Пустая строчка для разделения эмпирических характеристик и ответа
        lbl_empty3.grid(column=0, row=17)

        lbl24 = Label(newWindow, text="Ответ: Эмпирический коэффициент корреляции = " + str(p))  # Ответ
        lbl24.grid(column=0, row=18)

    newWindow = Toplevel(window)
    newWindow.title("Эмпирические характеристики")
    newWindow.geometry('1000x500')

    lbl = Label(newWindow,
                text="Если вам надо найти эмпирический коэффициент корреляции ρ(X, Y), то вам нужно ввести следующие данные:",
                font=('Franklin Gothic Medium Cond', 10))
    lbl.grid(column=0, row=0, columnspan=6)

    lbl = Label(newWindow, text="Введите значения:", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbl.grid(column=0, row=1)

    lblt = Label(newWindow, text="Y  /  X", font=('Franklin Gothic Medium Cond', 10))
    lblt.grid(column=1, row=1)

    ytxt = Entry(newWindow, width=10)  # Entry по Y
    ytxt.grid(column=1, row=2)

    ytxt2 = Entry(newWindow, width=10)
    ytxt2.grid(column=1, row=3)

    ytxt3 = Entry(newWindow, width=10)
    ytxt3.grid(column=1, row=4)

    txt = Entry(newWindow, width=10)  # Entry по всем значениям
    txt.grid(column=2, row=2)

    txt1 = Entry(newWindow, width=10)
    txt1.grid(column=2, row=3)

    txt2 = Entry(newWindow, width=10)
    txt2.grid(column=2, row=4)

    txt3 = Entry(newWindow, width=10)
    txt3.grid(column=3, row=2)

    txt4 = Entry(newWindow, width=10)
    txt4.grid(column=3, row=3)

    txt5 = Entry(newWindow, width=10)
    txt5.grid(column=3, row=4)

    txt6 = Entry(newWindow, width=10)
    txt6.grid(column=4, row=2)

    txt7 = Entry(newWindow, width=10)
    txt7.grid(column=4, row=3)

    txt8 = Entry(newWindow, width=10)
    txt8.grid(column=4, row=4)

    txt9 = Entry(newWindow, width=10)
    txt9.grid(column=5, row=2)

    txt10 = Entry(newWindow, width=10)
    txt10.grid(column=5, row=3)

    txt11 = Entry(newWindow, width=10)
    txt11.grid(column=5, row=4)

    xtxt = Entry(newWindow, width=10)  # Entry по X
    xtxt.grid(column=2, row=1)

    xtxt2 = Entry(newWindow, width=10)
    xtxt2.grid(column=3, row=1)

    xtxt3 = Entry(newWindow, width=10)
    xtxt3.grid(column=4, row=1)

    xtxt4 = Entry(newWindow, width=10)
    xtxt4.grid(column=5, row=1)

    lbln = Label(newWindow, text="Введите значение n:", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbln.grid(column=6, row=1)

    ntxt = Entry(newWindow, width=10)  # Entry по значению n
    ntxt.grid(column=7, row=1)

    btn = Button(newWindow, text="Подтвердить", command=get_text)
    btn.grid(column=8, row=1)


def DOV_INTER1():
    def get_text():
        res = "Ваша введённая выборка:{}".format(txt.get())
        res2 = "{}".format(txt.get())
        res3 = res2.split()
        res4 = list(map(float, res3))
        Mean_A = mean(res4)  # Поиск среднего значения с помощью библиотеки statistics
        Sorted_A = sorted(res4)
        Median_A = median(Sorted_A)
        Min_A = Sorted_A[0]
        Max_A = Sorted_A[-1]
        R = Max_A - Min_A  # Поиск размаха
        D = 0
        for i in res4:  # Для каждого элемента в массиве A
            D += ((
                          i - Mean_A) ** 2)  # D = значение массива - среднее значение и всё это в степени 2 и результат прибавляется к D до тех пор пока элементы в выборке не закончатся
        Disper_A = D / len(res4)  # D делим на количество элементов выборки A и находим дисперсию
        KV_A = sqrt(
            Disper_A)  # С помощью sqrt из библиотеки math, извлекаем корень из дисперсии и находим средне квадратическое отклонение
        Ocen = (2.33 * KV_A) / sqrt(len(res4))  # Находим точность оценки, при надёжности оценки 0.98

        Result1_min = Mean_A - Ocen
        Result1_max = Mean_A + Ocen

        lbl2.configure(text=res)
        lbl3 = Label(newWindow, text="Кол-во элементов выборки = " + str(len(res3)))
        lbl3.grid(column=0, row=2)
        lbl4 = Label(newWindow, text="Среднее арифметическое значение = " + str(round(Mean_A, 2)))
        lbl4.grid(column=0, row=3)
        lbl5 = Label(newWindow, text="Медиана = " + str(round(Median_A, 2)))
        lbl5.grid(column=0, row=4)
        lbl6 = Label(newWindow, text="Размах = " + str(round(R, 2)))
        lbl6.grid(column=0, row=5)
        lbl7 = Label(newWindow, text="Дисперсия = " + str(round(Disper_A, 2)))
        lbl7.grid(column=0, row=6)
        lbl8 = Label(newWindow, text="Среднее квадратическое отклонение = " + str(round(KV_A, 2)))
        lbl8.grid(column=0, row=7)
        lbl9 = Label(newWindow, text="Доверительный интервал = [" + str(round(Result1_min, 2)) + ", " + str(
            round(Result1_max, 2)) + "]")
        lbl9.grid(column=0, row=8)

    newWindow = Toplevel(window)
    newWindow.title("Доверительный интервал для мат. ожид. и D(X) при a=0.98")
    newWindow.geometry('600x500')

    lbl = Label(newWindow,
                text="Введите выборку и будет произведён автоматический расчёт с помощью надёжности оценки 0.98",
                font=('Franklin Gothic Medium Cond', 10))
    lbl.grid(column=0, row=0, columnspan=4)

    lbl = Label(newWindow, text="Введите выборку", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbl.grid(column=0, row=1)

    txt = Entry(newWindow, width=10)
    txt.grid(column=1, row=1)

    lbl2 = Label(newWindow, text="Ваша введённая выборка:", font=('Franklin Gothic Medium Cond', 10))
    lbl2.grid(column=3, row=1)

    btn = Button(newWindow, text="Подтвердить", command=get_text)
    btn.grid(column=2, row=1)


def DOV_INTER2():
    def get_text2():
        res = "Ваша введённая выборка:{}".format(txt.get())
        res2 = "{}".format(txt.get())
        res3 = res2.split()
        res4 = list(map(float, res3))
        Mean_A = mean(res4)  # Поиск среднего значения с помощью библиотеки statistics
        Sorted_A = sorted(res4)
        Median_A = median(Sorted_A)
        Min_A = Sorted_A[0]
        Max_A = Sorted_A[-1]
        R = Max_A - Min_A  # Поиск размаха
        D = 0
        for i in res4:  # Для каждого элемента в массиве A
            D += ((
                          i - Mean_A) ** 2)  # D = значение массива - среднее значение и всё это в степени 2 и результат прибавляется к D до тех пор пока элементы в выборке не закончатся
        Disper_A = D / len(res4)  # D делим на количество элементов выборки A и находим дисперсию
        KV_A = sqrt(
            Disper_A)  # С помощью sqrt из библиотеки math, извлекаем корень из дисперсии и находим средне квадратическое отклонение

        Result2_min = Median_A - KV_A
        Result2_max = Median_A + KV_A

        lbl2.configure(text=res)
        lbl3 = Label(newWindow, text="Кол-во элементов выборки = " + str(len(res3)))
        lbl3.grid(column=0, row=2)
        lbl4 = Label(newWindow, text="Среднее арифметическое значение = " + str(round(Mean_A, 2)))
        lbl4.grid(column=0, row=3)
        lbl5 = Label(newWindow, text="Медиана = " + str(round(Median_A, 2)))
        lbl5.grid(column=0, row=4)
        lbl6 = Label(newWindow, text="Размах = " + str(round(R, 2)))
        lbl6.grid(column=0, row=5)
        lbl7 = Label(newWindow, text="Дисперсия = " + str(round(Disper_A, 2)))
        lbl7.grid(column=0, row=6)
        lbl8 = Label(newWindow, text="Среднее квадратическое отклонение = " + str(round(KV_A, 2)))
        lbl8.grid(column=0, row=7)
        lbl9 = Label(newWindow, text="Доверительный интервал = [" + str(round(Result2_min, 2)) + ", " + str(
            round(Result2_max, 2)) + "]")
        lbl9.grid(column=0, row=8)

    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    newWindow.title("Доверительный интервал по выборке")

    lbl = Label(newWindow, text="Введите выборку и будет произведён автоматический расчёт с помощью ср. кв. отклонения",
                font=('Franklin Gothic Medium Cond', 10))
    lbl.grid(column=0, row=0, columnspan=4)

    lbl = Label(newWindow, text="Введите выборку", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbl.grid(column=0, row=1)

    txt = Entry(newWindow, width=10)
    txt.grid(column=1, row=1)

    lbl2 = Label(newWindow, text="Ваша введённая выборка:", font=('Franklin Gothic Medium Cond', 10))
    lbl2.grid(column=3, row=1)

    btn = Button(newWindow, text="Подтвердить", command=get_text2)
    btn.grid(column=2, row=2)


def DOV_INTER3():
    def get_text():
        res = "Ваше значение n (количество недель) = {}".format(txt.get())
        n = int("{}".format(txt.get()))
        print(n)
        r = float("{}".format(txt2.get()))
        srkv = float("{}".format(txt3.get()))
        leftres = r - 1.96 * (srkv / sqrt(n))
        rightres = r + 1.96 * (srkv / sqrt(n))

        lbl33.configure(text=res)
        lbl4 = Label(newWindow, text="Выборочная средняя r = " + str(r))
        lbl4.grid(column=3, row=1)
        lbl5 = Label(newWindow, text="ср. кв. отклонение = " + str(srkv))
        lbl5.grid(column=3, row=2)

        lbl9 = Label(newWindow,
                     text="Доверительный интервал = [" + str(round(leftres, 4)) + "," + str(round(rightres, 4)) + "]")
        lbl9.grid(column=0, row=7)

    newWindow = Toplevel(window)
    newWindow.geometry('600x500')
    newWindow.title("Доверительный интервал для мат. ожид. при среднем выборки и средкв. откл. при a=0.95")
    lbl = Label(newWindow, text="Введите n (количество недель)", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbl.grid(column=0, row=0)

    txt = Entry(newWindow, width=10)
    txt.grid(column=1, row=0)

    lbl2 = Label(newWindow, text="Введите выборочную среднюю r", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbl2.grid(column=0, row=1)

    txt2 = Entry(newWindow, width=10)
    txt2.grid(column=1, row=1)

    lbl3 = Label(newWindow, text="Введите ср. кв. отклонение", font=('Franklin Gothic Medium Cond', 10, 'bold'))
    lbl3.grid(column=0, row=2)

    txt3 = Entry(newWindow, width=10)
    txt3.grid(column=1, row=2)

    lbl33 = Label(newWindow, text="Ваши значения:", font=('Franklin Gothic Medium Cond', 10))
    lbl33.grid(column=3, row=0)

    btn = Button(newWindow, text="Подтвердить", command=get_text)
    btn.grid(column=2, row=0)


def variance_analysis():
    """Однофакторный дисперсионный анализ"""

    def solve():
        solved1, solved2, solved3 = Label(newWindow), Label(newWindow), Label(newWindow)
        try:
            data = {float(i.split(' - ')[0]): [float(j) for j in i.split(' - ')[1].split(', ')] for i in
                    txt_input.get().split('; ')}
            n, k = len([data[i] for i in data][0]), len(data)
            squeres = []
            for i in data.values():
                squeres.extend(i)
            squeres = list(map(lambda x: x ** 2, squeres))
            x_means = [round(sum(data[i]) / len(data[i]), 4) for i in data]
            gen_x_mean = round(sum(x_means) / k, 4)
            Q = round(sum(squeres) - n * k * gen_x_mean ** 2, 4)
            Qa = round(n * sum(map(lambda x: x ** 2, x_means)) - n * k * gen_x_mean ** 2, 4)
            Qe = Q - Qa
            F = round((Qa / (k - 1)) / (Qe / (k * (n - 1))), 4)
            solved1['text'] = f"Результат: выборочное значение статистики Фишера равно {str(F)}"
            solved2['text'] = f"Квантиль распределения Fa при {(k-1)=}, {k*(n-1)=} см. по таблице"
            solved3['text'] = f"Если F < Fa, гипотеза H0 принимается, иначе - отклоняется."
        except (ValueError, IndexError):
            solved1['text'] = "Ошибка ввода, попробуйте ещё раз." + " " * 100
            solved2['text'], solved3['text'] = " " * 150, " " * 150
        finally:
            solved1.grid(column=0, row=3, sticky=W)
            solved2.grid(column=0, row=4, sticky=W)
            solved3.grid(column=0, row=5, sticky=W)

    newWindow = Toplevel(window)
    newWindow.geometry('745x670')
    newWindow.title("Однофакторный дисперсионный анализ")
    text = """Проверяется нулевая гипотеза H0 об отсутствии влияния на результативный признак X некоторого фактора A,
имеющего k уровней. Сопостовляется дисперсия за счёт воздействия фактора A с дисперсией, обусловленной
случайными причинами. Если различие несущественно, то влияние фактора А на признак Х незначительно.
Вводите данные в формате уровень фактора - наблюдения через запятую."""
    Label(newWindow, text=text, justify=LEFT, font=('Franklin Gothic Medium Cond', 10)).grid(column=0, row=0, sticky=W)
    Label(newWindow, text="Введите значения в формате \"k1 - x1, x2, ...; k2 - x1, x2, ...\" :",
          justify=LEFT, font=('Franklin Gothic Medium Cond', 10, 'bold')).grid(column=0, row=1, sticky=W)
    txt_input = Entry(newWindow, width=60)
    txt_input.grid(column=0, row=2, sticky=W)
    Button(newWindow, text="Решить", command=solve).place(x=365, y=88)
    image = Label(newWindow)
    image.image = PhotoImage(file='./Fisher.png')
    image['image'] = image.image
    image.place(x=0, y=175)
    Label(newWindow, text="Таблица распределения Фишера", font=('Franklin Gothic Medium Cond', 10)).place(x=0, y=635)


def xi_square():
    """Критерий хи-квадрат Пирсона"""

    def solve():
        solved = Label(newWindow, justify=LEFT)
        try:
            fig, ax = plt.subplots()
            data = [(float(i.split(' - ')[0]), float(i.split(' - ')[1])) for i in txt_input.get().split('; ')]
            xi = round(sum(map(lambda x: (x[0] - x[1]) ** 2 / x[1], data)), 4)
            real, theory, labels = [i[0] for i in data], [i[1] for i in data], [i for i in range(1, len(data) + 1)]
            x = np.arange(len(labels))
            ax.bar(x - 0.175, real, 0.35, label='Эмпирические наблюдения', color='b')
            ax.bar(x + 0.175, theory, 0.35, label='Теоретические наблюдения', color='g')
            ax.set_title('Распределение хи-квадрат')
            ax.set_xticks(x, labels)
            ax.legend()
            plt.savefig('graph.png')
            newWindow1 = Toplevel(window)
            newWindow1.title("График")
            image1 = Label(newWindow1)
            image1.image = PhotoImage(file='./graph.png')
            image1['image'] = image1.image
            image1.pack()
#MatplotlibDeprecationWarning: Support for FigureCanvases without a required_interactive_framework attribute was deprecated
            text = f"""Эмпирическое значение критерия равно {xi} при числе степеней свободы равному {len(data) - 1}.
Если реальное значение меньше табличного, то гипотеза H0 принимается, иначе отклоняется."""
            solved['text'] = text
            remove('./graph.png')
        except (ValueError, IndexError, ZeroDivisionError):
            solved['text'] = "Ошибка ввода, попробуйте ещё раз." + " " * 150 + "\n" + " " * 200
        finally:
            solved.place(x=0, y=125)

    newWindow = Toplevel(window)
    newWindow.geometry('830x600')
    newWindow.title("Критерий хи-квадрат Пирсона")
    text = """Критерий Пирсона отвечает на вопрос о том, с одинаковой ли частотой встречаются разные значения признака
в эмпирическом и теоретическом (или двух эмпирических) распределениях. Выдвигается гипотеза H0, согласно которой
эмпирическое распределение признака не отличается от теоретического распределения. Для решения необходимо ввести
эмпирические частоты и теоретические в формате x1 - p1; x2 - p2; ...; xn - pn. Уровень значимости a определяется
по таблице. Уровень доверия равен 1 - a. Число степеней свободы равно числу элементов вариационного ряда - 1."""
    Label(newWindow, text=text, justify=LEFT, font=('Franklin Gothic Medium Cond', 10)).grid(column=0, row=0, sticky=W)
    Label(newWindow, text="Введите значения в формате \"x1 - p1; x2 - p2; ...; xn - pn\" :",
          font=('Franklin Gothic Medium Cond', 10, 'bold')).grid(column=0, row=1, sticky=W)
    txt_input = Entry(newWindow, width=60)
    txt_input.grid(column=0, row=2, sticky=W)
    Button(newWindow, text="Решить", command=solve).place(x=365, y=105)
    image = Label(newWindow)
    image.image = PhotoImage(file='./Pirson.png')
    image['image'] = image.image
    image.place(x=0, y=160)
    Label(newWindow, text="Таблица распределения хи-квадрат Пирсона.",
          font=('Franklin Gothic Medium Cond', 10)).place(x=0, y=570)



def dispersions():
    """Расчёт общей, групповой, внутригрупповой и межгрупповой дисперсий"""

    def solve():
        solved1 = Label(newWindow, justify=LEFT, font=('Franklin Gothic Medium Cond', 10))
        solved2 = Label(newWindow, justify=LEFT, font=('Franklin Gothic Medium Cond', 10))
        solved3 = Label(newWindow, justify=LEFT, font=('Franklin Gothic Medium Cond', 10))
        solved4 = Label(newWindow, justify=LEFT, font=('Franklin Gothic Medium Cond', 10))
        try:
            data = {float(i.split(' - ')[0]): [float(j) for j in i.split(' - ')[1].split(', ')] for i in
                    txt_input.get().split('; ')}
            n = sum([len(data[i]) for i in data])
            data_sums = [(i, sum(data[i])) for i in data]
            data_ns = [(i, len(data[i])) for i in data]
            data_means = [(i[0][0], round(i[0][1] / i[1][1], 4)) for i in zip(data_sums, data_ns)]
            data_dev_sums = [(i[0][0], round(sum(map(lambda x: (x - i[1][1]) ** 2, i[0][1])), 4))
                             for i in zip(data.items(), data_means)]
            data_deviations = [(i[0][0], round(i[0][1] / i[1][1], 4)) for i in zip(data_dev_sums, data_ns)]
            str_data_devs = "; ".join([f"группа {int(i[0])} - {i[1]}" for i in data_deviations])
            inner_desp = round(sum([i[1] for i in data_dev_sums]) / n, 4)
            mean = sum([sum(data[i]) for i in data]) / n
            general_disp = sum([sum(map(lambda x: (x - mean) ** 2, data[i])) for i in data]) / n
            between_desp = round(sum([(i[1] - mean) ** 2 for i in data_means]) / n, 4)
            solved1['text'] = f"Общая дисперсия: {round(general_disp, 4)}" + " " * 50
            solved2['text'] = f"Групповые дисперсии: {str_data_devs}"
            solved3['text'] = f"Внутригрупповая дисперсия: {inner_desp}"
            solved4['text'] = f"Межгрупповая дисперсия: {between_desp}"
        except (ValueError, IndexError, ZeroDivisionError):
            solved1['text'] = "Ошибка ввода, попробуйте ещё раз." + " " * 30
            solved2['text'], solved3['text'], solved4['text'] = " " * 150, " " * 150, " " * 150
        finally:
            solved1.grid(column=0, row=3, sticky=W)
            solved2.grid(column=0, row=4, sticky=W)
            solved3.grid(column=0, row=5, sticky=W)
            solved4.grid(column=0, row=6, sticky=W)

    newWindow = Toplevel(window)
    newWindow.geometry('740x250')
    newWindow.title("Расчёт всех видов дисперсий")
    text = """Общая дисперсия измеряет вариацию признака по всей совокупности под влиянием всех факторов.
Межгрупповая дисперсия характеризует систематическую вариацию, то есть различия в величине изучаемого признака,
возникшего под влиянием пизнака-фактора, положенного в основание группироваки.
Внутригрупповая дисперсия отражает случайную вариацию, то есть часть вариации, происходящую под влиянием
неучтенных факторов и не зависящую от признака-фактора, положенного в основаие группировки.
Групповые дисперсии отражают вариации признаков только за счёт условий и причин, действующих внутри групп."""
    Label(newWindow, text=text, justify=LEFT, font=('Franklin Gothic Medium Cond', 10)).grid(column=0, row=0,
                                                                                             sticky=W)
    Label(newWindow, text="Введите значения в формате \"k1 - x1, x2, ...; k2 - x1, x2, ...\" :",
          font=('Franklin Gothic Medium Cond', 10, 'bold')).grid(column=0, row=1, sticky=W)
    txt_input = Entry(newWindow, width=60)
    txt_input.grid(column=0, row=2, sticky=W)
    Button(newWindow, text="Решить", command=solve).place(x=365, y=120)


def solve1win():
    """Несмещённая оценка дисперсии D(X) по статическому распределению выборки"""

    def solve1():
        solved = Label(solveWin)
        try:
            data = txt_input.get().split('; ')
            xs, ns = [int(i.split(' - ')[0]) for i in data], [int(i.split(' - ')[1]) for i in data]
            variance = round(sum([x ** 2 * n for x, n in zip(xs, ns)]) /
                             sum(ns) - (sum([x * n for x, n in zip(xs, ns)]) / sum(ns)) ** 2, 4)
            gen_variance = round((sum(ns) / (sum(ns) - 1)) * variance, 4)
            text = f"Несмещённой оценкой ген. дисперсии D(X)={variance} является s^2={gen_variance}"
            solved['text'] = text
        except (ValueError, IndexError, ZeroDivisionError):
            solved['text'] = "Ошибка ввода, попробуйте ещё раз." + " " * 100
        finally:
            solved.grid(column=0, row=2, sticky=W)

    solveWin = Toplevel(window)
    solveWin.title("Несмещённая оценка дисперсии D(X) по статическому распределению выборки")
    solveWin.geometry('600x80')
    Label(solveWin,
          text="Выборочное распределение в формате (признак) x1 - (кол-во повторов) n1; x2 - n2; ...; xm - nm",
          font=('Franklin Gothic Medium Cond', 10)).grid(column=0, row=0, sticky=W)
    txt_input = Entry(solveWin, width=40)
    txt_input.grid(column=0, row=1, sticky=W)
    Button(solveWin, text="Решить", command=solve1).place(x=245, y=19)


def solve2win():
    """Несмещённая оценка дисперсии D(X) по значениям выборки и генеральному среднему"""

    def solve2():
        solved = Label(solveWin)
        try:
            data = list(map(float, txt_input1.get().split('; ')))
            gen_mean = float(txt_input2.get())
            n = len(data)
            gen_variance = round(sum(map(lambda x: (x - gen_mean) ** 2, data)) / n, 4)
            text = f"Приближённое значение ген. дисперсии D(X) является несмещённая оценка s^2={gen_variance}"
            solved['text'] = text
        except (ValueError, IndexError, ZeroDivisionError):
            solved['text'] = "Ошибка ввода, попробуйте ещё раз." + " " * 100
        finally:
            solved.place(x=0, y=85)

    solveWin = Toplevel(window)
    solveWin.title("Несмещённая оценка дисперсии D(X) по значениям выборки и генеральному среднему")
    solveWin.geometry('600x110')
    Label(solveWin, text="Введите значения выборки через точку с запятой:",
          font=('Franklin Gothic Medium Cond', 10, 'bold')).grid(column=0, row=0, sticky=W)
    txt_input1 = Entry(solveWin, width=40)
    txt_input1.grid(column=0, row=1, sticky=W)
    Label(solveWin, text="Введите генеральное среднее:",
          font=('Franklin Gothic Medium Cond', 10, 'bold')).grid(column=0, row=2, sticky=W)
    txt_input2 = Entry(solveWin, width=5)
    txt_input2.grid(column=0, row=3, sticky=W)
    Button(solveWin, text="Решить", command=solve2).place(x=35, y=59)


def solve3win():
    """Несмещённая оценка дисперсии D(X) по значениям выборки"""

    def solve3():
        solved = Label(solveWin)
        try:
            data = list(map(float, txt_input.get().split('; ')))
            n = len(data)
            mean = round(sum(data) / n, 4)
            gen_variance = round(sum(map(lambda x: (x - mean) ** 2, data)) / (n - 1), 4)
            text = f"Приближённое значение ген. дисперсии D(X) является несмещённая оценка s^2={gen_variance}"
            solved['text'] = text
        except (ValueError, IndexError, ZeroDivisionError):
            solved['text'] = "Ошибка ввода, попробуйте ещё раз." + " " * 100
        finally:
            solved.place(x=0, y=44)

    solveWin = Toplevel(window)
    solveWin.title("Несмещённая оценка дисперсии D(X) по значениям выборки")
    solveWin.geometry('600x80')
    Label(solveWin, text="Введите значения выборки через точку с запятой:",
          font=('Franklin Gothic Medium Cond', 10, 'bold')).grid(column=0, row=0, sticky=W)
    txt_input = Entry(solveWin, width=40)
    txt_input.grid(column=0, row=1, sticky=W)
    Button(solveWin, text="Решить", command=solve3).place(x=245, y=18)


solve1 = Button(window, text="Несмещённая оценка D(X) по стат. распр. выборки",
                command=solve1win, relief=GROOVE, width=45)
solve2 = Button(window, text="Несмещённая оценка D(X) по выборке и ген. ср.",
                command=solve2win, relief=GROOVE, width=45)
solve3 = Button(window, text="Несмещённая оценка D(X) по выборке",
                command=solve3win, relief=GROOVE, width=45)
solve4 = Button(window, text="По выборке",
                command=DOV_INTER2, relief=GROOVE, width=60)
solve5 = Button(window, text="Дов. интер. для мат. ожид. и D(X) при a=0.98",
                command=DOV_INTER1, relief=GROOVE, width=60)
solve6 = Button(window, text="Дов. интер. для мат. ожид. при среднем выборки и средкв. откл. при a=0.95",
                command=DOV_INTER3, relief=GROOVE, width=60)


def delete_button(*args):
    for elem in args:
        elem.grid_remove()


def add_button1():
    """Точечные оценки"""
    delete_button(solve4, solve5, solve6)
    for i in range(1, 3 + 1):
        eval(f"solve{i}.grid(column=1, row={i - 1}, sticky=W)")


def add_button2():
    """Доверительные интервалы"""
    delete_button(solve1, solve2, solve3)
    for i in range(1, 3 + 1):
        eval(f"solve{i + 3}.grid(column=1, row={i}, sticky=W)")


Button(window, text="Эмпирические характеристики", command=EMP, relief=GROOVE, width=35).grid(column=0, row=0, sticky=W)
Button(window, text="Точечные оценки", command=add_button1, relief=GROOVE, width=35).grid(column=0, row=1, sticky=W)
Button(window, text="Доверительные интервалы", command=add_button2, relief=GROOVE, width=35).grid(column=0, row=2,
                                                                                                  sticky=W)
Button(window, text="Однофакторный дисперсионный анализ", command=variance_analysis, relief=GROOVE,
       width=35).grid(column=0, row=3, sticky=W)
Button(window, text="Критерий хи-квадрат Пирсона", command=xi_square, relief=GROOVE, width=35).grid(column=0, row=4,
                                                                                                    sticky=W)
Button(window, text="Расчёт всех видов дисперсий", command=dispersions, relief=GROOVE, width=35).grid(column=0, row=5,
                                                                                                      sticky=W)

if __name__ == '__main__':
    window.mainloop()
