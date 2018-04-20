from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Cell Seeding Calculator -by Yunkai Zhang')
# win.geometry('450x680')

win.option_add("*Font", "Arial 12")

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
Label(text='Volume per well (μL)').grid(row=2, column=0, stick=E)
Label(text='Excess Factor (%)').grid(row=3, column=0, stick=E)

num_wells = IntVar()
input_num_wells = Entry(win, textvariable=num_wells)
input_num_wells.grid(row=0, column=1, stick=S, padx=10)

cells_well = IntVar()
input_cells_well = Entry(win, textvariable=cells_well)
input_cells_well.grid(row=1, column=1)

v_well = IntVar()
input_v_well = Entry(win, textvariable=v_well)
input_v_well.grid(row=2, column=1)

excess = DoubleVar()
input_excess = Entry(win, textvariable=excess).grid(row=3, column=1)
excess.set('120')

Label(text='').grid(row=4, column=0)
Label(text='Input Here: ', fg='#FF5733').grid(row=4, column=1, stick=W)

Label(text='Cell Density from Auto Counter \n (Cells/mL)').grid(row=5, column=0, stick=E)
Label(text='Dilution Factor').grid(row=6, column=0, stick=E)

dilution = DoubleVar()
input_dilution = Entry(win, textvariable=dilution).grid(row=6, column=1)
dilution.set('1')

density = DoubleVar()
input_d1 = Entry(win, textvariable=density).grid(row=5, column=1)
density.set('')


def click_density():
    a = num_wells.get()
    b = cells_well.get()
    c = v_well.get()
    dil = dilution.get()
    e = excess.get()
    den = density.get()
    vc = (a * b * e) / (den * dil * 100)
    vm = (c * a / 1000 - vc) * (e / 100)
    if vm > 0:
        string1 = "Volume of Cell Suspension = {:.2f} mL".format(vc)
        string2 = "Volume of Medium = {:.3f} mL".format(vm)
        output1.config(text=string1)
        output2.config(text=string2)
    else:
        string1 = "Cells are too diluted"
        string2 = string1
        output1.config(text=string1, fg='red', font = 'Arial 12 bold')
        output2.config(text=string2, fg='red', font = 'Arial 12 bold')

Button(win, text='Calculate Cell Density', command=click_density).grid(
    row=7, column=0, columnspan=2, pady=20)

Label(text='').grid(row=8, column=0, columnspan=2)

output1 = Message(win, text="Volume of Cell Suspension", width=500, fg='#3361FF')
output1.grid(row=9, column=0, columnspan=2)

output2 = Message(win, text="Volume of Medium", width=500, fg='#3361FF')
output2.grid(row=10, column=0, columnspan=2)

Label(text='').grid(row=11, column=0, columnspan=2)

win.mainloop()
