

from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
import pandas
from PIL import ImageTk


window = Tk()
window.title = ("LAPTOP")
window.geometry('1000x550')
window.configure(bg="#02095d")
image = ImageTk.PhotoImage(
    file=r"C:\Users\abdel\Desktop\New folder\lapstart.png")

labelim = Label(window, image=image, border=0)
labelim.place(x=0, y=0)


exc = pandas.read_excel("lap.xlsx")


def range_fun():
    newwindow = Tk()
    newwindow.title = ("LAPTOP")
    newwindow.geometry("1570x750")
    newwindow.configure(bg="#02095d")

    def bud():
        def bud1():

            exc = pandas.read_excel("lap.xlsx")
            lapti = Label(newwindow, text="Code                                     Model Name                                              Price(LE) ", font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=10, y=155)

            price = exc[exc['Price (LE)'] <= int(max.get())]
            price = price[price['Price (LE)'] >= int(min.get())]

            lap = Label(newwindow, text=f"{price['Model name']}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)

            lap1 = Label(newwindow, text=f"{price['Price (LE)']}",  anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)

            def choose_fun():
                def destroy_fun():
                    newwindow.destroy()

                def for_prog(RAM, hard, core_i, speed):
                    if RAM >= 8 and hard >= 0.5 and core_i >= 5 and speed >= 2:
                        labfor = Label(newwindow, text="Programming : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=350)

                    else:
                        labfor = Label(newwindow, text="Programming : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=350)

                def for_graphic(RAM, core_i, cores_n, speed):
                    if RAM >= 16 and core_i >= 5 and cores_n >= 6 and speed >= 1:
                        labfor = Label(newwindow, text="Graphics : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=390)
                    else:
                        labfor = Label(newwindow, text="Graphics : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=390)

                def for_gaming(RAM,  SSD, core_i, cores_n, vram):
                    if RAM >= 8 and core_i >= 5 and SSD == 1 and cores_n >= 6 and vram >= 4:
                        labfor = Label(newwindow, text="Gaming : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=430)
                    else:
                        labfor = Label(newwindow, text="Gaming : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=430)

                def for_videditing(RAM, core_i, cores_n,  vram):
                    if RAM >= 16 and core_i >= 5 and cores_n >= 4 and vram >= 2:
                        labfor = Label(newwindow, text="Vidio Editing : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=470)
                    else:
                        labfor = Label(newwindow, text="Vidio Editing : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=470)

                def for_acc(RAM, core_i, cores_n, speed):
                    if RAM >= 8 and core_i >= 5 and cores_n >= 4 and speed >= 2.7:
                        labfor = Label(newwindow, text="Accounting and Microsoft Office : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=844, y=590)
                    else:
                        labfor = Label(newwindow, text="Accounting and Microsoft Office : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=844, y=590)

                def for_dataS(RAM, hard, SSD, core_i, cores_n, vram):
                    if RAM >= 8 and hard >= 0.5 and SSD == 1 and core_i > 7 and cores_n >= 4 and vram >= 4:
                        labfor = Label(newwindow, text="Data Science : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=550)
                    else:
                        labfor = Label(newwindow, text="Data Science : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=550)

                def for_arch(RAM, hard, SSD, core_i, vram):
                    if RAM >= 16 and hard >= 0.5 and SSD == 1 and core_i >= 5 and vram >= 4:
                        labfor = Label(newwindow, text="Architecture : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=510)
                    else:
                        labfor = Label(newwindow, text="Architecture : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=510)

                def for_MAT(RAM, SSD, cores_n):
                    if RAM >= 8 and SSD == 1 and cores_n >= 4:
                        labfor = Label(newwindow, text="MATLAB : ✅", fg="#77d89b",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=350)
                    else:
                        labfor = Label(newwindow, text="MATLAB : ❎", fg="red",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=350)

                def for_ML(RAM, SSD, core_i, cores_n, vram):
                    if RAM >= 16 and SSD == 1 and core_i >= 7 and cores_n >= 6 and vram >= 6:
                        labfor = Label(newwindow, text="Machine Learning : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=390)
                    else:
                        labfor = Label(newwindow, text="Machine Learning : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=390)

                def for_onlinel(RAM, speed):
                    if RAM >= 4 and speed >= 2:
                        labfor = Label(newwindow, text="Online Learning : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1074, y=430)
                    else:
                        labfor = Label(newwindow, text="Online Learning : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1074, y=430)

                def for_business(RAM, SSD, core_i, speed):
                    if RAM >= 8 and SSD == 1 and core_i >= 5 and speed >= 1.6:
                        labfor = Label(newwindow, text="Business : ✅", fg="#77d89b",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=470)
                    else:
                        labfor = Label(newwindow, text="Business : ❎", fg="red",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=470)

                def for_CS(RAM, core_i, speed):
                    if RAM >= 16 and core_i >= 5 and speed >= 2.5:
                        labfor = Label(newwindow, text="Cyber Security : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1079, y=510)
                    else:
                        labfor = Label(newwindow, text="Cyber Security : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1079, y=510)

                def for_computerS(RAM, SSD, core_i, speed):
                    if RAM >= 12 and SSD == 1 and core_i >= 5 and speed >= 2.4:
                        labfor = Label(newwindow, text="Computer Science : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=550)
                    else:
                        labfor = Label(newwindow, text="Computer Science : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=550)

                specs = Label(newwindow, text="Laptop's specs", font=(
                    "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=900, y=30)
                code = int(choose.get())
                lap_cl = Label(newwindow, text=f"{exc.iloc[code]}", font=("Calibri", 16, BOLD), anchor='n', height=8, justify=LEFT, fg="white", bg="#02095d").place(
                    x=850, y=80)
                lap_c = exc.iloc[code]
                features = Label(newwindow, text="Laptop's features", font=(
                    "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=900, y=300)
                for_prog(lap_c[2], lap_c[3], lap_c[5], lap_c[7])
                for_graphic(lap_c[2], lap_c[5], lap_c[6], lap_c[7])
                for_gaming(lap_c[2], lap_c[4], lap_c[5], lap_c[6], lap_c[8])
                for_videditing(lap_c[2], lap_c[5], lap_c[6],  lap_c[8])
                for_acc(lap_c[2], lap_c[5], lap_c[6], lap_c[7])
                for_dataS(lap_c[2], lap_c[3], lap_c[4],
                          lap_c[5], lap_c[6], lap_c[8])
                for_arch(lap_c[2], lap_c[3], lap_c[4], lap_c[5], lap_c[8])
                for_MAT(lap_c[2], lap_c[4], lap_c[6])
                for_ML(lap_c[2], lap_c[4], lap_c[5], lap_c[6], lap_c[8])
                for_onlinel(lap_c[2], lap_c[7])
                for_business(lap_c[2], lap_c[4], lap_c[5], lap_c[7])
                for_CS(lap_c[2], lap_c[5], lap_c[7])
                for_computerS(lap_c[2], lap_c[4], lap_c[5], lap_c[7])

                def buy_fun():

                    def price_fun():
                        if state.get() == "Ex-Client":
                            lapr = Label(newwindow, text=f"Fortuantelly you have 10% discount and the laptop will cost you {lap_c[9] * (90/100):.2f} LE", fg="yellow",
                                         bg="black", font=("Calibri", 20, BOLD)).place(x=650, y=690)
                        elif state.get() == "first time":
                            lapr = Label(newwindow, text=f"Fortuantelly you have 5% discount and the laptop will cost you {lap_c[9] * (95/100):.2f} LE", fg="yellow",
                                         bg="black", font=("Calibri", 20, BOLD)).place(x=650, y=690)

                    state = ttk.Combobox(newwindow, values=[
                        "Ex-Client", "first time"], width=8, font=("Calibri", 15, BOLD))
                    state.place(x=400, y=690)
                    btn_st = Button(newwindow, text="OK", fg="black",
                                    bg="white", font=("Calibri", 14, BOLD), command=price_fun).place(x=510, y=685)

                btn_b = Button(newwindow, text="Buy", bg="green",
                               fg="white", command=buy_fun, font=("Calibri", 18, BOLD)).place(x=150, y=680)
                la_ca = Label(newwindow, text="If you want to see another one change the code", fg="white",
                              bg="#02095d", font=("Calibri", 14, BOLD)).place(x=150, y=630)
                btn_th = Button(newwindow, text="Back home", command=destroy_fun, bg="red",
                                fg="white", font=("Calibri", 18, BOLD)).place(x=220, y=680)

            labch = Label(newwindow, text="Choose with code", font=(
                "Calibri", 18, BOLD), fg="yellow", bg="#02095d")
            labch.place(x=150, y=570)
            choose = Entry(newwindow, font=(
                "Calibri", 18, BOLD),  width=5, fg="red")
            choose.place(x=350, y=570)
            btn_c = Button(newwindow, text="choose", command=choose_fun, fg="#02095d",
                           bg="yellow", font=("Calibri", 18, BOLD)).place(x=450, y=560)

        def bud2():
            exc = pandas.read_excel("lap.xlsx")
            lapti = Label(newwindow, text="Code                                      Model Name                                  Price(LE) ", font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=10, y=155)
            price = exc[exc['Price (LE)'] <= int(max.get())]

            lap = Label(newwindow, text=f"{price['Model name']}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)

            lap1 = Label(newwindow, text=f"{price['Price (LE)']}",  anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)

            def choose_fun():
                def destroy_fun():
                    newwindow.destroy()

                def for_prog(RAM, hard, core_i, speed):
                    if RAM >= 8 and hard >= 0.5 and core_i >= 5 and speed >= 2:
                        labfor = Label(newwindow, text="Programming : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=350)

                    else:
                        labfor = Label(newwindow, text="Programming : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=350)

                def for_graphic(RAM, core_i, cores_n, speed):
                    if RAM >= 16 and core_i >= 5 and cores_n >= 6 and speed >= 1:
                        labfor = Label(newwindow, text="Graphics : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=390)
                    else:
                        labfor = Label(newwindow, text="Graphics : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=390)

                def for_gaming(RAM,  SSD, core_i, cores_n, vram):
                    if RAM >= 8 and core_i >= 5 and SSD == 1 and cores_n >= 6 and vram >= 4:
                        labfor = Label(newwindow, text="Gaming : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=430)
                    else:
                        labfor = Label(newwindow, text="Gaming : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=824, y=430)

                def for_videditing(RAM, core_i, cores_n,  vram):
                    if RAM >= 16 and core_i >= 5 and cores_n >= 4 and vram >= 2:
                        labfor = Label(newwindow, text="Vidio Editing : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=470)
                    else:
                        labfor = Label(newwindow, text="Vidio Editing : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=470)

                def for_acc(RAM, core_i, cores_n, speed):
                    if RAM >= 8 and core_i >= 5 and cores_n >= 4 and speed >= 2.7:
                        labfor = Label(newwindow, text="Accounting and Microsoft Office : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=844, y=590)
                    else:
                        labfor = Label(newwindow, text="Accounting and Microsoft Office : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=844, y=590)

                def for_dataS(RAM, hard, SSD, core_i, cores_n, vram):
                    if RAM >= 8 and hard >= 0.5 and SSD == 1 and core_i > 7 and cores_n >= 4 and vram >= 4:
                        labfor = Label(newwindow, text="Data Science : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=550)
                    else:
                        labfor = Label(newwindow, text="Data Science : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=550)

                def for_arch(RAM, hard, SSD, core_i, vram):
                    if RAM >= 16 and hard >= 0.5 and SSD == 1 and core_i >= 5 and vram >= 4:
                        labfor = Label(newwindow, text="Architecture : ✅", fg="#77d89b", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=510)
                    else:
                        labfor = Label(newwindow, text="Architecture : ❎", fg="red", bg="#02095d", font=(
                            "Calibri", 17, BOLD)).place(x=800, y=510)

                def for_MAT(RAM, SSD, cores_n):
                    if RAM >= 8 and SSD == 1 and cores_n >= 4:
                        labfor = Label(newwindow, text="MATLAB : ✅", fg="#77d89b",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=350)
                    else:
                        labfor = Label(newwindow, text="MATLAB : ❎", fg="red",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=350)

                def for_ML(RAM, SSD, core_i, cores_n, vram):
                    if RAM >= 16 and SSD == 1 and core_i >= 7 and cores_n >= 6 and vram >= 6:
                        labfor = Label(newwindow, text="Machine Learning : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=390)
                    else:
                        labfor = Label(newwindow, text="Machine Learning : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=390)

                def for_onlinel(RAM, speed):
                    if RAM >= 4 and speed >= 2:
                        labfor = Label(newwindow, text="Online Learning : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1074, y=430)
                    else:
                        labfor = Label(newwindow, text="Online Learning : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1074, y=430)

                def for_business(RAM, SSD, core_i, speed):
                    if RAM >= 8 and SSD == 1 and core_i >= 5 and speed >= 1.6:
                        labfor = Label(newwindow, text="Business : ✅", fg="#77d89b",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=470)
                    else:
                        labfor = Label(newwindow, text="Business : ❎", fg="red",
                                       bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=470)

                def for_CS(RAM, core_i, speed):
                    if RAM >= 16 and core_i >= 5 and speed >= 2.5:
                        labfor = Label(newwindow, text="Cyber Security : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1079, y=510)
                    else:
                        labfor = Label(newwindow, text="Cyber Security : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1079, y=510)

                def for_computerS(RAM, SSD, core_i, speed):
                    if RAM >= 12 and SSD == 1 and core_i >= 5 and speed >= 2.4:
                        labfor = Label(newwindow, text="Computer Science : ✅",
                                       fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=550)
                    else:
                        labfor = Label(newwindow, text="Computer Science : ❎",
                                       fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=550)

                specs = Label(newwindow, text="Laptop's specs", font=(
                    "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=900, y=30)
                code = int(choose.get())
                lap_cl = Label(newwindow, text=f"{exc.iloc[code]}", font=("Calibri", 16, BOLD), anchor='n', height=8, justify=LEFT, fg="white", bg="#02095d").place(
                    x=850, y=80)
                lap_c = exc.iloc[code]
                features = Label(newwindow, text="Laptop's features", font=(
                    "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=900, y=300)
                for_prog(lap_c[2], lap_c[3], lap_c[5], lap_c[7])
                for_graphic(lap_c[2], lap_c[5], lap_c[6], lap_c[7])
                for_gaming(lap_c[2], lap_c[4], lap_c[5], lap_c[6], lap_c[8])
                for_videditing(lap_c[2], lap_c[5], lap_c[6],  lap_c[8])
                for_acc(lap_c[2], lap_c[5], lap_c[6], lap_c[7])
                for_dataS(lap_c[2], lap_c[3], lap_c[4],
                          lap_c[5], lap_c[6], lap_c[8])
                for_arch(lap_c[2], lap_c[3], lap_c[4], lap_c[5], lap_c[8])
                for_MAT(lap_c[2], lap_c[4], lap_c[6])
                for_ML(lap_c[2], lap_c[4], lap_c[5], lap_c[6], lap_c[8])
                for_onlinel(lap_c[2], lap_c[7])
                for_business(lap_c[2], lap_c[4], lap_c[5], lap_c[7])
                for_CS(lap_c[2], lap_c[5], lap_c[7])
                for_computerS(lap_c[2], lap_c[4], lap_c[5], lap_c[7])

                def buy_fun():

                    def price_fun():
                        if state.get() == "Ex-Client":
                            lapr = Label(newwindow, text=f"Fortuantelly you have 10% discount and the laptop will cost you {lap_c[9] * (90/100):.2f} LE", fg="yellow",
                                         bg="black", font=("Calibri", 20, BOLD)).place(x=650, y=690)
                        elif state.get() == "first time":
                            lapr = Label(newwindow, text=f"Fortuantelly you have 5% discount and the laptop will cost you {lap_c[9] * (95/100):.2f} LE", fg="yellow",
                                         bg="black", font=("Calibri", 20, BOLD)).place(x=650, y=690)

                    state = ttk.Combobox(newwindow, values=[
                        "Ex-Client", "first time"], width=8, font=("Calibri", 15, BOLD))
                    state.place(x=400, y=690)
                    btn_st = Button(newwindow, text="OK", fg="black",
                                    bg="white", font=("Calibri", 14, BOLD), command=price_fun).place(x=510, y=685)

                btn_b = Button(newwindow, text="Buy", bg="green",
                               fg="white", command=buy_fun, font=("Calibri", 18, BOLD)).place(x=150, y=680)
                la_ca = Label(newwindow, text="If you want to see another one change the code", fg="white",
                              bg="#02095d", font=("Calibri", 14, BOLD)).place(x=150, y=630)
                btn_th = Button(newwindow, text="Back home", command=destroy_fun, bg="red",
                                fg="white", font=("Calibri", 18, BOLD)).place(x=220, y=680)

            labch = Label(newwindow, text="Choose with code", font=(
                "Calibri", 18, BOLD), fg="yellow", bg="#02095d")
            labch.place(x=150, y=570)
            choose = Entry(newwindow, font=(
                "Calibri", 18, BOLD),  width=5, fg="red")
            choose.place(x=350, y=570)
            btn_c = Button(newwindow, text="choose", command=choose_fun, fg="#02095d",
                           bg="yellow", font=("Calibri", 18, BOLD)).place(x=450, y=560)

        if budget.get() == "from:to":
            minl = Label(newwindow, text="From ", font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d", height=1).place(x=70, y=90)
            maxl = Label(newwindow, text="To", font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d", height=1).place(x=280, y=90)
            min = Entry(newwindow, font=("Calibri", 18, BOLD), width=6)
            min.place(x=140, y=90)
            max = Entry(newwindow, font=("Calibri", 18, BOLD), width=6)
            max.place(x=330, y=90)
            btn2 = Button(newwindow, font=("Calibri", 14, BOLD), text="continue", height=1, command=bud1,
                          fg="#02095d").place(x=430, y=90)

        elif budget.get() == "maximum budget":
            maxl = Label(newwindow, text="Maximum is", font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=70, y=90)
            max = Entry(newwindow, font=("Calibri", 18, BOLD), width=6)
            max.place(x=230, y=90)
            btn2 = Button(newwindow, font=("Calibri", 14, BOLD), text="continue", height=1, command=bud2,
                          fg="#02095d").place(x=430, y=90)

    labbu = Label(newwindow, text="Put your budget", font=(
        "Calibri", 25, BOLD), fg="yellow", bg="#02095d")
    labbu.place(x=5, y=30)
    budget = ttk.Combobox(
        newwindow, values=["from:to", "maximum budget"], width=14,  font=("Calibri", 17, BOLD))
    budget.place(x=260, y=37)
    btn_bu = Button(newwindow, text="OK", command=bud, fg="#02095d", bg="yellow", font=(
        "Calibri", 15, BOLD)).place(x=470, y=35)


def fields():
    newwindow = Tk()
    newwindow.title = ("LAPTOP")
    newwindow.geometry("1570x750")
    newwindow.configure(bg="#02095d")

    def for_prog(RAM, hard, core_i, speed):
        if RAM >= 8 and hard >= 0.5 and core_i >= 5 and speed >= 2:
            labfor = Label(newwindow, text="Programming : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=350)

        else:
            labfor = Label(newwindow, text="Programming : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=350)

    def for_graphic(RAM, core_i, cores_n, speed):
        if RAM >= 16 and core_i >= 5 and cores_n >= 6 and speed >= 1:
            labfor = Label(newwindow, text="Graphics : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=824, y=390)
        else:
            labfor = Label(newwindow, text="Graphics : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=824, y=390)

    def for_gaming(RAM,  SSD, core_i, cores_n, vram):
        if RAM >= 8 and core_i >= 5 and SSD == 1 and cores_n >= 6 and vram >= 4:
            labfor = Label(newwindow, text="Gaming : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=824, y=430)
        else:
            labfor = Label(newwindow, text="Gaming : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=824, y=430)

    def for_videditing(RAM, core_i, cores_n,  vram):
        if RAM >= 16 and core_i >= 5 and cores_n >= 4 and vram >= 2:
            labfor = Label(newwindow, text="Vidio Editing : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=470)
        else:
            labfor = Label(newwindow, text="Vidio Editing : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=470)

    def for_acc(RAM, core_i, cores_n, speed):
        if RAM >= 8 and core_i >= 5 and cores_n >= 4 and speed >= 2.7:
            labfor = Label(newwindow, text="Accounting and Microsoft Office : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=844, y=590)
        else:
            labfor = Label(newwindow, text="Accounting and Microsoft Office : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=844, y=590)

    def for_dataS(RAM, hard, SSD, core_i, cores_n, vram):
        if RAM >= 8 and hard >= 0.5 and SSD == 1 and core_i > 7 and cores_n >= 4 and vram >= 4:
            labfor = Label(newwindow, text="Data Science : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=550)
        else:
            labfor = Label(newwindow, text="Data Science : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=550)

    def for_arch(RAM, hard, SSD, core_i, vram):
        if RAM >= 16 and hard >= 0.5 and SSD == 1 and core_i >= 5 and vram >= 4:
            labfor = Label(newwindow, text="Architecture : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=510)
        else:
            labfor = Label(newwindow, text="Architecture : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=800, y=510)

    def for_MAT(RAM, SSD, cores_n):
        if RAM >= 8 and SSD == 1 and cores_n >= 4:
            labfor = Label(newwindow, text="MATLAB : ✅", fg="#77d89b",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=350)
        else:
            labfor = Label(newwindow, text="MATLAB : ❎", fg="red",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=350)

    def for_ML(RAM, SSD, core_i, cores_n, vram):
        if RAM >= 16 and SSD == 1 and core_i >= 7 and cores_n >= 6 and vram >= 6:
            labfor = Label(newwindow, text="Machine Learning : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=390)
        else:
            labfor = Label(newwindow, text="Machine Learning : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=390)

    def for_onlinel(RAM, speed):
        if RAM >= 4 and speed >= 2:
            labfor = Label(newwindow, text="Online Learning : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1074, y=430)
        else:
            labfor = Label(newwindow, text="Online Learning : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1074, y=430)

    def for_business(RAM, SSD, core_i, speed):
        if RAM >= 8 and SSD == 1 and core_i >= 5 and speed >= 1.6:
            labfor = Label(newwindow, text="Business : ✅", fg="#77d89b",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=470)
        else:
            labfor = Label(newwindow, text="Business : ❎", fg="red",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1109, y=470)

    def for_CS(RAM, core_i, speed):
        if RAM >= 16 and core_i >= 5 and speed >= 2.5:
            labfor = Label(newwindow, text="Cyber Security : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1079, y=510)
        else:
            labfor = Label(newwindow, text="Cyber Security : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1079, y=510)

    def for_computerS(RAM, SSD, core_i, speed):
        if RAM >= 12 and SSD == 1 and core_i >= 5 and speed >= 2.4:
            labfor = Label(newwindow, text="Computer Science : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=550)
        else:
            labfor = Label(newwindow, text="Computer Science : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=1061, y=550)

    def show():
        exc = pandas.read_excel("lap.xlsx")
        lapti = Label(newwindow, text="Code                                     Model Name                                              Price(LE) ", font=(
            "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=10, y=155)
        if fieldsC.get() == "Programming":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[0:10]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[0:10]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Graphics":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[10:20]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[10:20]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Gaming":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[20:30]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[20:30]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Vidio-editing":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[30:40]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[30:40]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Accounting and Microsoft office":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[40:50]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[40:50]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Data Science":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[50:60]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[50:60]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Architecture":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[60:70]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[60:70]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "MATLAP":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[70:80]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[70:80]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Machine Learning":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[80:90]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[80:90]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Online Learning":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[90:100]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[90:100]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Business":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[100:110]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[100:110]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Cyber Security":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[110:120]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[110:120]}", anchor="e", justify=RIGHT, width=5, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)
        elif fieldsC.get() == "Computer Science":
            lap = Label(newwindow, text=f"{exc['Model name'].iloc[120:130]}", anchor="e", justify=LEFT, font=(
                "Calibri", 18, BOLD),  fg="white", bg="#02095d").place(x=20, y=200)
            lap1 = Label(newwindow, text=f"{exc['Price (LE)'].iloc[120:130]}", anchor="e", justify=RIGHT, width=5, height=6, font=(
                "Calibri", 18, BOLD), fg="white", bg="#02095d").place(x=611, y=200)

        def choose_fun():
            def destroy_fun():
                newwindow.destroy()

            specs = Label(newwindow, text="Laptop's specs", font=(
                "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=900, y=30)
            code = int(choose.get())
            lap_cl = Label(newwindow, text=f"{exc.iloc[code]}", font=("Calibri", 16, BOLD), anchor='n', height=8, justify=LEFT, fg="white", bg="#02095d").place(
                x=850, y=80)
            lap_c = exc.iloc[code]
            features = Label(newwindow, text="Laptop's features", font=(
                "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=900, y=300)
            for_prog(lap_c[2], lap_c[3], lap_c[5], lap_c[7])
            for_graphic(lap_c[2], lap_c[5], lap_c[6], lap_c[7])
            for_gaming(lap_c[2], lap_c[4], lap_c[5], lap_c[6], lap_c[8])
            for_videditing(lap_c[2], lap_c[5], lap_c[6],  lap_c[8])
            for_acc(lap_c[2], lap_c[5], lap_c[6], lap_c[7])
            for_dataS(lap_c[2], lap_c[3], lap_c[4],
                      lap_c[5], lap_c[6], lap_c[8])
            for_arch(lap_c[2], lap_c[3], lap_c[4], lap_c[5], lap_c[8])
            for_MAT(lap_c[2], lap_c[4], lap_c[6])
            for_ML(lap_c[2], lap_c[4], lap_c[5], lap_c[6], lap_c[8])
            for_onlinel(lap_c[2], lap_c[7])
            for_business(lap_c[2], lap_c[4], lap_c[5], lap_c[7])
            for_CS(lap_c[2], lap_c[5], lap_c[7])
            for_computerS(lap_c[2], lap_c[4], lap_c[5], lap_c[7])

            def buy_fun():

                def price_fun():
                    if state.get() == "Ex-Client":
                        lapr = Label(newwindow, text=f"Fortuantelly you have 10% discount and the laptop will cost you {lap_c[9] * (90/100):.2f} LE", fg="yellow",
                                     bg="black", font=("Calibri", 20, BOLD)).place(x=650, y=690)
                    elif state.get() == "first time":
                        lapr = Label(newwindow, text=f"Fortuantelly you have 5% discount and the laptop will cost you {lap_c[9] * (95/100):.2f} LE", fg="yellow",
                                     bg="black", font=("Calibri", 20, BOLD)).place(x=650, y=690)

                state = ttk.Combobox(newwindow, values=[
                                     "Ex-Client", "first time"], width=8, font=("Calibri", 15, BOLD))
                state.place(x=400, y=690)
                btn_st = Button(newwindow, text="OK", fg="black",
                                bg="white", font=("Calibri", 14, BOLD), command=price_fun).place(x=510, y=685)

            btn_b = Button(newwindow, text="Buy", bg="green",
                           fg="white", command=buy_fun, font=("Calibri", 18, BOLD)).place(x=150, y=680)
            la_ca = Label(newwindow, text="If you want to see another one change the code", fg="white",
                          bg="#02095d", font=("Calibri", 14, BOLD)).place(x=150, y=630)
            btn_th = Button(newwindow, text="Back home", command=destroy_fun, bg="red",
                            fg="white", font=("Calibri", 18, BOLD)).place(x=220, y=680)

        labch = Label(newwindow, text="Choose with code", font=(
            "Calibri", 18, BOLD), fg="yellow", bg="#02095d")
        labch.place(x=150, y=570)
        choose = Entry(newwindow, font=(
            "Calibri", 18, BOLD),  width=5, fg="red")
        choose.place(x=350, y=570)
        btn_c = Button(newwindow, text="choose", command=choose_fun, fg="#02095d",
                       bg="yellow", font=("Calibri", 18, BOLD)).place(x=450, y=560)

    labfi = Label(newwindow, text="Choose the field", font=(
        "Calibri", 25, BOLD), fg="yellow", bg="#02095d")
    labfi.place(x=200, y=30)
    fieldsC = ttk.Combobox(newwindow, values=["Programming", "Graphics", "Gaming", "Vidio-editing", "Accounting and Microsoft office", "Data Science",
                           "Architecture", "MATLAB", "Machine Learning", "Online Learning", "Business", "Cyber Security", "Computer Science"],  font=("Calibri", 17, BOLD))
    fieldsC.place(x=185, y=80)
    btn_show = Button(newwindow, text="Show", command=show, fg="#02095d", bg="yellow", font=(
        "Calibri", 18, BOLD)).place(x=500, y=80)


def check_fun():
    newwindow = Tk()
    newwindow.title = ("LAPTOP")
    newwindow.geometry("1200x600")
    newwindow.configure(bg="#02095d")

    def for_prog(RAM, hard, core_i, speed):
        if RAM >= 8 and hard >= 0.5 and core_i >= 5 and speed >= 2:
            labfor = Label(newwindow, text="Programming : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=100)

        else:
            labfor = Label(newwindow, text="Programming : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=100)

    def for_graphic(RAM, core_i, cores_n, speed):
        if RAM >= 16 and core_i >= 5 and cores_n >= 6 and speed >= 1:
            labfor = Label(newwindow, text="Graphics : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=600, y=150)
        else:
            labfor = Label(newwindow, text="Graphics : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=600, y=150)

    def for_gaming(RAM,  SSD, core_i, cores_n, vram):
        if RAM >= 8 and core_i >= 5 and SSD == 1 and cores_n >= 6 and vram >= 4:
            labfor = Label(newwindow, text="Gaming : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=600, y=200)
        else:
            labfor = Label(newwindow, text="Gaming : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=600, y=200)

    def for_videditing(RAM, core_i, cores_n,  vram):
        if RAM >= 16 and core_i >= 5 and cores_n >= 4 and vram >= 2:
            labfor = Label(newwindow, text="Vidio Editing : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=250)
        else:
            labfor = Label(newwindow, text="Vidio Editing : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=250)

    def for_acc(RAM, core_i, cores_n, speed):
        if RAM >= 8 and core_i >= 5 and cores_n >= 4 and speed >= 2.7:
            labfor = Label(newwindow, text="Accounting and Microsoft Office : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=620, y=400)
        else:
            labfor = Label(newwindow, text="Accounting and Microsoft Office : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=620, y=400)

    def for_dataS(RAM, hard, SSD, core_i, cores_n, vram):
        if RAM >= 8 and hard >= 0.5 and SSD == 1 and core_i > 7 and cores_n >= 4 and vram >= 4:
            labfor = Label(newwindow, text="Data Science : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=350)
        else:
            labfor = Label(newwindow, text="Data Science : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=350)

    def for_arch(RAM, hard, SSD, core_i, vram):
        if RAM >= 16 and hard >= 0.5 and SSD == 1 and core_i >= 5 and vram >= 4:
            labfor = Label(newwindow, text="Architecture : ✅", fg="#77d89b", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=300)
        else:
            labfor = Label(newwindow, text="Architecture : ❎", fg="red", bg="#02095d", font=(
                "Calibri", 17, BOLD)).place(x=576, y=300)

    def for_MAT(RAM, SSD, cores_n):
        if RAM >= 8 and SSD == 1 and cores_n >= 4:
            labfor = Label(newwindow, text="MATLAB : ✅", fg="#77d89b",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=885, y=100)
        else:
            labfor = Label(newwindow, text="MATLAB : ❎", fg="red",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=885, y=100)

    def for_ML(RAM, SSD, core_i, cores_n, vram):
        if RAM >= 16 and SSD == 1 and core_i >= 7 and cores_n >= 6 and vram >= 6:
            labfor = Label(newwindow, text="Machine Learning : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=837, y=150)
        else:
            labfor = Label(newwindow, text="Machine Learning : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=837, y=150)

    def for_onlinel(RAM, speed):
        if RAM >= 4 and speed >= 2:
            labfor = Label(newwindow, text="Online Learning : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=850, y=200)
        else:
            labfor = Label(newwindow, text="Online Learning : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=850, y=200)

    def for_business(RAM, SSD, core_i, speed):
        if RAM >= 8 and SSD == 1 and core_i >= 5 and speed >= 1.6:
            labfor = Label(newwindow, text="Business : ✅", fg="#77d89b",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=885, y=250)
        else:
            labfor = Label(newwindow, text="Business : ❎", fg="red",
                           bg="#02095d", font=("Calibri", 17, BOLD)).place(x=885, y=250)

    def for_CS(RAM, core_i, speed):
        if RAM >= 16 and core_i >= 5 and speed >= 2.5:
            labfor = Label(newwindow, text="Cyber Security : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=855, y=300)
        else:
            labfor = Label(newwindow, text="Cyber Security : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=855, y=300)

    def for_computerS(RAM, SSD, core_i, speed):
        if RAM >= 12 and SSD == 1 and core_i >= 5 and speed >= 2.4:
            labfor = Label(newwindow, text="Computer Science : ✅",
                           fg="#77d89b", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=837, y=350)
        else:
            labfor = Label(newwindow, text="Computer Science : ❎",
                           fg="red", bg="#02095d", font=("Calibri", 17, BOLD)).place(x=837, y=350)

    def check():
        def destroy_fun():
            newwindow.destroy()

        features = Label(newwindow, text="Your laptop's features", font=(
            "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=646, y=30)

        for_prog(int(ram.get()), int(hard.get()),
                 int(core.get()), int(speed.get()))
        for_graphic(int(ram.get()), int(core.get()),
                    int(numcore.get()), int(speed.get()))
        for_gaming(int(ram.get()), int(ssd.get()), int(
            core.get()), int(numcore.get()), int(vram.get()))
        for_videditing(int(ram.get()), int(core.get()),
                       int(numcore.get()), int(vram.get()))
        for_acc(int(ram.get()), int(core.get()),
                int(numcore.get()), int(speed.get()))
        for_dataS(int(ram.get()), int(hard.get()), int(ssd.get()),
                  int(core.get()), int(numcore.get()), int(vram.get()))
        for_arch(int(ram.get()), int(hard.get()), int(
            ssd.get()), int(core.get()), int(vram.get()))
        for_MAT(int(ram.get()), int(ssd.get()), int(numcore.get()))
        for_ML(int(ram.get()), int(ssd.get()), int(
            core.get()), int(numcore.get()), int(vram.get()))
        for_onlinel(int(ram.get()), int(speed.get()))
        for_business(int(ram.get()), int(ssd.get()),
                     int(core.get()), int(speed.get()))
        for_CS(int(ram.get()), int(core.get()), int(speed.get()))
        for_computerS(int(ram.get()), int(ssd.get()),
                      int(core.get()), int(speed.get()))
        btn_show = Button(newwindow, text="Back Home", fg="yellow", bg="#02095d", font=(
            "Calibri", 18, BOLD), command=destroy_fun).place(x=720, y=450)

    inputl = Label(newwindow, text="Input laptop specs", font=(
        "Calibri", 25, BOLD), fg="yellow", bg="#02095d").place(x=115, y=30)

    ram_l = Label(newwindow, text="RAM in GB", font=("Calibri", 15, BOLD), fg="white", bg="#02095d"
                  ).place(x=126, y=100)
    ram = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    ram.place(x=300, y=100)
    hard_l = Label(newwindow, text="HARD in TB", font=("Calibri", 15, BOLD), fg="white", bg="#02095d"
                   ).place(x=124.5, y=150)
    hard = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    hard.place(x=300, y=150)
    ssd_l = Label(newwindow, text="SSD or not (1 or 0)", font=(
        "Calibri", 15, BOLD), fg="white", bg="#02095d").place(x=100, y=200)
    ssd = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    ssd.place(x=300, y=200)
    core_l = Label(newwindow, text="core i", font=("Calibri", 15, BOLD), fg="white", bg="#02095d"
                   ).place(x=145, y=250)
    core = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    core.place(x=300, y=250)
    numcore_l = Label(newwindow, text="Number of cores", font=(
        "Calibri", 15, BOLD), fg="white", bg="#02095d").place(x=105, y=300)
    numcore = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    numcore.place(x=300, y=300)
    speed_l = Label(newwindow, text="Speed in GHz", font=(
        "Calibri", 15, BOLD), fg="white", bg="#02095d").place(x=120, y=350)
    speed = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    speed.place(x=300, y=350)
    vram_l = Label(newwindow, text="VRAM in GB", font=("Calibri", 15, BOLD), fg="white", bg="#02095d"
                   ).place(x=124.5, y=400)
    vram = Entry(newwindow, font=("Calibri", 17, BOLD),  width=5, fg="red")
    vram.place(x=300, y=400)

    btn_show = Button(newwindow, text="Show", fg="#02095d", bg="yellow", font=(
        "Calibri", 18, BOLD), command=check).place(x=210, y=450)


btn1 = Button(text="Check my laptop", command=check_fun,
              fg="#022caf", bg="white", font=("Calibri", 17, BOLD), borderwidth=1).place(x=115, y=150)

btn2 = Button(text="Recommended laptops in a field",
              command=fields, fg="#022caf", bg="white", font=("Calibri", 17, BOLD), borderwidth=1).place(x=50, y=250)

btn3 = Button(text="Avillable laptops in range",
              command=range_fun, fg="#022caf", bg="white", font=("Calibri", 17, BOLD), borderwidth=1).place(x=80, y=350)


window.mainloop()
