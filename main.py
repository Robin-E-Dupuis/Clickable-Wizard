from tkinter import *

count = 0
def click():
    global count
    count += 1
    print("hello traveler! you clicked me "+str(count)+" times!")
    if(count>50 and count<52):
        print("Wow! You really are dedicated to clicking!")
    if(count>100 and count<102):
        print("Well, what can I say... You really are a master clicker!")
window=Tk()

photo = PhotoImage(file='img_1.png')

button1 = Button(window, text="click me!!", command=click,
                 font=("Comic Sans", 15),
                 fg="#5ced73",
                 background="purple",
                 activebackground="purple",
                 activeforeground="#5ced73",
                 image=photo,
                 compound="bottom")
button1.pack()
window.mainloop()



