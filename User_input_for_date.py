from tkinter import *
from tkinter import messagebox
import calendar

class inputDialog(Toplevel):
    
    def __init__(self, parent): # Carissa
        Toplevel.__init__(self,parent)

        self.month = StringVar()
        self.date = StringVar()
        self.hour = StringVar()
        self.minute = StringVar()
        self.day = IntVar()

        self.title("Foogle")
        self.geometry("360x140")
        self.iconbitmap(r'book_icon.ico')
        
        self.label_month =Label(self, text = "Please enter the month (eg 1,2,10,12): ")
        self.entry_month = Entry(self,textvariable = self.month)

        self.label_date =Label(self, text = "Please enter the date (eg 1,2,10,28): ")
        self.entry_date = Entry(self,textvariable = self.date)

        self.label_hour =Label(self, text = "Please enter the hour (eg 00 to 23): ")
        self.entry_hour = Entry(self,textvariable = self.hour)

        self.label_minute =Label(self, text = "Please enter the minute (eg 00 to 59): ")
        self.entry_minute = Entry(self,textvariable = self.minute)

        done_button = Button(self, text = "DONE", command = self.set_date)


        self.label_month.grid(row = 0, column = 0)
        self.entry_month.grid(row = 0, column = 1)
        self.label_date.grid(row = 1, column = 0)
        self.entry_date.grid(row = 1, column = 1)
        self.label_hour.grid(row = 2, column = 0)
        self.entry_hour.grid(row = 2, column = 1)
        self.label_minute.grid(row = 3, column = 0)
        self.entry_minute.grid(row = 3, column = 1)
        done_button.grid (row=4,column =1)

        
    def set_date(self): # Nikita
        month_from_user = self.entry_month.get()
        date_from_user = self.entry_date.get()
        hour_from_user = self.entry_hour.get()
        minute_from_user = self.entry_minute.get()

        if month_from_user == "" or date_from_user == "" or hour_from_user == "" or minute_from_user == "":
            messagebox.showerror('Error!', 'Please fill up all values ')

        else:
            try:
                month_from_user = int(month_from_user)
                date_from_user = int(date_from_user)
                hour_from_user = int(hour_from_user)
                minute_from_user = int(minute_from_user)

                if month_from_user >= 13:
                    messagebox.showerror('Error!', 'Please enter the vaild month number between 1 to 12! ')

                elif date_from_user >= 32:
                    messagebox.showerror('Error!', 'Please enter the vaild date number between 1 to 31! ')

                elif hour_from_user >= 24:
                    messagebox.showerror('Error!', 'Please enter the vaild time between 00 to 23!')

                elif minute_from_user >= 60:
                    messagebox.showerror('Error!', 'Please enter the vaild time between 00 to 59!')
                # import calendar to find th desired day of the week

                else:
                    self.day.set(calendar.weekday(2019, month_from_user, date_from_user))
                    self.destroy()

            except ValueError:
                label_error_text = Label(self)
                label_error_text["text"]="Error! Please enter valid number!"
                label_error_text.grid (row = 4, column = 0)

    def show(self):
        self.wm_deiconify()
        self.wait_window()
        return self.month.get(),self.date.get(),self.hour.get(),self.minute.get(),self.day.get()
