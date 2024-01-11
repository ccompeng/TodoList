from tkinter import *

todo_list = list()


# saves entered tasks to file
def save_data():
    with open('todo_list.txt', 'w') as file:
        for task in todo_list:
            file.write('{}\n'.format(task))

        file.close()


# get the data from data file
def get_data():
    with open('todo_list.txt', 'r') as file:
        for line in file.readlines():
            todo_list.append(line.rstrip())

        file.close()


# dsiplays tasks on the screen
def display_todos():
    listbox.delete(0, END)

    for todo in todo_list:
        listbox.insert('end', todo)


# add the data in the list
def add_todo():
    if entry_todo.get() != '':
        todo_list.append(entry_todo.get())
        warning_label.configure(text='', bg='white')
        entry_todo.delete(0, 'end')

        display_todos()
    else:
        warning_label.configure(text='input field is required!', bg='red', fg='white', font=font_tuple_bold)


# warning before deleting
def delete_warning():
    todo = listbox.get('active')

    warning_label.configure(text=(todo + ' \nwill deleted. Are you sure?'), bg='red', fg='white', font=font_tuple_bold)
    delete_button.place(relx=0.64, rely=0.09)
    cancel_button.place(relx=0.8, rely=0.09)


# delete selected tasks
def delete_todo():
    deleted = listbox.get('active')

    if deleted in todo_list:
        todo_list.remove(deleted)

    warning_label.configure(text='', bg='white')
    delete_button.place(relx=1, rely=1)
    cancel_button.place(relx=1, rely=1)

    display_todos()


# cancel the deleting
def cancel_btn_func():
    warning_label.configure(text='', bg='white')
    delete_button.place(relx=1, rely=1)
    cancel_button.place(relx=1, rely=1)


# tuples for fonts
font_tuple_regular = ('Monospace', 12)
font_tuple_bold = ('Monospace', 12, 'bold')


if __name__ == '__main__':
    root = Tk()
    root.geometry('480x600')
    root.title('ToDo App')
    root.resizable(False, False)
    root.configure(bg='white')

    title_label = Label(root)
    title_label.configure(text='ToDO List', bg='white', fg='black', font=font_tuple_bold)
    entry_todo = Entry(root, bd=8, width=36, fg='black', bg='#EDE4F3', font=font_tuple_regular, relief=FLAT)
    warning_label = Label(root)
    warning_label.configure(text='', bg='white')
    submit_button = Button(
        root,
        bd=3,
        bg='green',
        fg='white',
        font=font_tuple_regular,
        text='Add +',
        width=8,
        height=1,
        command=add_todo
    )
    listbox = Listbox(
        root,
        bg='#EDE4F3',
        font=font_tuple_regular,
        width=48,
        height=20,
        bd=0,
        selectmode=SINGLE,
        relief=FLAT
    )
    delete_warning_btn = Button(
        root,
        text='Delete Selected',
        bg='red',
        fg='white',
        font=font_tuple_bold,
        command=delete_warning
    )
    delete_button = Button(
        root,
        text='Delete',
        bg='red',
        fg='white',
        font=font_tuple_bold,
        command=delete_todo
    )
    cancel_button = Button(
        root,
        text='Exit',
        bg='green',
        fg='white',
        font=font_tuple_bold,
        command=cancel_btn_func
    )

    entry_todo.place(relx=0.05, rely=0.01)
    submit_button.place(relx=0.78, rely=0.01)
    warning_label.place(relx=0.05, rely=0.08)
    title_label.place(relx=0.05, rely=0.14)
    listbox.place(relx=0.05, rely=0.2)
    delete_warning_btn.place(relx=0.05, rely=0.9)

    get_data()
    display_todos()

    root.mainloop()

    if root.destroy:
        save_data()
