import tkinter as tk

#window properties
window=tk.Tk()
window.title="Calculator"
window.geometry("300x400")
window.configure(bg="#303030")
window.resizable(False, False)

#input field
input = ""

#calculator display
display=tk.Label(window, text=input, width=280, fg="#ffffff",bg="#474747", anchor="w", padx=15, pady=15)
display.config(font=("Courier New",24))
display.pack(padx=10, pady=10)

#buttons
labels=[["0", "1", "4", "7", "C"],
        [".", "2", "5", "8", "("],
        ["%", "3", "6", "9", ")"],
        ["=", "+", "-","×", "÷"]]

def clicked(ch):
    global input
    input+=str(ch)
    display.config(text=input)

def clear():
    global input
    input=""
    display.config(text="")

def equals():
    global input
    try:
        display.config(text=eval(input))
        input=""
    except:
        display.config(text="ERROR")

buttons=[[0 for x in range(5)]for y in range(4)]
for i in range(4):
    for j in range(5):
        buttons[i][j] = tk.Button(window, text=labels[i][j], fg="#ffffff",bg="#474747", anchor="center", command=lambda: clicked())
        buttons[i][j].config(font=("Courier New",24))
        buttons[i][j].place(x=10+i*78, y=400-(j+1)*60)

buttons[0][4].config(command=clear)
buttons[3][0].config(command=equals)

#temporary solution
buttons[0][0].config(command=lambda: clicked("0"))
buttons[1][0].config(command=lambda: clicked("."))
buttons[2][0].config(command=lambda: clicked("%"))

buttons[0][1].config(command=lambda: clicked("1"))
buttons[1][1].config(command=lambda: clicked("2"))
buttons[2][1].config(command=lambda: clicked("3"))
buttons[3][1].config(command=lambda: clicked("+"))

buttons[0][2].config(command=lambda: clicked("4"))
buttons[1][2].config(command=lambda: clicked("5"))
buttons[2][2].config(command=lambda: clicked("6"))
buttons[3][2].config(command=lambda: clicked("-"))

buttons[0][3].config(command=lambda: clicked("7"))
buttons[1][3].config(command=lambda: clicked("8"))
buttons[2][3].config(command=lambda: clicked("9"))
buttons[3][3].config(command=lambda: clicked("*"))

buttons[1][4].config(command=lambda: clicked("("))
buttons[2][4].config(command=lambda: clicked(")"))
buttons[3][4].config(command=lambda: clicked("/"))


window.mainloop()