"""
A program that stores book information:
Title, Author,
Year, ISBN


The user can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import functions

def get_selected_row(event):
    try:
        global selected_tuple
        index = list.curselection()[0]
        selected_tuple = list.get(index)

        entry_titile.delete(0,END)
        entry_titile.insert(END, selected_tuple[1])
        entry_author.delete(0,END)
        entry_author.insert(END, selected_tuple[2])
        entry_year.delete(0,END)
        entry_year.insert(END, selected_tuple[3])
        entry_isbn.delete(0,END)
        entry_isbn.insert(END, selected_tuple[4])
    except IndexError:
        pass

    
def view_all_command():
    list.delete(0, END)
    for row in functions.view_all():
        list.insert(END, row)

def search_command():
        list.delete(0, END)
        for row in functions.search(titile_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            list.insert(END, row)

def add_command():
    functions.insert(titile_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list.delete(0, END)
    list.insert(END, (titile_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    functions.delete(selected_tuple[0])

def update_command():
    functions.update(selected_tuple[0],titile_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()

window.title("Book Library")
functions.connect()

title_label = Label(window, text='Title')
title_label.grid(row=0,column=0)
titile_text = StringVar()
entry_titile = Entry(window, textvariable=titile_text)
entry_titile.grid(row=0,column=1)

author_label = Label(window, text='Author')
author_label.grid(row=0,column=2)
author_text = StringVar()
entry_author = Entry(window, textvariable=author_text)
entry_author.grid(row=0,column=3)

year_label = Label(window, text='Year')
year_label.grid(row=1,column=0)
year_text = StringVar()
entry_year = Entry(window, textvariable=year_text)
entry_year.grid(row=1,column=1)

isbn_label = Label(window, text='ISBN')
isbn_label.grid(row=1,column=2)
isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1,column=3)

viewall_button = Button(window, text="View all", width=12, command=view_all_command)
viewall_button.grid(row=3, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=4, column=3)

add_button = Button(window, text="Add entry", width=12, command=add_command)
add_button.grid(row=5, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=6, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=7, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=8, column=3)

list = Listbox(window, height=8, width=35)
list.grid(row=2, column=0, rowspan=7, columnspan=2)

scb = Scrollbar(window)
scb.grid(row=3, column=2, rowspan=6)

list.configure(yscrollcommand=scb.set)
scb.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)
window.mainloop()