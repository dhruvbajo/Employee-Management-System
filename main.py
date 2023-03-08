from tkinter import *
from tkinter import messagebox
import pandas


# Saving Data
def save():
    name = name_input.get()
    gender = radio_state.get()
    mobile = mobile_input.get()
    address = address_input.get()
    id = id_input.get()
    dob = dob_input.get()
    age = age_input.get()
    email = email_input.get()

    if len(name) == 0 or len(address) == 0 or len(id) == 0 or len(dob) == 0 or len(age) == 0:
        messagebox.showinfo(title="Oops!", message="Please make Sure You Didn't Leave Any Box Empty!")
    elif len(mobile) != 10:
        messagebox.showinfo(title="Oops!", message="Please enter the correct 10 digit mobile no.")
    else:
        is_ok = messagebox.askokcancel(title="INFO", message=f"These are the details entered:\nname:{name}\n"
                                                             f"gender:{gender}\nmobile:{mobile}\naddress:{address}\n"
                                                             f"id no.:{id}\ndob:{dob}\nage:{age}\nemail:{email}"
                                                             f"\nIs it okay to save?")
        if is_ok:
            with open("data.csv", "a") as data_file:
                data_file.write(f"{name},{gender},{mobile},{address},{id},{dob},{age},{email}\n")
                name_input.delete(0, END)
                mobile_input.delete(0, END)
                address_input.delete(0, END)
                id_input.delete(0, END)
                dob_input.delete(0, END)
                age_input.delete(0, END)
                email_input.delete(0, END)
                messagebox.showinfo(title="added", message="The employee has been added to the database")


# gui setup
window = Tk()
window.title("Employee Management System")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="download.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

employee_label = Label(text="EMPLOYEE MANAGEMENT SYSTEM", font=("arial", 12, "bold"))
employee_label.grid(column=1, row=1, pady=25)

name_label = Label(text="Name:")
name_label.grid(column=0, row=2, pady=10)

gender_label = Label(text="Gender:")
gender_label.grid(column=0, row=3, pady=10)

mobile_label = Label(text="Mobile No.:")
mobile_label.grid(column=0, row=4, pady=10)

address_label = Label(text="Address:")
address_label.grid(column=0, row=5, pady=10)

id_label = Label(text="ID No.:")
id_label.grid(column=0, row=6, pady=10)

dob_label = Label(text="Date Of Birth:")
dob_label.grid(column=0, row=7, pady=10)

age_label = Label(text="Age:")
age_label.grid(column=0, row=8, pady=10)

email_label = Label(text="Email:")
email_label.grid(column=0, row=9, pady=10)

name_input = Entry(width=50)
name_input.grid(column=1, row=2, columnspan=2)
name_input.focus()

radio_state = StringVar()
radio_state.set(None)
male = Radiobutton(text="Male", value="Male", variable=radio_state)
male.grid(column=1, row=3)
female = Radiobutton(text="Female", value="Female", variable=radio_state)
female.grid(column=2, row=3)

mobile_input = Entry(width=50)
mobile_input.grid(column=1, row=4, columnspan=2)

address_input = Entry(width=50)
address_input.grid(column=1, row=5, columnspan=2)

id_input = Entry(width=50)
id_input.grid(column=1, row=6, columnspan=2)

dob_input = Entry(width=50)
dob_input.grid(column=1, row=7, columnspan=2)

age_input = Entry(width=50)
age_input.grid(column=1, row=8, columnspan=2)

email_input = Entry(width=50)
email_input.grid(column=1, row=9, columnspan=2)

add = Button(text="ADD", width=30, command=save)
add.grid(column=1, row=10, pady=20)

window.mainloop()
print(pandas.read_csv("data.csv"))
