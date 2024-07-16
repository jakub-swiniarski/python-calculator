import tkinter as tk

window       = tk.Tk()
window.title = "Calculator"
window.geometry("300x400")
window.configure(bg = "#303030")
window.resizable(False, False)
input   = ""
display = tk.Label(
    window,
    text   = input,
    width  = 280,
    fg     = "#ffffff",
    bg     = "#474747",
    anchor = "w",
    padx   = 15,
    pady   = 15
)
display.config(font = ("Courier New", 24))
display.pack(padx = 10, pady = 10)

def clicked(ch):
    global input
    input += str(ch)
    display.config(text = input)

def clear():
    global input
    input = ""
    display.config(text = "")

def equals():
    global input
    try:
        display.config(text=eval(input))
        input=""
    except:
        display.config(text="ERROR")


def main():
    labels = [
        ["0", "1", "4", "7", "C"],
        [".", "2", "5", "8", "("],
        ["%", "3", "6", "9", ")"],
        ["=", "+", "-", "*", "/"]
    ]

    buttons = [[0 for x in range(5)] for y in range(4)]
    for i in range(4):
        for j in range(5):
            buttons[i][j] = tk.Button(
                window,
                text    = labels[i][j],
                font    = ("Courier New", 24),
                fg      = "#ffffff",
                bg      = "#474747",
                anchor  = "center",
                command = lambda i = i, j = j: clicked(labels[i][j])
            )
            buttons[i][j].place(x = 10 + i * 78, y = 400 - (j + 1) * 60)

    buttons[2][0].config(command = lambda: clicked("*0.01"))
    buttons[0][4].config(command = clear)
    buttons[3][0].config(command = equals)

    window.mainloop()

if __name__=="__main__": 
    main() 
