import tkinter as tk


main = tk.Tk()

userInput = tk.Variable()

Number = tk.Entry(main, width = 35, borderwidth = 5,textvariable = userInput)
Number.grid(row = 0, column = 2, columnspan  = 3, padx = 10, pady = 10)


def button_add(value):
    Number.insert(tk.END, value)

#Collects the operator when the button is pressed
def operator(con):
    global initial
    initial = userInput.get()
    Number.delete(0, tk.END) #Deletes initial number to allow the next number to collect
    global operation
    operation = con #Defines the operator selected by the user for future use
    
#Solves the equation
def equal(operator):
    second = userInput.get() #Collects the second number inputted by the 

    if operator == "+":
        solution = int(initial) + int(second)
    elif operator == "-":
        solution = int(initial) - int(second)
    elif operator == "*":
        solution = int(initial) * int(initial)
    
    
        
    Number.delete(0,tk.END)
    Number.insert(tk.END,solution)



#define Buttons
button_1 = tk.Button(main, text = "1", padx = 40, pady =20, command = lambda:button_add(1))
button_1.grid(column = 1,row = 1)
button_2 = tk.Button(main, text = "2", padx = 40, pady =20, command = lambda:button_add(2))
button_2.grid(column = 2,row = 1)
button_3 = tk.Button(main, text = "3", padx = 40, pady =20, command = lambda:button_add(3))
button_3.grid(column = 3,row = 1)
button_4 = tk.Button(main, text = "4", padx = 40, pady =20, command = lambda:button_add(4))
button_4.grid(column = 1,row = 2)
button_5 = tk.Button(main, text = "5", padx = 40, pady =20, command = lambda:button_add(5))
button_5.grid(column = 2,row = 2)
button_6 = tk.Button(main, text = "6", padx = 40, pady =20, command = lambda:button_add(6))
button_6.grid(column = 3,row = 2)
button_7 = tk.Button(main, text = "7", padx = 40, pady =20, command = lambda:button_add(7))
button_7.grid(column = 1,row = 3)
button_8 = tk.Button(main, text = "8", padx = 40, pady =20, command = lambda:button_add(8))
button_8.grid(column = 2,row = 3)
button_9 = tk.Button(main, text = "9", padx = 40, pady =20, command = lambda:button_add(9))
button_9.grid(column = 3,row = 3)
button_0 = tk.Button(main, text = "0", padx = 40, pady =20, command = lambda:button_add(0))
button_0.grid(column = 2,row = 4)
button_plus = tk.Button(main, text = "+", padx = 40, pady =20, command = lambda:operator("+"))
button_plus.grid(column = 1,row = 5)
button_plus = tk.Button(main, text = "-", padx = 40, pady =20, command = lambda:operator("-"))
button_plus.grid(column = 2,row = 5)
button_plus = tk.Button(main, text = "x", padx = 40, pady =20, command = lambda:operator("*"))
button_plus.grid(column = 3,row = 5)
button_equal = tk.Button(main, text = "=", padx = 40, pady =20, command = lambda:equal(operation))
button_equal.grid(column = 2,row = 6)



main.mainloop()
