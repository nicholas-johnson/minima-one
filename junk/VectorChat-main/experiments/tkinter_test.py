import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

greeting = tk.Label(text='Hello Vector', padx=10, pady=10)
greeting.pack()

button = tk.Button(text='Listen', padx=10, pady=10)
button.pack()

def handle_keypress(event):
    print('keypress', event)

window.bind('<Key>', handle_keypress)

window.mainloop()