import tkinter as tk

root = tk.Tk()
root.title("Python App")

def on_click():
    lbl.config(text="The btn clicked")

lbl = tk.Label(root, text="Hello World")
lbl.grid(column=0, row=0)

print(lbl.config().keys())

btn = tk.Button(root,text="Click me",command=on_click)
btn.grid(column=1,row=0,padx=10,pady=10)

root.mainloop()