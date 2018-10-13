import tkinter
from tkinter import *
from tkinter import messagebox

class Commission_Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry()
        self.master.title('Commission Calulator')
        self.grid()
        
        
        #cp_profit
        #label 
        self.cp_pofit_label=Label(self, text='Customer Pay Profit:')
        self.cp_pofit_label.grid(row=0, column=0, sticky= 'e')
        #entry
        self.cp_pofit_entry=Entry(self)
        self.cp_pofit_entry.grid(row=0, column=1)
        #w_profit
        #label 
        self.w_pofit_label=Label(self, text='Warranty Profit:')
        self.w_pofit_label.grid(row=1, column=0, sticky= 'e')
        #entry
        self.w_profit_entry=Entry(self)
        self.w_profit_entry.grid(row=1, column=1)
        
        self.calculate_button=Button(self, text='calculate', command=self.calculate)
        self.calculate_button.grid(row=0, column=3, rowspan=2)
        
        self.commission_statement_label=Label(self, text='Earned Commission:')
        self.commission_statement_label.grid(row=3, column=0)
        
        self.earned_commission_label=Label(self, text="")
        self.earned_commission_label.grid(row=3, column=1)
        
    def calculate(self):
        cp_profit = self.cp_pofit_entry.get()
        w_profit = self.w_profit_entry.get()
        
        
        try:
            cp_profit=float(cp_profit)
            w_profit=float(w_profit)
            earned_commission =(cp_profit*.14)+(w_profit*.06)
        except ValueError:
            tkinter.messagebox.showerror('Error', 'You have to input two numbers, IDIOT!')
            
        self.earned_commission_label['text']=earned_commission
        
        

        
        
        
Commission_Calculator().mainloop()