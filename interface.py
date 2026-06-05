import tkinter as tk

def click():
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("Button App")
window.geometry("300x200")

label = tk.Label(window, text="Click the button")
label.pack()

button = tk.Button(window, text="Click Me", command=click)
button.pack()

window.mainloop()