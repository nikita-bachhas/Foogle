from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

import User_input_for_date
import List_of_stores

timeNow = datetime.now()
dt_string = ""
weekday = ""

# Instance method - self (to bring the values around)
class Mainwindow(Frame):

    def __init__(self, parent): # Yi Xian
        Frame.__init__(self, parent)
        # Window Config
        root.title("Foogle")
        root.geometry("700x500")
        root.iconbitmap('book_icon.ico')        # https://www.flaticon.es/icono-gratis/diccionario_917219

        # Import current date,time,weekday
        self.timeNow = datetime.now()
        self.current_weekday = timeNow.weekday()
        self.current_time = datetime.now().time()

        # TEXT - Label(*Window name*, text =* *)
        text = Label(self, text = "WELCOME TO NTU\nNORTH SPINE CANTEEN!", bg = "black", fg = "#ffc000", font="broadway 25 bold", height = "3", width = "30")
        text.pack()

        # To insert photo & text
        self.folder = "background_root.png"         # https://sites.psu.edu/emilykohler/2016/03/03/vegan-brochure-review/
        self.load = Image.open(self.folder)
        self.photo = ImageTk.PhotoImage(self.load)
        self.e = Label(self, text = "North Spine Plaza NS2.1-02-03/01A\nCASHLESS PAYMENT ONLY\n",\
                  compound = CENTER, font = "Times 20 bold", image = self.photo).pack()

        # Button to self.current_date_time function, Open store based on current date and time
        current_date_and_time = Button(self, text = "Store's Menu",font = "Times 12 bold", command = self.current_date_time)
        current_date_and_time.place(x = 140,y = 190)

        # Button to self.date_from_user function, Open a new window for the user to key in the desired date and time
        user_input = Button(self, text = "Date and Time of Visit", font = "Times 12 bold", command = self.date_from_user)
        user_input.place(x = 270,y = 190)

        # Button to self.close_root_window function, Exit the whole window
        close_the_app = Button(self, text = "Exit",font = "Times 12 bold", command = self.close_root_window)
        close_the_app.place(x = 460,y = 190)

        # Change the format of the desired date and time
    def setNewDateTime(self,newMonth,newDate,newHour,newMinute): # Nikita
        self.timeNow = timeNow.replace(minute= int(newMinute[0]) * 10 + int(newMinute[1]) , hour = int(newHour[0]) * 10 + int(newHour[1]),second = 0, year = 2019, month = int(newMonth), day = int(newDate))

        # Open/import the file User_input_for_date and pass back the values to main file
    def date_from_user(self): # Nikita
        # Return the values from the file
        themonth,thedate,thehour,theminute,theday = User_input_for_date.inputDialog(self).show()
        self.current_weekday = theday
        thetime = int(str(thehour) + str(theminute))
        self.current_time = thetime
        self.setNewDateTime(themonth,thedate,thehour,theminute)

        # Open/import the file List_of_stores
    def current_date_time(self): # Yi Xian
        # dd/mm/YY H:M:S
        self.dt_string = timeNow.strftime("%d/%m/%Y %H:%M:%S")
        self.current_time = self.timeNow.time()
        displaymenu = List_of_stores.displaydialog(self, self.current_weekday, self.dt_string, self.current_time)

    # Close the window when user press 'EXIT' button
    def close_root_window(self):
        root.destroy()
    

if __name__ == "__main__":
    root = Tk()
    root.wm_geometry("400x200")
    Mainwindow(root).pack(fill="both", expand=True)
    root.mainloop()
