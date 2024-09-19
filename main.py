from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    ## each has been redone with list comprehension
    # password_list = []
    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    blank = False
    if website == '' or email == '' or password == '':
        blank = True

    if blank:
        messagebox.showinfo(title="Missing Fields", message="Make sure no fields are missing")
        return

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail {email} \nPassword: {password} \nIs it ok to save?')

    if is_ok:
        with open('my-passwords.txt', 'a') as f:
            f.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Saver')
window.config(pady=40, padx=40)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_l = Label(text='Website:')
web_l.grid(row=1, column=0)

email_l = Label(text='Email/Username:')
email_l.grid(row=2, column=0)

pass_l = Label(text='Password:')
pass_l.grid(row=3, column=0)

web_entry = Entry(text="Website", width=39)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(text="Email", width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'test@gmail.com')

pass_entry = Entry(text="Password", width=21)
pass_entry.grid(row=3, column=1)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
