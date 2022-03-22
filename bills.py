""" This program will:
          *  take input from user(s) to calculate how much they paid in bills
          *  give option to split the amounts evenly and tell who owes who and how much 
          *  give option to write to/ create a file and write data to it"""

import pyinputplus as pyip
from datetime import datetime
#                                      0123456789012345678
now = datetime.now() # gets date/ time 2022-03-03 14:51:01.123


class PersonsBills:
    def __init__(self, name):
        self.name = name
        self.waterBill = 0      #1
        self.electricBill = 0   #2
        self.mortgage = 0       #3
        self.childCare = 0      #4
        self.phoneBill = 0      #5
        self.insurance = 0      #6         
        self.internet = 0       #7
        self.other = 0          #8
        self.total = 0              
        self.amountToReceive = 0    
        self.amountToPay = 0        
    
    # method to display menu of bills to be added
    def setBills(self):
        userInput = int
        while input != 0:
            print(" ~~~~~~~~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~~~~~~~ ")
            print(" 1 ..... Enter Water bill")
            print(" 2 ..... Enter Electric bill")
            print(" 3 ..... Enter Mortgage")
            print(" 4 ..... Enter Child care bill")
            print(" 5 ..... Enter Phone bill")
            print(" 6 ..... Enter Insurance bill")
            print(" 7 ..... Enter Internet bill")
            print(" 8 ..... Enter Other bill")
            print(" 9 ..... Display bill amounts already entered") 
            print(" 0 ..... Exit " + self.name + "'s bills ")
            userInput = pyip.inputNum()
            if userInput == 0:
                menu()
            if userInput == 1:
                self.waterBill = pyip.inputNum("How much did %s pay for the Water bill? " % (self.name))
            if userInput == 2:
                self.electricBill = pyip.inputNum("How much did %s pay for the Electric bill? " % (self.name))
            if userInput == 3:
                self.mortgage = pyip.inputNum("How much did %s pay for the Mortgage? " % (self.name))
            if userInput == 4:
                self.childCare = pyip.inputNum("How much did %s pay for Child care? " % (self.name))
            if userInput == 5:
                self.phoneBill = pyip.inputNum("How much did %s pay for the Phone bill? " % (self.name))
            if userInput == 6:
                self.insurance = pyip.inputNum("How much did %s pay for Insurance? " % (self.name))
            if userInput == 7:
                self.internet = pyip.inputNum("How much did %s pay for Internet? " % (self.name))
            if userInput == 8:
                self.other = pyip.inputNum("How much did %s pay for the Other? " % (self.name))
            if userInput == 9:
                self.displayBillAmounts()
    
    # method to display bill amounts by a certain user
    def displayBillAmounts(self):
        print(" ********** %s's Bills Paid ********** " % (self.name))
        print("Water.......: " + "${:.2f}".format(self.waterBill))
        print("Electricity.: " + "${:.2f}".format(self.electricBill))
        print("Mortgage....: " + "${:.2f}".format(self.mortgage))
        print("Child care..: " + "${:.2f}".format(self.childCare))
        print("Phone.......: " + "${:.2f}".format(self.phoneBill))
        print("Insurance...: " + "${:.2f}".format(self.insurance))
        print("Internet....: " + "${:.2f}".format(self.internet))
        print("Other.......: " + "${:.2f}".format(self.other))
        print("Amount to pay to other : " + "${:.2f}".format(self.amountToPay))
        print("Amount to receive from other : " + "${:.2f}".format(self.amountToReceive))
     
     # method to calculate total amount paid in bills
    def calculateTotal(self):
        self.total = self.waterBill + self.electricBill + self.mortgage + self.childCare + self.phoneBill + self.insurance + self.internet + self.other
        return self.total
    

    # method to determine who owes who and how much
    def whoOwesWho(self):
        if user1.total == 0:
            user1.calculateTotal()
        if user2.total == 0:
            user2.calculateTotal()
        # if user 1 paid more in bills
        if user1.total > user2.total:
            # gets difference of the two totals
            difference = user1.total - user2.total
            amountOwed = (difference / 2)
            user2.amountToPay = amountOwed #user2 owes money
            user1.amountToReceive = amountOwed # user1 should receive money
            #print("%s owes %s : $%d " % (user2.name, user1.name, amountOwed))
            print(user2.name + " owes " + user1.name + " : " + "${:.2f}".format(user2.amountToPay))
            #if user 2 paid more in bills
        elif user1.total < user2.total:
            difference = user2.total - user1.total
            amountOwed = (difference / 2)
            user1.amountToPay = amountOwed
            user2.amountToReceive = amountOwed
            #print("%s owes %s : $%d " % (user1.name, user2.name, amountOwed))
            print(user1.name + " owes " + user2.name + " : " + "${:.2f}".format(user1.amountToPay))
        else:
            print("Each person paid the same. Yall good. ")
        
    def printToFile(self):
        # opens file for appending/ creates file if it does not already exist
        f = open("billsDataFile.txt", "a+")
        f.write("\n")
        f.write("****************************************")
        f.write(str(now) + "\n")
        f.write("******* %s's bills for the month *******\n" % (self.name))
        f.write("Water       : " + "${:.2f}".format(self.waterBill) + "\n")
        f.write("Electricity : " + "${:.2f}".format(self.electricBill) + "\n")
        f.write("Mortgage    : " + "${:.2f}".format(self.mortgage) + "\n")
        f.write("Child Care  : " + "${:.2f}".format(self.childCare) + "\n")
        f.write("Phone       : " + "${:.2f}".format(self.phoneBill) + "\n")
        f.write("Insurance   : " + "${:.2f}".format(self.insurance) + "\n")
        f.write("Internet    : " + "${:.2f}".format(self.internet) + "\n")
        f.write("Other       : " + "${:.2f}".format(self.other) + "\n")
        f.write(" ******************************************\n")
        f.write("Your total      : " + "${:.2f}".format(self.total) + "\n")
        f.write("You owe         : " + "${:.2f}".format(self.amountToPay) + "\n")
        f.write("You are getting : " + "${:.2f}".format(self.amountToReceive) + " from the other person \n")
        f.write(" ******************************************\n")
        f.write(" ******************************************\n\n")
        


# get user names and capitalize the first letter            
user1 = pyip.inputStr("Enter person 1's name ")
user1 = user1.capitalize() 
user2 = pyip.inputStr("Enter person 2's name ")
user2 = user2.capitalize()

#instantiate classes for each user
user1 = PersonsBills(user1)
user2 = PersonsBills(user2)


# main menu
def menu():
    input = int
    while input != 0:
        print(" ~~~~~~~~~~ MENU ~~~~~~~~~~ ")
        print(" 1 ..... Enter bills for %s " % (user1.name))
        print(" 2 ..... Enter bills for %s " % (user2.name))
        print(" 3 ..... Calculate totals ")
        print(" 4 ..... 50/50 split (who owes who and how much) ") 
        print(" 5 ..... Write info to file ") 
        print(" 0 ..... Exit Program")
        input = pyip.inputNum()
        if input == 0:
            print("Exiting program ....")
            quit()
        if input == 1:
            user1.setBills()
        if input == 2:
            user2.setBills()
        if input == 3:
            user1.calculateTotal()
            user2.calculateTotal()
        
            print("########## TOTALS ########## ")
            print(user1.name + "'s total : " + "${:.2f}".format(user1.total)) # prints totals in $$ format (with two decimal places)
            print(user2.name + "'s total : " + "${:.2f}".format(user2.total)) # prints totals in $$ format (with two decimal places)
        if input == 4:
            user2.whoOwesWho()
        if input == 5:
            user1.printToFile()
            user2.printToFile()
            

menu()
