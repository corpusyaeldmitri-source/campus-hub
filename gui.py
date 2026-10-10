import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("1000x650")
root.title("Campus Hub")

def dashboard():
    hide()
    root.after(50)
    db_frame.place(x=150, y=52)

def tasks():
    hide()
    root.after(50)
    tsk_frame.place(x=150, y=52)

def projects():
    hide()
    root.after(50)
    prj_frame.place(x=150, y=52)

def assignments():
    hide()
    root.after(50)
    ass_frame.place(x=150, y=52)

ch_header = ttk.Label(root, text="Campus Hub", font=("Helvetica", "24"))
ch_header.place(x=10, y=15)

dashboard_btn = tk.Button(root, text="Dashboard", font=("Helvetica", "18"), height=2, width=8, command=dashboard)
dashboard_btn.place(x=20, y=50)

tasks_btn = tk.Button(root, text="Tasks", font=("Helvetica", "18"), height=2, width=8, command=tasks)
tasks_btn.place(x=20, y=105)

projects_btn = tk.Button(root, text="Projects", font=("Helvetica", "18"), height=2, width=8, command=projects)
projects_btn.place(x=20, y=160)

assignments_btn = tk.Button(root, text="Assignments", font=("Helvetica", "18"), height=2, width=8, command=assignments)
assignments_btn.place(x=20, y=215)

db_frame = tk.Frame(root, bg="black", height="575", width="825", relief="sunken")
tsk_frame = tk.Frame(root, bg="gray", height="575", width="825", relief="sunken")
prj_frame = tk.Frame(root, bg="maroon", height="575", width="825", relief="sunken")
ass_frame = tk.Frame(root, bg="pink", height="575", width="825", relief="sunken")

def hide():
    db_frame.place_forget()
    tsk_frame.place_forget()
    prj_frame.place_forget()
    ass_frame.place_forget()

hidebutton = tk.Button(root, text="Hide", command=hide)
hidebutton.place(x=10, y=500)

db_frame.place(x=150, y=52)

root.mainloop()