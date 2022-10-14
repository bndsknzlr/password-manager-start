from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, "end")

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_address = website_entry.get()
    email_input = mail_entry.get()
    password_input = password_entry.get()
    new_data = {
        web_address: {
            "email": email_input,
            "password": password_input,

        }
    }
    if web_address == "" or email_input == "" or password_input == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # updating data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, "end")
            website_entry.delete(0, "end")
            mail_entry.delete(0, "end")
            mail_entry.insert(0, "a.supertyp@gmx.com")


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #

def search_password():
    search_term = website_entry.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    result = data[search_term]
    messagebox.showwarning(title=f"{search_term}", message=f"Email: {result['email']}\nPassword: {result['password']}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# create labels

l1 = Label(text="Website:")
l1.grid(column=0, row=1)

l2 = Label(text="Email/Username:")
l2.grid(column=0, row=2)

l3 = Label(text="Password:")
l3.grid(column=0, row=3)

# create entry-boxes

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2, sticky=W)
mail_entry.insert(0, "a.supertyp@gmx.com")

# create buttons

create_password_button = Button(text="create password", width=10, command=generate_password)
create_password_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

search_button = Button(text="Search", width=10, command=search_password)
search_button.grid(row=1, column=2, sticky=W)

window.mainloop()
