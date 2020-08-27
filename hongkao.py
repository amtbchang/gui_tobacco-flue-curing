from tkinter import *
from tkinter import ttk

#value1
def index1():
    value1 = float(x1.get())
    if float(value1) < 24:
        p1.set(0)
        return p1
    elif value1 > 120:
        p1.set(1)
        return p1
    elif value1 >= 24 and  value1 < 48 :
        p1.set(2)
        return p1
    elif value1 >= 96 and  value1 <= 120:
        p1.set(3)
        return p1
    else:
        p1.set(5)
        return p1
#value2
def index2():
    value2 = float(x2.get())
    if value2 < 33:
        p2.set(0)
        return p2
    elif value2 >= 33 and  value2 < 35 :
        p2.set(2)
        return p2
    elif value2 >= 37.5 and  value2 <= 38:
        p2.set(3)
        return p2
    elif value2 >= 35 and  value2 <= 37.5:
        p2.set(5)
        return p2
    else:
        pass


#value3 
def index3():
    value3 = float(x3.get())
    if value3 < 33:
        p3.set(0)
        return p3
    elif value3 > 38.5:
        p3.set(1)
        return p3
    elif value3 >= 33 and  value3 <= 35 :
        p3.set(2)
        return p3
    elif value3 >= 38 and  value3 <= 38.5:
        p3.set(3)
        return p3
    else:
        p3.set(5)
        return p3

##4
def index4():
    value4 = float(x4.get())
    if value4 < 33:
        p4.set(0)
        return p4
    elif value4 > 38.5:
        p4.set(1)
        return p4
    elif value4 >= 33 and  value4 <= 35 :
        p4.set(2)
        return p4
    elif value4 >= 38 and  value4 <= 38.5:
        p4.set(3)
        return p4
    else:
        p4.set(5)
        return p4
#value5       
def index5():
    value5 = float(x5.get())
    if value5 < 24:
        p5.set(0)
        return p5
    elif value5 > 96:
        p5.set(1)
        return p5
    elif value5 >= 24 and  value5 <= 48 :
        p5.set(2)
        return p5
    elif value5 >= 72 and  value5 <= 96:
        p5.set(3)
        return p5
    else:
        p5.set(5)
        return p5
#value6
def index6():
    value6 = float(x6.get())
    if value6 < 33:
        p6.set(0)
        return p6
    elif value6 > 38.5:
        p6.set(1)
        return p6
    elif value6 >= 33 and  value6 <= 35 :
        p6.set(2)
        return p6
    elif value6 >= 38 and  value6 <= 38.5:
        p6.set(3)
        return p6
    else:
        p6.set(5)
        return p6
#value7
def index7():
    value7 = float(x7.get())
    if value7 < 35:
        p7.set(0)
        return p7
    elif value7 > 42:
        p7.set(1)
        return p7
    elif value7 >= 35 and  value7 <= 37 :
        p7.set(2)
        return p7
    elif value7 >= 40 and  value7 <= 42:
        p7.set(3)
        return p7
    else:
        p7.set(5)
        return p7
#value8
def index8():
    value8 = float(x8.get())
    if value8 >72:
        p8.set(0)
        return p8
    elif value8 >= 0 and  value8 < 24 :
        p8.set(2)
        return p8
    elif value8 >= 48 and  value8 <= 72:
        p8.set(3)
        return p8
    elif value8 >= 24 and  value8 <= 48:
        p8.set(5)
        return p8
    else:
        pass
#value9
def index9():
    value9 = float(x9.get())
    if value9 < 37:
        p9.set(0)
        return p9
    elif value9 > 43:
        p9.set(1)
        return p9
    elif value9 >= 37 and  value9 <= 38 :
        p9.set(2)
        return p9
    elif value9 >= 42 and  value9 <= 43:
        p9.set(3)
        return p9
    else:
        p9.set(5)
        return p9
#value10
def index10():
    value10 = float(x10.get())
    if value10 < 120:
        p10.set(0)
        return p10
    elif value10 > 240:
        p10.set(1)
        return p10
    elif value10 >= 120 and  value10 <= 144 :
        p10.set(2)
        return p10
    elif value10 >= 216 and  value10 <= 240:
        p10.set(3)
        return p10
    else:
        p10.set(5)
        return p10
def calculate(*args):
    P.set(float(p1.get()) + float(p2.get()) + float(p3.get()) +
          float(p4.get())+ float(p5.get()) + float(p6.get()) + float(p7.get()) 
          + float(p8.get()) + float(p9.get()) + float(p10.get()))


root = Tk()
root.title("烘烤工艺评分")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

x1 = StringVar()
x2 = StringVar()
x3 = StringVar()
x4 = StringVar()
x5 = StringVar()
x6 = StringVar()
x7 = StringVar()
x8 = StringVar()
x9 = StringVar()
x10 = StringVar()

p1 = StringVar()
p2 = StringVar()
p3 = StringVar()
p4 = StringVar()
p5 = StringVar()
p6 = StringVar()
p7 = StringVar()
p8 = StringVar()
p9 = StringVar()
p10 = StringVar()

P = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=x1)
feet_entry.grid(column=2, row=1, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x2)
feet_entry.grid(column=2, row=2, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x3)
feet_entry.grid(column=2, row=3, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x4)
feet_entry.grid(column=2, row=4, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x5)
feet_entry.grid(column=2, row=5, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x6)
feet_entry.grid(column=2, row=6, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x7)
feet_entry.grid(column=2, row=7, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x8)
feet_entry.grid(column=2, row=8, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x9)
feet_entry.grid(column=2, row=9, sticky=(W, E))
feet_entry = ttk.Entry(mainframe, width=7, textvariable=x10)
feet_entry.grid(column=2, row=10, sticky=(W, E))


ttk.Label(mainframe, textvariable=P).grid(column=3, row=12, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=5, row=12, sticky=W)

ttk.Label(mainframe, text="指标1").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="指标2").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="指标3").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="指标4").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="指标5").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="指标6").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="指标7").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="指标8").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text="指标9").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="指标10").grid(column=1, row=10, sticky=W)

ttk.Label(mainframe, textvariable=p1).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="评分", command=index1).grid(column=4, row=1, sticky=W)

ttk.Label(mainframe, textvariable=p2).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="评分", command=index2).grid(column=4, row=2, sticky=W)

ttk.Label(mainframe, textvariable=p3).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="评分", command=index3).grid(column=4, row=3, sticky=W)

ttk.Label(mainframe, textvariable=p4).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="评分", command=index4).grid(column=4, row=4, sticky=W)

ttk.Label(mainframe, textvariable=p5).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="评分", command=index5).grid(column=4, row=5, sticky=W)

ttk.Label(mainframe, textvariable=p6).grid(column=3, row=6, sticky=W)
ttk.Button(mainframe, text="评分", command=index6).grid(column=4, row=6, sticky=W)

ttk.Label(mainframe, textvariable=p7).grid(column=3, row=7, sticky=W)
ttk.Button(mainframe, text="评分", command=index7).grid(column=4, row=7, sticky=W)

ttk.Label(mainframe, textvariable=p8).grid(column=3, row=8, sticky=W)
ttk.Button(mainframe, text="评分", command=index8).grid(column=4, row=8, sticky=W)

ttk.Label(mainframe, textvariable=p9).grid(column=3, row=9, sticky=W)
ttk.Button(mainframe, text="评分", command=index9).grid(column=4, row=9, sticky=W)

ttk.Label(mainframe, textvariable=p10).grid(column=3, row=10, sticky=W)
ttk.Button(mainframe, text="评分", command=index10).grid(column=4, row=10, sticky=W)

ttk.Label(mainframe, text="总评分为：").grid(column=1, row=12, sticky=E)
ttk.Label(mainframe, text="").grid(column=3, row=12, sticky=W)

#ttk.Label(mainframe, text="名   称").grid(column=1, row=0, sticky=E)
ttk.Label(mainframe, text="输入值").grid(column=2, row=0, sticky=W)
ttk.Label(mainframe, text="分值").grid(column=3, row=0, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=15, pady=15)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()