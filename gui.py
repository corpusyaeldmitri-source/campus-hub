import tkinter as tk
import storage

root = tk.Tk()

root.geometry("1000x650")
root.title("Campus Hub")
root.configure(bg="light steel blue")
root.resizable(False, False)

tasks_list = []


# FUNCTIONS ----------------------------------------------------------------------------------------------------------------
def dashboard():
    hide()
    root.after(50)
    db_frame.place(x=140, y=52)
    db_taskstodo.place(x=130, y=10)
    db_taskdets.place(x=530, y=10)
    root.after(1, show_db)


def tasks():
    hide()
    root.after(50)
    tsk_frame.place(x=140, y=52)
    tsk_add_btn.place(x=10, y=10)
    tsk_remove_btn.place(x=110, y=10)
    tsk_edit_btn.place(x=210, y=10)


def projects():
    hide()
    root.after(50)
    prj_frame.place(x=140, y=52)


def assignments():
    hide()
    root.after(50)
    ass_frame.place(x=140, y=52)


def mark_finished(task_no):
    tasks_list[task_no]["Finished"] = True
    storage.storage_save(tasks_list)
    root.after(1, show_db)


def mark_unfinished(task_no):
    tasks_list[task_no]["Finished"] = False
    storage.storage_save(tasks_list)
    root.after(1, show_db)


def delete_task(task_no):
    del tasks_list[task_no]
    storage.storage_save(tasks_list)
    for widget in tsk_del_frame.winfo_children():
        widget.destroy()
    for widget in db_frame.winfo_children():
        widget.place_forget()
    root.after(10, show_db)


# TASK BUTTONS ----------------------------------------------------------------------------------------------------------------


def show_add_task():
    hide_task()
    root.after(
        10,
    )
    tsk_frame.after(50)
    tsk_name_add.place(x=35, y=48)
    tsk_sub_add.place(x=27, y=88)
    tsk_due_add.place(x=48, y=128)
    tsk_det_add.place(x=31, y=168)

    name_entry_add.place(x=120, y=50)
    sub_entry_add.place(x=120, y=90)
    date_entry_add.place(x=120, y=130)
    det_entry_add.place(x=120, y=170)

    add_button_task.place(x=705, y=500)
    clear_button_task.place(x=605, y=500)


def show_remove_task():
    hide_task()
    tsk_del_frame.place(x=10, y=50)
    placey = 10
    for task_no, task in enumerate(tasks_list):
        t_frame = tk.Frame(
            tsk_del_frame, bg="white", height="115", width="300", relief="groove", bd=7
        )
        task_status = "Complete" if task["Finished"] else "Not Complete"
        t_label = tk.Label(
            t_frame,
            text=f"Name: {task["Name"]}\nSubject: {task["Subject"]}\nDue date: {task["Due"]}\nStatus: {task_status}",
            font=("Helvetica", "18"),
            fg="black",
            bg="white",
            justify="left",
        )
        t_del_btn = tk.Button(
            tsk_del_frame,
            text="X",
            font=("Helvetica", "16"),
            height=2,
            width=1,
            bg="green",
            fg="black",
            borderwidth=0,
            command=lambda task_no=task_no: delete_task(task_no),
        )

        t_frame.place(x=10, y=placey)
        t_label.place(x=10, y=10)
        t_del_btn.place(x=310, y=placey)

        placey += 120


def clear_entry_task():
    name_entry_add.delete(0, tk.END)
    sub_entry_add.delete(0, tk.END)
    date_entry_add.delete(0, tk.END)
    det_entry_add.delete("1.0", "end")
    tsk_addsuccess_label.place_forget()


def save_task():
    task_name = name_entry_add.get().strip()
    task_subject = sub_entry_add.get().strip()
    task_due = date_entry_add.get().strip()
    task_details = det_entry_add.get("1.0", "end").strip()

    if (
        task_name.strip() == ""
        or task_subject.strip() == ""
        or task_due.strip() == ""
        or task_details.strip() == ""
    ):
        tsk_invalid_label.place(x=400, y=500)
        tsk_frame.after(1000, tsk_invalid_label.place_forget)
    else:
        task = {
            "Name": task_name,
            "Subject": task_subject,
            "Due": task_due,
            "Details": task_details,
            "Finished": False,
        }

        tasks_list.append(task)
        storage.storage_save(tasks_list)

        tsk_addsuccess_label.place(x=400, y=500)

        tsk_frame.after(1000, clear_entry_task)


hdr_border = tk.Frame(root, bg="black", height=36, width=176)
hdr_border.place(relx=0.5, y=27, anchor="center")
ch_header = tk.Label(
    root,
    text="Campus Hub",
    font=("Helvetica", "24"),
    fg="black",
    width="12",
    background="white",
)
ch_header.place(relx=0.5, y=27, anchor="center")

# SIDE BUTTONS ----------------------------------------------------------------------------------------------------------------
dashboard_btn = tk.Button(
    root,
    text="Dashboard",
    font=("Helvetica", "18"),
    height=2,
    width=8,
    borderwidth=0,
    command=dashboard,
)
dashboard_btn.place(x=10, y=50)

tasks_btn = tk.Button(
    root,
    text="Tasks",
    font=("Helvetica", "18"),
    height=2,
    width=8,
    borderwidth=0,
    command=tasks,
)
tasks_btn.place(x=10, y=105)

projects_btn = tk.Button(
    root,
    text="Projects",
    font=("Helvetica", "18"),
    height=2,
    width=8,
    borderwidth=0,
    command=projects,
)
projects_btn.place(x=10, y=160)

assignments_btn = tk.Button(
    root,
    text="Assignments",
    font=("Helvetica", "18"),
    height=2,
    width=8,
    borderwidth=0,
    command=assignments,
)
assignments_btn.place(x=10, y=215)

# MAIN FRAMES ----------------------------------------------------------------------------------------------------------------
db_frame = tk.Frame(root, bg="white", height="575", width="835", relief="sunken", bd=7)
tsk_frame = tk.Frame(root, bg="white", height="575", width="835", relief="sunken", bd=7)
prj_frame = tk.Frame(root, bg="white", height="575", width="835", relief="sunken", bd=7)
ass_frame = tk.Frame(root, bg="white", height="575", width="835", relief="sunken", bd=7)
tsk_del_frame = tk.Frame(
    tsk_frame, bg="light grey", height="505", width="800", relief="sunken", bd=7
)

# DASHBOARD ----------------------------------------------------------------------------------------------------------------
db_taskstodo = tk.Label(
    db_frame,
    text="Tasks",
    font=("Helvetica", "16"),
    fg="black",
    background="white",
)
db_taskdets = tk.Label(
    db_frame,
    text="Task Details",
    font=("Helvetica", "16"),
    fg="black",
    background="white",
)

db_notasks = tk.Label(
    db_frame,
    text="No tasks yet",
    font=("Helvetica", "16"),
    fg="black",
    background="white",
)
tasks_list = storage.storage_load()


def show_db():
    placey = 50
    for task_no, task in enumerate(tasks_list):
        t_frame = tk.Frame(
            db_frame, bg="light grey", height="115", width="300", relief="groove", bd=7
        )
        tdets_frame = tk.Frame(
            db_frame, bg="light grey", height="115", width="440", relief="groove", bd=7
        )
        task_status = "Complete" if task["Finished"] else "Not Complete"
        t_label = tk.Label(
            t_frame,
            text=f"Name: {task["Name"]}\nSubject: {task["Subject"]}\nDue date: {task["Due"]}\nStatus: {task_status}",
            font=("Helvetica", "18"),
            fg="black",
            bg="light grey",
            justify="left",
        )
        tdets_label = tk.Label(
            tdets_frame,
            text=f"{task["Details"]}",
            font=("Helvetica", "16"),
            fg="black",
            bg="light grey",
            justify="left",
        )
        tsk_done_btn = tk.Button(
            db_frame,
            text="✓",
            font=("Helvetica", "16"),
            height=2,
            width=1,
            bg="green",
            fg="black",
            borderwidth=0,
            command=lambda task_no=task_no: mark_finished(task_no),
        )
        tsk_undone_btn = tk.Button(
            db_frame,
            text="X",
            font=("Helvetica", "16"),
            height=2,
            width=1,
            bg="green",
            fg="black",
            borderwidth=0,
            command=lambda task_no=task_no: mark_unfinished(task_no),
        )

        t_frame.place(x=20, y=placey)
        tdets_frame.place(x=330, y=placey)
        t_label.place(x=10, y=5)
        tdets_label.place(x=10, y=2)
        tsk_done_btn.place(x=775, y=placey)
        tsk_undone_btn.place(x=775, y=placey + 50)
        placey += 120


# ADD TASKS ----------------------------------------------------------------------------------------------------------------
tsk_add_btn = tk.Button(
    tsk_frame,
    text="Add task",
    font=("Helvetica", "16"),
    height=1,
    width=7,
    borderwidth=0,
    bg="white",
    command=show_add_task,
)
tsk_remove_btn = tk.Button(
    tsk_frame,
    text="Remove task",
    font=("Helvetica", "16"),
    height=1,
    width=7,
    borderwidth=0,
    bg="white",
    command=show_remove_task,
)
tsk_edit_btn = tk.Button(
    tsk_frame,
    text="Edit task",
    font=("Helvetica", "16"),
    height=1,
    width=7,
    borderwidth=0,
    bg="white",
)
add_button_task = tk.Button(
    tsk_frame,
    bg="white",
    text="Add Task",
    font=("Helvetica", "16"),
    height=1,
    width=7,
    borderwidth=0,
    command=save_task,
)
clear_button_task = tk.Button(
    tsk_frame,
    bg="white",
    text="Clear",
    font=("Helvetica", "16"),
    height=1,
    width=7,
    borderwidth=0,
    command=clear_entry_task,
)


tsk_name_add = tk.Label(
    tsk_frame,
    text="Task name:",
    font=("Helvetica", "16"),
    fg="black",
    bg="white",
)
tsk_sub_add = tk.Label(
    tsk_frame,
    text="Task subject:",
    font=("Helvetica", "16"),
    fg="black",
    bg="white",
)
tsk_due_add = tk.Label(
    tsk_frame,
    text="Due date:",
    font=("Helvetica", "16"),
    fg="black",
    bg="white",
)
tsk_det_add = tk.Label(
    tsk_frame,
    text="Task details:",
    font=("Helvetica", "16"),
    fg="black",
    bg="white",
)

tsk_addsuccess_label = tk.Label(
    tsk_frame,
    text="Task added successfully.",
    font=("Helvetica", "16"),
    fg="green",
    bg="white",
)

tsk_invalid_label = tk.Label(
    tsk_frame,
    text="Please fill in all fields!",
    font=("Helvetica", "18"),
    fg="red",
    bg="white",
)

name_entry_add = tk.Entry(tsk_frame, width=75, bg="white", borderwidth=1, fg="black")
sub_entry_add = tk.Entry(tsk_frame, width=75, bg="white", borderwidth=1, fg="black")
date_entry_add = tk.Entry(tsk_frame, width=75, bg="white", borderwidth=1, fg="black")
det_entry_add = tk.Text(tsk_frame, width=96, bg="white", borderwidth=1, fg="black")


# HIDE ----------------------------------------------------------------------------------------------------------------
def hide_task():
    name_entry_add.place_forget()
    sub_entry_add.place_forget()
    date_entry_add.place_forget()
    det_entry_add.place_forget()

    tsk_name_add.place_forget()
    tsk_sub_add.place_forget()
    tsk_due_add.place_forget()
    tsk_det_add.place_forget()

    clear_button_task.place_forget()
    add_button_task.place_forget()
    tsk_del_frame.place_forget()


def hide():
    db_frame.place_forget()
    tsk_frame.place_forget()
    prj_frame.place_forget()
    ass_frame.place_forget()


hidebutton = tk.Button(root, text="Hide", command=hide)
hidebutton.place(x=10, y=500)

dashboard()
show_db()

if tasks_list == []:
    db_notasks.place(x=100, y=50)
else:
    db_notasks.place_forget()

root.mainloop()
