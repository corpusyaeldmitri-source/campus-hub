import tkinter as tk

root = tk.Tk()

root.geometry("1000x650")
root.title("Campus Hub")

CH_header = tk.Label(root, text="Campus Hub", font=("Helvetica", "24"))
CH_header.place(x=15, y=5)

root.mainloop()