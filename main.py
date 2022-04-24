import tkinter as tk

def btn1():
    def judgement(bmi):
        if bmi>=18.5 and bmi<24:
            return True
        else:
            return False
    
    cm=float(ent1.get())
    kg=float(ent2.get())
    bmi=(kg)/((cm)/100)**2
    J=judgement(bmi)
    lab4.config(text=round(bmi,2))
    lab5.config(tk.PhotoImage(file=''))
    

win=tk.Tk()
win.geometry('400x200')
win.resizable(False,False)
win.config(bg='cyan')
win.title('BMI Calculator by Hui')

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

btn1=tk.Button(text='開始計算',command=btn1)

btn1.grid(row=3,columnspan=2)

lab4=tk.Label()
lab4.config(bg='cyan')
lab4.grid(row=0,column=2,rowspan=2,columnspan=2)

lab5=tk.Label()
lab4.config(bg='cyan')
lab4.grid(row=2,column=2,rowspan=2,columnspan=2)

win.mainloop()