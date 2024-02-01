import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1:3306", # or the hostname of your database server
    user="root", # your database username
    password="Pinguspikey1!", # your database password
    database="PasswordManager" # the name of the database you want to connect to
    )

mycursor = mydb.cursor()

def show_frame1():
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack()

def show_frame2():
    frame1.pack_forget()
    frame3.pack_forget()
    frame2.pack()

def show_frame3():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack()

#window
window = tk.Tk() #window block
window.title("Login") #tab name
window.geometry('350x350')
window.configure(bg="black")

frame1 = tk.Frame(bg="black") #tkinter container 
frame2 = tk.Frame(bg="black") #tkinter container 
frame3 = tk.Frame(bg="black") #tkinter container 

#creaing widgets frame1
label = tk.Label(frame1, text="Login", bg="black", fg="#FF0077", font=("Arial", 30))
username = tk.Label(frame1, text="Username", bg="black", fg="white", font=("Arial", 16))
user_entry = tk.Entry(frame1, font=("Arial", 16))
password = tk.Label(frame1, text="Password", bg="black", fg="white", font=("Arial", 16))
password_entry = tk.Entry(frame1, show="*", font=("Arial", 16))
login_button = tk.Button(frame1, text="Login", bg="#FF0077", fg="white", font=("Arial", 16), command=show_frame2)
new_user_button = tk.Button(frame1, text="New User", bg="#FF0077", fg="white", font=("Arial", 16), command=show_frame3)

#creaing widgets frame2 (Login)
logged_in = tk.Label(frame2, text="Logged In", bg="black", fg="#FF0077", font=("Arial", 30))
back_button1 = tk.Button(frame2, text="Back", bg="#FF0077", fg="white", font=("Arial", 16), command=show_frame1)

#creaing widgets frame3 (Register)
register = tk.Label(frame3, text="Register", bg="black", fg="#FF0077", font=("Arial", 30))
first_name = tk.Label(frame3, text="First Name", bg="black", fg="white", font=("Arial", 16))
first_name_entry = tk.Entry(frame3, font=("Arial", 16))
last_name = tk.Label(frame3, text="Last Name", bg="black", fg="white", font=("Arial", 16))
last_name_entry = tk.Entry(frame3, font=("Arial", 16))
username_2 = tk.Label(frame3, text="Username", bg="black", fg="white", font=("Arial", 16))
user_entry_2 = tk.Entry(frame3, font=("Arial", 16))
password_2 = tk.Label(frame3, text="Password", bg="black", fg="white", font=("Arial", 16))
password_entry_2 = tk.Entry(frame3, show="*", font=("Arial", 16))
email_address = tk.Label(frame3, text="Email Address", bg="black", fg="white", font=("Arial", 16))
email_address_entry = tk.Entry(frame3, font=("Arial", 16))
birthdate = tk.Label(frame3, text="Birthday", bg="black", fg="white", font=("Arial", 16))
birthdate_entry = tk.Entry(frame3, font=("Arial", 16))
back_button2 = tk.Button(frame3, text="Back", bg="#FF0077", fg="white", font=("Arial", 16), command=show_frame1)

#placing widgets frame1
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) #this is geometry placer. there are pack, place, & grid.
username.grid(row=1, column=0)
user_entry.grid(row=1, column=1, pady=10)
password.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=15)
new_user_button.grid(row=4, column=0, columnspan=2)

#placing widgets frame2 (Logged in)
logged_in.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
back_button1.grid(row=4, column=0, columnspan=2)

#placing widgets frame3 (Register)
register.grid(row=0, column=0, columnspan=4, sticky="news", pady=40)
first_name.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1, padx=5)
last_name.grid(row=1, column=2)
last_name_entry.grid(row=1, column=3, padx=5)
username_2.grid(row=2, column=0)
user_entry_2.grid(row=2, column=1, pady=10)
password_2.grid(row=2, column=2)
password_entry_2.grid(row=2, column=3)
email_address.grid(row=3, column=0)
email_address_entry.grid(row=3, column=1)
birthdate.grid(row=3, column=2)
birthdate_entry.grid(row=3, column=3)
back_button2.grid(row=4, column=0, columnspan=4, pady=15)

frame1.pack()
window.update()
window.mainloop() #this runs it continuosly(loop), making it viewable.