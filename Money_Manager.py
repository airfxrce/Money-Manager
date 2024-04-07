import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from datetime import date
from datetime import datetime, timedelta

balance_bankacc = 0.0
balance_cash = 0.0
first = True
class MainWindow:
    def __init__(self):
        self.main_window = tk.Tk() 
        self.main_window.geometry("350x650")
        self.main_window.title("Money Manager")
        self.main_window.configure(bg = "#404040") 

        global balance_bankacc
        global balance_cash
        global first

        balance_bankacc = 0
        balance_cash = 0

        self.EXCEL_FILE = "income.xlsx"
        self.EXCEL_FILE1 = "expense.xlsx"


        self.category_list_income = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}

        df = pd.read_excel(self.EXCEL_FILE)
        df1 = pd.read_excel(self.EXCEL_FILE1)


        self.current_date = datetime.today()
        self.current_date = self.current_date.date()
        self.week_ago = self.current_date - timedelta(days=7)
        self.month_ago = self.current_date - timedelta(days=30)
        self.year_ago = self.current_date - timedelta(days=365)

        combostyle = ttk.Style()

        combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                    {'configure':
                                    {'selectbackground': '#404040',
                                       'fieldbackground': '#404040',
                                       'background': '#404040'
                                       }}}
                         )
        combostyle.theme_use('combostyle')



        self.day = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}
        self.week = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}
        self.month = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}
        self.year = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}


        self.day_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}
        self.week_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}
        self.month_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}
        self.year_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}

    
        
        for ind in df.index:
            df_date = pd.to_datetime(df['Date'][ind]).date()
            category = df["Category"][ind]
            money_count = df["Money Count"][ind]
            account = df["Account"][ind]
            
            if df_date == self.current_date:
                self.day[category] += money_count
                self.week[category] += money_count
                self.month[category] += money_count
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash += money_count

            elif (df_date < self.current_date) and (df_date >= self.week_ago):
                self.week[category] += money_count
                self.month[category] += money_count
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash +=money_count


            elif (df_date < self.week_ago) and (df_date >= self.month_ago):
                self.month[category] += money_count
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash += money_count


            elif (df_date < self.month_ago) and (df_date >= self.year_ago):
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash +=money_count
            first = False
                
        
        for ind in df1.index:
            df1_date = pd.to_datetime(df1['Date'][ind]).date()
            category = df1["Category"][ind]
            money_count = df1["Money Count"][ind]
            account = df1["Account"][ind]
            
            if df1_date == self.current_date:
                self.day_expense[category] += money_count
                self.week_expense[category] += money_count
                self.month_expense[category] += money_count
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc  -= money_count
                else:
                    balance_cash -= money_count

            elif (df1_date < self.current_date) and (df1_date >= self.week_ago):
                self.week_expense[category] += money_count
                self.month_expense[category] += money_count
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc  -= money_count
                else:
                    balance_cash -=money_count


            elif (df1_date < self.week_ago) and (df1_date >= self.month_ago):
                self.month_expense[category] += money_count
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc  -= money_count
                else:
                    balance_cash -= money_count


            elif (df1_date < self.month_ago) and (df1_date >= self.year_ago):
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc -= money_count
                else:
                    balance_cash -=money_count

        def switch_mainwindow():
            self.main_window.destroy()
            MainWindow2()
        
                
        def account_change(event):
            get_account = self.text_account.get()
            if get_account == "Bank account":
                self.text_moneycount.config(text = str(balance_bankacc) + "$")
            else:
                self.text_moneycount.config(text = str(balance_cash) + "$")
                
        self.text_account = ttk.Combobox(self.main_window ,font = ("Arial", 16)) 
        self.text_account["values"] = ("Bank account" , "Cash")
        self.text_account.pack()

        self.text_account.bind("<<ComboboxSelected>>", account_change)
        

        self.text_moneycount = tk.Label(self.main_window, text = "0" + "$", font = ("Arial", 18),bd="0",bg = "#404040", fg="white") 
        self.text_moneycount.pack()
        
        self.button_expense = tk.Button(self.main_window, text= "Expense" ,bg = "#404040", bd = "0", fg = "white", command = switch_mainwindow) 
        self.button_expense.place(x=270,y=60, height = 35, width = 55)
        self.button_income = tk.Button(self.main_window, text= "Income", bg = "#404040", bd = "0", fg = "white", font= "Arial 10 underline") 
        self.button_income.place(x=30,y=60, height = 35, width = 55)
        def show_graph_day():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.day["Gift"], self.day["Salary"],self.day["Investment"], self.day["Other"]]
            labels = ["Gift", "Salary" , "Investment", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080"]
            ax.pie(slices, labels = labels,colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        def show_graph_month():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.month["Gift"], self.month["Salary"],self.month["Investment"], self.month["Other"]]
            labels = ["Gift", "Salary" , "Investment", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080"]
            ax.pie(slices, labels = labels,colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        def show_graph_week():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.week["Gift"], self.week["Salary"],self.week["Investment"], self.week["Other"]]
            labels = ["Gift", "Salary" , "Investment", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080"] 
            ax.pie(slices, labels = labels, colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        def show_graph_year():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.year["Gift"], self.year["Salary"],self.year["Investment"], self.year["Other"]]
            labels = ["Gift", "Salary" , "Investment", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080"] 
            ax.pie(slices, labels = labels,colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        

        

        self.button_day = tk.Button(self.main_window , text= "Day", bg = "#404040", bd = "0", fg = "white", command = show_graph_day) 
        self.button_day.place(x=30,y=125, height = 30,width = 40)
        self.button_week = tk.Button(self.main_window , text= "Week", bg = "#404040", bd = "0", fg = "white", command = show_graph_week) 
        self.button_week.place(x=100,y=125, height = 30,width = 40)
        self.button_month = tk.Button(self.main_window , text= "Month", bg = "#404040", bd = "0", fg = "white", command = show_graph_month) 
        self.button_month.place(x=215,y=125, height = 30,width = 40)
        self.button_year = tk.Button(self.main_window , text= "Year", bg = "#404040", bd = "0", fg = "white", command = show_graph_year) 
        self.button_year.place(x=285,y=125, height = 30,width = 40)
        self.text_date = tk.Label(self.main_window, text = "15.11.2023", font = ("Arial", 10), bd="0",bg = "#404040", fg="white") 
        self.text_date.pack(pady = 115)

        fig, ax = plt.subplots()
        fig.set_figheight(3)
        frame = tk.Frame(self.main_window)

        canvas = FigureCanvasTkAgg(fig, master = frame)
        fig.set_facecolor((0.25, 0.25, 0.25))
        canvas.get_tk_widget().pack()
        frame.place(x = -150, y = 150)

        def add_data():
            self.main_window.destroy()
            ExpenseWindow()


        self.button_plus = tk.Button(self.main_window, text= "+", bg = "white",bd = "0", fg = "black", command = add_data) 
        self.button_plus.place(x = 315, y = 600, height = 25, width = 25)

        

        

        self.main_window.mainloop()

class MainWindow2():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("350x650")
        self.main_window.title("Money Manager")
        self.main_window.configure(bg = "#404040")
        global balance_bankacc
        global balance_cash
        global first

        balance_bankacc = 0
        balance_cash = 0

        self.EXCEL_FILE = "income.xlsx"
        self.EXCEL_FILE1 = "expense.xlsx"

        df1 = pd.read_excel(self.EXCEL_FILE1)
        df = pd.read_excel(self.EXCEL_FILE)

        self.category_list_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}

        

        self.current_date = datetime.today()
        self.current_date = self.current_date.date()
        self.week_ago = self.current_date - timedelta(days=7)
        self.month_ago = self.current_date - timedelta(days=30)
        self.year_ago = self.current_date - timedelta(days=365)

        combostyle = ttk.Style()

        combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                    {'configure':
                                    {'selectbackground': '#404040',
                                       'fieldbackground': '#404040',
                                       'background': '#404040'
                                       }}}
                         )
        combostyle.theme_use('combostyle')
        
        self.day = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}
        self.week = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}
        self.month = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}
        self.year = {
            "Salary": 0.0,
            "Gift" : 0.0,
            "Investment": 0.0,
            "Other": 0.0}


        self.day_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}
        self.week_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}
        self.month_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}
        self.year_expense = {
            "Food": 0.0,
            "Health" : 0.0,
            "Home": 0.0,
            "Cafe": 0.0,
            "Education": 0.0,
            "Gift": 0.0,
            "Family": 0.0,
            "Sport": 0.0,
            "Auto": 0.0,
            "Entertainment": 0.0,
            "Purchase": 0.0,
            "Other": 0.0,}

        for ind in df.index:
            df_date = pd.to_datetime(df['Date'][ind]).date()
            category = df["Category"][ind]
            money_count = df["Money Count"][ind]
            account = df["Account"][ind]
            
            if df_date == self.current_date:
                self.day[category] += money_count
                self.week[category] += money_count
                self.month[category] += money_count
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash += money_count

            elif (df_date < self.current_date) and (df_date >= self.week_ago):
                self.week[category] += money_count
                self.month[category] += money_count
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash +=money_count


            elif (df_date < self.week_ago) and (df_date >= self.month_ago):
                self.month[category] += money_count
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash += money_count


            elif (df_date < self.month_ago) and (df_date >= self.year_ago):
                self.year[category] += money_count
                if account == "Bank account":
                    balance_bankacc += money_count
                else:
                    balance_cash +=money_count
            first = False
                
        
        for ind in df1.index:
            df1_date = pd.to_datetime(df1['Date'][ind]).date()
            category = df1["Category"][ind]
            money_count = df1["Money Count"][ind]
            account = df1["Account"][ind]
            
            if df1_date == self.current_date:
                self.day_expense[category] += money_count
                self.week_expense[category] += money_count
                self.month_expense[category] += money_count
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc  -= money_count
                else:
                    balance_cash -= money_count

            elif (df1_date < self.current_date) and (df1_date >= self.week_ago):
                self.week_expense[category] += money_count
                self.month_expense[category] += money_count
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc  -= money_count
                else:
                    balance_cash -=money_count


            elif (df1_date < self.week_ago) and (df1_date >= self.month_ago):
                self.month_expense[category] += money_count
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc  -= money_count
                else:
                    balance_cash -= money_count


            elif (df1_date < self.month_ago) and (df1_date >= self.year_ago):
                self.year_expense[category] += money_count
                if account == "Bank account":
                    balance_bankacc -= money_count
                else:
                    balance_cash -=money_count

        def switch_mainwindow():
            self.main_window.destroy()
            MainWindow()

        def account_change(event):
            get_account = self.text_account.get()
            if get_account == "Bank account":
                self.text_moneycount.config(text = str(balance_bankacc) + "$")
            else:
                self.text_moneycount.config(text = str(balance_cash) + "$")
                
        self.text_account = ttk.Combobox(self.main_window ,font = ("Arial", 16))
        self.text_account["values"] = ("Bank account" , "Cash")
        self.text_account.pack()

        self.text_account.bind("<<ComboboxSelected>>", account_change)
        

        self.text_moneycount = tk.Label(self.main_window, text = "0" + "$", font = ("Arial", 18),bd="0",bg = "#404040", fg="white") 
        self.text_moneycount.pack()
        
        self.button_expense = tk.Button(self.main_window, text= "Expense" ,bg = "#404040", bd = "0", fg = "white", font= "Arial 10 underline") 
        self.button_expense.place(x=270,y=60, height = 35, width = 55)
        self.button_income = tk.Button(self.main_window, text= "Income", bg = "#404040", bd = "0", fg = "white", command = switch_mainwindow) 
        self.button_income.place(x=30,y=60, height = 35, width = 55)

        def show_graph_day():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.day_expense["Food"], self.day_expense["Health"],self.day_expense["Home"], self.day_expense["Cafe"], self.day_expense["Education"], self.day_expense["Gift"], self.day_expense["Family"],
                      self.day_expense["Sport"], self.day_expense["Auto"],
                      self.day_expense["Entertainment"], self.day_expense["Purchase"], self.day_expense["Other"]]
            labels = ["Food", "Health" , "Home", "Cafe", "Education", "Gift", "Family", "Sport", "Auto", "Entertainment", "Purchase", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080", "#FF0000", "#FFFF00","#000000", "#006400", "#00BFFF", "#191970","#800080","#8B4513"] 
            ax.pie(slices, labels = labels,colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        def show_graph_month():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.month_expense["Food"], self.month_expense["Health"],self.month_expense["Home"], self.month_expense["Cafe"], self.month_expense["Education"], self.month_expense["Gift"],
                      self.month_expense["Family"], self.month_expense["Sport"], self.month_expense["Auto"],
                      self.month_expense["Entertainment"], self.month_expense["Purchase"], self.month_expense["Other"]]
            labels = ["Food", "Health" , "Home", "Cafe", "Education", "Gift", "Family", "Sport", "Auto", "Entertainment", "Purchase", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080", "#FF0000", "#FFFF00","#000000", "#006400", "#00BFFF", "#191970","#800080","#8B4513"] 
            ax.pie(slices, labels = labels,colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        def show_graph_week():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.week_expense["Food"], self.week_expense["Health"],self.week_expense["Home"], self.week_expense["Cafe"], self.week_expense["Education"], self.week_expense["Gift"],
                      self.week_expense["Family"], self.week_expense["Sport"], self.week_expense["Auto"],
                      self.week_expense["Entertainment"], self.week_expense["Purchase"], self.week_expense["Other"]]
            labels = ["Food", "Health" , "Home", "Cafe", "Education", "Gift", "Family", "Sport", "Auto", "Entertainment", "Purchase", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080", "#FF0000", "#FFFF00","#000000", "#006400", "#00BFFF", "#191970","#800080","#8B4513"] 
            ax.pie(slices, labels = labels, colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        def show_graph_year():
            df = pd.read_excel(self.EXCEL_FILE)
            slices = [self.year_expense["Food"], self.year_expense["Health"],self.year_expense["Home"], self.year_expense["Cafe"], self.year_expense["Education"],
                      self.year_expense["Gift"], self.year_expense["Family"], self.year_expense["Sport"], self.year_expense["Auto"],
                      self.year_expense["Entertainment"], self.year_expense["Purchase"], self.year_expense["Other"]]
            labels = ["Food", "Health" , "Home", "Cafe", "Education", "Gift", "Family", "Sport", "Auto", "Entertainment", "Purchase", "Other"]
            colors = ["#FFFFFF", "#4B0082", "#00FFFF", "#000080", "#FF0000", "#FFFF00","#000000", "#006400", "#00BFFF", "#191970","#800080","#8B4513"] 
            ax.pie(slices, labels = labels,colors = colors, wedgeprops = {"edgecolor":"black"})
            canvas.draw()
            ax.clear()

        self.button_day = tk.Button(self.main_window , text= "Day", bg = "#404040", bd = "0", fg = "white", command = show_graph_day) 
        self.button_day.place(x=30,y=125, height = 30,width = 40)
        self.button_week = tk.Button(self.main_window , text= "Week", bg = "#404040", bd = "0", fg = "white", command = show_graph_week) 
        self.button_week.place(x=100,y=125, height = 30,width = 40)
        self.button_month = tk.Button(self.main_window , text= "Month", bg = "#404040", bd = "0", fg = "white", command = show_graph_month) 
        self.button_month.place(x=215,y=125, height = 30,width = 40)
        self.button_year = tk.Button(self.main_window , text= "Year", bg = "#404040", bd = "0", fg = "white", command = show_graph_year) 
        self.button_year.place(x=285,y=125, height = 30,width = 40)
        self.text_date = tk.Label(self.main_window, text = "15.11.2023", font = ("Arial", 10), bd="0",bg = "#404040", fg="white") 
        self.text_date.pack(pady = 115)

        fig, ax = plt.subplots()
        fig.set_figheight(3)
        frame = tk.Frame(self.main_window)

        canvas = FigureCanvasTkAgg(fig, master = frame)
        fig.set_facecolor((0.25, 0.25, 0.25))
        canvas.get_tk_widget().pack()
        frame.place(x = -150, y = 150)

        def add_data():
            self.main_window.destroy()
            ExpenseWindow()


        self.button_plus = tk.Button(self.main_window, text= "+", bg = "white",bd = "0", fg = "black", command = add_data) 
        self.button_plus.place(x = 315, y = 600, height = 25, width = 25)

        

        

        self.main_window.mainloop()



class ExpenseWindow: #expense window class
    def __init__(self):
        self.expense_window = tk.Tk()
        self.expense_window.geometry("350x650")
        self.expense_window.title("Money Manager")
        self.expense_window.configure(bg = "#404040")

        def on_focus_in(entry):
            if entry.cget('state') == 'disabled':
                entry.configure(state='normal')
                entry.delete(0, 'end')

        def on_focus_out(entry, placeholder):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.configure(state='disabled')

        def switch_to_income():
            self.expense_window.destroy()
            IncomeWindow()
            

        self.text_account = tk.Label(self.expense_window, text = "Add", font = ("Arial", 18), bd="0",bg = "#404040", fg="white") 
        self.text_account.pack(pady = 15)
        
        self.button_expense = tk.Button(self.expense_window, text= "Income" ,bg = "#404040", bd = "0", fg = "white", command = switch_to_income)
        self.button_expense.place(x=270,y=60, height = 35, width = 55)
        self.button_expense = tk.Button(self.expense_window, text= "Expense", bg = "#404040", bd = "0", fg = "white", font= "Arial 10 underline") 
        self.button_expense.place(x=30,y=60, height = 35, width = 55)

        entry_money_count_expense = tk.Entry(self.expense_window, width=50, bg = "#404040") 
        entry_money_count_expense.pack(pady = (50,0),anchor="w", padx = 40)
        entry_money_count_expense.insert(0, "Money Count")
        entry_money_count_expense.configure(state='disabled')
        x_focus_in = entry_money_count_expense.bind('<Button-1>', lambda x: on_focus_in(entry_money_count_expense))
        x_focus_out = entry_money_count_expense.bind(
        '<FocusOut>', lambda x: on_focus_out(entry_money_count_expense, 'Money Count'))

        entry_date_expense = tk.Entry(self.expense_window, width=50, bg = "#404040") 
        entry_date_expense.pack(pady = (20,0), anchor="w", padx = 40)
        entry_date_expense.insert(0, "Date")
        entry_date_expense.configure(state='disabled')
        x_focus_in = entry_date_expense.bind('<Button-1>', lambda x: on_focus_in(entry_date_expense))
        x_focus_out = entry_date_expense.bind(
        '<FocusOut>', lambda x: on_focus_out(entry_date_expense, 'Date'))

        self.text_account_expense = tk.Label(self.expense_window, text = "Account", font = ("Arial", 10), bd="0",bg = "#404040", fg="white") 
        self.text_account_expense.pack(pady = (20,0), anchor="w", padx = 40)
        n = tk.StringVar() 
        self.account_choose = ttk.Combobox(self.expense_window, width = 27, textvariable = n)
        self.account_choose["values"] = ("Bank account" , "Cash")
        self.account_choose.place(x = 125 , y = 187)
        


        self.text_category_expense = tk.Label(self.expense_window, text = "Category", font = ("Arial", 10), bd="0",bg = "#404040", fg="white") 
        self.text_category_expense.pack(pady = (20,0),anchor="w", padx = 40)

        self.selected_category_expense = ""

        def set_category(category, c):
            self.selected_category_expense = category
            c.config(bg = "#404040")

        self.icon1 = PhotoImage(file = "food.png")
        self.icon1 = self.icon1.subsample(2,2)
        self.icon2 = PhotoImage(file = "health.png")
        self.icon2 = self.icon2.subsample(2,2)
        self.icon3 = PhotoImage(file = "home.png")
        self.icon3 = self.icon3.subsample(2,2)
        self.icon4 = PhotoImage(file = "cafe.png")
        self.icon4 = self.icon4.subsample(2,2)
        self.icon5 = PhotoImage(file = "education.png")
        self.icon5 = self.icon5.subsample(2,2)
        self.icon6 = PhotoImage(file = "gift1.png")
        self.icon6 = self.icon6.subsample(2,2)
        self.icon7 = PhotoImage(file = "family.png")
        self.icon7 = self.icon7.subsample(2,2)
        self.icon8 = PhotoImage(file = "sport.png")
        self.icon8 = self.icon8.subsample(2,2)
        self.icon9 = PhotoImage(file = "auto.png")
        self.icon9 = self.icon9.subsample(2,2)
        self.icon10 = PhotoImage(file = "entertainment.png")
        self.icon10 = self.icon10.subsample(2,2)
        self.icon11 = PhotoImage(file = "purchase.png")
        self.icon11 = self.icon11.subsample(2,2)
        self.icon12 = PhotoImage(file = "other1.png")
        self.icon12 = self.icon12.subsample(2,2)
        
       

        self.buttonframe = tk.Frame(self.expense_window) # для таблицы
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)
        self.buttonframe.columnconfigure(2, weight = 1)
        self.buttonframe.columnconfigure(3, weight = 1)

        category1 = tk.Button(self.buttonframe) # создание таблицы
        category1.config(image = self.icon1, height = 30, command = lambda: set_category("Food", category1))
        category1.grid(row = 0, column = 0, sticky = tk.W +tk.E)
        
        category2 = tk.Button(self.buttonframe)
        category2.config(image = self.icon2, height = 30, command = lambda: set_category("Health", category2))
        category2.grid(row = 0, column = 1, sticky = tk.W +tk.E)
        
        category3 = tk.Button(self.buttonframe)
        category3.config(image = self.icon3, height = 30, command = lambda: set_category("Home", category3))
        category3.grid(row = 0, column = 2, sticky = tk.W +tk.E)
        
        category4 = tk.Button(self.buttonframe)
        category4.config(image = self.icon4, height = 30, command = lambda: set_category("Cafe", category4))
        category4.grid(row = 0, column = 3, sticky = tk.W +tk.E)
        
        category5 = tk.Button(self.buttonframe)
        category5.config(image = self.icon5, height = 30, command = lambda: set_category("Education", category5))
        category5.grid(row = 1, column = 0, sticky = tk.W +tk.E)
        
        category6 = tk.Button(self.buttonframe)
        category6.config(image = self.icon6, height = 30, command = lambda: set_category("Gift", category6))
        category6.grid(row = 1, column = 1, sticky = tk.W +tk.E)
        
        category7 = tk.Button(self.buttonframe)
        category7.config(image = self.icon7, height = 30, command = lambda: set_category("Family", category7))
        category7.grid(row = 1, column = 2, sticky = tk.W +tk.E)
        
        category8 = tk.Button(self.buttonframe)
        category8.config(image = self.icon8, height = 30, command = lambda: set_category("Sport", category8))
        category8.grid(row = 1, column = 3, sticky = tk.W +tk.E)
        
        category9 = tk.Button(self.buttonframe)
        category9.config(image = self.icon9, height = 30, command = lambda: set_category("Auto", category9))
        category9.grid(row = 2, column = 0, sticky = tk.W +tk.E)
        
        category10 = tk.Button(self.buttonframe)
        category10.config(image = self.icon10, height = 30, command = lambda: set_category("Entertainment", category10))
        category10.grid(row = 2, column = 1, sticky = tk.W +tk.E)
        
        category11 = tk.Button(self.buttonframe)
        category11.config(image = self.icon11, height = 30, command = lambda: set_category("Purchase", category11))
        category11.grid(row = 2, column = 2, sticky = tk.W +tk.E)
        
        category12 = tk.Button(self.buttonframe)
        category12.config(image = self.icon12, height = 30, command = lambda: set_category("Other", category12))
        category12.grid(row = 2, column = 3, sticky = tk.W +tk.E)

        self.buttonframe.pack(pady = (10,0),fill="x")

        entry_comment_expense = tk.Entry(self.expense_window, width=50, bg = "#404040") 
        entry_comment_expense.pack(pady = (20,0), anchor="w", padx = 40)
        entry_comment_expense.insert(0, "Comment")
        entry_comment_expense.configure(state='disabled')
        x_focus_in = entry_comment_expense.bind('<Button-1>', lambda x: on_focus_in(entry_comment_expense))
        x_focus_out = entry_comment_expense.bind(
        '<FocusOut>', lambda x: on_focus_out(entry_comment_expense, 'Comment'))

        self.EXCEL_FILE = "expense.xlsx"

        self.category_list = {
            "Food": 0,
            "Health" : 0,
            "Home": 0,
            "Cafe": 0,
            "Education": 0,
            "Gift": 0,
            "Family": 0,
            "Sport": 0,
            "Auto": 0,
            "Entertainment": 0,
            "Purchase": 0,
            "Other": 0}

        df = pd.read_excel(self.EXCEL_FILE)

        for ind in df.index:
            if df["Category"][ind] == "Food":
                self.category_list["Food"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Health":
                self.category_list["Health"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Home":
                self.category_list["Home"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Cafe":
                self.category_list["Cafe"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Education":
                self.category_list["Education"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Gift":
                self.category_list["Gift"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Family":
                self.category_list["Family"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Sport":
                self.category_list["Sport"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Auto":
                self.category_list["Auto"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Entertainment":
                self.category_list["Entertainment"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Purchase":
                self.category_list["Purchase"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Other":
                self.category_list["Other"] += df["Money Count"][ind]

        def add_expense():
            df = pd.read_excel(self.EXCEL_FILE)
            data_expense = {
                "Money Count": entry_money_count_expense.get(),
                "Date": entry_date_expense.get(),
                "Account": self.account_choose.get(),
                "Category": self.selected_category_expense,
                "Comment": entry_comment_expense.get()}
            
            df = df._append(data_expense , ignore_index = True)
            
            if data_expense["Category"] == "Food":
                self.category_list["Food"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Health":
                self.category_list["Health"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Home":
                self.category_list["Home"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Cafe":
                self.category_list["Cafe"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Education":
                self.category_list["Education"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Gift":
                self.category_list["Gift"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Family":
                self.category_list["Family"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Sport":
                self.category_list["Sport"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Auto":
                self.category_list["Auto"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Entertainment":
                self.category_list["Entertainment"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Purchase":
                self.category_list["Purchase"] += int(data_expense["Money Count"])

            if data_expense["Category"] == "Other":
                self.category_list["Other"] += int(data_expense["Money Count"])

            column_names = ["Money Count" , "Date" , "Account" , "Category" , "Comment"]

            df.to_excel(self.EXCEL_FILE , index = False ,header = column_names)

            self.expense_window.destroy()
            MainWindow2()

        self.button_add_expense = tk.Button(self.expense_window , text= "Add", bg = "#404040", bd = "0", fg = "white", command = add_expense) 
        self.button_add_expense.pack(pady = (190,0))
        
class IncomeWindow: #income window class
    def __init__(self):
        self.income_window = tk.Tk()
        self.income_window.geometry("350x650")
        self.income_window.title("Money Manager")
        self.income_window.configure(bg = "#404040")
        
        def on_focus_in(entry):
            if entry.cget('state') == 'disabled':
                entry.configure(state='normal')
                entry.delete(0, 'end')

        def on_focus_out(entry, placeholder):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.configure(state='disabled')

        def switch_to_expense():
            self.income_window.destroy()
            ExpenseWindow()

        self.text_account = tk.Label(self.income_window, text = "Add", font = ("Arial", 18), bd="0",bg = "#404040", fg="white") 
        self.text_account.pack(pady = 15)
        
        self.button_income = tk.Button(self.income_window, text= "Income" ,bg = "#404040", bd = "0", fg = "white", font= "Arial 10 underline") 
        self.button_income.place(x=270,y=60, height = 35, width = 55)
        self.button_income = tk.Button(self.income_window, text= "Expense", bg = "#404040", bd = "0", fg = "white", command = switch_to_expense) 
        self.button_income.place(x=30,y=60, height = 35, width = 55)


        entry_money_count_income = tk.Entry(self.income_window, width=50, bg = "#404040") 
        entry_money_count_income.pack(pady = (50,0),anchor="w", padx = 40)
        entry_money_count_income.insert(0, "Money Count")
        entry_money_count_income.configure(state='disabled')
        x_focus_in = entry_money_count_income.bind('<Button-1>', lambda x: on_focus_in(entry_money_count_income))
        x_focus_out = entry_money_count_income.bind(
        '<FocusOut>', lambda x: on_focus_out(entry_money_count_income, 'Money Count'))

        entry_date_income = tk.Entry(self.income_window, width=50, bg = "#404040") 
        entry_date_income.pack(pady = (20,0), anchor="w", padx = 40)
        entry_date_income.insert(0, "Date")
        entry_date_income.configure(state='disabled')
        x_focus_in = entry_date_income.bind('<Button-1>', lambda x: on_focus_in(entry_date_income))
        x_focus_out = entry_date_income.bind(
        '<FocusOut>', lambda x: on_focus_out(entry_date_income, 'Date'))

        self.text_account_income = tk.Label(self.income_window, text = "Account", font = ("Arial", 10), bd="0",bg = "#404040", fg="white") 
        self.text_account_income.pack(pady = (20,0), anchor="w", padx = 40)
        n = tk.StringVar() 
        self.account_choose = ttk.Combobox(self.income_window, width = 27, textvariable = n)
        self.account_choose["values"] = ("Bank account" , "Cash")
        self.account_choose.place(x = 125 , y = 187)

        self.text_category_income = tk.Label(self.income_window, text = "Category", font = ("Arial", 10), bd="0",bg = "#404040", fg="white") 
        self.text_category_income.pack(pady = (20,0),anchor="w", padx = 40)

        self.selected_category_income = ""

        def set_category(category, c):
            self.selected_category_income = category
            c.config(bg = "#404040")

        self.icon1 = PhotoImage(file = "salary.png")
        self.icon1 = self.icon1.subsample(2,2)
        self.icon2 = PhotoImage(file = "gift.png")
        self.icon2 = self.icon2.subsample(2,2)
        self.icon3 = PhotoImage(file = "investment.png")
        self.icon3 = self.icon3.subsample(2,2)
        self.icon4 = PhotoImage(file = "other.png")
        self.icon4 = self.icon4.subsample(2,2)

        self.buttonframe = tk.Frame(self.income_window) 
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)
        self.buttonframe.columnconfigure(2, weight = 1)
        self.buttonframe.columnconfigure(3, weight = 1)

        category1 = tk.Button(self.buttonframe)
        category1.config(image = self.icon1, height = 30, command = lambda: set_category("Salary", category1))
        category1.grid(row = 0,column = 0,sticky = tk.S + tk.N + tk.E + tk.W)
        category2 = tk.Button(self.buttonframe)
        category2.config(image = self.icon2, command = lambda: set_category("Gift", category2))
        category2.grid(row = 0,column = 1,sticky = tk.S + tk.N + tk.E + tk.W)
        category3 = tk.Button(self.buttonframe)
        category3.config(image = self.icon3,  command = lambda: set_category("Investment",category3))
        category3.grid(row = 0,column = 2,sticky = tk.S + tk.N + tk.E + tk.W)
        category4 = tk.Button(self.buttonframe)
        category4.config(image = self.icon4, command = lambda: set_category("Other",category4))
        category4.grid(row = 0,column = 3,sticky = tk.S + tk.N + tk.E + tk.W)

        self.buttonframe.pack(pady = (10,0), fill = "x")



        entry_comment_income = tk.Entry(self.income_window, width=50, bg = "#404040") 
        entry_comment_income.pack(pady = (20,0), anchor="w", padx = 40)
        entry_comment_income.insert(0, "Comment")
        entry_comment_income.configure(state='disabled')
        x_focus_in = entry_comment_income.bind('<Button-1>', lambda x: on_focus_in(entry_comment_income))
        x_focus_out = entry_comment_income.bind(
        '<FocusOut>', lambda x: on_focus_out(entry_comment_income, 'Comment'))

        self.EXCEL_FILE = "income.xlsx"


        self.category_list = {
            "Salary": 0,
            "Gift" : 0,
            "Investment": 0,
            "Other": 0}

        df = pd.read_excel(self.EXCEL_FILE)

        for ind in df.index:
            if df["Category"][ind] == "Salary":
                self.category_list["Salary"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Gift":
                self.category_list["Gift"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Investment":
                self.category_list["Investment"] += df["Money Count"][ind]
            elif df["Category"][ind] == "Other":
                self.category_list["Other"] += df["Money Count"][ind]




        def add_income():
            df = pd.read_excel(self.EXCEL_FILE)
            data_income = {
                "Money Count": entry_money_count_income.get(),
                "Date": entry_date_income.get(),
                "Account": self.account_choose.get(),
                "Category": self.selected_category_income,
                "Comment": entry_comment_income.get()}

            df = df._append(data_income , ignore_index = True)
    
            if data_income["Category"] == "Gift":
                self.category_list["Gift"] += int(data_income["Money Count"])

            if data_income["Category"] == "Salary":
                self.category_list["Salary"] += int(data_income["Money Count"])

            if data_income["Category"] == "Investment":
                self.category_list["Investment"] += int(data_income["Money Count"])

            if data_income["Category"] == "Other":
                self.category_list["Other"] += int(data_income["Money Count"])

            column_names = ["Money Count" , "Date" , "Account" , "Category" , "Comment"]
            
            df.to_excel(self.EXCEL_FILE , index = False ,header = column_names)
            

            self.income_window.destroy()
            MainWindow()



        self.button_add_income = tk.Button(self.income_window , text= "Add", bg = "#404040", bd = "0", fg = "white", command = add_income) 
        self.button_add_income.pack(pady = (240,0))


MainWindow()
        







     

