import tkinter as tk

def btn1():
    cm=ent1.get()
    kg=ent2.get()
    float(cm)
    float(kg)
    bmi=(kg)/((cm)/100)**2
    print(bmi)
    

win=tk.Tk()
win.geometry('200x400')
win.resizable(False,False)
win.config(bg='cyan')
win.title='BMI Calculator by Hui'

lab0=tk.Label(text='BMI計算器')
lab0.config(bg='pink',font=('微軟正黑體',30,'bold'))
lab0.grid(row=0,columnspan=2)

lab1=tk.Label(text='身高(cm)')
lab1.config(bg='cyan')
lab1.grid(row=1,column=0)
ent1=tk.Entry()
ent1.grid(row=1,column=1)

lab2=tk.Label(text='體重(kg)')
lab2.config(bg='cyan')
lab2.grid(row=2,column=0)
ent2=tk.Entry()
ent2.grid(row=2,column=1)

btn1=tk.Button(text='開始計算',command=btn1())
btn1.config()
btn1.grid(row=3,columnspan=2)

lab4=tk.Label()
lab4.config(bg='cyan')
lab4.grid(row=4,columnspan=2)

win.mainloop()