from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
import json
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def serach():
    try:
        with open("Password generator\passwords.json","r") as data_file:
            #read old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR",message=f"File doesn't exist.")
    else:
        website = website_input.get()
        if len(website) > 0:
            if website in data:
                data_found = data[website]
                email = data_found["Email"]
                password = data_found["Password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
               
            else:
                messagebox.showerror(title="ERROR",message=f"No data found for {website}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password = []
    password += [random.choice(letters) for _ in range(nr_letters)]
    password += [random.choice(symbols) for _ in range(nr_symbols)]
    password += [random.choice(numbers) for _ in range(nr_numbers)]


    random.shuffle(password)
    new_password = "".join(password)

    password_input.insert(0,new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data =  {
        website:{
            "Email":email,
            "Password": password
        }
    }

    if len(password) > 0 or len(website) > 0:
        try:
            with open("Password generator\passwords.json","r") as data_file:
                #read old data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("Password generator\passwords.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        
        else:
            #update data
            data.update(new_data)
        
            with open("Password generator\passwords.json","w") as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
            
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
            
        # with open("Password generator\password.txt",mode="a") as file:
        #     file.write(f"{website} | {email} | {password}\n")
        #     website_input.delete(0,END)
        #     password_input.delete(0,END)
    else:
        messagebox.showwarning("Warning","Please don't leave any fields empty!!!")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

#logo
canvas = Canvas(height=200,width=200,highlightthickness=0)
logo_img = PhotoImage(file="Password Generator\logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row=0,column=1)


#website field
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_input = Entry(width=31)
website_input.grid(row=1,column=1,sticky="EW")
website_input.focus()

#search button
search_button = Button(text="Search",command=serach)
search_button.grid(row=1,column=2,sticky="EW")

#email feild
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_input = Entry(width=31)
email_input.grid(row=2,column=1,columnspan=2,sticky="EW")
email_input.insert(END,"ishitagupta932@gmail.com")

#password feild
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_input = Entry()
password_input.grid(row=3,column=1,sticky="EW")

password_generate_button = Button(text="Generate Password",command=generate_password)
password_generate_button.grid(row=3,column=2,sticky="EW")


#add button
add_button = Button(text = "Add",width=31,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")

window.mainloop()