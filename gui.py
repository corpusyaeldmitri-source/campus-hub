import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("1000x650")
root.title("Campus Hub")
root.configure(bg="light steel blue")
root.resizable(False, False)


#FUNCTIONS
def dashboard():
    hide()
    root.after(50)
    db_frame.place(x=140, y=52)
    db_todo.place(x=10, y=10)

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

hdr_border = tk.Frame(root, bg="black", height=36, width=176)
hdr_border.place(relx=0.5, y=27, anchor="center")
ch_header = tk.Label(root, text="Campus Hub", font=("Helvetica", "24"), fg="black", width="12", background="white")
ch_header.place(relx=0.5, y=27, anchor="center")


# SIDE BUTTONS
dashboard_btn = tk.Button(root, text="Dashboard", font=("Helvetica", "18"), height=2, width=8, borderwidth="0", command=dashboard)
dashboard_btn.place(x=10, y=50)

tasks_btn = tk.Button(root, text="Tasks", font=("Helvetica", "18"), height=2, width=8, borderwidth="0", command=tasks)
tasks_btn.place(x=10, y=105)

projects_btn = tk.Button(root, text="Projects", font=("Helvetica", "18"), height=2, width=8, borderwidth="0", command=projects)
projects_btn.place(x=10, y=160)

assignments_btn = tk.Button(root, text="Assignments", font=("Helvetica", "18"), height=2, width=8, borderwidth="0", command=assignments)
assignments_btn.place(x=10, y=215)

# FRAMES
db_frame = tk.Frame(root, bg="white", height="575", width="835", relief="sunken", bd=7)
tsk_frame = tk.Frame(root, bg="gray", height="575", width="835", relief="sunken", bd=7)
prj_frame = tk.Frame(root, bg="maroon", height="575", width="835", relief="sunken", bd=7)
ass_frame = tk.Frame(root, bg="pink", height="575", width="835", relief="sunken", bd=7)

# DASHBOARD
db_todo = tk.Label(db_frame, text="To do:", font=("Helvetica", "16"), fg="black", background="white")

def hide():
    db_frame.place_forget()
    tsk_frame.place_forget()
    prj_frame.place_forget()
    ass_frame.place_forget()

hidebutton = tk.Button(root, text="Hide", command=hide)
hidebutton.place(x=10, y=500)

dashboard()

root.mainloop()