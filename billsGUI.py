from tkinter import *
from tkinter import ttk
from datetime import datetime

now = datetime.now() # gets date/ time 2022-03-03 14:51:01.123

# person1 = str(input("What is your name ?")) #! commented out for testing
person1 = 'justin'
person1 = person1.capitalize()
# person2 = str(input("What is user 2's name?")) #! commented out for testing
person2 = 'zack'
person2 = person2.capitalize()

class PersonsBills:
    def __init__(self, name):
        self.name = name
        self.waterAmount = 0          #1
        self.electricAmount = 0       #2
        self.mortgageAmount = 0       #3
        self.childCareAmount = 0      #4
        self.phoneAmount = 0          #5
        self.insuranceAmount = 0      #6         
        self.internetAmount = 0       #7
        self.otherAmount = 0          #8
        self.total = 0              
        self.amountToReceive = 0    
        self.amountToPay = 0        
    ###################################    functions   ################################################33
    def calculateTotal(self):
        # get variables from entry fields and assign them to variables
        self.electricAmount = float(electricityBillField.get() or 0)
        self.mortgageAmount = float(mortgageBillField.get() or 0)
        self.phoneAmount = float(phoneBillField.get() or 0)
        self.insuranceAmount = float(insuranceBillField.get() or 0)
        self.waterAmount = float(waterBillField.get() or 0)
        self.internetAmount = float(internetBillField.get() or 0)
        self.childCareAmount = float(childCareField.get() or 0)
        self.otherAmount = float(otherField.get() or 0)

        # calculate total amount of all bills paid
        self.total = (self.electricAmount + self.mortgageAmount + self.phoneAmount 
                        + self.insuranceAmount + self.waterAmount + self.internetAmount + self.childCareAmount + self.otherAmount) 

        #label to display total amount
        totalLabel = Label(root, text = (self.name + "'s Total : " + str(self.total)))
        totalLabel.grid(column = 3, row = 13, columnspan = 1)
  


#instantiate classes for each user
User1 = PersonsBills(person1)
User2 = PersonsBills(person2)


#initializing root window
root = Tk()
root.title('Bills Data')
# root.geometry('300x300')

#############################################   buttons   ###################################################
saveToFileButton = ttk.Button(root, text = "Save to file")
saveToFileButton.grid(column = 1, row = 11, columnspan = 1)
saveToFileButton.state(['disabled']) #! disabled the button until function is added


calculateTotalButton = ttk.Button(root, text = "Calculate Total", command = lambda: User1.calculateTotal()) #! this is for user 1... for now
calculateTotalButton.grid(column = 0, row = 11, columnspan = 1)
#calculateTotalButton.state(['disabled']) #! disabled the button until function is added


whoOwesWhoButton = ttk.Button(root, text = " Who Owes Who?")
whoOwesWhoButton.grid(column = 3, row = 11, columnspan = 1)
whoOwesWhoButton.state(['disabled']) #! disabled the button until function is added

##################################   User1's Entry field labels   ##################################################
electricityBillLabel = Label(root, text = "Electricity Amount", fg = 'blue', font = ("Helvetica", 12))
electricityBillLabel.grid(column = 0, row = 2, columnspan = 1)

mortgageBillLabel = Label(root, text = "Mortgage Amount", fg = 'blue', font = ("Helvetica", 12))
mortgageBillLabel.grid(column = 0, row = 3, columnspan = 1)

phoneBillLabel = Label(root, text = "Phone Amount", fg = 'blue', font = ("Helvetica", 12))
phoneBillLabel.grid(column = 0, row = 4, columnspan = 1)

insuranceBillLabel = Label(root, text = "Insurance Amount", fg = 'blue', font = ("Helvetica", 12))
insuranceBillLabel.grid(column = 0, row = 5, columnspan = 1)

waterBillLabel = Label(root, text = "Water Amount", fg = 'blue', font = ("Helvetica", 12))
waterBillLabel.grid(column = 0, row = 6, columnspan = 1)

internetBillLabel = Label(root, text = "Internet Amount", fg = 'blue', font = ("Helvetica", 12))
internetBillLabel.grid(column = 0, row = 7, columnspan = 1)

childCareLabel = Label(root, text = "Child Care Amount", fg = 'blue', font = ("Helvetica", 12))
childCareLabel.grid(column = 0, row = 8, columnspan = 1)

otherLabel = Label(root, text = "Other Amount", fg = 'blue', font = ("Helvetica", 12))
otherLabel.grid(column = 0, row = 9, columnspan = 1)

#!#################################   User2's Entry field labels   ##################################################
user2ElectricityBillLabel = Label(root, text = "Electricity Amount", fg = 'red', font = ("Helvetica", 12))
user2ElectricityBillLabel.grid(column = 5, row = 2, columnspan = 1)

user2MortgageBillLabel = Label(root, text = "Mortgage Amount", fg = 'red', font = ("Helvetica", 12))
user2MortgageBillLabel.grid(column = 5, row = 3, columnspan = 1)

user2PhoneBillLabel = Label(root, text = "Phone Amount", fg = 'red', font = ("Helvetica", 12))
user2PhoneBillLabel.grid(column = 5, row = 4, columnspan = 1)

user2InsuranceBillLabel = Label(root, text = "Insurance Amount", fg = 'red', font = ("Helvetica", 12))
user2InsuranceBillLabel.grid(column = 5, row = 5, columnspan = 1)

user2WaterBillLabel = Label(root, text = "Water Amount", fg = 'red', font = ("Helvetica", 12))
user2WaterBillLabel.grid(column = 5, row = 6, columnspan = 1)

user2InternetBillLabel = Label(root, text = "Internet Amount", fg = 'red', font = ("Helvetica", 12))
user2InternetBillLabel.grid(column = 5, row = 7, columnspan = 1)

user2ChildCareBillLabel = Label(root, text = "Child Care Amount", fg = 'red', font = ("Helvetica", 12))
user2ChildCareBillLabel.grid(column = 5, row = 8, columnspan = 1)

user2OtherLabel = Label(root, text = "Other Amount", fg = 'red', font = ("Helvetica", 12))
user2OtherLabel.grid(column = 5, row = 9, columnspan = 1)



###############################  entry fields  ##############################################
electricityBillField = Entry()
electricityBillField.grid(column = 3, row = 2, columnspan = 1)

mortgageBillField = Entry()
mortgageBillField.grid(column = 3, row = 3, columnspan = 1)

phoneBillField = Entry()
phoneBillField.grid(column = 3, row = 4, columnspan = 1)

insuranceBillField = Entry()
insuranceBillField.grid(column = 3, row = 5, columnspan = 1)

waterBillField = Entry()
waterBillField.grid(column = 3, row = 6, columnspan = 1)

internetBillField = Entry()
internetBillField.grid(column = 3, row = 7, columnspan = 1)

childCareField = Entry()
childCareField.grid(column = 3, row = 8, columnspan = 1)

otherField = Entry()
otherField.grid(column = 3, row = 9, columnspan = 1)



root.mainloop()
