import sqlite3
from backend import Database
import sys
from tkinter import *

database = Database("Libriary.db")


def get_selected_row(event):
    global selected_tuple
    index = list_widget.curselection()[0]
    selected_tuple = list_widget.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    list_widget.delete(0, END)
    for row in database.view():
        list_widget.insert(END, row)


def search_command():
    list_widget.delete(0, END)
    for row in database.search(tf_title.get(), tf_author.get(), tf_year.get(), tf_isbn.get()):
        list_widget.insert(END, row)


def insert_command():
    database.insert(tf_title.get(), tf_author.get(), tf_year.get(), tf_isbn.get())
    list_widget.delete(0, END)
    list_widget.insert(END, (tf_title.get(), tf_author.get(), tf_year.get(), tf_isbn.get()))
    view_command()


def delete_command():
    database.delete(selected_tuple[0])
    view_command()


def update_command():
    database.update(selected_tuple[0], tf_title.get(), tf_author.get(), tf_year.get(), tf_isbn.get())
    view_command()


def close_command():
    sys.exit()


def clear_command():
    database.clear()
    view_command()


window = Tk()
window.wm_title("BookStore")

title = Label(window, text="Title")
year = Label(window, text="Year")
author = Label(window, text="Author")
isbn = Label(window, text="ISBN")
title.grid(row=0, column=0)
year.grid(row=0, column=2)
author.grid(row=1, column=0)
isbn.grid(row=1, column=2)

tf_title = StringVar()
tf_year = StringVar()
tf_author = StringVar()
tf_isbn = StringVar()
e1 = Entry(window, textvariable=tf_title)
e2 = Entry(window, textvariable=tf_year)
e3 = Entry(window, textvariable=tf_author)
e4 = Entry(window, textvariable=tf_isbn)
e1.grid(row=0, column=1)
e2.grid(row=0, column=3)
e3.grid(row=1, column=1)
e4.grid(row=1, column=3)

list_widget = Listbox(window)
list_widget.grid(row=2, column=1, rowspan=7, columnspan=1)
list_widget.bind("<<ListboxSelect>>", get_selected_row)

view_all = Button(window, text="View all", width=12, command=view_command)
search_entry = Button(window, text="Search entry", width=12, command=search_command)
add_entry = Button(window, text="Add entry", width=12, command=insert_command)
_update = Button(window, text="Update", width=12, command=update_command)
_delete = Button(window, text="Delete", width=12, command=delete_command)
_drop = Button(window, text="Clear", width=12, command=clear_command)
_close = Button(window, text="Close", width=12, command=close_command)
view_all.grid(row=2, column=3)
search_entry.grid(row=3, column=3)
add_entry.grid(row=4, column=3)
_update.grid(row=5, column=3)
_delete.grid(row=6, column=3)
_close.grid(row=7, column=3)
_drop.grid(row=8, column=3)

scroll = Scrollbar(window, width=20)
scroll.grid(row=2, column=2, rowspan=6)

window.mainloop()
