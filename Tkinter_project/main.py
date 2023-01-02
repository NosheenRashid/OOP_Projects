# from tkinter import *  # import everything
#
# # the class of tkinter is Tk()
# window = Tk()
#
# window.title("MY First GUI Program")  # --> we can see this title at the very top of screen
#
# window.minsize(width=500, height=300)  # the next thing is sizing the screen
#
# #  here we use another class from tkinter called Label()
# my_label = Label(text="I am a Label.", font=("cursive", 24, "bold"))
#
# # to show our label we have to use pack() to pack our label on to the screen
# my_label.pack()  # we can also change its direction but for moving it in center write expand=True
#
# my_label["text"] = "Nosheen Rashid"
# my_label.config(text="New Text")  # by doing this we configure or change our label
#
#
# # action that we want to perform on a button
# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)
#
#
# # Buttons
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
# #  Inputs
# input = Entry()
# input.pack()
#
# # we write this line of code at the end
# window.mainloop()
