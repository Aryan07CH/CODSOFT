''' --------- TASK 2 ----------
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.

Perform the calculation and display the result.
'''
from tkinter import *

root = Tk()
root.minsize(width=400, height=600)
root.config(bg="black")
root.title("Calculator")
cal = Label(root, text="Calculator", font=("TIMES NEW ROMAN", 32),
            width=15, height=2, fg="orange", bg="black")
cal.pack()

l = Label(root, font=("bold", 20), width=22,
          height=2, borderwidth=1, relief="solid", bg="grey")
l.place(x=18, y=80)

equ = ""


def clear():
    global equ
    equ = ""
    l.config(text=equ, bg="grey", fg="white")


def show(val):
    global equ
    equ += val
    l.config(text=equ)


def calculate():
    global equ
    result = ""
    if equ != "":
        try:
            result = eval(equ)
        except:
            result = "Error"
            equation = ""
    l.config(text=result, fg="black", bg="grey")


Button(root, text="C", bg="black", fg="orange", font=("bold", 15), height=2, width=7, command=lambda: clear()).place(x=20,
        y=160)
Button(root, text="/", bg="black",fg="orange",font=("bold", 15), height=2, width=7, command=lambda: show("/")).place(x=108, y=160)
Button(root, text="*", bg="black",fg="orange",font=("bold", 15), height=2, width=7, command=lambda: show("*")).place(x=196, y=160)
Button(root, text="-", bg="black",fg="orange", font=("bold", 15), height=2, width=7, command=lambda: show("-")).place(x=284, y=160)

Button(root, text="7", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("7")).place(x=20, y=224)
Button(root, text="8", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("8")).place(x=108, y=224)
Button(root, text="9", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("9")).place(x=196, y=224)
Button(root, text="+", bg="black",fg="orange", font=("bold", 14), height=5, width=7, command=lambda: show("+")).place(x=284, y=224)

Button(root, text="4", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("4")).place(x=20, y=287)
Button(root, text="5", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("5")).place(x=108, y=287)
Button(root, text="6", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("6")).place(x=196, y=287)

Button(root, text="1", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("1")).place(x=20, y=350)
Button(root, text="2", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("2")).place(x=108, y=350)
Button(root, text="3", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show("3")).place(x=196, y=350)
Button(root, text="=", bg="black",fg="orange", font=("bold", 14), height=5, width=7, command=lambda: calculate()).place(x=284, y=350)

Button(root, text="0", bg="black",fg="white", font=("bold", 15), height=2, width=15, command=lambda: show("0")).place(x=20, y=413)
Button(root, text="del .", bg="black",fg="white", font=("bold", 15), height=2, width=7, command=lambda: show(".")).place(x=196,
                                                                                                             y=413)

root.mainloop()
