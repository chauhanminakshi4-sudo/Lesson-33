from tkinter import *

root = Tk()
root.title("Login App")
root.geometry("400x400")

frame = Frame(root, bg="#d0efff", width=360, height=200)
frame.place(x=20, y=0)

Label(frame, text="Full Name", bg="#3895D3", fg="white").place(x=20, y=20)
Label(frame, text="Email Id", bg="#3895D3", fg="white").place(x=20, y=80)
Label(frame, text="Password", bg="#3895D3", fg="white").place(x=20, y=140)

name = Entry(frame)
email = Entry(frame)
password = Entry(frame, show="*")

name.place(x=150, y=20)
email.place(x=150, y=80)
password.place(x=150, y=140)

textbox = Text(root, height=5, width=40, bg="#BEBEBE")
textbox.place(x=20, y=250)

def display():
    textbox.insert(END, "Hey " + name.get())
    textbox.insert(END, "\nCongratulations for your new account!")

Button(root, text="Create Account", command=display, bg="red").place(x=130, y=210)

root.mainloop()