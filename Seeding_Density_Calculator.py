from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Cell Seeding Calculator -by Yunkai Zhang')
# win.geometry('430x680')

MenuBar = Menu(win)
win.config(menu=MenuBar)


def _about():
    messagebox.showinfo(
        title='About', message='Cell Seeding Calculator by Yunkai Zhang')

helpMenu = Menu(MenuBar)
MenuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='About', command=_about)

Label(text='Number of wells').grid(row=0, column=0, stick=E)
Label(text='Density (#cells per well)').grid(row=1, column=0, stick=E)

num_wells = IntVar()
num_wells.set(96)
input_num_wells = Entry(win, textvariable=num_wells)
input_num_wells.grid(row=0, column=1, stick=S, padx=10)

cells_well = IntVar()
input_cells_well = Entry(win, textvariable=cells_well)
cells_well.set("4000")
input_cells_well.grid(row=1, column=1)

l3 = Label(win, text='Volume per well (μL)')
l3.grid(row=2, column=0, stick=E)
v_well = IntVar()
input_v_well = Entry(win, textvariable=v_well)
v_well.set('80')
input_v_well.grid(row=2, column=1)

l4 = Label(win, text='Dilution Factor (%)')
l4.grid(row=3, column=0, stick=E)
dilution = DoubleVar()
input_dilution = Entry(win, textvariable=dilution)
dilution.set('100')
input_dilution.grid(row=3, column=1)

l5 = Label(win, text='Excess Factor (%)')
l5.grid(row=4, column=0, stick=E)
excess = DoubleVar()
input_excess = Entry(win, textvariable=excess)
excess.set('120')
input_excess.grid(row=4, column=1)

Label(text='').grid(row=5, column=0)
Label(text='Input: ', fg='red').grid(row=5, column=1, stick=W)

l7 = Label(win, text='Cell Density from Auto Counter \n Format: (a)e(b), e.g. 1e5')
l7.grid(row=6, column=0, stick=E)
d1 = DoubleVar()
input_d1 = Entry(win, textvariable=d1)
d1.set('')
input_d1.grid(row=6, column=1)


def click_density():
    a = num_wells.get()
    b = cells_well.get()
    c = v_well.get()
    d = dilution.get()
    e = excess.get()
    g = d1.get()
    vc = (a*b*e)/(g*d)
    vm = (c*a/1000-vc)*(e/100)
    string1 = str("Volume of Cell Suspension = %6.2f mL" % vc)
    string2 = str("Volume of Medium = %6.2f mL" % vm)
    output1.config(text=string1)
    output2.config(text=string2)

Label(text='').grid(row=8, column=0, columnspan=2)

output1 = Message(win, text="Volume of Cell Suspension", width=500, fg='blue')
output1.grid(row=9, column=0, columnspan=2)

output2 = Message(win, text="Volume of Medium", width=500, fg='blue')
output2.grid(row=10, column=0, columnspan=2)

Button(win, text='Calculate Cell Density', command=click_density).grid(
    row=11, column=0, columnspan=2, pady=20)

win.mainloop()