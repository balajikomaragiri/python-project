import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        messagebox.showinfo("Success", f"Contact {name} added successfully.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact {name} removed successfully.")
        else:
            messagebox.showerror("Error", f"Contact {name} not found.")

    def search_contact(self, name):
        if name in self.contacts:
            messagebox.showinfo("Contact Found", f"Name: {name}, Phone Number: {self.contacts[name]}")
        else:
            messagebox.showerror("Error", f"Contact {name} not found.")

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            messagebox.showinfo("Success", f"Contact {name} updated successfully.")
        else:
            messagebox.showerror("Error", f"Contact {name} not found.")

    def display_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"Name: {name}, Phone Number: {phone_number}" for name, phone_number in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

def add_contact_window():
    def add_contact():
        name = name_entry.get()
        phone_number = phone_entry.get()
        contact_book.add_contact(name, phone_number)
        add_contact_window.destroy()

    add_contact_window = tk.Toplevel(root)
    add_contact_window.title("Add Contact")

    name_label = tk.Label(add_contact_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(add_contact_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    phone_label = tk.Label(add_contact_window, text="Phone Number:")
    phone_label.grid(row=1, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(add_contact_window)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    add_button = tk.Button(add_contact_window, text="Add", command=add_contact)
    add_button.grid(row=2, columnspan=2, padx=5, pady=5)

def remove_contact_window():
    def remove_contact():
        name = name_entry.get()
        contact_book.remove_contact(name)
        remove_contact_window.destroy()

    remove_contact_window = tk.Toplevel(root)
    remove_contact_window.title("Remove Contact")

    name_label = tk.Label(remove_contact_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(remove_contact_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    remove_button = tk.Button(remove_contact_window, text="Remove", command=remove_contact)
    remove_button.grid(row=1, columnspan=2, padx=5, pady=5)

def search_contact_window():
    def search_contact():
        name = name_entry.get()
        contact_book.search_contact(name)
        search_contact_window.destroy()

    search_contact_window = tk.Toplevel(root)
    search_contact_window.title("Search Contact")

    name_label = tk.Label(search_contact_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(search_contact_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    search_button = tk.Button(search_contact_window, text="Search", command=search_contact)
    search_button.grid(row=1, columnspan=2, padx=5, pady=5)

def display_contacts():
    contact_book.display_contacts()

root = tk.Tk()
root.title("Contact Book")

contact_book = ContactBook()

add_button = tk.Button(root, text="Add Contact", command=add_contact_window)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Contact", command=remove_contact_window)
remove_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact_window)
search_button.pack(pady=5)

display_button = tk.Button(root, text="Display Contacts", command=display_contacts)
display_button.pack(pady=5)

root.mainloop()
