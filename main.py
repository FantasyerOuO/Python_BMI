import tkinter as tk
class BMI:
    def btn1(self):   
        # def judgement(bmi):
        #     if bmi>=18.5 and bmi<24:
        #         img=tk.PhotoImage(file='Picture\P2.gif')
        #         self.lab5.config(image=img)    
        
        #     else:
        #         img=tk.PhotoImage(file='Picture\P1.gif')
        #         self.lab5.config(image=img)
        
        cm=float(self.ent1.get())
        kg=float(self.ent2.get())
        bmi=(kg)/((cm)/100)**2
        self.lab4.config(text=round(bmi,2)) 
        
    def __init__(self):
        self.win=tk.Tk()
        self.win.geometry('400x400')
        # win.resizable(False,False)
        self.win.config(bg='cyan')
        self.win.title('BMI Calculator by Hui')       
        self.lab0=tk.Label(text='BMI計算器')
        self.lab0.config(bg='pink',font=('微軟正黑體',30,'bold'))
        self.lab0.grid(row=0,column=0,columnspan=2)
        self.lab1=tk.Label(text='身高(cm)')
        self.lab1.config(bg='cyan')
        self.lab1.grid(row=1,column=0)
        self.ent1=tk.Entry(text=155)
        self.ent1.grid(row=1,column=1)
        self.lab2=tk.Label(text='體重(kg)')
        self.lab2.config(bg='cyan')
        self.lab2.grid(row=2,column=0)
        self.ent2=tk.Entry(text=52)
        self.ent2.grid(row=2,column=1)
        self.btn_1=tk.Button(text='開始計算',command=BMI.btn1)
        self.btn_1.grid(row=3,column=0,columnspan=2)
        self.lab4=tk.Label()
        self.lab4.config(bg='cyan')
        self.lab4.grid(row=0,column=2,columnspan=2)
        self.lab5=tk.Label()
        self.lab5.config()
        self.lab5.grid(row=2,column=2,rowspan=2,columnspan=2)
        self.win.mainloop() 
        
      

    
Start=BMI()