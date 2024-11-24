import tkinter as tk
from tkinter import messagebox, ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x600")
        self.root.configure(bg="#e0e0e0")
        
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=10, background="white", foreground="black")
        self.style.map("TButton", 
                       foreground=[("active", "#ffffff"), ("disabled", "#d9d9d9")],
                       background=[("active", "#45a049")])
        
        # Title
        title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#e0e0e0", fg="#333333")
        title_label.pack(pady=10)
        
        # Entry box for new tasks
        self.task_entry = tk.Entry(root, font=("Helvetica", 12), width=35, bd=2, relief=tk.GROOVE, fg="#333333", bg="#ffffff")
        self.task_entry.pack(pady=10)
        
        # Add task button
        add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), height=15, width=35, bd=2, relief=tk.GROOVE, selectbackground="#a6a6a6", fg="#333333", bg="#ffffff")
        self.task_listbox.pack(pady=10)
        
        # Delete task button
        delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)
        
        # Clear all tasks button
        clear_button = ttk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
