from tkinter import *

def add_task():
    task = task_entry.get()
    if task != '':
        task_list.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    task_list.delete(ANCHOR)

def clear_list():
    task_list.delete(0, END)

root = Tk()
root.title('To-Do List App')

task_frame = Frame(root)
task_frame.pack()

task_scroll = Scrollbar(task_frame)
task_scroll.pack(side=RIGHT, fill=Y)

task_list = Listbox(task_frame, height=10, width=50, yscrollcommand=task_scroll.set)
task_list.pack(side=LEFT, fill=BOTH)

task_scroll.config(command=task_list.yview)

task_entry = Entry(root, width=50)
task_entry.pack()

add_button = Button(root, text='Add Task', command=add_task)
add_button.pack()

delete_button = Button(root, text='Delete Task', command=delete_task)
delete_button.pack()

clear_button = Button(root, text='Clear List', command=clear_list)
clear_button.pack()

root.mainloop()