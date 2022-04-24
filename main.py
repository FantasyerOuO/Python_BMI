# BMI Calculator by FantasyerOuO 
# FantasyerOuO's First Project
import tkinter as tk
from tkinter import END, PhotoImage, messagebox

def btn_0():
    messagebox.showinfo('Info','This BMI Calculator By FantasyerOuO\nVersion:1.0\n\nIf you have any question,you can email to me please:\nsungx12097@gmail.com')

def btn_1():
    def init():
        win.geometry('200x150')
        lab4.config(text='')
        lab5.config(text='',bg='gray')
    
    def judgement_2(bmi):
        if bmi>=18.5 and bmi<24:
            lab5.config(bg='white',fg='green')
            lab5.config(text='PASS',font=('微軟正黑體',20,'bold'))    
    
        else:
            lab5.config(bg='white',fg='red')
            lab5.config(text='FAIL',font=('微軟正黑體',20,'bold'))
    def judgement_1(cm,kg):
        if float(cm)>=300 or float(cm)<=0 or float(kg)<=0 :
            return False
        else:
            return True
                    
    init()    
    cm=(ent1.get())
    kg=(ent2.get())
    J1=judgement_1(cm,kg)
    if J1==True:
        pass
    else:
        messagebox.showwarning('Error','Reinput your \'Height\' and \'Weight\' ')
        ent1.delete(0,END)
        ent2.delete(0,END)
        return
    win.geometry('200x250')
    bmi=float(kg)/(float(cm)/100)**2
    J=judgement_2(bmi)
    lab4.config(text=round(bmi,2))    
              
    

win=tk.Tk()
win.geometry('200x150')
win.resizable(False,False)
win.config(bg='gray')
win.title('BMI')

win.iconbitmap('Picture\circle.ico')

lab0=tk.Label()
lab0.config(bg='black')
lab0.grid(row=0,column=0,columnspan=2)
btn0=tk.Button(lab0,text='BMI計算器',font=('微軟正黑體',20,'bold'),bg='yellow',command=btn_0)
btn0.pack()

lab1=tk.Label(text='身高(cm)')
lab1.config(bg='gray')
lab1.grid(row=1,column=0)
ent1=tk.Entry(text=155)
ent1.config()
ent1.grid(row=1,column=1)

lab2=tk.Label(text='體重(kg)')
lab2.config(bg='gray')
lab2.grid(row=2,column=0)
ent2=tk.Entry(text=52)
ent2.grid(row=2,column=1)

btn1=tk.Button(text='開始計算',command=btn_1)
btn1.grid(row=3,columnspan=2)

lab4=tk.Label()
lab4.config(bg='gray')
lab4.grid(row=4,column=0,columnspan=2)

lab5=tk.Label()
lab5.config(bg='gray')
lab5.grid(row=5,column=0,rowspan=2,columnspan=2)


win.mainloop()