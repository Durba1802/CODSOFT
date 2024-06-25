import tkinter as tk
from tkinter import messagebox

tasks = []

def create_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        updated_task = task_entry.get()
        if updated_task:
            tasks[selected_task_index] = updated_task
            update_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

def track_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        # Implement tracking logic here (for example, updating task status)
        tasks[selected_task_index] += " (tracked)"  # Placeholder for tracking action
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to track!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def main():
    global root
    root = tk.Tk()
    root.title("To-Do List App")
    
    # Task Entry
    global task_entry
    task_entry = tk.Entry(root, width=50)
    task_entry.pack(pady=10)
    
    # Buttons
    create_button = tk.Button(root, text="Create Task", width=20, command=create_task)
    create_button.pack(pady=5)
    
    update_button = tk.Button(root, text="Update Task", width=20, command=update_task)
    update_button.pack(pady=5)
    
    track_button = tk.Button(root, text="Track Task", width=20, command=track_task)
    track_button.pack(pady=5)
    
    # Task Listbox
    global task_listbox
    task_listbox = tk.Listbox(root, width=50)
    task_listbox.pack(padx=10, pady=10)
    
    # Initialize the listbox with any existing tasks
    update_listbox()
    
    root.mainloop()

if __name__ == "__main__":
    main()