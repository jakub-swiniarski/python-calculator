import tkinter as tk

#window properties
window=tk.Tk()
window.title="Calculator"
window.geometry("300x400")
window.configure(bg="#303030")

#calculator display
display=tk.Label(window, text="example text", width=280, fg="#ffffff",bg="#474747", anchor="center", pady=15)
display.config(font=("Courier New",20))
display.pack(padx=10, pady=10)

window.mainloop()