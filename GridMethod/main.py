from tkinter import *


window = Tk()
window.title("Grid")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label = Label(text="Label")
label.grid(column=0, row=0)

# Button
button = Button(text="Click Me!")
button.grid(column=1, row=1)

# Button
button1 = Button(text="Click Me!")
button1.grid(column=2, row=0)

# Entry
entry = Entry()
entry.grid(column=3, row=2)





window.mainloop()