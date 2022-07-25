from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageTk

class displaydialog(Toplevel):

    def ReadtxtFile(self): # Carissa
        self.MenuItems = {}
        StallName = ""
        self.Stallcounter = 0

        ListInStall = []

        with open("stall_menu.txt") as f_in:
            lines = f_in.readlines()
            for i in lines:
                listOfLines = i.split(',')

                ListOfDay = []
                for each in range(5, len(listOfLines)):             # List of 5, last one make a list for days
                    ListOfDay.append(int(listOfLines[each]))

                    # Directory
                eachItem = { "Stall": listOfLines[0],
                             "Name" : listOfLines[1],
                             "Price" : listOfLines[2],
                             "OpeningHrs" : listOfLines[3],
                             "ClosingHrs" : listOfLines[4],
                             "OperatingDays" : ListOfDay
                    }
                    # Blank - first stall - Last stall
                if StallName == "" or StallName != listOfLines[0] or lines.index(i) == len(lines) - 1:
                    StallName = listOfLines[0]

                    if self.Stallcounter > 0: # Chicken Rice stall start with one

                        if lines.index(i) == len(lines) - 1:
                            ListInStall.append(eachItem) # Append the stall list to directory

                        self.MenuItems["Stall" + str(self.Stallcounter)] = ListInStall
                        ListInStall = []
                    self.Stallcounter += 1
                ListInStall.append(eachItem) # Append again (Not in the loop)

    def operationhour(self): # Carissa
        stringtoprint = self.MenuItems["Stall" + str(self.SelectedStore)][0]["Stall"]
        stringtoprint += "\nOperation Hour:\nMonday - Friday : 0800 - 2030\nSaturday : 0800 - 1430\nSunday/PH : CLOSED"
        messagebox.showinfo("Foogle", stringtoprint)

    def waitingtime(self): # Carissa
        self.new = Toplevel()
        self.new.title("Foogle")
        self.new.geometry("450x100")
        self.new.iconbitmap(r'book_icon.ico')
        self.label_waiting_time =Label(self.new, text = "Please enter the number of people in front of you: ")
        self.entry_waiting_time = Entry(self.new)
        check_button = Button(self.new, text="CHECK", command=self.calculate_waiting_time)
        self.label_waiting_time.grid(row = 0, column = 0)
        self.entry_waiting_time.grid(row=0, column=1)
        check_button.grid(row=1, column=0)

    def calculate_waiting_time(self): # Carissa
        printthis = self.WaitingTime[self.SelectedStore]
        try:
            no_of_ppl = int(self.entry_waiting_time.get())
            total_waiting_time = no_of_ppl * printthis
            string_total_waiting_time = str(total_waiting_time)
            string_to_display = "Waiting time: " + string_total_waiting_time
            label_2 = Label(self.new)
            label_2["text"] = string_to_display
            label_2.grid(row=1, column=1)

        except ValueError:
            messagebox.showerror('Error!', 'Please enter a vaild number!')

    def CompareTime (self,timeA, timeB, isSmaller): # Carissa
        #TimeA = datetime.time , TimeB = String , bool if smaller or bigger
        #isSmaller is true, isBigger is false

        newTime = timeA.replace(hour = int(timeB[0] + timeB[1]) , minute = int(timeB[2] + timeB[3]))

        if timeA < newTime and isSmaller:
            return True
        elif timeA > newTime and isSmaller:
            return False
        if timeA > newTime and not(isSmaller):
            return True
        elif timeA < newTime and not(isSmaller):
            return False

    def ShowStoreMenu(self,stallNo): # Carissa

        self.SelectedStore = stallNo

        if len(self.GridLabels):
            self.GridLabels = []

            for label in self.grid_slaves(0,1):
                label.grid_forget()

            self.right_frame = Frame(self, width=450, height=400, bg='#1A160B')
            self.right_frame.grid(row=0, column=1, padx=10, pady=5)

        itemsShowed = 0
            # Display all stalls using loop
        for each in self.MenuItems["Stall" + str(stallNo)]:
            if self.day in each['OperatingDays']:
                if self.CompareTime(self.theTimeNow, each["OpeningHrs"] , False ) and self.CompareTime(self.theTimeNow,each["ClosingHrs"], True):
                    newLabel = Label(self.right_frame, text=(each['Name']) + '        $' + (each['Price']),
                                     font="30").grid(row=self.MenuItems["Stall" + str(stallNo)].index(each), column=0,
                                                     padx=5, pady=5)
                    self.GridLabels.append(newLabel)

                    itemsShowed += 1

        if itemsShowed == 0:
            newLabel2 = Label(self.right_frame, text = "SORRY, IT'S CLOSED!!", font = 'Calibri 25 bold').grid(row=1, column=0, padx=5, pady=5)
            self.GridLabels.append(newLabel2)


    def __init__(self, parent,hello = None,dt_string = None, theTime = None): # Nikita
        Toplevel.__init__(self, parent)
        self.title("Foogle")
        self.geometry("900x600")
        self.iconbitmap(r'book_icon.ico')

        self.filename = PhotoImage(file="background_menu.png")          # https://www.pexels.com/photo/five-white-plates-with-different-kinds-of-dishes-54455/
        self.background_label = Label(self, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.ReadtxtFile()
        self.day = hello
        self.date = dt_string
        self.theTimeNow = theTime

        # Create Frame widget # Create frame within left_frame # Create label above the tool_bar
        left_frame = Frame(self, width=200, height=500, bg = '#1A160B')
        left_frame.grid(row=0, column=0, padx=20, pady=5)
        tool_bar = Frame(left_frame, width=180, height=430, bg='#1A160B')
        tool_bar.grid(row=2, column=0, padx=5, pady=5)
        Label(left_frame, text="Menu", fg = 'white',bg ='#1A160B', font="Forte 25 bold").grid(row=1, column=0, padx=5, pady=5)

        self.GridLabels = []

        self.SelectedStore = 0

        self.WaitingTime = [0,1,2,1,3,1] # Waiting time per person for each store

        # Using loop to display buttons for all stall based on the directory
        for i in range(1,self.Stallcounter):        # Carissa
            menubutton = Button(tool_bar, text= self.MenuItems["Stall" + str(i)][0]["Stall"] , font='15', command=partial(self.ShowStoreMenu, i))
            menubutton.grid(row=i, column=0, padx=5, pady=5)

        # Create Frame widget # Create frame within right_frame # Create label above the tool_bar
        self.right_frame = Frame(self, width=0, height=0, bg='#1A160B')
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)
        operationhour = Button(self, text='Operation Hour', font='15', command=self.operationhour)
        operationhour.place(x=730, y=280)
        waitingtime = Button(self, text='Waiting Time', font='15', command= self.waitingtime)
        waitingtime.place(x=730, y=330)
