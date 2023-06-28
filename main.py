import tkinter as tk

#window properties
window=tk.Tk()
window.title="Calculator"
window.geometry("300x400")
window.configure(bg="#303030")
window.resizable(False, False)

#calculator display
display=tk.Label(window, text="", width=280, fg="#ffffff",bg="#474747", anchor="w", padx=15, pady=15)
display.config(font=("Courier New",24))
display.pack(padx=10, pady=10)

#buttons
labels=[["0", "1", "4", "7", "C"],
        [".", "2", "5", "8", "("],
        ["%", "3", "6", "9", ")"],
        ["=", "+", "-","×", "÷"]]
buttons=[[0 for x in range(5)]for y in range(4)]
for i in range(4):
    for j in range(5):
        buttons[i][j] = tk.Button(window, text=labels[i][j], fg="#ffffff",bg="#474747", anchor="center")
        buttons[i][j].config(font=("Courier New",24))
        buttons[i][j].place(x=10+i*78, y=400-(j+1)*60)
        
window.mainloop()