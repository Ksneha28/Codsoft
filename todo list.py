import tkinter as tk

root = tk.Tk()
root.title("TODO LIST APP")
root.geometry("400x400")
frame = tk.Frame()
frame.pack(pady=20)

todolist_label = tk.Label(frame, text="TODO LIST", font=("times",14), bg="green")
todolist_label.grid(row=0, column=2, columnspan=4)

display_field = tk.Entry(frame)
display_field.grid(row=1, column=2, columnspan=4)

listbox = tk.Listbox(frame)
listbox.grid(row=2, column=2, columnspan=4)

#functions to submit, edit, and delete tasks
def submit_task():
    task = display_field.get()
    listbox.insert(tk.END, task)

def edit_task():
    task_index = listbox.curselection()
    if task_index:
        edit_task = display.get()
        if edit_task:
            listbox.delete(task_index)
            listbox.insert(task_index, edit_task)
            display.delete(0, tk.END)
    
def delete_task():
    task_index = listbox.curselection()
    listbox.delete(task_index)

#creating Buttons
submit_button = tk.Button(frame, text="SUBMIT", command=submit_task)
submit_button.grid(row=1, column=6, columnspan=2)

edit_button = tk.Button(frame, text="EDIT", command=edit_task)
edit_button.grid(row=3, column=3, columnspan=2)

delete_button = tk.Button(frame, text="DELETE", command=delete_task)
delete_button.grid(row=4, column=3, columnspan=2)

root.mainloop()
