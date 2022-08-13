from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


root = Tk()
root.title("StrongPass")
root.iconbitmap("assets/password.ico")
root.geometry("500x500")


# CREATE FRAME
main_frame = Frame(root, width=480, height=480)
main_frame.pack(fill="both", expand=1)

# WEBSITE
website_frame = LabelFrame(main_frame, text="Website")
website_frame.pack(pady=20)

website_entry = Entry(website_frame, font=("Helvetica", 24))
website_entry.pack(padx=10, pady=10)

# HOW LONG?
size_frame = LabelFrame(main_frame, text="How long will it be?")
size_frame.pack(pady=20)

size_scale = Scale(size_frame, from_=8, to=16, orient="horizontal", length=300)
size_scale.pack(padx=10, pady=10)

# CREATE PASSWORD BUTTON AND FUNCTION
def create_pass():
    # check for filled fields
    if not website_entry.get():
        messagebox.showwarning("WARNING!", "What is the purpose of this password? Fill all fields")
    else:
        # clear created box
        created_entry.delete(0, END)
        created_frame.config(text=f"Your password for {website_entry.get().title()}")
        
        password = ""
        alphabet = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890!$@%"
        password_length = int(size_scale.get())

        for _ in range(password_length):
            password += random.choice(alphabet)

        created_entry.insert(0, password)

def copy_to():
    root.clipboard_clear()
    root.clipboard_append(created_entry.get())


create_button = Button(main_frame, text="Create password", command=create_pass).pack(padx=10)

# CREATE DISPLAY TO SHOW PASSWORD
created_frame = LabelFrame(main_frame, text="Your password")
created_frame.pack(pady=20)

created_entry = Entry(created_frame, font=("Helvetica", 24), bd=0, bg="systembuttonface")
created_entry.pack(padx=10, pady=10)

clipboard_button = Button(main_frame, text="Copy", command=copy_to).pack(padx=10)

root.mainloop()