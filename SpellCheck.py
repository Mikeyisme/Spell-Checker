import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#93CDFF")

def spellCheck(): 
    word = enter_text.get()
    txt = TextBlob(word)
    right_text = str(txt.correct())

    correct_text = Label(root, text = "correct text is : ",font=("poppins", 20), bg="white", fg="black")
    correct_text.place(x=100, y=250)
    spell.config(text=right_text)

heading = Label(root, text = "Check Spelling", font=("Helvetica", 30, "bold"), bg="#93CDFF", fg="#012341")
heading.pack(pady=(50,0))

enter_text = Entry(root, justify="center", width=15, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", width=15, font=("arial", 20, "bold"), fg="white", bg="#21130d", command= spellCheck)
button.pack()

spell = Label(root, font=("poppins", 20), bg="white", fg="green")
spell.place(x=350, y=250)

root.mainloop()

