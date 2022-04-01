from tkinter import *
from tkinter import ttk
from datetime import datetime

now = datetime.now() # gets date/ time 2022-03-03 14:51:01.123

# person1 = str(input("What is your name ?")) #! commented out for testing
person1 = 'user 1' #! this is just here for testing: user will provide the names when done
person1 = person1.capitalize()
# person2 = str(input("What is user 2's name?")) #! commented out for testing
person2 = 'user 2' #! this is just here for testing: user will provide the names when done
person2 = person2.capitalize()

class PersonsBills:
    def __init__(self, name):
        self.name = name
        self.waterAmount = 0          
        self.electricAmount = 0       
        self.mortgageAmount = 0       
        self.childCareAmount = 0      
        self.phoneAmount = 0          
        self.insuranceAmount = 0             
        self.internetAmount = 0       
        self.otherAmount = 0          
        self.total = 0              
        self.amountToReceive = 0    
        self.amountToPay = 0


    ###################################    functions   ################################################33
    def calculateTotals(self):
        # get variables from user1's entry fields and assign them to variables
        User1.electricAmount = float(electricityBillField.get() or 0)
        User1.mortgageAmount = float(mortgageBillField.get() or 0)
        User1.phoneAmount = float(phoneBillField.get() or 0)
        User1.insuranceAmount = float(insuranceBillField.get() or 0)
        User1.waterAmount = float(waterBillField.get() or 0)
        User1.internetAmount = float(internetBillField.get() or 0)
        User1.childCareAmount = float(childCareField.get() or 0)
        User1.otherAmount = float(otherField.get() or 0)

        # calculate total amount of all bills paid
        User1.total = (User1.electricAmount + User1.mortgageAmount + User1.phoneAmount 
                        + User1.insuranceAmount + User1.waterAmount + User1.internetAmount + User1.childCareAmount + User1.otherAmount) 

        #label to display total amount in correct $$ format
        user1TotalLabel = Label(root, text = (User1.name + "'s Total : "+ "${:.2f}".format(User1.total)))
        user1TotalLabel.grid(column = 3, row = 13, columnspan = 1)

        #! get variables from user2's entry fields and assign them to variables
        User2.electricAmount = float(user2ElectricityBillField.get() or 0)
        User2.mortgageAmount = float(user2MortgageBillField.get() or 0)
        User2.phoneAmount = float(user2PhoneBillField.get() or 0)
        User2.insuranceAmount = float(user2InsuranceBillField.get() or 0)
        User2.waterAmount = float(user2WaterBillField.get() or 0)
        User2.internetAmount = float(user2InternetBillField.get() or 0)
        User2.childCareAmount = float(user2ChildCareBillField.get() or 0)
        User2.otherAmount = float(user2OtherField.get() or 0)

        #! calculate total amount of all bills paid
        User2.total = (User2.electricAmount + User2.mortgageAmount + User2.phoneAmount 
                        + User2.insuranceAmount + User2.waterAmount + User2.internetAmount + User2.childCareAmount + User2.otherAmount) 

        #! label to display total amount in correct $$ format
        user2TotalLabel = Label(root, text = (User2.name + "'s Total : " + "${:.2f}".format(User2.total)))
        user2TotalLabel.grid(column = 6, row = 13, columnspan = 1)


    def whoOwesWho(self):
        whoOwesWhoLabel.config(text = "")
        
        User1.calculateTotals() # this calculates both user's totals
        if User1.total > User2.total: # if user1 paid more than user2
            difference = User1.total - User2.total
            amountOwed = (difference / 2)
            User2.amountToPay = amountOwed
            User1.amountToReceive = amountOwed
            # prints: user2 owes user 1 : $_______ at the bottom of the gui in correct currency format
            whoOwesWhoLabel.config(text = User2.name + " owes " + User1.name + " : " + "${:.2f}".format(User2.amountToPay))
        elif User1.total < User2.total: # if user2 paid more than user1
            difference = User2.total - User1.total
            amountOwed = (difference / 2)
            User1.amountToPay = amountOwed
            User2.amountToReceive = amountOwed
            # prints: user1 owes user 2 : $_______ at the bottom of the gui in correct currency format
            whoOwesWhoLabel.config(text = User1.name + " owes " + User2.name + " : " + "${:.2f}".format(User1.amountToPay))
        else:
            whoOwesWhoLabel.config(text = " Y'all each paid the same amount in bills this month ")
            




#instantiate classes for each user
User1 = PersonsBills(person1)
User2 = PersonsBills(person2)


#initializing root window
root = Tk()
root.title('Bills Data')
# root.geometry('300x300')

#############################################   buttons   ###################################################
saveToFileButton = ttk.Button(root, text = "Save to file")
saveToFileButton.grid(column = 1, row = 11, columnspan = 2)
saveToFileButton.state(['disabled']) #! disabled the button until function is added


calculateTotalButton = ttk.Button(root, text = "Calculate Totals", command = lambda: User1.calculateTotals()) 
calculateTotalButton.grid(column = 3, row = 11, columnspan = 2)
#calculateTotalButton.state(['disabled']) #! disabled the button until function is added


whoOwesWhoButton = ttk.Button(root, text = " Who Owes Who?", command = lambda: User1.whoOwesWho())
whoOwesWhoButton.grid(column = 5, row = 11, columnspan = 2)
#whoOwesWhoButton.state(['disabled']) #! disabled the button until function is added
################################# Name labels at top ###############################################################
user1Label = Label(root, text = User1.name + "'s Bills", fg = 'blue', font = ("Helvetica", 14))
user1Label.grid(column = 0, row = 1, columnspan = 1)

user2Label = Label(root, text = User2.name + "'s Bills", fg = 'red', font = ("Helvetica", 14))
user2Label.grid(column = 5, row = 1, columnspan = 1)

################################# Name labels at bottom ###############################################################
whoOwesWhoLabel = Label(root, text = ' ')
whoOwesWhoLabel.grid(column = 3, row = 14, columnspa = 4)

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



###############################  user1's entry fields  ##############################################
electricityBillField = Entry()
electricityBillField.grid(column = 2, row = 2, columnspan = 1)

mortgageBillField = Entry()
mortgageBillField.grid(column = 2, row = 3, columnspan = 1)

phoneBillField = Entry()
phoneBillField.grid(column = 2, row = 4, columnspan = 1)

insuranceBillField = Entry()
insuranceBillField.grid(column = 2, row = 5, columnspan = 1)

waterBillField = Entry()
waterBillField.grid(column = 2, row = 6, columnspan = 1)

internetBillField = Entry()
internetBillField.grid(column = 2, row = 7, columnspan = 1)

childCareField = Entry()
childCareField.grid(column = 2, row = 8, columnspan = 1)

otherField = Entry()
otherField.grid(column = 2, row = 9, columnspan = 1)

#!##############################  user2's entry fields  ##############################################

user2ElectricityBillField = Entry()
user2ElectricityBillField.grid(column = 6, row = 2, columnspan = 1)

user2MortgageBillField = Entry()
user2MortgageBillField.grid(column = 6, row = 3, columnspan = 1)

user2PhoneBillField = Entry()
user2PhoneBillField.grid(column = 6, row = 4, columnspan = 1)

user2InsuranceBillField = Entry()
user2InsuranceBillField.grid(column = 6, row = 5, columnspan = 1)

user2WaterBillField = Entry()
user2WaterBillField.grid(column = 6, row = 6, columnspan = 1)

user2InternetBillField = Entry()
user2InternetBillField.grid(column = 6, row = 7, columnspan = 1)

user2ChildCareBillField = Entry()
user2ChildCareBillField.grid(column = 6, row = 8, columnspan = 1)

user2OtherField = Entry()
user2OtherField.grid(column = 6, row = 9, columnspan = 1)

root.mainloop()
