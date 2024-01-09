import tkinter as tk
from tkinter import messagebox
import random
import string

class PassGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry('470x220+200+150')

        self.label=tk.Label(root,text='Password Generator',
             font=("Comic Sans MS",18),width=60,bd=5,bg='sky blue', fg='black')
        self.label.pack(side='top')

        self.length_label = tk.Label(root, text="Password Length:",font=7)
        self.length_label.place(x=80,y=80)

        self.length_entry = tk.Entry(root)
        self.length_entry.place(x=250,y=85)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.pass_gen,
                                         bd=5,bg='sky blue', fg='black',font=("sarif",12))
        self.generate_button.pack(side='bottom')

        self.password_label = tk.Label(root, text="")
        self.password_label.pack(side='bottom')

    def pass_gen(self):

        length = self.length_entry.get()

        if not length.isdigit():
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Password length should be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Generated Password is: {password}",font=("Arial",13))
        self.password_label.place(x=150,y=150)

def main():
    root = tk.Tk()
    app = PassGenApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()