from tkinter import *
from tkinter import ttk





root = Tk() # initializing root window
root.title('Calculator')
root.resizable(0, 0) # prevents root window from being resized

############################ operation buttons #################################
clearButton = ttk.Button(root, text = 'CLR', command = lambda: clear())
clearButton.grid(column = 4, row = 1,)

addButton = ttk.Button(root, text = '+', command = lambda: press(" + ")) 
addButton.grid(column = 4, row = 2 )

minusButton = ttk.Button(root, text = '-', command = lambda: press(' - '))
minusButton.grid(column = 4, row = 3)

multiplyButton = ttk.Button(root, text = 'X', command = lambda: press(' * '))
multiplyButton.grid(column = 4, row = 4)

divideButton = ttk.Button(root, text = '÷', command = lambda: press(' / '))
divideButton.grid(column = 4, row = 5)

equalButton = ttk.Button(root, text = '=', command = lambda: equalPress())
equalButton.grid(column = 4, row = 6)



############################## number buttons ##################################
numberOneButton = ttk.Button(root, text = '1', command = lambda: press(1))
numberOneButton.grid(column = 1, row = 3)

numberTwoButton = ttk.Button(root, text = '2', command = lambda: press(2))
numberTwoButton.grid(column = 2, row = 3)

numberThreeButton = ttk.Button(root, text = '3', command = lambda: press(3))
numberThreeButton.grid(column = 3, row = 3)

numberFourButton = ttk.Button(root, text = '4', command = lambda: press(4))
numberFourButton.grid(column = 1, row = 4)

numberFiveButton = ttk.Button(root, text = '5', command = lambda: press(5))
numberFiveButton.grid(column = 2, row = 4)

numberSixButton = ttk.Button(root, text = '6', command = lambda: press(6))
numberSixButton.grid(column = 3, row = 4)

numberSevenButton = ttk.Button(root, text = 7, command = lambda: press(7))
numberSevenButton.grid(column = 1, row = 5)

numberEightButton = ttk.Button(root, text = '8', command = lambda: press(8))
numberEightButton.grid(column = 2, row = 5)

numberNineButton = ttk.Button(root, text = '9', command = lambda: press(9))
numberNineButton.grid(column = 3, row = 5)

numberZeroButton = ttk.Button(root, text = '0', command = lambda: press(0))
numberZeroButton.grid(column = 1, row = 6, columnspan = 3, sticky = EW) #column spans from East to West (goes all the way across horizontally)

######################## top entry field ##########################
equation = StringVar()


expressionField = Entry(root, textvariable = equation)
expressionField.grid(column = 1, row = 1, columnspan = 3, sticky= NSEW, rowspan = 2)

################### methods ####################################
expression = "" # globally declare expression variable

def press(num):
    """ function to update expression in the entry field """
    global expression
   
    expression = expression + (str(num)) # concatenate string to display in entry field

    equation.set(expression) #update expression
    

def clear():
    """ method to clear out contents of entry field"""
    global expression

    expression = ""
    equation.set("")

    #enable buttons (if disabled from error)
    numberOneButton.state(['!disabled'])
    numberTwoButton.state(['!disabled'])
    numberThreeButton.state(['!disabled'])
    numberFourButton.state(['!disabled'])
    numberFiveButton.state(['!disabled'])
    numberSixButton.state(['!disabled'])
    numberSevenButton.state(['!disabled'])
    numberEightButton.state(['!disabled'])
    numberNineButton.state(['!disabled'])
    numberZeroButton.state(['!disabled'])
    multiplyButton.state(['!disabled'])
    divideButton.state(['!disabled'])
    addButton.state(['!disabled'])
    minusButton.state(['!disabled'])
    equalButton.state(['!disabled'])

def equalPress():
    try:
        answer = str(eval(expression))
        equation.set(answer)
    except:
        answer = "ERROR"
        equation.set(answer)
        # disable all buttons except the clear button if there is an error
        numberOneButton.state(['disabled']) 
        numberTwoButton.state(['disabled']) 
        numberThreeButton.state(['disabled']) 
        numberFourButton.state(['disabled'])
        numberFiveButton.state(['disabled'])
        numberSixButton.state(['disabled'])
        numberSevenButton.state(['disabled'])
        numberEightButton.state(['disabled'])
        numberNineButton.state(['disabled'])
        numberZeroButton.state(['disabled'])
        multiplyButton.state(['disabled'])
        divideButton.state(['disabled'])
        addButton.state(['disabled'])
        minusButton.state(['disabled'])
        equalButton.state(['disabled'])
        
        


root.mainloop()
