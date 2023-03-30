import tkinter as tk
from tkinter import ttk
import backend
import database

def add_expense():
    category_id = int(category_var.get())
    description = description_entry.get()
    amount = float(amount_entry.get())
    date = date_entry.get()
    backend.add_expense(category_id, description, amount, date)
    update_expenses()

def update_expenses():
    expenses_list.delete(0, tk.END)
    for expense in backend.view_expenses():
        expenses_list.insert(tk.END, expense)

def fill_categories():
    for category in backend.get_categories():
        category_dropdown['values'] = (*category_dropdown['values'], category)

database.initialize_db()
root = tk.Tk()
root.title("Expense Tracker")

# UI components
description_label = ttk.Label(root, text="Description:")
description_label.grid(row=0, column=0)
description_entry = ttk.Entry(root)
description_entry.grid(row=0, column=1)

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=1, column=0)
amount_entry = ttk.Entry(root)
amount_entry.grid(row=1, column=1)

category_label = ttk.Label(root, text="Category:")
category_label.grid(row=2, column=0)
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(root, textvariable=category_var)
category_dropdown.grid(row=2, column=1)

date_label = ttk.Label(root, text="Date:")
date_label.grid(row=3, column=0)
date_entry = ttk.Entry(root)
date_entry.grid(row=3, column=1)

add_button = ttk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=4, column=1)

expenses_list = tk.Listbox(root, height=10, width=50)
expenses_list.grid(row=5, column=0, columnspan=2)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=expenses_list.yview)
scrollbar.grid(row=5, column=2, sticky="ns")
expenses_list.configure(yscrollcommand=scrollbar.set)

# Fill categories and update expenses
fill_categories()
update_expenses()

root.mainloop()

