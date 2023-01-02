from tkinter import *


# Action perform on button
def calculate():
    result = float(entry.get())
    km = round(result * 1.609)
    label3.config(text=km)


window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label1
label = Label(text="Miles")
label.grid(column=2, row=0)

# Label2
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

# Label3
label3 = Label(text="0")
label3.grid(column=1, row=1)

# Label4
label4 = Label(text="Km")
label4.grid(column=2, row=1)




# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
