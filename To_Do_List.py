import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

print("TASK--1")
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__=="__main__":
    rootW = tk.Tk()
    rootW.title("To-Do List App")

    rootW.geometry("500x450+750+250")

    rootW.configure(bg="#FAEBD7")


    header_frame = tk.Frame(rootW, bg="#FAEBD7")
    header_frame.pack(fill="both")
    header_label = ttk.Label(
    header_frame,
    text="The To-Do List",
    font=("Algerian", "30"),
    background="#FAEBD7",
    foreground="#8B4513"
    )
    header_label.pack(padx=20, pady=20)

    functions_frame = tk.Frame(rootW, bg="#FAEBD7")
    functions_frame.pack(side="left", expand=True, fill="both")
    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )

    task_label.place(x=30, y=30)

    entry_task = tk.Entry(rootW, width=50)
    entry_task.pack(pady=30)
    entry_task.place(x=170,y=120)

    btn_add = tk.Button(rootW, text="Add Task", command=add_task)
    btn_add.pack()

    listbox_tasks = tk.Listbox(rootW, selectmode=tk.SINGLE, width=40)
    listbox_tasks.pack(pady=30)
    listbox_tasks.place(x=170,y=180)

    btn_delete = tk.Button(rootW, text="Delete Task", command=delete_task)
    btn_delete.pack()

    btn_add.place(x=30, y=150)
    btn_delete.place(x=30, y=190)

    rootW.mainloop()