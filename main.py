from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c'
               ,'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*','(',')','+','-','/']

    nl = 6
    nn = 4
    ns = 2

    pass1 = ""
    for i in range(1 , (nl+1)):
        A = random.choice(letters)
        pass1+=A
    for i in range(1,nn+1):
        B = random.choice(numbers)
        pass1+=B
    for i in range(1,ns+1):
        C = random.choice(symbols)
        pass1+=C
    password_entry.insert(0,pass1)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n"
                                                 f"Email:{email} \nPassword:{password} \n It is ok to save?")
    if is_ok:
        with open("data.txt","a") as data_file:
            data_file.write(f"{website} |{email} | {password}\n")
            website_entry.delete(0,END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

button = Button
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label =Label(text="Email Address:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)


gpb = Button(text="Generate Password",command=pass_gen)
gpb.grid(row=3, column=2)
addb = Button(text="Add",width=36,command=save)
addb.grid(row=4,column=1,columnspan=2)

window.mainloop()