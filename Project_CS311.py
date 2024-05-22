from tkinter import ttk , messagebox
from tkinter.font import Font
from PIL import Image , ImageTk
import tkinter as tk 
import sqlite3
import datetime
a
# Create function to connect database 
def connection(): 
    global database , cursor
    database = sqlite3.connect("db/login.db")
    cursor = database.cursor()

    # Create the table if it doesn't exist
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT , firstname TEXT , lastname TEXT , age INTEGER , identification INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT , Start_Station TEXT , End_Station TEXT , Cards INTEGER , Prices INTEGER , Date TEXT , Time TEXT , name TEXT , username TEXT , Sky_Train TEXT)')
 
# Define a function to handle the button click event
def submit_no_card():
    # Get the values of the username and password fields
    username = entry_sign_up_username.get()
    password = entry_sign_up_password.get()
    confirm_password = entry_sign_up_confirm_password.get()

    if username == "Username": 
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Username. ❌")

    elif password == "Password":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Password. ❌")

    elif confirm_password == "Confirm Password":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Confirm Password. ❌")

    else:
        if password == confirm_password: 
            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM users WHERE username = ?", [username])
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Skytrain App says :", "Username already exists!")
                login_click()
            else:
                cursor.execute("INSERT INTO users VALUES (?, ? , ? , ? , ? , ?)", (username, password , '' , '' , '' , ''))
                database.commit()
                messagebox.showinfo("Skytrain App says :", "User created successfully. ✅ ")
                login_click()
        else:
            messagebox.showwarning("Skytrain App says :","A Confirm Password is not Correct! Please Try again. ❌")

def submit_with_card():
    username = entry_sign_up_username.get()
    password = entry_sign_up_password.get()
    confirm_password = entry_sign_up_confirm_password.get()

    if username == "Username": 
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Username. ❌")

    elif password == "Password":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Password. ❌")

    elif confirm_password == "Confirm Password":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Confirm Password. ❌")

    else:
        if password == confirm_password: 
            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM users WHERE username = ?", [username])
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Skytrain App says :" , "Username already exists!")
                sign_up_click()
            else:
                cursor.execute("INSERT INTO users VALUES (?, ? , ? , ? , ? , ?)", (username, password , '' , '' , '' , ''))
                database.commit()
                messagebox.showinfo("Skytrain App says :" , "User created successfully! ✅")
                sign_up_with_card()
        else:
            messagebox.showwarning("Skytrain App says :" , "A Confirm Password is not Correct! Please Try again. ❌")

def database_card_member(): 
    global username , name, lastname, age, identification

    try :
        username = entry_sign_up_username.get()
    except NameError:
        username = entry_login_username.get()

    name             = entry_sign_up_name.get()
    lastname         = entry_sign_up_lastname.get()
    age              = entry_sign_up_age.get()
    identification   = entry_sign_up_identification.get()

    if name == "Name":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Name. ❌")

    elif lastname == "Lastname":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Lastname. ❌")

    elif age == "Age":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Age. ❌")

    elif identification == "Identification Card": 
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Identification Card. ❌")

    elif not age.isdigit():
        messagebox.showwarning("Skytrain App says :" , "Please enter your age in numbers! don't add the text. ❌")

    elif not identification.isdigit(): 
        messagebox.showwarning("Skytrain App says :" , "Please enter your identification in numbers! don't add the text. ❌")

    else:
        cursor.execute("SELECT * FROM users WHERE username = ?" , [username])
        result = cursor.fetchall()
        if result: 
            cursor.execute("SELECT * FROM users WHERE identification = ?", [identification])
            result = cursor.fetchall()
            if result: 
                messagebox.showinfo("Skytrain App says :" , "identification already exists!")
            else:
                sql = "UPDATE users SET firstname = ? , lastname = ? , age = ? , identification = ? WHERE username = ?"
                cursor.execute(sql , [name , lastname , age , identification , username])
                database.commit()
                messagebox.showinfo("Skytrain App says :" , "User created to member successfully! ✅")
                adult_card()

def adult_card():    
    try : 
        background_widget_sign_up_card.grid_forget()
        background_right_sign_up_card.grid_forget()
        background_widget_sign_up.grid_forget()
        background_right_sign_up.grid_forget()

    except NameError :
        background_widget_sign_up_card.grid_forget()
        background_right_sign_up_card.grid_forget()

    cursor.execute("SELECT * FROM users WHERE username = ?" , [username])
    result = cursor.fetchall()
                
    background_right_adult = tk.Frame(root , background = "#F2F2F2")
    background_right_adult.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_adult.rowconfigure(0 , weight = 0)
    background_right_adult.rowconfigure(1 , weight = 1)
    background_right_adult.columnconfigure(0 , weight = 5)

    background_right_top_adult = tk.Frame(background_right_adult , background = '#FFFFFF')
    background_right_top_adult.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_adult.rowconfigure(0 , weight = 1)
    background_right_top_adult.columnconfigure(0 , weight = 1)

    background_widget_adult = tk.Frame(root , background = "#FFFFFF")
    background_widget_adult.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_adult.rowconfigure(0 , weight = 0)
    background_widget_adult.rowconfigure(1 , weight = 0)
    background_widget_adult.rowconfigure(2 , weight = 0)
    background_widget_adult.rowconfigure(3 , weight = 0)
    background_widget_adult.rowconfigure(4 , weight = 0)
    background_widget_adult.rowconfigure(5 , weight = 0)
    background_widget_adult.columnconfigure(0 , weight = 1)
    background_widget_adult.columnconfigure(1 , weight = 1)

    if 60 > result[0][4] > 23: 
        text_top = "•  Adult card"
        text_heading = "You get the Adult card for BTS and MRT."
        image_bts_card = image_adult_bts
        image_mrt_card = image_adult_2
        text_discount = "You get discount 0% "
        text_discount_2 = "You get discount 0% "

    elif 23 >= result[0][4] >= 15: 
        text_top = "•  Student card "
        text_heading = "You get the Student card for BTS and MRT."
        image_bts_card = image_student_bts
        image_mrt_card = image_student_3
        text_discount = "You get discount 10%"
        text_discount_2 = "You get discount 10%"

    elif 14 >= result[0][4] >= 0:
        text_top = "•  Kid card "
        text_heading = "You get the Student card for BTS But Child card for MRT."
        image_bts_card = image_dont_have
        image_mrt_card = image_kid_2
        text_discount = "Don't have information"
        text_discount_2 = "You get discount 50%"

    else:
        text_top = "•  Old card"
        text_heading = "You get the old card for BTS and MRT."
        image_bts_card = image_old_bts
        image_mrt_card = image_old_3
        text_discount = "You get discount 50%"
        
        text_discount_2 = "You get discount 50%"

    tk.Label(background_right_top_adult , text = text_top , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_adult , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')
    
    tk.Label(background_widget_adult , text = f"Congratulations! {text_heading}" , background = "#FFFFFF" , font = "Calibri 16 bold" , foreground = '#5E95FF').grid(row = 0 , columnspan = 2 , sticky = 'news' , ipady = 15)
    tk.Label(background_widget_adult , text = f"BTS" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 1 , column = 0 , pady = 5 , padx = 45 , sticky = 'w')
    tk.Label(background_widget_adult , text = f"MRT" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 1 , column = 1 , pady = 5 , padx = 45 , sticky = 'w')
    tk.Label(background_widget_adult , image = image_bts_card , background = "#FFFFFF").grid(row = 2 , column = 0 , sticky = 'news')
    tk.Label(background_widget_adult , image = image_mrt_card , background = "#FFFFFF").grid(row = 2 , column = 1 , sticky = 'news')
    tk.Label(background_widget_adult , text = text_discount , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 3 , column = 0 , sticky = 'news')
    tk.Label(background_widget_adult , text = text_discount_2 , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 3 , column = 1 , sticky = 'news')

    tk.Button(background_widget_adult , image = image_next , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = login_click_2).grid(row = 4 , columnspan = 2 , sticky = 'ns' , pady = 12)

    tk.Label(background_widget_adult , image = image_veg , background = "#FFFFFF").grid(row = 5 , columnspan = 2)


def login_click_2(): 
    login_click()

def submit_login():  
    username = entry_login_username.get()
    password = entry_login_password.get()

    if username == "Username" and password == "Password" :
        messagebox.showwarning("Skytrain App says :","Please Enter your Username or Password. ❌")

    else :
        sql = "select * from users where username = ?;"
        cursor.execute(sql,[username])
        result = cursor.fetchone()

        if result :
            sql = "select * from users where password = ?;"
            cursor.execute(sql,[password])
            result = cursor.fetchone()

            if result :
                messagebox.showinfo("Skytrain App says :","Login Successfully. ✅")
                bts_mrt()
            else :
                if password == 'Password': 
                    messagebox.showwarning("Skytrain App says :","Please Enter Your Password!! ❌")
                else: 
                    messagebox.showwarning("Skytrain App says :","Incorrect Password!! Please try again. ❌ ")
        else :
            messagebox.showwarning("Skytrain App says :" , "Check Username incorrect!! ❌")

def sign_up_member():
    username_login = entry_login_username.get()
    password_login = entry_login_password.get()

    if username_login == "Username": 
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Username. ❌")

    elif password_login == "Password":
        messagebox.showwarning("Skytrain App says :" , f"Please Complete The Password. ❌")

    else :
        sql = "select * from users where username = ?;"
        cursor.execute(sql,[username_login])
        result = cursor.fetchall()
    
        if result :
            sql = "select * from users where username = ? and password = ?;"
            cursor.execute(sql,[username_login,password_login])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Skytrain App says :" , "Username and Password of your Correct! ✅")
                sign_up_with_card()
            else :
                messagebox.showwarning("Skytrain App says :","Incorrect Password \nPlease try again ❌")

# Create function "create_window" to get and create application with tkinter and set background , Font. and set name window "root".
def create_window(): 
    root = tk.Tk()
    root.title("Project CS311 : BTS&MRT BY Warapob&Weerapat")

    image_logo = ImageTk.PhotoImage(file = "image/logo_bts.png")

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 800  # Set the width of the window
    window_height = 650  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2))

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    root.rowconfigure(0 , weight = 0)
    root.rowconfigure(1 , weight = 1)
    root.columnconfigure(0 , weight = 0)
    root.columnconfigure(1 , weight = 1)
    root.option_add("*font" , "Calibri 16 bold")
    root.iconphoto(False , image_logo)
    return root 

def return_menu():
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 800  # Set the width of the window
    window_height = 650  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2))

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    background_right_bts_car.grid_forget()
    background_widget_bts_car.grid_forget()
    background_top_right.grid_forget()

    background_top_left_2 = tk.Frame(root , background = "#2D3237")
    background_top_right_2 = tk.Frame(root , background = "#505254")
    background_left_2 = tk.Frame(root , background = "#4BA5FF")
    background_right_2 = tk.Frame(root , background = "#F2F2F2")
    background_right_top_2 = tk.Frame(background_right , background = '#FFFFFF')
    background_right_bottom_2 = tk.Frame(root , background = "#FFFFFF")

    background_top_left_2.grid(row = 0 , column = 0 , sticky = 'news')
    background_top_left_2.rowconfigure(0 , weight = 0)
    background_top_left_2.columnconfigure(0 , weight = 0)

    # background top right is mean text "S K Y T R A I N - A P P"
    background_top_right_2.grid(row = 0 , column = 1 , sticky = 'news')
    background_top_right_2.rowconfigure(0 , weight = 1)
    background_top_right_2.columnconfigure(0 , weight = 0)
    background_top_right_2.columnconfigure(1 , weight = 0)
    background_top_right_2.columnconfigure(2 , weight = 0)
    background_top_right_2.columnconfigure(3 , weight = 1)
    background_top_right_2.columnconfigure(4 , weight = 0)

    background_left_2.grid(row = 1 , column = 0 , sticky = 'news')
    background_left_2.rowconfigure((0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11) , weight = 1)
    background_left_2.columnconfigure(0 , weight = 1)

    background_right_2.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_2.rowconfigure(0 , weight = 0)
    background_right_2.rowconfigure(1 , weight = 1)
    background_right_2.columnconfigure(0 , weight = 5)

    background_right_top_2.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_2.rowconfigure(0 , weight = 1)
    background_right_top_2.columnconfigure(0 , weight = 1)

    background_right_bottom_2.grid(row = 1 , column = 1 , sticky = 's')
    background_right_bottom_2.rowconfigure(0 , weight = 1)
    background_right_bottom_2.rowconfigure(1 , weight = 1)
    background_right_bottom_2.rowconfigure(2 , weight = 1)
    background_right_bottom_2.rowconfigure(3 , weight = 1)
    background_right_bottom_2.columnconfigure(0 , weight = 1)
    background_right_bottom_2.columnconfigure(1 , weight = 1)

    tk.Label(background_top_left_2 , image = image_open_skylogo , background = "#2D3237").grid(row = 0 , column = 0 , padx = 10)

    tk.Label(background_top_right_2 , text = "• Menu" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipadx = 15)
    tk.Label(background_top_right_2 , text = "• BTS" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 1 , sticky = 'w' , ipadx = 15)
    tk.Label(background_top_right_2 , text = "• MRT" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 2 , sticky = 'w' , ipadx = 15)
    tk.Button(background_top_right_2 , image = image_open_login , background = "#505254" , bd = 0 , activebackground = "#505254" , command = login_click).grid(row = 0 , column = 3 , sticky = 'e' , ipadx = 15)
    tk.Button(background_top_right_2 , image = image_open_sign_up , background = "#505254" , bd = 0 , activebackground = "#505254" , command = sign_up_click).grid(row = 0 , column = 4 , sticky = 'e' , ipadx = 15)

    list_sky_text = ["S" , "K" , "Y" , "T" , "R" , "A" , "I" , "N" , "-" , "A" , "P" , "P"]
    for index , menu in enumerate(list_sky_text): 
        tk.Label(background_left_2 , text = menu , font = bigfont , foreground = "#000000" , background = "#4BA5FF").grid(row = index , column = 0 , pady = 3)

    tk.Label(background_right_top_2 , text = "•  Menu" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_2 , image = image_skytrain , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')
    
    tk.Label(background_right_bottom_2 , image = image_text_you_must_login , background = "#FFFFFF").grid(row = 0 , columnspan = 2 , sticky = 'n' , pady = 23)
    tk.Button(background_right_bottom_2 , image = image_login_one , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = login_click).grid(row = 1 , columnspan = 2 , sticky = 'n' , pady = 15)
    tk.Button(background_right_bottom_2 , image = image_sign_up_one , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = sign_up_click).grid(row = 2 , columnspan = 2 , sticky = 'ns' , pady = 5)
    tk.Label(background_right_bottom_2 , image = image_veg , background = "#FFFFFF").grid(row = 3 , columnspan = 2)
    
# Create function "set_background" to set background (defult) in root.  
def set_background():  
    global background_top_right
    # background top left is mean image logo skytrain app 
    background_top_left.grid(row = 0 , column = 0 , sticky = 'news')
    background_top_left.rowconfigure(0 , weight = 0)
    background_top_left.columnconfigure(0 , weight = 0)

    # background top right is mean text "S K Y T R A I N - A P P"
    background_top_right.grid(row = 0 , column = 1 , sticky = 'news')
    background_top_right.rowconfigure(0 , weight = 1)
    background_top_right.columnconfigure(0 , weight = 0)
    background_top_right.columnconfigure(1 , weight = 0)
    background_top_right.columnconfigure(2 , weight = 0)
    background_top_right.columnconfigure(3 , weight = 1)
    background_top_right.columnconfigure(4 , weight = 0)

    background_left.grid(row = 1 , column = 0 , sticky = 'news')
    background_left.rowconfigure((0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11) , weight = 1)
    background_left.columnconfigure(0 , weight = 1)

    background_right.grid(row = 1 , column = 1 , sticky = 'news')
    background_right.rowconfigure(0 , weight = 0)
    background_right.rowconfigure(1 , weight = 1)
    background_right.columnconfigure(0 , weight = 5)

    background_right_top.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top.rowconfigure(0 , weight = 1)
    background_right_top.columnconfigure(0 , weight = 1)

    background_right_bottom.grid(row = 1 , column = 1 , sticky = 's')
    background_right_bottom.rowconfigure(0 , weight = 1)
    background_right_bottom.rowconfigure(1 , weight = 1)
    background_right_bottom.rowconfigure(2 , weight = 1)
    background_right_bottom.rowconfigure(3 , weight = 1)
    background_right_bottom.columnconfigure(0 , weight = 1)
    background_right_bottom.columnconfigure(1 , weight = 1)

# Create function to add widget in background 
def add_widget_in_background():   
    tk.Label(background_top_left , image = image_open_skylogo , background = "#2D3237").grid(row = 0 , column = 0 , padx = 10)

    tk.Label(background_top_right , text = "• Menu" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipadx = 15)
    tk.Label(background_top_right , text = "• BTS" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 1 , sticky = 'w' , ipadx = 15)
    tk.Label(background_top_right , text = "• MRT" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 2 , sticky = 'w' , ipadx = 15)
    tk.Button(background_top_right , image = image_open_login , background = "#505254" , bd = 0 , activebackground = "#505254" , command = login_click).grid(row = 0 , column = 3 , sticky = 'e' , ipadx = 15)
    tk.Button(background_top_right , image = image_open_sign_up , background = "#505254" , bd = 0 , activebackground = "#505254" , command = sign_up_click).grid(row = 0 , column = 4 , sticky = 'e' , ipadx = 15)

    list_sky_text = ["S" , "K" , "Y" , "T" , "R" , "A" , "I" , "N" , "-" , "A" , "P" , "P"]
    for index , menu in enumerate(list_sky_text): 
        tk.Label(background_left , text = menu , font = bigfont , foreground = "#000000" , background = "#4BA5FF").grid(row = index , column = 0 , pady = 3)

    tk.Label(background_right_top , text = "•  Menu" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right , image = image_skytrain , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')
    
    tk.Label(background_right_bottom , image = image_text_you_must_login , background = "#FFFFFF").grid(row = 0 , columnspan = 2 , sticky = 'n' , pady = 23)
    tk.Button(background_right_bottom , image = image_login_one , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = login_click).grid(row = 1 , columnspan = 2 , sticky = 'n' , pady = 15)
    tk.Button(background_right_bottom , image = image_sign_up_one , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = sign_up_click).grid(row = 2 , columnspan = 2 , sticky = 'ns' , pady = 5)
    tk.Label(background_right_bottom , image = image_veg , background = "#FFFFFF").grid(row = 3 , columnspan = 2)

def login_click(): 
    global entry_login_username , entry_login_password , background_right_login , background_widget_login , button_eye
    background_right.grid_forget()
    background_right_bottom.grid_forget()

    background_right_login = tk.Frame(root , background = "#F2F2F2")
    background_right_login.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_login.rowconfigure(0 , weight = 0)
    background_right_login.rowconfigure(1 , weight = 1)
    background_right_login.columnconfigure(0 , weight = 5)

    background_right_top_login = tk.Frame(background_right_login , background = '#FFFFFF')
    background_right_top_login.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_login.rowconfigure(0 , weight = 1)
    background_right_top_login.columnconfigure(0 , weight = 1)

    background_widget_login = tk.Frame(root , background = "#FFFFFF")
    background_widget_login.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_login.rowconfigure(0 , weight = 0)
    background_widget_login.rowconfigure(1 , weight = 0)
    background_widget_login.rowconfigure(2 , weight = 0)
    background_widget_login.rowconfigure(3 , weight = 0)
    background_widget_login.rowconfigure(4 , weight = 0)
    background_widget_login.rowconfigure(5 , weight = 0)
    background_widget_login.rowconfigure(6 , weight = 0)
    background_widget_login.columnconfigure(0 , weight = 1)
    background_widget_login.columnconfigure(1 , weight = 1)

    tk.Label(background_right_top_login , text = "•  Login" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_login , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')
    
    # tk.Label(background_widget_login , background = "#F2F2F2").grid(row = 0 , column = 0 , sticky = 'news')
    tk.Label(background_widget_login , text = "Login to your Account" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 1 , column = 0 , sticky = 'wn' , padx = 25 , ipady = 15)
    entry_login_username = tk.Entry(background_widget_login , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_login_username.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_login_username.grid(row = 2 , columnspan = 2 , ipady = 3 , pady = 17)
    entry_login_username.insert(0, 'Username')  # insert default text
    entry_login_username.bind('<FocusIn>', entry_click_in_login)  # bind click event
    entry_login_username.bind('<FocusOut>', entry_exit_in_login)  # bind exit event

    entry_login_password = tk.Entry(background_widget_login , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold") , show = '')
    entry_login_password.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_login_password.grid(row = 3 , columnspan = 2 , ipady = 3 , pady = 35)
    entry_login_password.insert(0 , 'Password')
    entry_login_password.bind('<FocusIn>', entry_password_click_in_login)  # bind click event
    entry_login_password.bind('<FocusOut>', entry_password_exit_in_login) # bind exit event
    
    button_eye = tk.Button(background_widget_login , image = image_eye_open , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = eye_show)
    button_eye.grid(row = 3 , column = 1 , sticky = 'ns')

    login_button = tk.Button(background_widget_login , image = image_login_account , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = submit_login)
    login_button.grid(row = 4 , columnspan = 2 , sticky = 'ews' , pady = 5)

    tk.Label(background_widget_login , text = "Don't have a membership card?" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 5 , column = 0 , sticky = 'e' , ipadx = 25 , pady = 35)
    tk.Button(background_widget_login , image = image_sign_up_in_login , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = check_result).grid(row = 5 , column = 1 , sticky = 'w' , padx = 5 , pady = 35)

    tk.Label(background_widget_login , image = image_veg , background = "#FFFFFF").grid(row = 6 , columnspan = 2)

    # Enter Keyborad 
    root.bind('<Return>', lambda event: login_button.invoke())
    
def eye_show(): 
    if entry_login_password.cget('show') == '':
        entry_login_password.config(show = '*')
        button_eye.config(image = image_eye_close)
    else:
        entry_login_password.config(show = '')
        button_eye.config(image = image_eye_open)

def check_result(): 
    username = entry_login_username.get()
    password = entry_login_password.get()

    if username == 'Username' and password == 'Password': 
        messagebox.showwarning("Skytrain App says :" , "Please Enter Your Username and Password! ❌")
    else: 
        sql = "SELECT * FROM users WHERE username = ?;"

        cursor.execute(sql , [username])

        result = cursor.fetchall()

        if result: 
            sql = "SELECT * FROM users WHERE username = ? AND password = ?;"

            cursor.execute(sql , [username , password])

            result = cursor.fetchall()

            if result: 
                if result[0][2] == '' or result[0][3] == '' or result[0][4] == '' or result[0][5] == '': 
                    sign_up_member()
                else: 
                    messagebox.showwarning("Skytrain App says :" , "You have already subscribed to your account.")
            else: 
                if password == 'Password': 
                    messagebox.showwarning("Skytrain App says :" , "Please Enter Your Password") 
                else:
                    messagebox.showwarning("Skytrain App says : " , "Check Password incorrect!")
        else: 
            messagebox.showwarning("Skytrain App says :" , "Check Username incorrect!")

# create 'username' in entry of username 
def entry_click_in_login(event):
    # Function to handle the click event
    if entry_login_username.get() == 'Username':
        entry_login_username.delete(0, tk.END)  # delete all the text in the entry
        entry_login_username.insert(0, '')  # insert blank for user input
        entry_login_username.config(fg='black', font = ('Calibri', 18 , "bold"))

def entry_exit_in_login(event):
    # Function to handle the exit event
    if entry_login_username.get() == '':
        entry_login_username.insert(0, 'Username')  # insert default text
        entry_login_username.config(fg = '#B1B1B1' , font = ('Calibri', 18 , "bold"))  # set text color to grey

# create 'password' in entry of password
def entry_password_click_in_login(event): 
    if entry_login_password.get() == 'Password':
        entry_login_password.delete(0, tk.END)  # delete all the text in the entry
        entry_login_password.insert(0, '')  # insert blank for user input
        entry_login_password.config(fg = 'black', font = ('Calibri', 18 , "bold") , show = '')

def entry_password_exit_in_login(event): 
    if entry_login_password.get() == '': 
        entry_login_password.insert(0 , "Password")
        entry_login_password.config(fg = "#B1B1B1" , font = ('Calibri', 18 , "bold") , show = '')

def sign_up_click(): 
    global entry_sign_up_username , entry_sign_up_password , entry_sign_up_confirm_password , background_widget_sign_up , background_right_sign_up , button_eye_2 , button_eye_3
    background_right.grid_forget()
    background_right_bottom.grid_forget()

    background_right_sign_up = tk.Frame(root , background = "#F2F2F2")
    background_right_sign_up.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_sign_up.rowconfigure(0 , weight = 0)
    background_right_sign_up.rowconfigure(1 , weight = 1)
    background_right_sign_up.columnconfigure(0 , weight = 5)

    background_right_top_sign_up = tk.Frame(background_right_sign_up , background = '#FFFFFF')
    background_right_top_sign_up.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_sign_up.rowconfigure(0 , weight = 1)
    background_right_top_sign_up.columnconfigure(0 , weight = 1)

    background_widget_sign_up = tk.Frame(root , background = "#FFFFFF")
    background_widget_sign_up.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_sign_up.rowconfigure(0 , weight = 0)
    background_widget_sign_up.rowconfigure(1 , weight = 0)
    background_widget_sign_up.rowconfigure(2 , weight = 0)
    background_widget_sign_up.rowconfigure(3 , weight = 0)
    background_widget_sign_up.rowconfigure(4 , weight = 0)
    background_widget_sign_up.rowconfigure(5 , weight = 0)
    background_widget_sign_up.rowconfigure(6 , weight = 0)
    background_widget_sign_up.columnconfigure(0 , weight = 1)
    background_widget_sign_up.columnconfigure(1 , weight = 1)

    tk.Label(background_right_top_sign_up , text = "•  Sign up" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_sign_up , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')
    
    tk.Label(background_widget_sign_up , text = "Create Your Account" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'wn' , padx = 25 , ipady = 15)

    entry_sign_up_username = tk.Entry(background_widget_sign_up , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_username.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_username.grid(row = 1 , columnspan = 2 , ipady = 3)
    entry_sign_up_username.insert(0, 'Username')  # insert default text
    entry_sign_up_username.bind('<FocusIn>', entry_click_sign_up)  # bind click event
    entry_sign_up_username.bind('<FocusOut>', entry_exit_sign_up)  # bind exit event

    entry_sign_up_password = tk.Entry(background_widget_sign_up , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_password.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_password.grid(row = 2 , columnspan = 2 , ipady = 3 , pady = 40)
    entry_sign_up_password.insert(0 , 'Password')
    entry_sign_up_password.bind('<FocusIn>', entry_password_click_sign_up)  # bind click event
    entry_sign_up_password.bind('<FocusOut>', entry_password_exit_sign_up) # bind exit event
    
    entry_sign_up_confirm_password = tk.Entry(background_widget_sign_up , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_confirm_password.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_confirm_password.grid(row = 3 , columnspan = 2 , ipady = 3)
    entry_sign_up_confirm_password.insert(0 , 'Confirm Password')
    entry_sign_up_confirm_password.bind('<FocusIn>', entry_confirm_password_click_sign_up)  # bind click event
    entry_sign_up_confirm_password.bind('<FocusOut>', entry_confirm_password_exit_sign_up) # bind exit event

    button_eye_2 = tk.Button(background_widget_sign_up , image = image_eye_open , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = eye_show_2)
    button_eye_2.place(relx = 0.735 , rely = 0.22)

    button_eye_3 = tk.Button(background_widget_sign_up , image = image_eye_open , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = eye_show_3)
    button_eye_3.place(relx = 0.735 , rely = 0.38)

    tk.Button(background_widget_sign_up , image = image_sign_up_no_card , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = submit_no_card).grid(row = 4 , columnspan = 2 , sticky = 'ns' , pady = 20)
    tk.Button(background_widget_sign_up , image = image_sign_up_with_card , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = submit_with_card).grid(row = 5 , columnspan = 2 , sticky = 'ns')

    tk.Label(background_widget_sign_up , image = image_veg , background = "#FFFFFF").grid(row = 6 , columnspan = 2)

def eye_show_2(): 
    if entry_sign_up_password.cget('show') == '':
        entry_sign_up_password.config(show = '*')
        button_eye_2.config(image = image_eye_close)
    else:
        entry_sign_up_password.config(show = '')
        button_eye_2.config(image = image_eye_open)

def eye_show_3(): 
    if entry_sign_up_confirm_password.cget('show') == '':
        entry_sign_up_confirm_password.config(show = '*')
        button_eye_3.config(image = image_eye_close)
    else:
        entry_sign_up_confirm_password.config(show = '')
        button_eye_3.config(image = image_eye_open)

def entry_click_sign_up(event):
    # Function to handle the click event
    if entry_sign_up_username.get() == 'Username':
        entry_sign_up_username.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_username.insert(0, '')  # insert blank for user input
        entry_sign_up_username.config(fg='black', font = ('Calibri', 18 , "bold"))

def entry_exit_sign_up(event):
    # Function to handle the exit event
    if entry_sign_up_username.get() == '':
        entry_sign_up_username.insert(0, 'Username')  # insert default text
        entry_sign_up_username.config(fg = '#B1B1B1' , font = ('Calibri', 18 , "bold"))  # set text color to grey

# create 'password' in entry of password
def entry_password_click_sign_up(event): 
    if entry_sign_up_password.get() == 'Password':
        entry_sign_up_password.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_password.insert(0, '')  # insert blank for user input
        entry_sign_up_password.config(fg = 'black', font = ('Calibri', 18 , "bold") , show = '')

def entry_password_exit_sign_up(event): 
    if entry_sign_up_password.get() == '': 
        entry_sign_up_password.insert(0 , "Password")
        entry_sign_up_password.config(fg = "#B1B1B1" , font = ('Calibri', 18 , "bold") , show = '')

# create 'confirm password' in entry of 'confirm password' 
def entry_confirm_password_click_sign_up(event): 
    if entry_sign_up_confirm_password.get() == 'Confirm Password':
        entry_sign_up_confirm_password.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_confirm_password.insert(0, '')  # insert blank for user input
        entry_sign_up_confirm_password.config(fg = 'black', font = ('Calibri', 18 , "bold") , show = '')

def entry_confirm_password_exit_sign_up(event): 
    if entry_sign_up_confirm_password.get() == '': 
        entry_sign_up_confirm_password.insert(0 , "Confirm Password")
        entry_sign_up_confirm_password.config(fg = "#B1B1B1" , font = ('Calibri', 18 , "bold") , show = '')

def sign_up_with_card(): 
    global entry_sign_up_name , entry_sign_up_lastname , entry_sign_up_age , entry_sign_up_identification , background_right_sign_up_card , background_widget_sign_up_card
    # background_widget_sign_up.grid_forget()

    background_right_sign_up_card = tk.Frame(root , background = "#F2F2F2")
    background_right_sign_up_card.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_sign_up_card.rowconfigure(0 , weight = 0)
    background_right_sign_up_card.rowconfigure(1 , weight = 5)
    background_right_sign_up_card.columnconfigure(0 , weight = 5)

    background_right_top_sign_up_card = tk.Frame(background_right_sign_up_card , background = '#FFFFFF')
    background_right_top_sign_up_card.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_sign_up_card.rowconfigure(0 , weight = 1)
    background_right_top_sign_up_card.columnconfigure(0 , weight = 1)

    background_widget_sign_up_card = tk.Frame(root , background = "#FFFFFF")
    background_widget_sign_up_card.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_sign_up_card.rowconfigure(0 , weight = 0)
    background_widget_sign_up_card.rowconfigure(1 , weight = 0)
    background_widget_sign_up_card.rowconfigure(2 , weight = 0)
    background_widget_sign_up_card.rowconfigure(3 , weight = 0)
    background_widget_sign_up_card.rowconfigure(4 , weight = 0)
    background_widget_sign_up_card.rowconfigure(5 , weight = 0)
    background_widget_sign_up_card.columnconfigure(0 , weight = 1)
    background_widget_sign_up_card.columnconfigure(1 , weight = 1)

    tk.Label(background_right_top_sign_up_card , text = "•  Sign up with card" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_sign_up_card , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')
    tk.Label(background_widget_sign_up_card , text = "Fill in your information" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'wn' , padx = 25 , pady = 22)

    entry_sign_up_name = tk.Entry(background_widget_sign_up_card , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_name.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_name.grid(row = 1 , columnspan = 2 , ipady = 3)
    entry_sign_up_name.insert(0, 'Name')  # insert default text
    entry_sign_up_name.bind('<FocusIn>', entry_name_click_sign_up_card)  # bind click event
    entry_sign_up_name.bind('<FocusOut>', entry_name_exit_sign_up_card)  # bind exit event

    entry_sign_up_lastname = tk.Entry(background_widget_sign_up_card , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_lastname.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_lastname.grid(row = 2 , columnspan = 2 , ipady = 3 , pady = 35)
    entry_sign_up_lastname.insert(0 , 'Lastname')
    entry_sign_up_lastname.bind('<FocusIn>', entry_lastname_click_sign_up_card)  # bind click event
    entry_sign_up_lastname.bind('<FocusOut>', entry_lastname_exit_sign_up_card) # bind exit event
    
    entry_sign_up_age = tk.Entry(background_widget_sign_up_card , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_age.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_age.grid(row = 3 , columnspan = 2 , ipady = 3)
    entry_sign_up_age.insert(0 , 'Age')
    entry_sign_up_age.bind('<FocusIn>', entry_age_click_sign_up_card)  # bind click event
    entry_sign_up_age.bind('<FocusOut>', entry_age_exit_sign_up_card) # bind exit event

    entry_sign_up_identification = tk.Entry(background_widget_sign_up_card , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#B1B1B1', font = ('Calibri', 18 , "bold"))
    entry_sign_up_identification.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_sign_up_identification.grid(row = 4 , columnspan = 2 , ipady = 3 , pady = 35)
    entry_sign_up_identification.insert(0 , 'Identification Card')
    entry_sign_up_identification.bind('<FocusIn>', entry_Identification_click_sign_up_card)  # bind click event
    entry_sign_up_identification.bind('<FocusOut>', entry_Identification_exit_sign_up_card) # bind exit event

    sign_up_card = tk.Button(background_widget_sign_up_card , image = image_sign_up_with_card_complete , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = database_card_member)
    sign_up_card.grid(row = 5 , columnspan = 2)

    tk.Label(background_widget_sign_up_card , image = image_veg , background = "#FFFFFF").grid(row = 6 , columnspan = 2)
    
    # Enter Keyborad 
    root.bind('<Return>', lambda event: sign_up_card.invoke())

def entry_name_click_sign_up_card(event):
    # Function to handle the click event
    if entry_sign_up_name.get() == 'Name':
        entry_sign_up_name.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_name.insert(0, '')  # insert blank for user input
        entry_sign_up_name.config(fg='black', font = ('Calibri', 18 , "bold"))

def entry_name_exit_sign_up_card(event):
    # Function to handle the exit event"""
    if entry_sign_up_name.get() == '':
        entry_sign_up_name.insert(0, 'Name')  # insert default text
        entry_sign_up_name.config(fg = '#B1B1B1' , font = ('Calibri', 18 , "bold"))  # set text color to grey

def entry_lastname_click_sign_up_card(event): 
    if entry_sign_up_lastname.get() == 'Lastname':
        entry_sign_up_lastname.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_lastname.insert(0, '')  # insert blank for user input
        entry_sign_up_lastname.config(fg = 'black', font = ('Calibri', 18 , "bold"))

def entry_lastname_exit_sign_up_card(event): 
    if entry_sign_up_lastname.get() == '': 
        entry_sign_up_lastname.insert(0 , "Lastname")
        entry_sign_up_lastname.config(fg = "#B1B1B1" , font = ('Calibri', 18 , "bold"))

def entry_age_click_sign_up_card(event): 
    if entry_sign_up_age.get() == 'Age':
        entry_sign_up_age.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_age.insert(0, '')  # insert blank for user input
        entry_sign_up_age.config(fg = 'black', font = ('Calibri', 18 , "bold"))

def entry_age_exit_sign_up_card(event): 
    if entry_sign_up_age.get() == '': 
        entry_sign_up_age.insert(0 , "Age")
        entry_sign_up_age.config(fg = "#B1B1B1" , font = ('Calibri', 18 , "bold"))

def entry_Identification_click_sign_up_card(event): 
    if entry_sign_up_identification.get() == 'Identification Card':
        entry_sign_up_identification.delete(0, tk.END)  # delete all the text in the entry
        entry_sign_up_identification.insert(0, '')  # insert blank for user input
        entry_sign_up_identification.config(fg = 'black', font = ('Calibri', 18 , "bold"))

def entry_Identification_exit_sign_up_card(event): 
    if entry_sign_up_identification.get() == '': 
        entry_sign_up_identification.insert(0 , "Identification Card")
        entry_sign_up_identification.config(fg = "#B1B1B1" , font = ('Calibri', 18 , "bold"))

def bts_mrt(): 
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 800  # Set the width of the window
    window_height = 650  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2))

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    global background_right_bts_car , background_widget_bts_car , result
    background_right_login.grid_forget()
    background_widget_login.grid_forget()
    background_top_right.grid_forget()

    background_top1_right = tk.Frame(root , background = "#505254")
    background_top1_right.grid(row = 0 , column = 1 , sticky = 'news')
    background_top1_right.rowconfigure(0 , weight = 1)
    background_top1_right.columnconfigure(0 , weight = 0)
    background_top1_right.columnconfigure(1 , weight = 0)
    background_top1_right.columnconfigure(2 , weight = 0)
    background_top1_right.columnconfigure(3 , weight = 1)
    background_top1_right.columnconfigure(4 , weight = 0)

    background_right_bts_car = tk.Frame(root , background = "#F2F2F2")
    background_right_bts_car.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_bts_car.rowconfigure(0 , weight = 0)
    background_right_bts_car.rowconfigure(1 , weight = 5)
    background_right_bts_car.columnconfigure(0 , weight = 5)

    background_right_top_bts_car = tk.Frame(background_right_bts_car , background = '#FFFFFF')
    background_right_top_bts_car.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_bts_car.rowconfigure(0 , weight = 1)
    background_right_top_bts_car.columnconfigure(0 , weight = 1)

    background_widget_bts_car = tk.Frame(root , background = "#FFFFFF")
    background_widget_bts_car.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_bts_car.rowconfigure(0 , weight = 0)
    background_widget_bts_car.rowconfigure(1 , weight = 0)
    background_widget_bts_car.rowconfigure(2 , weight = 0)
    background_widget_bts_car.rowconfigure(3 , weight = 0)
    background_widget_bts_car.columnconfigure(0 , weight = 1)
    background_widget_bts_car.columnconfigure(1 , weight = 1)
    
    tk.Label(background_top1_right , text = "• Menu" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipadx = 15)
    tk.Label(background_top1_right , text = "• BTS" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 1 , sticky = 'w' , ipadx = 15)
    tk.Label(background_top1_right , text = "• MRT" , background = "#505254" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 2 , sticky = 'w' , ipadx = 15)
    tk.Button(background_top1_right , image = image_logout , background = "#505254" , bd = 0 , activebackground = "#505254" , command = return_menu).grid(row = 0 , column = 3 , sticky = 'e' , ipadx = 15)

    tk.Label(background_right_bts_car , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')

    sql = "SELECT * FROM users WHERE username = ?;"

    cursor.execute(sql , [entry_login_username.get()])

    result = cursor.fetchall()

    print(result[0][0])

    tk.Label(background_right_top_bts_car , text = "•  BTS & MRT" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_bts_car , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Button(background_widget_bts_car , image = image_bts , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = function_BTS).grid(row = 1 , column = 0 , sticky = 'e' , pady = 38 , padx = 15)
    tk.Button(background_widget_bts_car , image = image_mrt , background = "#FFFFFF" , bd = 0 , activebackground = "#FFFFFF" , command = function_MRT).grid(row = 1 , column = 1 , sticky = 'w' , pady = 37 , padx = 15)
    
    tk.Label(background_widget_bts_car , text = "BTS Route!" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 1, column = 0 , sticky = 'n' , pady = 15)
    tk.Label(background_widget_bts_car , text = "MRT Route!" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 1 , column = 1 , sticky = 'n'  , pady = 15) 
    tk.Label(background_widget_bts_car , text = "Please select your travel route." , background = "#FFFFFF" , font = "Calibri 19 bold").grid(row = 1 , columnspan = 2 , sticky = 'wes' , pady = 45)
    tk.Label(background_widget_bts_car , image = image_veg , background = "#FFFFFF").grid(row = 2 , columnspan = 2)

def function_BTS():
    global background_right_bts , background_widget_bts , background_right_top_bts , entry_number
    root.option_add("*font" , ("Angsana new" , 16))
    background_right_bts_car.grid_forget()
    background_widget_bts_car.grid_forget()
    
    background_right_bts = tk.Frame(root , background = "#F2F2F2")
    background_right_bts.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_bts.rowconfigure(0 , weight = 0)
    background_right_bts.rowconfigure(1 , weight = 5)
    background_right_bts.columnconfigure(0 , weight = 5)

    background_right_top_bts = tk.Frame(background_right_bts , background = '#FFFFFF')
    background_right_top_bts.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_bts.rowconfigure(0 , weight = 1)
    background_right_top_bts.columnconfigure(0 , weight = 1)

    background_widget_bts = tk.Frame(root , background = "#FFFFFF")
    background_widget_bts.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_bts.rowconfigure(0 , weight = 0)
    background_widget_bts.rowconfigure(1 , weight = 0)
    background_widget_bts.rowconfigure(2 , weight = 0)
    background_widget_bts.rowconfigure(3 , weight = 0)
    background_widget_bts.rowconfigure(4 , weight = 0)
    background_widget_bts.rowconfigure(5 , weight = 0)
    background_widget_bts.rowconfigure(6 , weight = 0)
    background_widget_bts.columnconfigure(0 , weight = 1)
    background_widget_bts.columnconfigure(1 , weight = 1)

    
    tk.Label(background_right_bts , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')

    tk.Label(background_right_top_bts , text = "•  BTS 🚄" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_bts , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)
    
    global start_station_combo , end_station_combo 

    # Create the station selection widgets
    start_station_label = ttk.Label(background_widget_bts, text = "Start station:" , background = "#FFFFFF" , font = "Calibri 16 bold")
    start_station_label.grid(row = 0 , column = 0 , padx = 155 , sticky = 'nw' ,pady = 10)
    start_station_combo = ttk.Combobox(background_widget_bts, values = ['[N24] คูคต', '[N23] แยก คปอ.', '[N22] พิพิธภัณฑ์กองทัพอากาศ', '[N21] โรงพยาบาลภูมิพลอดุลยเดช'
                            , '[N20] สะพานใหม่' , '[N19] สายหยุด' , '[N18] พหลโยธิน 59' , '[N17] วัดพระศรีมหาธาตุ' , '[N16] กรมทหารราบที่ 11' , '[N15] บางบัว' , '[N14] กรมป่าไม้' 
                            , '[N13] มหาวิทยาลัยเกษตรศาสตร์' , '[N12] เสนานิคม' , '[N11] รัชโยธิน' , '[N10] พหลโยธิน 24' , '[N9] ห้าแยกลาดพร้าว' , '[N8] หมอชิต' , '[N7] สะพานควาย'
                            , '[N6] เสนาร่วม' , '[N5] อารีย์' , '[N4] สนามเป้า' , '[N3] อนุสาวรีย์ชัยสมรภูมิ' , '[N2] พญาไท' , '[N1] ราชเทวี' , '[CEN] สยาม' , '[E1] ชิดลม' 
                            , '[E2] เพลินจิต' , '[E3] นานา' , '[E4] อโศก' , '[E5] พร้อมพงษ์' , '[E6] ทองหล่อ' , '[E7] เอกมัย' , '[E8] พระโขนง' , '[E9] อ่อนนุช' , '[E10] บางจาก'
                            , '[E11] ปุณณวิถี' , '[E12] อุดมสุข' , '[E13] บางนา' , '[E14] แบริ่ง' , '[E15] สำโรง' , '[E16] ปู่เจ้า' , '[E17] ช้างเอราวัณ' , '[E18] โรงเรียนนายเรือ'
                            , '[E19] ปากน้ำ' , '[E20] ศรีนครินทร์' , '[E21] แพรกษา' , '[E22] สายลวด' , '[E23] เคหะ' , '[W1] สนามกีฬาแห่งชาติ' , '[S1] ราชดำริ' , '[S2] ศาลาแดง' 
                            , '[S3] ช่องนนทรี' , '[S4] เซนต์หลุยส์' , '[S5] สุรศักดิ์' , '[S6] สะพานตากสิน' , '[S7] กรุงธนบุรี' , '[S8] วงเวียนใหญ่' , '[S9] โพธิ์นิมิตร' 
                            , '[S10] ตลาดพลู' , '[S11] วุฒากาศ' , '[S12] บางหว้า' , '[G1] กรุงธนบุรี' , '[G2] เจริญนคร' , '[G3] คลองสาน'] , width = 50 , state = "readonly")
    start_station_combo.set(" == กรุณาเลือกสถานีต้นทาง ==")
    start_station_combo.grid(row = 1 , columnspan = 2 , padx = 5  , sticky = 'n')

    end_station_label = tk.Label(background_widget_bts , text = "End station:" , background = "#FFFFFF" , font = "Calibri 16 bold")
    end_station_label.grid(row = 2 , column = 0 , padx = 155 , sticky = 'nw' , pady = 10) 
    end_station_combo = ttk.Combobox(background_widget_bts, background = "#FFFFFF" , font = ("Angsana New" , 16) , values = ['[N24] คูคต', '[N23] แยก คปอ.', '[N22] พิพิธภัณฑ์กองทัพอากาศ', '[N21] โรงพยาบาลภูมิพลอดุลยเดช'
                            , '[N20] สะพานใหม่' , '[N19] สายหยุด' , '[N18] พหลโยธิน 59' , '[N17] วัดพระศรีมหาธาตุ' , '[N16] กรมทหารราบที่ 11' , '[N15] บางบัว' , '[N14] กรมป่าไม้' 
                            , '[N13] มหาวิทยาลัยเกษตรศาสตร์' , '[N12] เสนานิคม' , '[N11] รัชโยธิน' , '[N10] พหลโยธิน 24' , '[N9] ห้าแยกลาดพร้าว' , '[N8] หมอชิต' , '[N7] สะพานควาย'
                            , '[N6] เสนาร่วม' , '[N5] อารีย์' , '[N4] สนามเป้า' , '[N3] อนุสาวรีย์ชัยสมรภูมิ' , '[N2] พญาไท' , '[N1] ราชเทวี' , '[CEN] สยาม' , '[E1] ชิดลม' 
                            , '[E2] เพลินจิต' , '[E3] นานา' , '[E4] อโศก' , '[E5] พร้อมพงษ์' , '[E6] ทองหล่อ' , '[E7] เอกมัย' , '[E8] พระโขนง' , '[E9] อ่อนนุช' , '[E10] บางจาก'
                            , '[E11] ปุณณวิถี' , '[E12] อุดมสุข' , '[E13] บางนา' , '[E14] แบริ่ง' , '[E15] สำโรง' , '[E16] ปู่เจ้า' , '[E17] ช้างเอราวัณ' , '[E18] โรงเรียนนายเรือ'
                            , '[E19] ปากน้ำ' , '[E20] ศรีนครินทร์' , '[E21] แพรกษา' , '[E22] สายลวด' , '[E23] เคหะ' , '[W1] สนามกีฬาแห่งชาติ' , '[S1] ราชดำริ' , '[S2] ศาลาแดง' 
                            , '[S3] ช่องนนทรี' , '[S4] เซนต์หลุยส์' , '[S5] สุรศักดิ์' , '[S6] สะพานตากสิน' , '[S7] กรุงธนบุรี' , '[S8] วงเวียนใหญ่' , '[S9] โพธิ์นิมิตร' 
                            , '[S10] ตลาดพลู' , '[S11] วุฒากาศ' , '[S12] บางหว้า' , '[G1] กรุงธนบุรี' , '[G2] เจริญนคร' , '[G3] คลองสาน']  , width = 50 , state = "readonly")
    end_station_combo.set(" == กรุณาเลือกสถานีปลายทาง ==")
    end_station_combo.grid(row = 3 , columnspan = 2 , padx = 5 , sticky = 'n')
    
    tk.Button(background_widget_bts , image = image_negative , bd = 0  , background = "#FFFFFF" , activebackground = "#FFFFFF" , command = decrement).grid(row = 4 , column = 0 , sticky = 'w' , padx = 125)
    tk.Button(background_widget_bts , image = image_positive , bd = 0  , background = "#FFFFFF" , activebackground = "#FFFFFF" , command = increment).grid(row = 4 , column = 1 , sticky = 'w')

    entry_number = tk.Entry(background_widget_bts , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#000000', font = ('Calibri', 18 , "bold"))
    entry_number.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_number.grid(row = 4 , columnspan = 2 , ipady = 3 , pady = 77)
    entry_number.insert(tk.END , '1')

    # Create the calculate button
    calculate_button = tk.Button(background_widget_bts , image = image_cal_price , background = "#FFFFFF" , bd = 0  , activebackground = "#FFFFFF" , command = calculate_and_show_fare)
    calculate_button.grid(row = 5 , columnspan = 2)

    tk.Label(background_widget_bts , image = image_veg , background = "#FFFFFF").grid(row = 6 , columnspan = 2)
    
    # Enter Keyborad 
    root.bind('<Return>', lambda event: calculate_button.invoke())

def increment():
    current_value = int(entry_number.get())
    if current_value < 100:
        entry_number.delete(0, tk.END)
        entry_number.insert(tk.END, str(current_value + 1))

def decrement():
    current_value = int(entry_number.get())
    if current_value > 1:
        entry_number.delete(0, tk.END)
        entry_number.insert(tk.END, str(current_value - 1))

def sky_train(start_station , end_station):
    global station_list
    root.option_add("*font" , ("Angsana New" , 16))
    station_list = ['[N24] คูคต', '[N23] แยก คปอ.', '[N22] พิพิธภัณฑ์กองทัพอากาศ', '[N21] โรงพยาบาลภูมิพลอดุลยเดช'
                        , '[N20] สะพานใหม่' , '[N19] สายหยุด' , '[N18] พหลโยธิน 59' , '[N17] วัดพระศรีมหาธาตุ' , '[N16] กรมทหารราบที่ 11' , '[N15] บางบัว' , '[N14] กรมป่าไม้' 
                        , '[N13] มหาวิทยาลัยเกษตรศาสตร์' , '[N12] เสนานิคม' , '[N11] รัชโยธิน' , '[N10] พหลโยธิน 24' , '[N9] ห้าแยกลาดพร้าว' , '[N8] หมอชิต' , '[N7] สะพานควาย'
                        , '[N6] เสนาร่วม' , '[N5] อารีย์' , '[N4] สนามเป้า' , '[N3] อนุสาวรีย์ชัยสมรภูมิ' , '[N2] พญาไท' , '[N1] ราชเทวี' , '[CEN] สยาม' , '[E1] ชิดลม' 
                        , '[E2] เพลินจิต' , '[E3] นานา' , '[E4] อโศก' , '[E5] พร้อมพงษ์' , '[E6] ทองหล่อ' , '[E7] เอกมัย' , '[E8] พระโขนง' , '[E9] อ่อนนุช' , '[E10] บางจาก'
                        , '[E11] ปุณณวิถี' , '[E12] อุดมสุข' , '[E13] บางนา' , '[E14] แบริ่ง' , '[E15] สำโรง' , '[E16] ปู่เจ้า' , '[E17] ช้างเอราวัณ' , '[E18] โรงเรียนนายเรือ'
                        , '[E19] ปากน้ำ' , '[E20] ศรีนครินทร์' , '[E21] แพรกษา' , '[E22] สายลวด' , '[E23] เคหะ' , '[W1] สนามกีฬาแห่งชาติ' , '[S1] ราชดำริ' , '[S2] ศาลาแดง' 
                        , '[S3] ช่องนนทรี' , '[S4] เซนต์หลุยส์' , '[S5] สุรศักดิ์' , '[S6] สะพานตากสิน' , '[S7] กรุงธนบุรี' , '[S8] วงเวียนใหญ่' , '[S9] โพธิ์นิมิตร' 
                        , '[S10] ตลาดพลู' , '[S11] วุฒากาศ' , '[S12] บางหว้า' , '[G1] กรุงธนบุรี' , '[G2] เจริญนคร' , '[G3] คลองสาน'] 
    
    '''
    Name list of station BTS 
    
    station_list[0] = '[N24] คูคต'
    station_list[1] = '[N23] แยก คปอ.'
    station_list[2] = '[N22] พิพิธภัณฑ์กองทัพอากาศ'
    station_list[3] = '[N21] โรงพยาบาลภูมิพลอดุลยเดช'
    station_list[4] = '[N20] สะพานใหม่
    station_list[5] = '[N19] สายหยุด'
    station_list[6] = '[N18] พหลโยธิน 59'
    station_list[7] = '[N17] วัดพระศรีมหาธาตุ'
    station_list[8] = '[N16] กรมทหารราบที่ 11'
    station_list[9] = '[N15] บางบัว'
    station_list[10] = '[N14] กรมป่าไม้' 
    station_list[11] = '[N13] มหาวิทยาลัยเกษตรศาสตร์'
    station_list[12] = '[N12] เสนานิคม'
    station_list[13] = '[N11] รัชโยธิน'
    station_list[14] = '[N10] พหลโยธิน 24'
    station_list[15] = '[N9] ห้าแยกลาดพร้าว'
    station_list[16] = '[N8] หมอชิต'
    station_list[17] = '[N7] สะพานควาย'
    station_list[18] = '[N6] เสนาร่วม'
    station_list[19] = '[N5] อารีย์'
    station_list[20] = '[N4] สนามเป้า'
    station_list[21] = '[N3] อนุสาวรีย์ชัยสมรภูมิ'
    station_list[22] = '[N2] พญาไท'
    station_list[23] = '[N1] ราชเทวี'
    station_list[24] = '[CEN] สยาม'
    station_list[25] = '[E1] ชิดลม' 
    station_list[26] = '[E2] เพลินจิต'
    station_list[27] = '[E3] นานา'
    station_list[28] = '[E4] อโศก'
    station_list[29] = '[E5] พร้อมพงษ์'
    station_list[30] = '[E6] ทองหล่อ'
    station_list[31] = '[E7] เอกมัย'
    station_list[32] = '[E8] พระโขนง'
    station_list[33] = '[E9] อ่อนนุช'
    station_list[34] = '[E10] บางจาก'
    station_list[35] = '[E11] ปุณณวิถี'
    station_list[36] = '[E12] อุดมสุข'
    station_list[37] = '[E13] บางนา'
    station_list[38] = '[E14] แบริ่ง'
    station_list[39] = '[E15] สำโรง'
    station_list[40] = '[E16] ปู่เจ้า'
    station_list[41] = '[E17] ช้างเอราวัณ'
    station_list[42] = '[E18] โรงเรียนนายเรือ'
    station_list[43] = '[E19] ปากน้ำ'
    station_list[44] = '[E20] ศรีนครินทร์'
    station_list[45] = '[E21] แพรกษา'
    station_list[46] = '[E22] สายลวด'
    station_list[47] = '[E23] เคหะ'
    station_list[48] = '[W1] สนามกีฬาแห่งชาติ'
    station_list[49] = '[S1] ราชดำริ' 
    station_list[50] = '[S2] ศาลาแดง'
    station_list[51] = '[S3] ช่องนนทรี'
    station_list[52] = '[S4] เซนต์หลุยส์' 
    station_list[53] = '[S5] สุรศักดิ์'
    station_list[54] = '[S6] สะพานตากสิน'
    station_list[55] = '[S7] กรุงธนบุรี' 
    station_list[56] = '[S8] วงเวียนใหญ่'
    station_list[57] = '[S9] โพธิ์นิมิตร' 
    station_list[58] = '[S10] ตลาดพลู'
    station_list[59] = '[S11] วุฒากาศ'
    station_list[60] = '[S12] บางหว้า'
    station_list[61] = '[G1] กรุงธนบุรี (Gold line)' 
    station_list[62] = '[G2] เจริญนคร'
    station_list[63] = '[G3] คลองสาน'
    
    '''


    # หากเริ่มสถานีใดสถานีหนึ่ง(ชิดลม - พระโขนง) 
    if start_station in [station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32]]: 
        # แล้วจบที่สถานีอ่อนนุช
        if end_station in [station_list[33]]:
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1]
        # แล้วจบที่สถานีบางจาก
        elif end_station in [station_list[34]]: 

            if result[0][4] == '':
                fares = [32 , 40 , 43 , 47 , 50 , 55 , 58 , 62]
            elif 60 > result[0][4] > 23: 
                fares = [32 , 40 , 43 , 47 , 50 , 55 , 58 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [27 , 35 , 38 , 42 , 45 , 50 , 53 , 57]
            else: 
                fares = [16 , 20 , 21 , 23 , 25 , 27 , 29 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 1)

            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1]

    if start_station in [station_list[34]]: 
        if end_station in [station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32]]: 
            if result[0][4] == '':
                fares = [32 , 40 , 43 , 47 , 50 , 55 , 58]
            elif 60 > result[0][4] > 23: 
                fares = [32 , 40 , 43 , 47 , 50 , 55 , 58]
            elif 23 >= result[0][4] >= 0: 
                fares = [27 , 35 , 38 , 42 , 45 , 50 , 53]
            else: 
                fares = [16 , 20 , 21 , 23 , 25 , 27 , 29]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index + 1)

            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1]


    # จาก สยาม 
    if start_station in [station_list[24]]: 
        if end_station in [station_list[33]]: 
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 47
            else: 
                price = 24

        elif end_station in [station_list[34]]: 
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

    # จาก อ่อนนุช - บางนา
    if start_station in [station_list[33] , station_list[34] , station_list[35] , station_list[36] , station_list[37]]: 
        # ไป แบริ่ง - เคหะ
        if end_station in [station_list[38] ,station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47]]:
            if result[0][4] == '':
                price = 15
            elif 60 > result[0][4] > 23: 
                price = 15
            elif 23 >= result[0][4] >= 0: 
                price = 10
            else: 
                price = 7

    # ในระหว่างเส้นทาง (คูคต - หมอชิต) หริอ (หมอชิต - คูคต) จะมีราคาเป็น 0 บาท เนื่องจากรถไฟฟ้ายังอยู่ในสัญญาที่ให้ฟรี 
    if start_station  in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6] , station_list[7] ,station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16]]:

        # จาก (คูคต - หมอชิต) ไป สถานีสะพานควาย) ราคา 17 บาท
        if end_station in [station_list[17]]:
            if result[0][4] == '':
                price = 17
            elif 60 > result[0][4] > 23: 
                price = 17
            elif 23 >= result[0][4] >= 0: 
                price = 17
            else: 
                price = 9
        
        # จาก (คูคต - หมอชิต) ไป เสนาร่วม ราคา 25 บาท
        elif end_station in [station_list[18]]:
            if result[0][4] == '':
                price = 25
            elif 60 > result[0][4] > 23: 
                price = 25
            elif 23 >= result[0][4] >= 0: 
                price = 25
            else: 
                price = 13

        # จาก (คูคต - หมอชิต) ไป อารีย์ ราคา 28 บาท    
        elif end_station in [station_list[19]]:
            if result[0][4] == '':
                price = 28
            elif 60 > result[0][4] > 23: 
                price = 28
            elif 23 >= result[0][4] >= 0: 
                price = 28
            else: 
                price = 14

        # จาก (คูคต - หมอชิต) ไป สนามเป้า ราคา 32 บาท    
        elif end_station in [station_list[20]]:
            if result[0][4] == '':
                price = 32
            elif 60 > result[0][4] > 23: 
                price = 32
            elif 23 >= result[0][4] >= 0: 
                price = 32
            else: 
                price = 16
        
        # จาก (คูคต - หมอชิต) ไป อนุสาวรีย์ชัยสมรภูมิ ราคา 35 บาท    
        elif end_station in [station_list[21]]:
            if result[0][4] == '':
                price = 35
            elif 60 > result[0][4] > 23: 
                price = 35
            elif 23 >= result[0][4] >= 0: 
                price = 35
            else: 
                price = 18
        
        # จาก (คูคต - หมอชิต) ไป พญาไท ราคา 40 บาท       
        elif end_station in [station_list[22]]:
            if result[0][4] == '':
                price = 40
            elif 60 > result[0][4] > 23: 
                price = 40
            elif 23 >= result[0][4] >= 0: 
                price = 40
            else: 
                price = 20
        
        # จาก (คูคต - หมอชิต) ไป ราชเทวี ราคา 43 บาท  
        elif end_station in [station_list[23]]:
            if result[0][4] == '':
                price = 43
            elif 60 > result[0][4] > 23: 
                price = 43
            elif 23 >= result[0][4] >= 0: 
                price = 43
            else: 
                price = 22

        # จาก (คูคต - หมอชิต) ไป (สยาม , ชิดลม , เพลินจิด , นานา , อโศก , พร้อมพงษ์ , ทองหล่อ , เอกมัย , พระโขนง , อ่อนนุช) ราคา 47 บาท      
        elif end_station in [station_list[24] , station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32] , station_list[33]]:
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 47
            else: 
                price = 24

        # จาก (คูคต - หมอชิต) ไป (บางจาก , ปุณณวิถี , อุดมสุข , บางนา , แบริ่ง , สำโรง , ปู่เจ้า , ช้างเอราวัณ , โรงเรียนนายเรือ , ปากน้ำ , ศรีนครินทร์ , แพรกษา , สายลวด , เคหะฯ) จะมีราคา 62 บาท
        elif end_station in [station_list[34] , station_list[35] , station_list[36] , station_list[37] , station_list[38] , station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47]]:
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

        # จาก (คูคต - หมอชิด) ไป ('สนามกีฬาแห่งชาติ' , 'ราชดำริ' , 'ศาลาแดง' ,'ช่องนนทรี' , 'เซนต์หลุยส์' , 'สุรศักดิ์' , 'สะพานตากสิน' , 'กรุงธนบุรี' , 'วงเวียนใหญ่') จะมีราคา 47 บาท
        elif end_station in [station_list[48] , station_list[49] , station_list[50] , station_list[51] , station_list[52] , station_list[53] , station_list[54] , station_list[55] , station_list[56]]:
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 47
            else: 
                price = 24
        
        # จาก (คูคต - หมอชิต) ไป ('โพธิ์นิมิตร' , 'ตลาดพลู' , 'วุฒากาศ' , 'บางหว้า') จะมีราคา 62 บาท
        elif end_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31
        else: 
            price = 0

    # ในระหว่างเส้นทางสถานี (สะพานควาย - สยาม) หรือ (สยาม - สะพานควาย) จะถูกคำนวณราคาตามระยะห่างของแต่ละสถานี  
    if start_station in [station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24]]:
        if end_station in [station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24]]:
            
            # ถ้าห่างกัน 1 สถานี จะมีราคา 17 บาท
            # ถ้าห่างกัน 2 สถานี จะมีราคา 25 บาท 
            # ถ้าห่างกัน 3 สถานี จะมีราคา 28 บาท 
            # ถ้าห่างกัน 4 สถานี จะมีราคา 32 บาท 
            # ถ้าห่างกัน 5 สถานี จะมีราคา 35 บาท 
            # ถ้าห่างกัน 6 สถานี จะมีราคา 40 บาท 
            # ถ้าห่างกัน 7 สถานี จะมีราคา 43 บาท 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1]

        # ถ้า สถานีปลายทาง คือ (คูคต , แยก คปอ. , พิพิธภัณฑ์กองทัพอากาศ , โรงพยาบาลภูมิพลอดุลยเดช , สะพานใหม่ , สายหยุด , พหลโยธิน 59 ,  วัดพระศรีมหาธาตุ , กรมทหารราบที่ 11 , 
        # บางบัว , กรมป่าไม้ , มหาวิทยาลัยเกษตรศาสตร์ , เสนานิคม , รัชโยธิน , พหลโยธิน 24 , ห้าแยกลาดพร้าว , หมอชิต)
        elif end_station in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6] , station_list[7] ,station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16]]:        
            
            # หากสถานีเริ่มต้น คือ "สะพานควาย" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 17 บาท
            if start_station in [station_list[17]]:
                if result[0][4] == '':
                    price = 17
                elif 60 > result[0][4] > 23: 
                    price = 17
                elif 23 >= result[0][4] >= 0: 
                    price = 17
                else: 
                    price = 9

            # หากสถานีเริ่มต้น คือ "เสนาร่วม" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 25 บาท
            elif start_station in [station_list[18]]:
                if result[0][4] == '':
                    price = 25
                elif 60 > result[0][4] > 23: 
                    price = 25
                elif 23 >= result[0][4] >= 0: 
                    price = 25
                else: 
                    price = 13

            # หากสถานีเริ่มต้น คือ "อารีย์" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 28 บาท
            elif start_station in [station_list[19]]:
                if result[0][4] == '':
                    price = 28
                elif 60 > result[0][4] > 23: 
                    price = 28
                elif 23 >= result[0][4] >= 0: 
                    price = 28
                else: 
                    price = 14

            # หากสถานีเริ่มต้น คือ "สนามเป้า" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 32 บาท
            elif start_station in [station_list[20]]:
                if result[0][4] == '':
                    price = 32
                elif 60 > result[0][4] > 23: 
                    price = 32
                elif 23 >= result[0][4] >= 0: 
                    price = 32
                else: 
                    price = 16

            # หากสถานีเริ่มต้น คือ "อนุสาวรีย์ชัยสมรภูมิ" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 35 บาท
            elif start_station in [station_list[21]]:
                if result[0][4] == '':
                    price = 35
                elif 60 > result[0][4] > 23: 
                    price = 35
                elif 23 >= result[0][4] >= 0: 
                    price = 35
                else: 
                    price = 18

            # หากสถานีเริ่มต้น คือ "พญาไท" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 40 บาท
            elif start_station in [station_list[22]]:
                if result[0][4] == '':
                    price = 40
                elif 60 > result[0][4] > 23: 
                    price = 40
                elif 23 >= result[0][4] >= 0: 
                    price = 40
                else: 
                    price = 20
            
            # หากสถานีเริ่มต้น คือ "ราชเทวี" แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 43 บาท
            elif start_station in [station_list[23]]:
                if result[0][4] == '':
                    price = 43
                elif 60 > result[0][4] > 23: 
                    price = 43
                elif 23 >= result[0][4] >= 0: 
                    price = 43
                else: 
                    price = 22

            # หากสถานีเริ่มต้น คืออย่างใดอย่างหนึ่ง ("สยาม" , "ชิดลม" , "เพลินจิต" , "นานา" , "อโศก" , "พร้อมพงษ์" , "ทองหล่อ" , "เอกมัย" , "พระโขนง" , "อ่อนนุช") แล้วไปยังสถานีปลายทางใดปลายทางหนึ่ง ที่เขียนไว้ด้านบน จะมีราคา 47 บาท
            elif start_station in [station_list[24] , station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32] , station_list[33]]:
                if result[0][4] == '':
                    price = 47
                elif 60 > result[0][4] > 23: 
                    price = 47
                elif 23 >= result[0][4] >= 0: 
                    price = 47
                else: 
                    price = 24

    # หากสถานีเริ่มต้น คืออย่างใดอย่างหนึ่ง ("ปุณณวิถี" , "อุดมสุข" , "บางนา" , "แบริ่ง" , "สำโรง" , "ปู่เจ้า" , "ช้างเอราวัณ" , "โรงเรียนนายเรือ" , "ปากน้ำ" , "ศรีนครินทร์" , "แพรกษา" , "สายลวด" , "เคหะ") 
    if start_station in [station_list[34] , station_list[35] , station_list[36] , station_list[37] , station_list[38] , station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47]]:
        
        # แล้วสถานีปลายทาง คืออย่างใดอย่างหนึ่ง (คูคต - ชิดลม)
        if end_station in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6] , station_list[7] ,station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16] , station_list[17] , station_list[18] ,station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24] , station_list[25]]:
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

    # ในระหว่างเส้นทาง (เคหะ - แบริ่ง) หริอ (แบริ่ง - เคหะ) จะมีราคาเป็น 0 บาท เนื่องจากรถไฟฟ้ายังอยู่ในสัญญาที่ให้ฟรี 
    if start_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38]]:
        if end_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38]]:
            if result[0][4] == '':
                price = 0
            elif 60 > result[0][4] > 23: 
                price = 0
            elif 23 >= result[0][4] >= 0: 
                price = 0
            else:
                price = 0

    # หากสถานีเริ่มต้น คืออย่างใดอย่างหนึ่ง (เคหะฯ - อ่อนนุช) 
    if start_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35] , station_list[34] , station_list[33]]:
        
        # แล้วสถานีปลายทาง คืออย่างใดอย่างหนึ่ง (บางนา - อ่อนนุช) จะมีราคา 15 บาท
        if end_station in [station_list[37] , station_list[36] , station_list[35] , station_list[34] , station_list[33]]:
            if result[0][4] == '':
                price = 15
            elif 60 > result[0][4] > 23: 
                price = 15
            elif 23 >= result[0][4] >= 0: 
                price = 10
            else: 
                price = 7

    # หากสถานีเริ่มต้น คืออย่างใดอย่างหนึ่ง (เคหะฯ - ปุณณวิถี)
    if start_station in  [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35]]:   
        
        # แล้วสถานีปลายทาง คือ "พระโขนง" จะมีราคา 32 บาท
        if end_station in station_list[32]: 
            if result[0][4] == '':
                price = 32
            elif 60 > result[0][4] > 23: 
                price = 32
            elif 23 >= result[0][4] >= 0: 
                price = 27
            else: 
                price = 16

        # แล้วสถานีปลายทาง คือ "เอกมัย" จะมีราคา 40 บาท
        elif end_station in station_list[31]:
            if result[0][4] == '':
                price = 40
            elif 60 > result[0][4] > 23: 
                price = 40
            elif 23 >= result[0][4] >= 0: 
                price = 35
            else: 
                price = 20

        # แล้วสถานีปลายทาง คือ "ทองหล่อ" จะมีราคา 43 บาท
        elif end_station in station_list[30]:
            if result[0][4] == '':
                price = 43
            elif 60 > result[0][4] > 23: 
                price = 43
            elif 23 >= result[0][4] >= 0: 
                price = 38
            else: 
                price = 21
        
        # แล้วสถานีปลายทาง คือ "พร้อมพงษ์" จะมีราคา 47 บาท
        elif end_station in station_list[29]:
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 42
            else: 
                price = 23
        
        # แล้วสถานีปลายทาง คือ "อโศก" จะมีราคา 50 บาท
        elif end_station in station_list[28]:
            if result[0][4] == '':
                price = 50
            elif 60 > result[0][4] > 23: 
                price = 50
            elif 23 >= result[0][4] >= 0: 
                price = 45
            else: 
                price = 25

        # แล้วสถานีปลายทาง คือ "นานา" จะมีราคา 55 บาท
        elif end_station in station_list[27]:
            if result[0][4] == '':
                price = 55
            elif 60 > result[0][4] > 23: 
                price = 55
            elif 23 >= result[0][4] >= 0: 
                price = 50
            else: 
                price = 27

        # แล้วสถานีปลายทาง คือ "เพลินจิต" จะมีราคา 58 บาท
        elif end_station in station_list[26]:
            if result[0][4] == '':
                price = 58
            elif 60 > result[0][4] > 23: 
                price = 58
            elif 23 >= result[0][4] >= 0: 
                price = 53
            else: 
                price = 29

    #  หากสถานีเริ่มต้น คืออย่างใดอย่างหนึ่ง (อ่อนนุช - สยาม)
    if start_station in [station_list[33] , station_list[32] , station_list[31] , station_list[30] , station_list[29] , station_list[28] , station_list[27] , station_list[26] , station_list[25] , station_list[24]]:
        
        # แล้วสถานีปลายทาง คืออย่างใดอย่างหนึ่ง ("พระโขนง" จนถึง "คูคต") ให้คำนวณตามระยะห่างของสถานีไปเลย ตามนี้
        if end_station in [station_list[32] , station_list[31] , station_list[30] , station_list[29] , station_list[28] , station_list[27] , station_list[26] , station_list[25] , station_list[24] , station_list[23] , station_list[22] , station_list[21] , station_list[20] , station_list[19] , station_list[18] , station_list[17] , station_list[16] , station_list[15] , station_list[14] , station_list[13] , station_list[12] , station_list[11] , station_list[10] , station_list[9] , station_list[8] , station_list[7] , station_list[6] , station_list[5] , station_list[4] , station_list[3] , station_list[2] , station_list[1] , station_list[0]]:
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 ]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 ]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 ]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 ]
             

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1]  

    # หากสถานีปลายทาง คือ อย่างใดอย่างหนึ่ง ("เคหะ" จนถึง "ชิดลม") ให้คำนวณตามระยะห่างของสถานี โดยยึดจากสถานีเริ่มต้นต่อไปนี้
    if end_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35] , station_list[34] , station_list[33] , station_list[32] , station_list[31] , station_list[30] , station_list[29] , station_list[28] , station_list[27] , station_list[26] , station_list[25]]:
        
        # หากสถานีเริ่มต้น คือ ราชเทวี ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares
        if start_station in [station_list[23]]:
            if result[0][4] == '':
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-2]
            else:
                price = fares[-1] 

        # หากสถานีเริ่มต้น คือ พญาไท ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares        
        elif start_station in [station_list[22]]:
            if result[0][4] == '':
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-3]
            else:
                price = fares[-1] 

        # หากสถานีเริ่มต้น คือ อนุสาวรีย์ชัยสมรภูมิ ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares      
        elif start_station in [station_list[21]]:
            if result[0][4] == '':
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-4]
            else:
                price = fares[-1] 


        # หากสถานีเริ่มต้น คือ สนามเป้า ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares      
        elif start_station in [station_list[20]]:
            if result[0][4] == '':
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-5]
            else:
                price = fares[-1] 


        # หากสถานีเริ่มต้น คือ อารีย์ ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares      
        elif start_station in [station_list[19]]:
            if result[0][4] == '':
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-6]
            else:
                price = fares[-1] 

        # หากสถานีเริ่มต้น คือ เสนาร่วม ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares      
        elif start_station in [station_list[18]]:
            if result[0][4] == '':
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-7]
            else:
                price = fares[-1] 


        # หากสถานีเริ่มต้น คือ สะพานควาย ให้คำนวณระยะห่างตามราคาที่เก็บอยู่ในตัวแปร fares      
        elif start_station in [station_list[17]]:
            if result[0][4] == '':
                fares = [47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23:  
                fares = [47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-8]
            else:
                price = fares[-1] 

        # หากสถานีปลายทาง คืออย่างใดอย่างหนึ่ง ("ปุณณวิถี" จนถึง "เคหะ")
        if end_station in [station_list[35] , station_list[36] , station_list[37] , station_list[38] , station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47]]:
            
            # แล้วสถานีเริ่มต้น คือ พระโขนง จะมีราคา 32 บาท
            if start_station in station_list[32]: 
                if result[0][4] == '':
                    price = 32
                elif 60 > result[0][4] > 23: 
                    price = 32
                elif 23 >= result[0][4] >= 0: 
                    price = 27
                else: 
                    price = 16

            # แล้วสถานีเริ่มต้น คือ เอกมัย  จะมีราคา 40 บาท
            elif start_station in station_list[31]: 
                if result[0][4] == '':
                    price = 40
                elif 60 > result[0][4] > 23: 
                    price = 40
                elif 23 >= result[0][4] >= 0: 
                    price = 35
                else: 
                    price = 20
            
            # แล้วสถานีเริ่มต้น คือ ทองหล่อ  จะมีราคา 43 บาท
            elif start_station in station_list[30]: 
                if result[0][4] == '':
                    price = 43
                elif 60 > result[0][4] > 23: 
                    price = 43
                elif 23 >= result[0][4] >= 0: 
                    price = 38
                else: 
                    price = 21
            
            # แล้วสถานีเริ่มต้น คือ พร้อมพงษ์  จะมีราคา 47 บาท
            elif start_station in station_list[29]: 
                if result[0][4] == '':
                    price = 47
                elif 60 > result[0][4] > 23: 
                    price = 47
                elif 23 >= result[0][4] >= 0: 
                    price = 42
                else: 
                    price = 23

            # แล้วสถานีเริ่มต้น คือ อโศก  จะมีราคา 50 บาท
            elif start_station in station_list[28]:
                if result[0][4] == '':
                    price = 50
                elif 60 > result[0][4] > 23: 
                    price = 50
                elif 23 >= result[0][4] >= 0: 
                    price = 45
                else: 
                    price = 25

            # แล้วสถานีเริ่มต้น คือ นานา  จะมีราคา 55 บาท
            elif start_station in station_list[27]:
                if result[0][4] == '':
                    price = 55
                elif 60 > result[0][4] > 23: 
                    price = 55
                elif 23 >= result[0][4] >= 0: 
                    price = 50
                else: 
                    price = 27

            # แล้วสถานีเริ่มต้น คือ เพลินจิต  จะมีราคา 58 บาท
            elif start_station in station_list[26]: 
                if result[0][4] == '':
                    price = 58
                elif 60 > result[0][4] > 23: 
                    price = 58
                elif 23 >= result[0][4] >= 0: 
                    price = 53
                else: 
                    price = 29

            # แล้วสถานีเริ่มต้น คือ ชิดลม หรือ สยาม  จะมีราคา 62 บาท
            elif start_station in [station_list[25] , station_list[24]]: 
                if result[0][4] == '':
                    price = 62
                elif 60 > result[0][4] > 23: 
                    price = 62
                elif 23 >= result[0][4] >= 0: 
                    price = 57
                else: 
                    price = 31

    # เริ่มจาก (คูคต - ราชเทวี) 
    if start_station in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6], station_list[7] , station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16] , station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24]]: 
        
        # ไปถึง สนามกีฬาแห่งชาติ โดยคำนวณราคาตามระยะห่างของสถานี 
        if end_station in [station_list[48]]:
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 24)

            if distance <= len(fares):
                price = fares[distance]
            else:
                price = fares[-1] 

    # เริ่มจาก (ชิดลม - เคหะ) 
    if start_station in [station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32] , station_list[33] , station_list[34] , station_list[35] , station_list[36] , station_list[37] , station_list[38] , station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47]]: 
        
        # ไปถึง สนามกีฬาแห่งชาติ โดยคำนวณราคาตามระยะห่างของสถานี 
        if end_station in [station_list[48]]:
            if result[0][4] == '':
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 24)
            print(start_index)
            print(end_index)
            print(distance)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

    # เริ่มจาก สนามกีฬาแห่งชาติ
    if start_station in station_list[48]: 
        # สถานีปลายทาง คือ ชิดลม จนถึง เคหะ โดยคำนวณตามนี้
        if end_station in [station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32] , station_list[33] , station_list[34] , station_list[35] , station_list[36] , station_list[37] , station_list[38] , station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47]]: 
            if result[0][4] == '':
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 60 > result[0][4] > 23: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62 , 62]
            elif 23 >= result[0][4] >= 0: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57 , 57]
            else: 
                fares = [13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31 , 31]
                
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index + 24)
            print(start_index)
            print(end_index)
            print(distance)
            print('love her')
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ คูคต จนถึง สยาม โดยคำนวณตามนี้
        if end_station in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6] , station_list[7] , station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16] , station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24]]: 
        
        # ไปถึง สนามกีฬาแห่งชาติ โดยคำนวณราคาตามระยะห่างของสถานี 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index + 23)
            print(start_index)
            print(end_index)
            print(distance)
            print("love")
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

    # เริ่มจาก (สะพานควาย - สยาม) 
    if start_station in [station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24]]: 
        # สถานีปลายทาง คือ ราชดำริ จนถึง วนเวียนใหญ่ ให้คำนวณตามนี้
        if end_station in [station_list[49] , station_list[50] , station_list[51] , station_list[52] , station_list[53] , station_list[54] , station_list[55] , station_list[56]]:                 
        
        # โดยคำนวณราคาตามระยะห่างของสถานี 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 24)
            print(start_index)
            print(end_index)
            print(distance)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ โพธิ์นิมิตร จนถึง บางหว้า ให้คำนวณตามนี้
        if end_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

    # เริ่มจาก (เคหะ - บางจาก)
    if start_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35] , station_list[34] , station_list[33]]:
         # สถานีปลายทาง คือ ราชดำริ จนถึง บางหว้า ให้คำนวณตามนี้
        if end_station in [station_list[49] , station_list[50] , station_list[51] , station_list[52] , station_list[53] , station_list[54] , station_list[55] , station_list[56] , station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

        if end_station in [station_list[40]]:
            if start_station in [station_list[34]]:
                if result[0][4] == '':
                    price = 15
                elif 60 > result[0][4] > 23: 
                    price = 15
                elif 23 >= result[0][4] >= 0: 
                    price = 10
                else: 
                    price = 7
    # เริ่มจาก (ชิดลม - อ่อนนุช)
    if start_station in [station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32] , station_list[33]]:
         # สถานีปลายทาง คือ ราชดำริ ให้คำนวณตามนี้
        if end_station in [station_list[49]]:
            if result[0][4] == '':
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47]
            else: 
                fares = [13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 25)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ ศาลาแดง ให้คำนวณตามนี้
        if end_station in [station_list[50]]:
            if result[0][4] == '':
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47]
            else: 
                fares = [14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 26)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ ช่องนนทรี ให้คำนวณตามนี้
        if end_station in [station_list[51]]:
            if result[0][4] == '':
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24]
                
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 27)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
        # สถานีปลายทาง คือ เซนต์หลุยส์ ให้คำนวณตามนี้ 
        if end_station in [station_list[52]]:
            if result[0][4] == '':
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 28)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ สุรศักดิ์  ให้คำนวณตามนี้
        if end_station in [station_list[53]]:
            if result[0][4] == '':
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 29)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ สะพานตากสิน ให้คำนวณตามนี้
        if end_station in [station_list[54]]:
            if result[0][4] == '':
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24]
                
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 30)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
        # สถานีปลายทาง คือ กรุงธนบุรี และ วนเวียนใหญ่ ให้มีราคาแค่ 47 บาท
        if end_station in [station_list[55] , station_list[56]]:
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 47
            else: 
                price = 24
                
        # สถานีปลายทาง คือ หลังจากสถานีโพธิ์นิมิตร เป็นต้นไป จะมีราคา 62 บาท
        if end_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 61
                

   # หากจุดเริ่มต้น จากราชดำริ ถึง บางหว้า 
    if start_station in [station_list[49] , station_list[50] , station_list[51] , station_list[52] , station_list[53] , station_list[54] , station_list[55] , station_list[56] , station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
        # สถานีปลายทาง คือ ราชดำริ 
        if end_station in [station_list[49]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 58 , 58 , 58 , 58]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 58 , 58 , 58 , 58]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 53 , 53 , 53 , 53]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 29 , 29 , 29 , 29]
                    
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ ศาลาแดง
        if end_station in [station_list[50]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 55 , 55 , 55 , 55]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 55 , 55 , 55 , 55]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 50 , 50 , 50 , 50]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 27 , 27 , 27 , 27]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ ช่องนนทรี
        if end_station in [station_list[51]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 50 , 50 , 50 , 50]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 50 , 50 , 50 , 50]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 45 , 45 , 45 , 45]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 25 , 25 , 25 , 25]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)

            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
        # สถานีปลายทาง คือ เซนต์หลุยส์
        if end_station in [station_list[52]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 42 , 42 , 42 , 42]
            else: 
                fares = [9 , 13 , 14 , 16 , 23 , 23 , 23 , 23]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ สุรศักดิ์
        if end_station in [station_list[53]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32]
            else: 
                fares = [9 , 13 , 14 , 16]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

            # ถ้าสถานีเริ่มต้น เป็น หลังจากสถานี โพธิ์นิมิตร เป็นต้นไป ให้มีราคาทั้งหมดคือ 43 บาท
            if start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
                if result[0][4] == '':
                    price = 43
                elif 60 > result[0][4] > 23: 
                    price = 43
                elif 23 >= result[0][4] >= 0: 
                    price = 38
                else: 
                    price = 21
        
        # สถานีปลายทาง คือ สะพานตากสิน
        if end_station in [station_list[54]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35] 
            else: 
                fares = [9 , 13 , 14 , 16 , 18]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

            # ถ้าสถานีเริ่มต้น เป็น หลังจากสถานี โพธิ์นิมิตร เป็นต้นไป ให้มีราคาทั้งหมดคือ 32 บาท
            if start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
                if result[0][4] == '':
                    price = 32
                elif 60 > result[0][4] > 23: 
                    price = 32
                elif 23 >= result[0][4] >= 0: 
                    price = 27
                else: 
                    price = 16
        
        # สถานีปลายทาง คือ กรุงธนบุรี
        if end_station in [station_list[55]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

            # ถ้าสถานีเริ่มต้น เป็น หลังจากสถานี โพธิ์นิมิตร เป็นต้นไป ให้มีราคาทั้งหมดคือ 32 บาท
            if start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
                if result[0][4] == '':
                    price = 32
                elif 60 > result[0][4] > 23: 
                    price = 32
                elif 23 >= result[0][4] >= 0: 
                    price = 27
                else: 
                    price = 16

        # สถานีปลายทาง คือ วงเวียนใหญ่
        if end_station in [station_list[56]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

            # ถ้าสถานีเริ่มต้น เป็น หลังจากสถานี โพธิ์นิมิตร เป็นต้นไป ให้มีราคาทั้งหมดคือ 32 บาท
            if start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
                if result[0][4] == '':
                    price = 15
                elif 60 > result[0][4] > 23: 
                    price = 15
                elif 23 >= result[0][4] >= 0: 
                    price = 10
                else: 
                    price = 7
        
        # สถานีปลายทาง คือ โพธิ์นิมิตร
        if end_station in [station_list[57]]: 
            if result[0][4] == '':
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 60 > result[0][4] > 23: 
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 23 >= result[0][4] >= 0: 
                fares = [10 , 27 , 27 , 38 , 42 , 45 , 50 , 53]
            else: 
                fares = [7 , 16 , 16 , 21 , 23 , 25 , 27 , 29]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ ตลาดพลู
        if end_station in [station_list[58]]: 
            if result[0][4] == '':
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 60 > result[0][4] > 23: 
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 23 >= result[0][4] >= 0: 
                fares = [10 , 27 , 27 , 38 , 42 , 45 , 50 , 53]
            else: 
                fares = [7 , 16 , 16 , 21 , 23 , 25 , 27 , 29]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 1)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
        # สถานีปลายทาง คือ วุฒากาศ
        if end_station in [station_list[59]]: 
            if result[0][4] == '':
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 60 > result[0][4] > 23: 
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 23 >= result[0][4] >= 0: 
                fares = [10 , 27 , 27 , 38 , 42 , 45 , 50 , 53]
            else: 
                fares = [7 , 16 , 16 , 21 , 23 , 25 , 27 , 29]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 2)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
        # สถานีปลายทาง คือ บางหว้า
        if end_station in [station_list[60]]: 
            if result[0][4] == '':
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 60 > result[0][4] > 23: 
                fares = [15 , 32 , 32 , 43 , 47 , 50 , 55 , 58]
            elif 23 >= result[0][4] >= 0: 
                fares = [10 , 27 , 27 , 38 , 42 , 45 , 50 , 53]
            else: 
                fares = [7 , 16 , 16 , 21 , 23 , 25 , 27 , 29]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index - 3)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 


    # ในระหว่างเส้นทาง โพธิ์นิมิตร จนถึง บางหว้า 
    if start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]: 
        if end_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
            if result[0][4] == '':
                price = 15
            elif 60 > result[0][4] > 23: 
                price = 15
            elif 23 >= result[0][4] >= 0: 
                price = 10
            else: 
                price = 7  
    
    # หากจุดเริ่มต้น จากราชดำริ ถึง วนเวียนใหญ่
    if start_station in [station_list[49] , station_list[50] , station_list[51] , station_list[52] , station_list[53] , station_list[54] , station_list[55] , station_list[56]]:
        # สถานีปลายทาง คือ คูคต - หมอชิต
        if end_station in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6] , station_list[7] , station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16] , station_list[17]]:
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 47
            else: 
                price = 24
        
        # สถานีปลายทาง คือ สะพานควาย - สยาม
        if end_station in [station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24]]: 
            if result[0][4] == '':
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [17 , 25 , 28 , 32 , 35 , 40 , 43 , 47 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [9 , 13 , 14 , 16 , 18 , 20 , 22 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(end_index - start_index + 24) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ ชิดลม
        if end_station in [station_list[25]]:
            if result[0][4] == '':
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47]
            else: 
                fares = [13 , 14 , 16 , 18 , 20 , 22 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index - 23) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ เพลินจิต
        if end_station in [station_list[26]]:
            if result[0][4] == '':
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [28 , 32 , 35 , 40 , 43 , 47 , 47 , 47]
            else: 
                fares = [14 , 16 , 18 , 20 , 22 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index - 22) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ นานา
        if end_station in [station_list[27]]:
            if result[0][4] == '':
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [32 , 35 , 40 , 43 , 47 , 47 , 47 , 47]
            else: 
                fares = [16 , 18 , 20 , 22 , 24 , 24 , 24 , 24]

            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index - 21) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ อโศก
        if end_station in [station_list[28]]:
            if result[0][4] == '':
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [35 , 40 , 43 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [18 , 20 , 22 , 24 , 24 , 24 , 24 , 24]
            
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index - 20) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

         # สถานีปลายทาง คือ พร้อมพงษ์
        if end_station in [station_list[29]]:
            if result[0][4] == '':
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [40 , 43 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [20 , 22 , 24 , 24 , 24 , 24 , 24 , 24]
            
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index - 19) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
        # สถานีปลายทาง คือ ทองหล่อ
        if end_station in [station_list[30]]:
            if result[0][4] == '':
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [43 , 47 , 47 , 47 , 47 , 47 , 47 , 47]
            else: 
                fares = [22 , 24 , 24 , 24 , 24 , 24 , 24 , 24]
            
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index - 18) 
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 

        # สถานีปลายทาง คือ เอกมัย , พระโขนง , อ่อนนุช
        if end_station in [station_list[31] , station_list[32] , station_list[33]]:
            if result[0][4] == '':
                price = 47
            elif 60 > result[0][4] > 23: 
                price = 47
            elif 23 >= result[0][4] >= 0: 
                price = 47
            else: 
                price = 24

        # สถานีปลายทาง คือ บางจาก - เคหะ (ที่เขียนในโค้ด เป็น เคหะ แล้วไป บางจาก)
        if end_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35] , station_list[34]]:
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

        # สถานีปลายทาง คิอ สนามกีฬาแห่งชาติ 
        if end_station in [station_list[48]]:
            if result[0][4] == '':
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47]
            elif 60 > result[0][4] > 23: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47]
            elif 23 >= result[0][4] >= 0: 
                fares = [25 , 28 , 32 , 35 , 40 , 43 , 47 , 47]
            else: 
                fares = [13 , 14 , 16 , 18 , 20 , 22 , 24 , 24]
                
            start_index = station_list.index(start_station)
            end_index = station_list.index(end_station)
            distance = abs(start_index - end_index) 
            print(start_index)
            print(end_index)
            print(distance)
            # Calculate fare based on distance traveled
            if distance <= len(fares):
                price = fares[distance-1]
            else:
                price = fares[-1] 
        
    # หากจุดเริ่มต้น จาก โพธิ์นิมิตร ถึง บางหว้า 
    if start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
       # สถานีปลายทาง คือ คูคต - สนามกีฬา
        if end_station in [station_list[0] , station_list[1] , station_list[2] , station_list[3] , station_list[4] , station_list[5] , station_list[6] , station_list[7] ,station_list[8] , station_list[9] , station_list[10] , station_list[11] , station_list[12] , station_list[13] , station_list[14] , station_list[15] , station_list[16] , station_list[17] , station_list[18] , station_list[19] , station_list[20] , station_list[21] , station_list[22] , station_list[23] , station_list[24] , station_list[25] , station_list[26] , station_list[27] , station_list[28] , station_list[29] , station_list[30] , station_list[31] , station_list[32] , station_list[33] , station_list[34] , station_list[35] , station_list[36] , station_list[37] , station_list[38] , station_list[39] , station_list[40] , station_list[41] , station_list[42] , station_list[43] , station_list[44] , station_list[45] , station_list[46] , station_list[47] , station_list[48]]:
            if result[0][4] == '':
                price = 62
            elif 60 > result[0][4] > 23: 
                price = 62
            elif 23 >= result[0][4] >= 0: 
                price = 57
            else: 
                price = 31

    if start_station in [station_list[27]]: 
        if end_station in [station_list[33]]: 
            if result[0][4] == '':
                price = 17
            elif 60 > result[0][4] > 23: 
                price = 17
            elif 23 >= result[0][4] >= 0: 
                price = 17
            else: 
                price = 9

    # คำนวณสถานีพิเศษ สายสีทอง 
    if end_station in [station_list[61] , station_list[62] , station_list[63]]:   
        # จากสถานี สยาม ไป สายสีทอง    
        if start_station in [station_list[24]]: 
            if result[0][4] == '':
                price = 43 + 16
            elif 60 > result[0][4] > 23: 
                price = 43 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 43 + 16
            else: 
                price = 22 + 8
        
        # จากสถานี เคหะ - บางจาก ไป สายสีทอง
        elif start_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35] , station_list[34]]:
            if result[0][4] == '':
                price = 62 + 16
            elif 60 > result[0][4] > 23: 
                price = 62 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 57 + 16
            else: 
                price = 31 + 8

        # จากสถานี ราชดำริ ไปสายสีทอง
        elif start_station in [station_list[49]]: 
            if result[0][4] == '':
                price = 40 + 16
            elif 60 > result[0][4] > 23: 
                price = 40 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 40 + 16
            else: 
                price = 20 + 8

        # จากสถานี ศาลาแดง ไปสายสีทอง
        elif start_station in [station_list[50]]: 
            if result[0][4] == '':
                price = 35 + 16
            elif 60 > result[0][4] > 23: 
                price = 35 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 35 + 16
            else: 
                price = 18 + 8

        # จากสถานี ช่องนนทรี ไปสายสีทอง
        elif start_station in [station_list[51]]: 
            if result[0][4] == '':
                price = 32 + 16
            elif 60 > result[0][4] > 23: 
                price = 32 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 32 + 16
            else: 
                price = 16 + 8

        # จากสถานี เซนต์หลุยส์ ไปสายสีทอง
        elif start_station in [station_list[52]]: 
            if result[0][4] == '':
                price = 28 + 16
            elif 60 > result[0][4] > 23: 
                price = 28 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 28 + 16
            else: 
                price = 14 + 8

        # จากสถานี สุรศักดิ์ ไปสายสีทอง
        elif start_station in [station_list[53]]: 
            if result[0][4] == '':
                price = 25 + 16
            elif 60 > result[0][4] > 23: 
                price = 25 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 25 + 16
            else: 
                price = 13 + 8

        # จากสถานี สะพานตากสิน , กรุงธนบุรี , วนเวียนใหญ่ ไปสายสีทอง
        elif start_station in [station_list[54] , station_list[55] , station_list[56]]: 
            if result[0][4] == '':
                price = 17 + 16
            elif 60 > result[0][4] > 23: 
                price = 17 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 17 + 16
            else: 
                price = 9 + 8

        # จากสถานี โพธิ์นิมิตร - บางหว้า ไป สายสีทอง
        elif start_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
            if result[0][4] == '':
                price = 32 + 16
            elif 60 > result[0][4] > 23: 
                price = 32 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 27 + 16
            else: 
                price = 16 + 8

        # จากสายสีทอง ไป สายสีทอง 
        elif start_station in [station_list[61] , station_list[62] , station_list[63]]: 
            if result[0][4] == '':
                price = 16
            elif 60 > result[0][4] > 23: 
                price = 16
            elif 23 >= result[0][4] >= 0: 
                price = 16
            else: 
                price = 8

        # จาก สถานี คุคต - ราชเทวี , ชิดลม - อ่อนนุช , สนามกีฬา ไป สายสีทอง
        else:
            if result[0][4] == '':
                price = 47 + 16
            elif 60 > result[0][4] > 23: 
                price = 47 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 47 + 16
            else: 
                price = 24 + 8
    


    # คำนวณสถานีพิเศษ สายสีทอง 
    if start_station in [station_list[61] , station_list[62] , station_list[63]]:   
        # จากสายสีทอง ไป สยาม
        if end_station in [station_list[24]]: 
            if result[0][4] == '':
                price = 43 + 16
            elif 60 > result[0][4] > 23: 
                price = 43 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 43 + 16
            else: 
                price = 22 + 8
        
        # จากสายสีทอง ไป เคหะ - บางจาก 
        elif end_station in [station_list[47] , station_list[46] , station_list[45] , station_list[44] , station_list[43] , station_list[42] , station_list[41] , station_list[40] , station_list[39] , station_list[38] , station_list[37] , station_list[36] , station_list[35] , station_list[34]]:
            if result[0][4] == '':
                price = 62 + 16
            elif 60 > result[0][4] > 23: 
                price = 62 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 57 + 16
            else: 
                price = 31 + 8

        # จากสายสีทอง ไป ราชดำริ 
        elif end_station in [station_list[49]]: 
            if result[0][4] == '':
                price = 40 + 16
            elif 60 > result[0][4] > 23: 
                price = 40 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 40 + 16
            else: 
                price = 20 + 8

        # จากสายสีทอง ไป ศาลาแดง 
        elif end_station in [station_list[50]]: 
            if result[0][4] == '':
                price = 35 + 16
            elif 60 > result[0][4] > 23: 
                price = 35 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 35 + 16
            else: 
                price = 18 + 8

        # จากสายสีทอง ไป ช่องนนทรี 
        elif end_station in [station_list[51]]: 
            if result[0][4] == '':
                price = 32 + 16
            elif 60 > result[0][4] > 23: 
                price = 32 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 32 + 16
            else: 
                price = 16 + 8

        # จากสายสีทอง ไป เซนต์หลุยส์ 
        elif end_station in [station_list[52]]: 
            if result[0][4] == '':
                price = 28 + 16
            elif 60 > result[0][4] > 23: 
                price = 28 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 28 + 16
            else: 
                price = 14 + 8

        # จากสายสีทอง ไป สุรศักดิ์ 
        elif end_station in [station_list[53]]: 
            if result[0][4] == '':
                price = 25 + 16
            elif 60 > result[0][4] > 23: 
                price = 25 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 25 + 16
            else: 
                price = 13 + 8

        # จากสายสีทอง ไป สะพานตากสิน , กรุงธนบุรี , วนเวียนใหญ่ 
        elif end_station in [station_list[54] , station_list[55] , station_list[56]]: 
            if result[0][4] == '':
                price = 17 + 16
            elif 60 > result[0][4] > 23: 
                price = 17 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 17 + 16
            else: 
                price = 9 + 8

        # จากสายสีทอง ไป โพธิ์นิมิตร - บางหว้า 
        elif end_station in [station_list[57] , station_list[58] , station_list[59] , station_list[60]]:
            if result[0][4] == '':
                price = 32 + 16
            elif 60 > result[0][4] > 23: 
                price = 32 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 27 + 16
            else: 
                price = 16 + 8

        # จากสายสีทอง ไป สายสีทอง 
        elif end_station in [station_list[61] , station_list[62] , station_list[63]]: 
            if result[0][4] == '':
                price = 16
            elif 60 > result[0][4] > 23: 
                price = 16
            elif 23 >= result[0][4] >= 0: 
                price = 16
            else: 
                price = 8

        # จากสายสีทอง ไป สถานี คุคต - ราชเทวี , ชิดลม - อ่อนนุช , สนามกีฬา 
        else:
            if result[0][4] == '':
                price = 47 + 16
            elif 60 > result[0][4] > 23: 
                price = 47 + 16
            elif 23 >= result[0][4] >= 0: 
                price = 47 + 16
            else: 
                price = 24 + 8

    if start_station == end_station: 
        price = 0
    return price 

def calculate_and_show_fare():
    global start_station , end_station , fare

    try: 
        start_station = start_station_combo.get()
        end_station = end_station_combo.get()

        if start_station == "" or start_station == " == กรุณาเลือกสถานีต้นทาง ==": 
            messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีต้นทาง")

        elif end_station == "" or end_station == " == กรุณาเลือกสถานีปลายทาง ==": 
            messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีปลายทาง")    
        
        elif start_station == end_station: 
            messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีที่แตกต่างกัน")

        else:
            messagebox.showinfo("Skytrain App says : " , "ข้อมูลถูกต้อง กดยืนยันเพื่อเข้าสู่หน้าคำนวณราคา")
            calculate_price_detail()
            
    except ValueError: 
        messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีต้นทาง")   

def calculate_price_detail(): 
    global background_right_bts_1 , background_price_bts , text_start , text_end , fare
    background_right_top_bts.grid_forget()
    background_widget_bts.grid_forget()
    
    background_right_bts_1 = tk.Frame(root , background = "#F2F2F2")
    background_right_bts_1.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_bts_1.rowconfigure(0 , weight = 0)
    background_right_bts_1.rowconfigure(1 , weight = 5)
    background_right_bts_1.columnconfigure(0 , weight = 5)

    background_right_top_bts_1 = tk.Frame(background_right_bts_1 , background = '#FFFFFF')
    background_right_top_bts_1.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_bts_1.rowconfigure(0 , weight = 1)
    background_right_top_bts_1.columnconfigure(0 , weight = 1)

    background_price_bts = tk.Frame(root , background = "#25519A")
    background_price_bts.grid(row = 1 , column = 1 , sticky = 's')
    background_price_bts.rowconfigure(0 , weight = 0)
    background_price_bts.rowconfigure(1 , weight = 0)
    background_price_bts.rowconfigure(2 , weight = 0)
    background_price_bts.rowconfigure(3 , weight = 0)
    background_price_bts.rowconfigure(4 , weight = 0)
    background_price_bts.rowconfigure(5 , weight = 0)
    background_price_bts.rowconfigure(6 , weight = 0)
    background_price_bts.rowconfigure(7 , weight = 0)
    background_price_bts.columnconfigure(0 , weight = 1)
    background_price_bts.columnconfigure(1 , weight = 1)
    
    if start_station in ['[G1] กรุงธนบุรี', '[G2] เจริญนคร', '[G3] คลองสาน']:
        if start_station == '[G1] กรุงธนบุรี':
            text_start = "สถานีกรุงธนบุรี (Gold Line) | Krung Thon Buri (Gold Line)"
        elif start_station == '[G2] เจริญนคร':
            text_start = "สถานีเจริญนคร | Charoen Nakhon"
        else:
            text_start = "สถานีคลองสาน | Khlong San"
        background_color_start = "#A88B34"

    elif start_station in ['[W1] สนามกีฬาแห่งชาติ', '[S1] ราชดำริ', '[S2] ศาลาแดง', '[S3] ช่องนนทรี', '[S4] เซนต์หลุยส์', '[S5] สุรศักดิ์', '[S6] สะพานตากสิน', '[S7] กรุงธนบุรี', '[S8] วงเวียนใหญ่', '[S9] โพธิ์นิมิตร', '[S10] ตลาดพลู', '[S11] วุฒากาศ', '[S12] บางหว้า']:
        if start_station == '[W1] สนามกีฬาแห่งชาติ':
            text_start = "สถานีสนามกีฬาแห่งชาติ | National Stadium"

        elif start_station == '[S1] ราชดำริ':
            text_start = "สถานีราชดำริ | Ratchadamri"

        elif start_station == '[S2] ศาลาแดง':
            text_start = "สถานีศาลาแดง | Sala Daeng"

        elif start_station == '[S3] ช่องนนทรี':
            text_start = "สถานีช่องนนทรี | Chong Nonsi"

        elif start_station == '[S4] เซนต์หลุยส์':
            text_start = "สถานีเซนต์หลุยส์ | Saint Louis"

        elif start_station == '[S5] สุรศักดิ์':
            text_start = "สถานีสุรศักดิ์ | Surasak"

        elif start_station == '[S6] สะพานตากสิน':
            text_start = "สถานีสะพานตากสิน | Saphan Taksin"

        elif start_station == '[S7] กรุงธนบุรี':
            text_start = "สถานีกรุงธนบุรี | Krung Thon Buri"

        elif start_station == '[S8] วงเวียนใหญ่':
            text_start = "สถานีวงเวียนใหญ่ | Wongwian Yai"

        elif start_station == '[S9] โพธิ์นิมิตร':
            text_start = "สถานีโพธิ์นิมิตร | Pho Nimit"

        elif start_station == '[S10] ตลาดพลู':
            text_start = "สถานีตลาดพลู | Talat Phlu"

        elif start_station == '[S11] วุฒากาศ':
            text_start = "สถานีวุฒากาศ | Wutthakat"

        else:
            text_start = "สถานีบางหว้า | Bang Wa"
        background_color_start = "#00807D"

    else: 
        if start_station == '[N24] คูคต': 
            text_start = "สถานีคูคต | Khu Khot"

        elif start_station == '[N23] แยก คปอ.': 
            text_start = "สถานีแยก คปอ. | Yaek Kor Por Aor"

        elif start_station == '[N22] พิพิธภัณฑ์กองทัพอากาศ':
            text_start = "สถานีพิพิธภัณฑ์กองทัพอากาศ | Royal Thai Air Force Museum"

        elif start_station == '[N21] โรงพยาบาลภูมิพลอดุลยเดช':
            text_start = "สถานีโรงพยาบาลภูมิพลอดุลยเดช | Bhumibol Adulyadej Hospital"

        elif start_station == '[N20] สะพานใหม่':
            text_start = "สถานีสะพานใหม่ | Saphan Mai"

        elif start_station == '[N19] สายหยุด':
            text_start = "สถานีสายหยุด | Sai Yud"

        elif start_station == '[N18] พหลโยธิน 59':
            text_start = "สถานีพหลโยธิน 59 | Phahon Yothin 59"

        elif start_station == '[N17] วัดพระศรีมหาธาตุ':
            text_start = "สถานีวัดพระศรีมหาธาตุ | Wat Phra Sri Mahathat"

        elif start_station == '[N16] กรมทหารราบที่ 11':
            text_start = "สถานีกรมทหารราบที่ 11 | 11th Infantry Regiment"

        elif start_station == '[N15] บางบัว':
            text_start = "สถานีบางบัว | Bang Bua"

        elif start_station == '[N14] กรมป่าไม้':
            text_start = "สถานีกรมป่าไม้ | Royal Forest Department"

        elif start_station == '[N13] มหาวิทยาลัยเกษตรศาสตร์':
            text_start = "สถานีมหาวิทยาลัยเกษตรศาสตร์ | Kasetsart University"

        elif start_station == '[N12] เสนานิคม':
            text_start = "สถานีเสนานิคม | Sena Nikhom"

        elif start_station == '[N11] รัชโยธิน':
            text_start = "สถานีรัชโยธิน | Ratchayothin"

        elif start_station == '[N10] พหลโยธิน 24':
            text_start = "สถานีพหลโยธิน 24 | Phahon Yothin 24"

        elif start_station == '[N9] ห้าแยกลาดพร้าว':
            text_start = "สถานีห้าแยกลาดพร้าว | Ha Yaek Lat Phrao"

        elif start_station == '[N8] หมอชิต':
            text_start = "สถานีหมอชิต | Mo Chit"

        elif start_station == '[N7] สะพานควาย':
            text_start = "สถานีสะพานควาย | Saphan Khwai"

        elif start_station == '[N6] เสนาร่วม':
            text_start = "สถานีเสนาร่วม | Sana Rom"

        elif start_station == '[N5] อารีย์':
            text_start = "สถานีอารีย์ | Ari"

        elif start_station == '[N4] สนามเป้า':
            text_start = "สถานีสนามเป้า | Sanam Pao"

        elif start_station == '[N3] อนุสาวรีย์ชัยสมรภูมิ':
            text_start = "สถานีอนุสาวรีย์ชัยสมรภูมิ | Victory Monument"

        elif start_station == '[N2] พญาไท':
            text_start = "สถานีพญาไท | Phaya Thai"

        elif start_station == '[N1] ราชเทวี':
            text_start = "สถานีราชเทวี | Ratchathewi"

        elif start_station == '[E1] ชิดลม':
            text_start = "สถานีชิดลม | Chit Lom"

        elif start_station == '[E2] เพลินจิต':
            text_start = "สถานีเพลินจิต | Phloen Chit"

        elif start_station == '[E3] นานา':
            text_start = "สถานีนานา | Nana"

        elif start_station == '[E4] อโศก':
            text_start = "สถานีอโศก | Asok"

        elif start_station == '[E5] พร้อมพงษ์':
            text_start = "สถานีพร้อมพงษ์ | Phrom Phong"

        elif start_station == '[E6] ทองหล่อ':
            text_start = "สถานีทองหล่อ | Thong Lo"

        elif start_station == '[E7] เอกมัย':
            text_start = "สถานีเอกมัย | Ekkamai"

        elif start_station == '[E8] พระโขนง':
            text_start = "สถานีพระโขนง | Phra Khanong"
            
        elif start_station == '[E9] อ่อนนุช':
            text_start = "สถานีอ่อนนุช | On Nut"

        elif start_station == '[E10] บางจาก':
            text_start = "สถานีบางจาก | Bang Chak"

        elif start_station == '[E11] ปุณณวิถี':
            text_start = "สถานีปุณณวิถี | Punnawithi"

        elif start_station == '[E12] อุดมสุข':
            text_start = "สถานีอุดมสุข | Udom Suk"

        elif start_station == '[E13] บางนา':
            text_start = "สถานีบางนา | Bang Na"

        elif start_station == '[E14] แบริ่ง':
            text_start = "สถานีแบริ่ง | Bearing"

        elif start_station == '[E15] สำโรง':
            text_start = "สถานีสำโรง | Samrong"

        elif start_station == '[E16] ปู่เจ้า':
            text_start = "สถานีปู่เจ้า | Pu Chao"

        elif start_station == '[E17] ช้างเอราวัณ':
            text_start = "สถานีช้างเอราวัณ | Chang Erawan"

        elif start_station == '[E18] โรงเรียนนายเรือ':
            text_start = "สถานีโรงเรียนนายเรือ | Royal Thai Naval Academy"

        elif start_station == '[E19] ปากน้ำ':
            text_start = "สถานีปากน้ำ | Pak Nam"

        elif start_station == '[E20] ศรีนครินทร์':
            text_start = "สถานีศรีนครินทร์ | Srinagarindra"

        elif start_station == '[E21] แพรกษา':
            text_start = "สถานีแพรกษา | Phraek Sa"

        elif start_station == '[E22] สายลวด':
            text_start = "สถานีสายลวด | Sai Luat"

        elif start_station == '[E23] เคหะ':
            text_start = "สถานีเคหะฯ | Kheha"
            
        else:
            text_start = "สถานีสยาม | Siam"
        background_color_start = "#7AB420"
    

    if end_station in ['[G1] กรุงธนบุรี' , '[G2] เจริญนคร' , '[G3] คลองสาน']:
        if end_station == '[G1] กรุงธนบุรี':
            text_end = "สถานีกรุงธนบุรี (Gold Line) | Krung Thon Buri (Gold Line)"
        elif end_station == '[G2] เจริญนคร':
            text_end = "สถานีเจริญนคร | Charoen Nakhon"
        else:
            text_end = "สถานีคลองสาน | Khlong San"
        background_color_end = "#A88B34"

    elif end_station in ['[W1] สนามกีฬาแห่งชาติ' , '[S1] ราชดำริ' , '[S2] ศาลาแดง' , '[S3] ช่องนนทรี' , '[S4] เซนต์หลุยส์' , '[S5] สุรศักดิ์' , '[S6] สะพานตากสิน' , '[S7] กรุงธนบุรี' , '[S8] วงเวียนใหญ่' , '[S9] โพธิ์นิมิตร' , '[S10] ตลาดพลู' , '[S11] วุฒากาศ' , '[S12] บางหว้า']:
        if end_station == '[W1] สนามกีฬาแห่งชาติ':
            text_end = "สถานีสนามกีฬาแห่งชาติ | National Stadium"

        elif end_station == '[S1] ราชดำริ':
            text_end = "สถานีราชดำริ | Ratchadamri"

        elif end_station == '[S2] ศาลาแดง':
            text_end = "สถานีศาลาแดง | Sala Daeng"

        elif end_station == '[S3] ช่องนนทรี':
            text_end = "สถานีช่องนนทรี | Chong Nonsi"

        elif end_station == '[S4] เซนต์หลุยส์':
            text_end = "สถานีเซนต์หลุยส์ | Saint Louis"

        elif end_station == '[S5] สุรศักดิ์':
            text_end = "สถานีสุรศักดิ์ | Surasak"
            
        elif end_station == '[S6] สะพานตากสิน':
            text_end = "สถานีสะพานตากสิน | Saphan Taksin"

        elif end_station == '[S7] กรุงธนบุรี':
            text_end = "สถานีกรุงธนบุรี | Krung Thon Buri"

        elif end_station == '[S8] วงเวียนใหญ่':
            text_end = "สถานีวงเวียนใหญ่ | Wongwian Yai"

        elif end_station == '[S9] โพธิ์นิมิตร':
            text_end = "สถานีโพธิ์นิมิตร | Pho Nimit"

        elif end_station == '[S10] ตลาดพลู':
            text_end = "สถานีตลาดพลู | Talat Phlu"

        elif end_station == '[S11] วุฒากาศ':
            text_end = "สถานีวุฒากาศ | Wutthakat"

        else:
            text_end = "สถานีบางหว้า | Bang Wa"
        background_color_end = "#00807D"

    else:
        if end_station == '[N24] คูคต': 
            text_end = "สถานีคูคต | Khu Khot"

        elif end_station == '[N23] แยก คปอ.': 
            text_end = "สถานีแยก คปอ. | Yaek Kor Por Aor"

        elif end_station == '[N22] พิพิธภัณฑ์กองทัพอากาศ':
            text_end = "สถานีพิพิธภัณฑ์กองทัพอากาศ | Royal Thai Air Force Museum"

        elif end_station == '[N21] โรงพยาบาลภูมิพลอดุลยเดช':
            text_end = "สถานีโรงพยาบาลภูมิพลอดุลยเดช | Bhumibol Adulyadej Hospital"

        elif end_station == '[N20] สะพานใหม่':
            text_end = "สถานีสะพานใหม่ | Saphan Mai"
        
        elif end_station == '[N19] สายหยุด':
            text_end = "สถานีสายหยุด | Sai Yud"

        elif end_station == '[N18] พหลโยธิน 59':
            text_end = "สถานีพหลโยธิน 59 | Phahon Yothin 59"

        elif end_station == '[N17] วัดพระศรีมหาธาตุ':
            text_end = "สถานีวัดพระศรีมหาธาตุ | Wat Phra Sri Mahathat"
        
        elif end_station == '[N16] กรมทหารราบที่ 11':
            text_end = "สถานีกรมทหารราบที่ 11 | 11th Infantry Regiment"

        elif end_station == '[N15] บางบัว':
            text_end = "สถานีบางบัว | Bang Bua"

        elif end_station == '[N14] กรมป่าไม้':
            text_end = "สถานีกรมป่าไม้ | Royal Forest Department"

        elif end_station == '[N13] มหาวิทยาลัยเกษตรศาสตร์':
            text_end = "สถานีมหาวิทยาลัยเกษตรศาสตร์ | Kasetsart University"

        elif end_station == '[N12] เสนานิคม':
            text_end = "สถานีเสนานิคม | Sena Nikhom"

        elif end_station == '[N11] รัชโยธิน':
            text_end = "สถานีรัชโยธิน | Ratchayothin"

        elif end_station == '[N10] พหลโยธิน 24':
            text_end = "สถานีพหลโยธิน 24 | Phahon Yothin 24"

        elif end_station == '[N9] ห้าแยกลาดพร้าว':
            text_end = "สถานีห้าแยกลาดพร้าว | Ha Yaek Lat Phrao"

        elif end_station == '[N8] หมอชิต':
            text_end = "สถานีหมอชิต | Mo Chit"

        elif end_station == '[N7] สะพานควาย':
            text_end = "สถานีสะพานควาย | Saphan Khwai"

        elif end_station == '[N6] เสนาร่วม':
            text_end = "สถานีเสนาร่วม | Sana Rom"

        elif end_station == '[N5] อารีย์':
            text_end = "สถานีอารีย์ | Ari"

        elif end_station == '[N4] สนามเป้า':
            text_end = "สถานีสนามเป้า | Sanam Pao"

        elif end_station == '[N3] อนุสาวรีย์ชัยสมรภูมิ':
            text_end = "สถานีอนุสาวรีย์ชัยสมรภูมิ | Victory Monument"

        elif end_station == '[N2] พญาไท':
            text_end = "สถานีพญาไท | Phaya Thai"

        elif end_station == '[N1] ราชเทวี':
            text_end = "สถานีราชเทวี | Ratchathewi"

        elif end_station == '[E1] ชิดลม':
            text_end = "สถานีชิดลม | Chit Lom"

        elif end_station == '[E2] เพลินจิต':
            text_end = "สถานีเพลินจิต | Phloen Chit"

        elif end_station == '[E3] นานา':
            text_end = "สถานีนานา | Nana"

        elif end_station == '[E4] อโศก':
            text_end = "สถานีอโศก | Asok"

        elif end_station == '[E5] พร้อมพงษ์':
            text_end = "สถานีพร้อมพงษ์ | Phrom Phong"

        elif end_station == '[E6] ทองหล่อ':
            text_end = "สถานีทองหล่อ | Thong Lo"

        elif end_station == '[E7] เอกมัย':
            text_end = "สถานีเอกมัย | Ekkamai"

        elif end_station == '[E8] พระโขนง':
            text_end = "สถานีพระโขนง | Phra Khanong"

        elif end_station == '[E9] อ่อนนุช':
            text_end = "สถานีอ่อนนุช | On Nut"

        elif end_station == '[E10] บางจาก':
            text_end = "สถานีบางจาก | Bang Chak"

        elif end_station == '[E11] ปุณณวิถี':
            text_end = "สถานีปุณณวิถี | Punnawithi"

        elif end_station == '[E12] อุดมสุข':
            text_end = "สถานีอุดมสุข | Udom Suk"

        elif end_station == '[E13] บางนา':
            text_end = "สถานีบางนา | Bang Na"

        elif end_station == '[E14] แบริ่ง':
            text_end = "สถานีแบริ่ง | Bearing"

        elif end_station == '[E15] สำโรง':
            text_end = "สถานีสำโรง | Samrong"

        elif end_station == '[E16] ปู่เจ้า':
            text_end = "สถานีปู่เจ้า | Pu Chao"

        elif end_station == '[E17] ช้างเอราวัณ':
            text_end = "สถานีช้างเอราวัณ | Chang Erawan"

        elif end_station == '[E18] โรงเรียนนายเรือ':
            text_end = "สถานีโรงเรียนนายเรือ | Royal Thai Naval Academy"

        elif end_station == '[E19] ปากน้ำ':
            text_end = "สถานีปากน้ำ | Pak Nam"

        elif end_station == '[E20] ศรีนครินทร์':
            text_end = "สถานีศรีนครินทร์ | Srinagarindra"

        elif end_station == '[E21] แพรกษา':
            text_end = "สถานีแพรกษา | Phraek Sa"

        elif end_station == '[E22] สายลวด':
            text_end = "สถานีสายลวด | Sai Luat"

        elif end_station == '[E23] เคหะ':
            text_end = "สถานีเคหะฯ | Kheha"
            
        else:
            text_end = "สถานีสยาม | Siam"
        background_color_end = "#7AB420"
    
    tk.Label(background_right_bts_1 , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news' , ipady = 15)

    tk.Label(background_right_top_bts_1 , text = "•  Calculate BTS [menu] 🚄" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_bts_1 , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Label(background_price_bts , text = "Calculate Prices" , background = "#25519A" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'nw' , padx = 25 , pady = 11)
    
    tk.Label(background_price_bts , text = "Start Station" , background = "#25519A" , foreground = "#C2CCFF" , font = "Calibri 16 bold").grid(row = 1 , column = 0 , sticky = 'nw' , padx = 55 , pady = 12)
    background_start_station = tk.Frame(background_price_bts , background = background_color_start)
    background_start_station.grid(row = 2 , columnspan = 2 , sticky = 'news' , padx = 45)
    background_start_station.rowconfigure(0 , weight = 1)
    background_start_station.columnconfigure(0 , weight = 1)
    tk.Label(background_start_station , text = text_start , background = background_color_start , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 0 , column = 0 , sticky = 'nws' , padx = 25 , pady = 10)
    
    print(start_station)
    print(end_station)
    
    tk.Label(background_price_bts , text = "End Station" , background = "#25519A" , foreground = "#C2CCFF" , font = "Calibri 16 bold").grid(row = 3 , column = 0 , sticky = 'nw' , padx = 55 , pady = 12)
    background_end_station = tk.Frame(background_price_bts , background = background_color_end)
    background_end_station.grid(row = 4 , columnspan = 2 , sticky = 'news' , padx = 45)
    background_end_station.rowconfigure(0 , weight = 1)
    background_end_station.columnconfigure(0 , weight = 1)
    tk.Label(background_end_station , text = text_end , background = background_color_end , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 0 , column = 0 , sticky = 'nws' , padx = 25 , pady = 10)

    fare = sky_train(start_station , end_station)

    if result[0][4] == "": 
        text = f"จาก '{start_station}' ไป '{end_station}' \nโดยสั่งบัตรทั้งหมด {entry_number.get()} บัตรจะมีราคา {fare * int(entry_number.get())} บาท (บัตรละ {fare} บาท)"
        tk.Label(background_price_bts , text = text , background = "#25519A" , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 5 , columnspan = 2 , pady = 10 , sticky = 'news')

    else: 
        text = f"จาก '{start_station}' ไป '{end_station}' \nเนื่องจากคุณอายุ {result[0][4]} ปี โดยสั่งบัตรทั้งหมด {entry_number.get()} บัตร ทำให้มีราคาอยู่ที่ {fare * int(entry_number.get())} บาท (บัตรละ {fare} บาท)"
        tk.Label(background_price_bts , text = text , background = "#25519A" , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 5 , columnspan = 2 , pady = 20 , sticky = 'news')

    tk.Button(background_price_bts , image = image_check_information , bd = 0 , activebackground = "#25519A" , background = "#25519A" , command = thank_you_order).grid(row = 6 , columnspan = 2 , sticky = 'ew')

    tk.Label(background_price_bts , image = image_veg , background = "#25519A").grid(row = 7 , columnspan = 2)

def thank_you_order(): 
    global result_2 , total_fare_bts
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 800  # Set the width of the window
    window_height = 770  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2)) - 35 

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    background_right_bts_1.grid_forget()
    background_price_bts.grid_forget()

    background_right_order = tk.Frame(root , background = "#F2F2F2")
    background_right_order.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_order.rowconfigure(0 , weight = 0)
    background_right_order.rowconfigure(1 , weight = 5)
    background_right_order.columnconfigure(0 , weight = 5)

    background_right_top_order = tk.Frame(background_right_order , background = '#FFFFFF')
    background_right_top_order.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_order.rowconfigure(0 , weight = 1)
    background_right_top_order.columnconfigure(0 , weight = 1)

    background_price_order = tk.Frame(root , background = "#25519A")
    background_price_order.grid(row = 1 , column = 1 , sticky = 's')
    background_price_order.rowconfigure(0 , weight = 0)
    background_price_order.rowconfigure(1 , weight = 0)
    background_price_order.rowconfigure(2 , weight = 0)
    background_price_order.rowconfigure(3 , weight = 0)
    background_price_order.columnconfigure(0 , weight = 1)
    background_price_order.columnconfigure(1 , weight = 1)
    
    tk.Label(background_right_top_order , text = "•  receipt [menu] 🧾" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_order , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Label(background_price_order , text = "Thank you for order!" , background = "#7AB420" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , columnspan = 2 , sticky = 'ews' , pady = 10 , ipady = 5)

    background_receipt = tk.Frame(background_price_order , background = "#FFFFFF")
    background_receipt.grid(row = 1 , columnspan = 2 , pady = 10)
    background_receipt.rowconfigure(0 , weight = 0)
    background_receipt.rowconfigure(1 , weight = 0)
    background_receipt.rowconfigure(2 , weight = 0)
    background_receipt.rowconfigure(3 , weight = 0)
    background_receipt.rowconfigure(4 , weight = 0)
    background_receipt.rowconfigure(5 , weight = 0)
    background_receipt.rowconfigure(6 , weight = 0)
    background_receipt.rowconfigure(7 , weight = 0)
    background_receipt.rowconfigure(8 , weight = 0)
    background_receipt.rowconfigure(9 , weight = 0)
    background_receipt.rowconfigure(10 , weight = 0)
    background_receipt.rowconfigure(11 , weight = 0)
    background_receipt.rowconfigure(12 , weight = 0)
    background_receipt.rowconfigure(13 , weight = 0)
    background_receipt.rowconfigure(14 , weight = 0)

    background_receipt.columnconfigure(0 , weight = 1)
    background_receipt.columnconfigure(1 , weight = 1)
    background_receipt.columnconfigure(2 , weight = 1)
    background_receipt.columnconfigure(3 , weight = 1)

    total_fare_bts = fare * int(entry_number.get())

    # Get the current time
    current_time = datetime.datetime.now()

    current_date = datetime.datetime.now().date()

    formatted_time = current_time.strftime("%H:%M:%S")

    sql = "INSERT INTO orders (Start_Station , End_Station , Cards , Prices , Date , Time , Username , Name , Sky_Train) VALUES (? , ? , ? , ? , ? , ? , ? , ? , ?)"

    cursor.execute(sql , [text_start , text_end , entry_number.get() , total_fare_bts , current_date , formatted_time , result[0][0] , f"{result[0][2]} {result[0][3]}" , "BTS"])
    
    database.commit()

    sql_select = "SELECT * FROM orders WHERE name = ? AND username = ? AND Sky_Train = ? ORDER BY id DESC"
    cursor.execute(sql_select, [f"{result[0][2]} {result[0][3]}", result[0][0] , "BTS"])
    result_2 = cursor.fetchall()

    tk.Label(background_receipt , text = "Sky Train Receipt" , background = "#FFFFFF" , font = ("Calibri" , 16 , "bold") , foreground = "#25519A").grid(row = 0 , columnspan = 4 , padx = 10 , sticky = 'ew')
    tk.Label(background_receipt , text = f"============================================\norder no. : {result_2[0][0]}\n============================================" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 14)).grid(row = 1 , columnspan = 4 , padx = 10 , sticky = 'n')
    tk.Label(background_receipt , text = "Code      |" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 0 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "Qty       |" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 1 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "Description       |" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 2 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "Price/Bath" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 3 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"{result_2[0][0]}       " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 0 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"{result_2[0][3]}       " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 1 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"BTS  Tickets         " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 2 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"{total_fare_bts}฿" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 3 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "-----------------------------------------------------------------" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 16)).grid(row = 6 , columnspan = 4 , padx = 10) 
    tk.Label(background_receipt , text = f"   • Start Station : {result_2[0][1]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Angsana new" , 12 , "bold")).grid(row = 7 , columnspan = 4 , padx = 10 , sticky = 'w')
    tk.Label(background_receipt , text = f"   • End Station   : {result_2[0][2]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Angsana new"  , 12 , "bold")).grid(row = 8 , columnspan = 4 , padx = 10 , sticky = 'w')

    if result[0][4] == '': 
        image_card = image_notmember 
        text_card = "  You have one-way ticket."
    elif 60 > result[0][4] > 23: 
        image_card = image_prepaid
        text_card = "  You have Prepaid ticket."
    elif 23 >= result[0][4] >= 0: 
        image_card = image_student
        text_card = "  You have Student ticket."
    else: 
        image_card = image_old
        text_card = "  You have OldCard ticket."
        
    tk.Label(background_receipt , image = image_card , text = text_card , compound = "left", foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 9 , columnspan = 4 , padx = 10 , sticky = 'new') 
    tk.Label(background_receipt , text = "-----------------------------------------------------------------" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 16)).grid(row = 10 , columnspan = 4 , padx = 10 , sticky = 'n')     
    tk.Label(background_receipt , text = "Date : " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 11 , column = 0 , padx = 10 , sticky = 'news')     
    tk.Label(background_receipt , text = f"{result_2[0][5]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 11 , column = 1 , padx = 10 , sticky = 'ws')     
    tk.Label(background_receipt , text = "Time : " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 12 , column = 0 , padx = 10 , sticky = 'news')     
    tk.Label(background_receipt , text = f"{result_2[0][6]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 12 , column = 1 , padx = 10 , sticky = 'ws')  
    tk.Label(background_receipt , text = f"Total" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 11 , column = 2  , padx = 10 , sticky = 'e' )  
    tk.Label(background_receipt , text = f"{total_fare_bts}฿" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 12 , column = 2 , padx = 10 , sticky = 'e')  
    tk.Label(background_receipt , text = "-----------------------------------------------------------------" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 16)).grid(row = 13 , columnspan = 4 , padx = 10)  
    tk.Label(background_receipt , text = "Thank you for order, We can't live without you!" , foreground = "#598723" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 14 , columnspan = 4 , padx = 10 , sticky = 'news')  
    
    tk.Button(background_price_order , image = image_check_history , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = detail_station_information).grid(row = 2 , column = 0 , pady = 10)
    tk.Button(background_price_order , image = image_back_to_bts_mrt , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = bts_mrt).grid(row = 2 , column = 1 , pady = 10)
    
    tk.Label(background_price_order , image = image_veg , background = "#25519A").grid(row = 3 , columnspan = 2)

def detail_station_information(): 
    global treeview_detail
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 1180  # Set the width of the window
    window_height = 720  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2)) - 35 

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    background_right_detail = tk.Frame(root , background = "#F2F2F2")
    background_right_detail.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_detail.rowconfigure(0 , weight = 0)
    background_right_detail.rowconfigure(1 , weight = 5)
    background_right_detail.columnconfigure(0 , weight = 5)

    background_right_top_detail = tk.Frame(background_right_detail , background = '#FFFFFF')
    background_right_top_detail.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_detail.rowconfigure(0 , weight = 1)
    background_right_top_detail.columnconfigure(0 , weight = 1)

    background_detail_bts = tk.Frame(root , background = "#25519A")
    background_detail_bts.place(x = 64 , y = 130 , relwidth = 0.946 , relheight = 0.82, anchor = "nw")
    background_detail_bts.rowconfigure(0 , weight = 1)
    background_detail_bts.rowconfigure(1 , weight = 0)
    background_detail_bts.columnconfigure(0 , weight = 0)
    background_detail_bts.columnconfigure(1 , weight = 0)
    background_detail_bts.columnconfigure(2 , weight = 0)

    tk.Label(background_right_detail , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')

    tk.Label(background_right_top_detail , text = "•  Detail BTS [menu] 🚄" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_detail , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Label(background_detail_bts , text = "Detail Station and information" , background = "#7AB420" , foreground = "#FFFFFF" , font = "Calibri 16 bold").place(relx = 0.5 , rely = 0.05 , anchor = "center" , relwidth = 1 , relheight = 0.08)

    scrollbary = tk.Scrollbar(background_detail_bts , orient = 'vertical', width = 20)
    scrollbary.place(x = -4 , relx = 0.992 , rely = 0.39 , relheight = 0.558 , anchor = 'e')

    treeview_detail = ttk.Treeview(background_detail_bts, columns = ("c1", "c2", "c3", "c4", "c5", "c6" , "c7"), height = 8)
    treeview_detail.place(relx = 0.485, rely = 0.39 , anchor = "center" , relwidth = 0.95 , relheight = 0.56)
    
    # Create a style object
    style = ttk.Style()

    # Configure the style to increase the line spacing
    style.configure("Treeview", rowheight = 30)  # Adjust the rowheight value as per your requirement

    # Apply the style to the Treeview widget
    treeview_detail["style"] = "Treeview"
    
    treeview_detail.configure(yscrollcommand = scrollbary.set)
    treeview_detail.configure(selectmode = "extended")
    scrollbary.configure(command = treeview_detail.yview)

    treeview_detail.heading('c1' , text = 'id' , anchor = 'center')
    treeview_detail.heading('c2' , text = 'Start Station' , anchor = 'w')
    treeview_detail.heading('c3' , text = 'End Station' , anchor = 'w')
    treeview_detail.heading('c4' , text = 'Cards' , anchor = 'center')
    treeview_detail.heading('c5' , text = 'Prices' , anchor = 'center')
    treeview_detail.heading('c6' , text = 'Date' , anchor = 'w')
    treeview_detail.heading('c7' , text = 'Time' , anchor = 'w')

    treeview_detail.column('c1' , width = 50 , anchor = ('center') , minwidth = 0 )
    treeview_detail.column('c2' , width = 365 , minwidth = 0)
    treeview_detail.column('c3' , width = 365 , minwidth = 0)
    treeview_detail.column('c4' , width = 50 , anchor = 'center' , minwidth = 0)
    treeview_detail.column('c5' , width = 40 , anchor = 'center' , minwidth = 0)
    treeview_detail.column('c6' , width = 70 , minwidth = 0)
    treeview_detail.column('c7' , width = 60 , minwidth = 0)
    treeview_detail.column('#0' , width = 0 , stretch = False)

    font_style = ("Angsana new" , 14)

    # Reverse the order of the result list
    result_2.reverse()

    # Clear the Treeview before inserting new data
    treeview_detail.delete(*treeview_detail.get_children())
    
    for index, data in enumerate(result_2):
        item = treeview_detail.insert('', 0, values = (data[0], data[1], data[2], data[3], data[4], data[5] , data[6]), tags=("custom_font"))

    database.commit()

    # Apply the font to the inserted item
    treeview_detail.tag_configure("custom_font" , font = font_style)  

    # Set the focus on the most recent data
    recent_item = treeview_detail.get_children()[0]  # Get the item identifier of the first item
    treeview_detail.selection_set(recent_item)  # Set the focus on the recent item

    treeview_detail.bind('<<TreeviewSelect>>', single_click)

    tk.Button(background_detail_bts , image = image_delete_history , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = delete_selected).place(rely = 0.76 , relx = 0.05 , anchor = 'w')
    tk.Button(background_detail_bts , image = image_exit , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command =  exit_program).place(rely = 0.76 , relx = 0.49 , anchor = 'center')
    tk.Button(background_detail_bts , image = image_back_to_bts_mrt , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = bts_mrt).place(rely = 0.76 , relx = 0.8 , anchor = 'center')

    tk.Label(background_detail_bts , text = "Thank you for using our application, we can't live without you!" , background = "#7AB420" , foreground = "#FFFFFF" , font = "Calibri 16 bold").place(relx = 0.5 , rely = 0.95 , anchor = "center" , relwidth = 1 , relheight = 0.08)

def exit_program():
    question = messagebox.askquestion("Skytrain App says : " , "Are you sure to Exit Application?")

    if question == "yes":
        exit()
    
def single_click(event): 
    global values
    selected_item = treeview_detail.selection()
    if not selected_item:
        return
    
    item = selected_item[0]
    values = treeview_detail.item(item, 'values')

def delete_selected():
    confirm = messagebox.askquestion("Skytrain App says:", "Confirm to Delete (Yes / No)!")
    if confirm == 'yes': 
        sql_delete = "DELETE FROM orders WHERE id = ?;"
        cursor.execute(sql_delete, [values[0]])
        database.commit()
        
        # Clear the existing data in the treeview_detail
        treeview_detail.delete(*treeview_detail.get_children())

        sql_select = "SELECT * FROM orders WHERE username = ? AND Sky_Train = ?;"
        cursor.execute(sql_select , [entry_login_username.get() , "BTS"])
        result_3 = cursor.fetchall()

        for index, data in enumerate(result_3):
            item = treeview_detail.insert('', 0, values = (data[0], data[1], data[2], data[3], data[4], data[5], data[6]), tags=("custom_font"))

        messagebox.showinfo("Admin:", "Delete Successfully!!")

def function_MRT(): 
    global background_right_mrt , background_widget_mrt , background_right_top_mrt , entry_number_mrt
    root.option_add("*font" , ("Angsana new" , 16))
    background_right_bts_car.grid_forget()
    background_widget_bts_car.grid_forget()
    
    background_right_mrt = tk.Frame(root , background = "#F2F2F2")
    background_right_mrt.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_mrt.rowconfigure(0 , weight = 0)
    background_right_mrt.rowconfigure(1 , weight = 5)
    background_right_mrt.columnconfigure(0 , weight = 5)

    background_right_top_mrt = tk.Frame(background_right_mrt , background = '#FFFFFF')
    background_right_top_mrt.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_mrt.rowconfigure(0 , weight = 1)
    background_right_top_mrt.columnconfigure(0 , weight = 1)

    background_widget_mrt = tk.Frame(root , background = "#DCF3FF")
    background_widget_mrt.grid(row = 1 , column = 1 , sticky = 's')
    background_widget_mrt.rowconfigure(0 , weight = 0)
    background_widget_mrt.rowconfigure(1 , weight = 0)
    background_widget_mrt.rowconfigure(2 , weight = 0)
    background_widget_mrt.rowconfigure(3 , weight = 0)
    background_widget_mrt.rowconfigure(4 , weight = 0)
    background_widget_mrt.rowconfigure(5 , weight = 0)
    background_widget_mrt.rowconfigure(6 , weight = 0)
    background_widget_mrt.columnconfigure(0 , weight = 1)
    background_widget_mrt.columnconfigure(1 , weight = 1)

    tk.Label(background_right_mrt , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')

    tk.Label(background_right_top_mrt , text = "•  MRT 🚄" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_mrt , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)
    
    global start_station_combo_mrt , end_station_combo_mrt 

    # Create the station selection widgets
    start_station_label = ttk.Label(background_widget_mrt, text = "Start station:" , background = "#DCF3FF" , font = "Calibri 16 bold")
    start_station_label.grid(row = 0 , column = 0 , padx = 155 , sticky = 'nw' ,pady = 10)
    start_station_combo_mrt = ttk.Combobox(background_widget_mrt, values = ['ท่าพระ [BL01]' , 'จรัญฯ 13 [BL02]' , 'ไฟฉาย [BL03]' , 'บางขุนนนท์ [BL04]' , 'บางยี่ขัน [BL05]' , 'สิรินธร [BL06]' , 
    'บางพลัด [BL07]' , 'บางอ้อ [BL18]' , 'บางโพ [BL09]' , 'เตาปูน [BL10]' , 'บางซื่อ [BL11]' , 'กำแพงเพชร [BL12]' , 'สวนจตุจักร [BL13]' , 
    'พหลโยธิน [BL14]' , 'ลาดพร้าว [BL15]' , 'รัชดาภิเษก [BL16]' , 'สุทธิสาร [BL17]' ,'ห้วยขวาง [BL18]' , 'ศูนย์วัฒนธรรมแห่งประเทศไทย [BL19]' , 
    'พระราม 9 [BL20]' , 'เพชรบุรี [BL21]' ,'สุขุมวิท [BL22]' , 'ศูนย์การประชุมแห่งชาติสิริกิต์ [BL23]' , 'คลองเตย [BL24]' , 'ลุมพินี [BL25]', 
    'สีลม [BL26]' , 'สามย่าน [BL27]' , 'หัวลำโพง [BL28]' , 'วัดมังกร [BL29]' , 'สามยอด [BL30]' , 'สนามไชย [BL31]' , 'อิสรภาพ [BL32]' ,
    'บางไผ่ [BL33]' , 'บางหว้า [BL34]' , 'เพชรเกษม 48 [BL35]' , 'ภาษีเจริญ [BL36]' , 'บางแค [BL37]' , 'หลักสอง [BL38]'] , width = 50 , state = "readonly")
    start_station_combo_mrt.set(" == กรุณาเลือกสถานีต้นทาง ==")
    start_station_combo_mrt.grid(row = 1 , columnspan = 2 , padx = 5  , sticky = 'n')


    #s = ttk.Style()
    # s.theme_use('clam')

    end_station_label = tk.Label(background_widget_mrt , text = "End station:" , background = "#DCF3FF" , font = "Calibri 16 bold")
    end_station_label.grid(row = 2 , column = 0 , padx = 155 , sticky = 'nw' , pady = 10) 
    end_station_combo_mrt = ttk.Combobox(background_widget_mrt, background = "#FFFFFF" , font = ("Angsana New" , 16) , values = ['ท่าพระ [BL01]' , 'จรัญฯ 13 [BL02]' , 'ไฟฉาย [BL03]' , 'บางขุนนนท์ [BL04]' , 'บางยี่ขัน [BL05]' , 'สิรินธร [BL06]' , 
    'บางพลัด [BL07]' , 'บางอ้อ [BL18]' , 'บางโพ [BL09]' , 'เตาปูน [BL10]' , 'บางซื่อ [BL11]' , 'กำแพงเพชร [BL12]' , 'สวนจตุจักร [BL13]' , 
    'พหลโยธิน [BL14]' , 'ลาดพร้าว [BL15]' , 'รัชดาภิเษก [BL16]' , 'สุทธิสาร [BL17]' ,'ห้วยขวาง [BL18]' , 'ศูนย์วัฒนธรรมแห่งประเทศไทย [BL19]' , 
    'พระราม 9 [BL20]' , 'เพชรบุรี [BL21]' ,'สุขุมวิท [BL22]' , 'ศูนย์การประชุมแห่งชาติสิริกิต์ [BL23]' , 'คลองเตย [BL24]' , 'ลุมพินี [BL25]', 
    'สีลม [BL26]' , 'สามย่าน [BL27]' , 'หัวลำโพง [BL28]' , 'วัดมังกร [BL29]' , 'สามยอด [BL30]' , 'สนามไชย [BL31]' , 'อิสรภาพ [BL32]' ,
    'บางไผ่ [BL33]' , 'บางหว้า [BL34]' , 'เพชรเกษม 48 [BL35]' , 'ภาษีเจริญ [BL36]' , 'บางแค [BL37]' , 'หลักสอง [BL38]']  , width = 50 , state = "readonly")
    end_station_combo_mrt.set(" == กรุณาเลือกสถานีปลายทาง ==")
    end_station_combo_mrt.grid(row = 3 , columnspan = 2 , padx = 5 , sticky = 'n')
    
    tk.Button(background_widget_mrt , image = image_negative , bd = 0  , background = "#DCF3FF" , activebackground = "#DCF3FF" , command = decrement_mrt).grid(row = 4 , column = 0 , sticky = 'w' , padx = 125)
    tk.Button(background_widget_mrt , image = image_positive , bd = 0  , background = "#DCF3FF" , activebackground = "#DCF3FF" , command = increment_mrt).grid(row = 4 , column = 1 , sticky = 'w')

    entry_number_mrt = tk.Entry(background_widget_mrt , width = 25 , borderwidth = 0, relief = 'flat', foreground = '#000000', font = ('Calibri', 18 , "bold"))
    entry_number_mrt.config(highlightcolor = "#B1B1B1" , highlightthickness = 1 , highlightbackground = "#B1B1B1")
    entry_number_mrt.grid(row = 4 , columnspan = 2 , ipady = 3 , pady = 77)
    entry_number_mrt.insert(tk.END , '1')

    # Create the calculate button
    calculate_button = tk.Button(background_widget_mrt , image = image_calculate_mrt , background = "#DCF3FF" , bd = 0  , activebackground = "#DCF3FF" , command = calculate_and_show_fare_mrt)
    calculate_button.grid(row = 5 , columnspan = 2)

    tk.Label(background_widget_mrt , image = image_veg , background = "#DCF3FF").grid(row = 6 , columnspan = 2)
    
    # Enter Keyborad 
    root.bind('<Return>', lambda event: calculate_button.invoke())

def increment_mrt():
    current_value = int(entry_number_mrt.get())
    if current_value < 100:
        entry_number_mrt.delete(0, tk.END)
        entry_number_mrt.insert(tk.END, str(current_value + 1))

def decrement_mrt():
    current_value = int(entry_number_mrt.get())
    if current_value > 1:
        entry_number_mrt.delete(0, tk.END)
        entry_number_mrt.insert(tk.END, str(current_value - 1))


def sky_train_mrt(start_station , end_station):
    global station_list_mrt
    root.option_add("*font" , ("Angsana New" , 16))
    station_list_mrt = ['ท่าพระ [BL01]' , 'จรัญฯ 13 [BL02]' , 'ไฟฉาย [BL03]' , 'บางขุนนนท์ [BL04]' , 'บางยี่ขัน [BL05]' , 'สิรินธร [BL06]' , 
    'บางพลัด [BL07]' , 'บางอ้อ [BL18]' , 'บางโพ [BL09]' , 'เตาปูน [BL10]' , 'บางซื่อ [BL11]' , 'กำแพงเพชร [BL12]' , 'สวนจตุจักร [BL13]' , 
    'พหลโยธิน [BL14]' , 'ลาดพร้าว [BL15]' , 'รัชดาภิเษก [BL16]' , 'สุทธิสาร [BL17]' ,'ห้วยขวาง [BL18]' , 'ศูนย์วัฒนธรรมแห่งประเทศไทย [BL19]' , 
    'พระราม 9 [BL20]' , 'เพชรบุรี [BL21]' ,'สุขุมวิท [BL22]' , 'ศูนย์การประชุมแห่งชาติสิริกิต์ [BL23]' , 'คลองเตย [BL24]' , 'ลุมพินี [BL25]', 
    'สีลม [BL26]' , 'สามย่าน [BL27]' , 'หัวลำโพง [BL28]' , 'วัดมังกร [BL29]' , 'สามยอด [BL30]' , 'สนามไชย [BL31]' , 'อิสรภาพ [BL32]' ,
    'บางไผ่ [BL33]' , 'บางหว้า [BL34]' , 'เพชรเกษม 48 [BL35]' , 'ภาษีเจริญ [BL36]' , 'บางแค [BL37]' , 'หลักสอง [BL38]'] 
    
    # จากท่าพระ ไป ทุกสถานี
    if start_station in [station_list_mrt[0]]: 
        if end_station in  [station_list_mrt[1] , station_list_mrt[2] , station_list_mrt[3] , station_list_mrt[4] , station_list_mrt[5] , station_list_mrt[6] , station_list_mrt[7] , station_list_mrt[8] , station_list_mrt[9] , station_list_mrt[10] , station_list_mrt[11] , station_list_mrt[12] , station_list_mrt[13] , station_list_mrt[14] , station_list_mrt[15] , station_list_mrt[16] , station_list_mrt[17] , station_list_mrt[18] , station_list_mrt[19] , station_list_mrt[20] , station_list_mrt[21] , station_list_mrt[22] , station_list_mrt[23] , station_list_mrt[24] , station_list_mrt[25] , station_list_mrt[26] , station_list_mrt[27] , station_list_mrt[28] , station_list_mrt[29] , station_list_mrt[30] , station_list_mrt[31] , station_list_mrt[32] , station_list_mrt[33] , station_list_mrt[34] , station_list_mrt[35] , station_list_mrt[36] , station_list_mrt[37]]:
            if result[0][4] == '':
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19 , 17 , 17 , 19 , 21 , 24 , 26 , 29]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19 , 17 , 17 , 19 , 21 , 24 , 26 , 29]
            elif 23 >= result[0][4] >= 15: 
                fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19 , 17 , 15 , 15 , 17 , 19 , 22 , 23 , 26]
            else: 
                fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11 , 10 , 9 , 9 , 10 , 11 , 12 , 13 , 15]

            start_index = station_list_mrt.index(start_station)
            end_index = station_list_mrt.index(end_station)
            distance = abs(end_index - start_index)
            print(distance - 1)
            if distance <= len(fares):
                price = fares[distance - 1]
            else:
                price = fares[-1]

    # จากทุกสถานี ไป ท่าพระ 
    if start_station in  [station_list_mrt[1] , station_list_mrt[2] , station_list_mrt[3] , station_list_mrt[4] , station_list_mrt[5] , station_list_mrt[6] , station_list_mrt[7] , station_list_mrt[8] , station_list_mrt[9] , station_list_mrt[10] , station_list_mrt[11] , station_list_mrt[12] , station_list_mrt[13] , station_list_mrt[14] , station_list_mrt[15] , station_list_mrt[16] , station_list_mrt[17] , station_list_mrt[18] , station_list_mrt[19] , station_list_mrt[20] , station_list_mrt[21] , station_list_mrt[22] , station_list_mrt[23] , station_list_mrt[24] , station_list_mrt[25] , station_list_mrt[26] , station_list_mrt[27] , station_list_mrt[28] , station_list_mrt[29] , station_list_mrt[30] , station_list_mrt[31] , station_list_mrt[32] , station_list_mrt[33] , station_list_mrt[34] , station_list_mrt[35] , station_list_mrt[36] , station_list_mrt[37]]:
        if end_station in [station_list_mrt[0]]: 
            if result[0][4] == '':
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19 , 17 , 17 , 19 , 21 , 24 , 26 , 29]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19 , 17 , 17 , 19 , 21 , 24 , 26 , 29]
            elif 23 >= result[0][4] >= 15: 
                fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19 , 17 , 15 , 15 , 17 , 19 , 22 , 23 , 26]
            else: 
                fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11 , 10 , 9 , 9 , 10 , 11 , 12 , 13 , 15]
           
            start_index = station_list_mrt.index(start_station)
            end_index = station_list_mrt.index(end_station)
            distance = abs(end_index - start_index)
            print(distance - 1)
            if distance <= len(fares):
                price = fares[distance - 1]
            else:
                price = fares[-1]


    #จาก จรัญ - สุขุมวิท
    if start_station in [station_list_mrt[1] , station_list_mrt[2] , station_list_mrt[3] , station_list_mrt[4] , station_list_mrt[5] , station_list_mrt[6] , station_list_mrt[7] , station_list_mrt[8] , station_list_mrt[9] , station_list_mrt[10] , station_list_mrt[11] , station_list_mrt[12] , station_list_mrt[13] , station_list_mrt[14] , station_list_mrt[15] , station_list_mrt[16] , station_list_mrt[17] , station_list_mrt[18] , station_list_mrt[19] , station_list_mrt[20] , station_list_mrt[21]]:
        
        # ไปจรัญ - สุขุมวิท เหมือนกัน
        if end_station in [station_list_mrt[1] , station_list_mrt[2] , station_list_mrt[3] , station_list_mrt[4] , station_list_mrt[5] , station_list_mrt[6] , station_list_mrt[7] , station_list_mrt[8] , station_list_mrt[9] , station_list_mrt[10] , station_list_mrt[11] , station_list_mrt[12] , station_list_mrt[13] , station_list_mrt[14] , station_list_mrt[15] , station_list_mrt[16] , station_list_mrt[17] , station_list_mrt[18] , station_list_mrt[19] , station_list_mrt[20] , station_list_mrt[21]]:
            if result[0][4] == '':
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43]
            elif 23 >= result[0][4] >= 15: 
                fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39]
            else: 
                fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22]
            
            start_index = station_list_mrt.index(start_station)
            end_index = station_list_mrt.index(end_station)
            distance = abs(end_index - start_index)
            print(distance - 1)
            if distance <= len(fares):
                price = fares[distance - 1]
            else:
                price = fares[-1]

        # ไปศูนย์สิริกิต์ - อิสรภาพ
        elif end_station in [station_list_mrt[22] , station_list_mrt[23] , station_list_mrt[24] , station_list_mrt[25] , station_list_mrt[26] , station_list_mrt[27] , station_list_mrt[28] , station_list_mrt[29] , station_list_mrt[30] , station_list_mrt[31]]:
            if result[0][4] == '':
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19]
            elif 23 >= result[0][4] >= 15: 
                fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19 , 17]
            else: 
                fares = [9  , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11 , 10]

            start_index = station_list_mrt.index(start_station)
            end_index = station_list_mrt.index(end_station)
            distance = abs(start_index - end_index)
            print(distance - 1)
            if distance <= len(fares):
                price = fares[distance - 1]
            else:
                price = fares[-1]

        # ไป บางไผ่ - บางหว้า
        elif end_station in [station_list_mrt[32] , station_list_mrt[33] , station_list_mrt[34] , station_list_mrt[35] , station_list_mrt[36] , station_list_mrt[37]]:
            # จากจรัญ 
            if start_station in [station_list_mrt[1]]:
                if result[0][4] == '':
                    fares = [19 , 21 , 24 , 26 , 29 , 31]
                elif 60 > result[0][4] > 23: 
                    fares = [19 , 21 , 24 , 26 , 29 , 31]
                elif 23 >= result[0][4] >= 15: 
                    fares = [17 , 19 , 22 , 23 , 26 , 28]
                else: 
                    fares = [10 , 11 , 12 , 13 , 15 , 16]

                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 30)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # จากไฟฉาย
            elif start_station in [station_list_mrt[2]]:
                if result[0][4] == '':
                    fares = [21 , 24 , 26 , 29 , 31 , 33]
                elif 60 > result[0][4] > 23: 
                    fares = [21 , 24 , 26 , 29 , 31 , 33]
                elif 23 >= result[0][4] >= 15: 
                    fares = [19 , 22 , 23 , 26 , 28 , 30] 
                else: 
                    fares = [11 , 12 , 13 , 15 , 16 , 17]


                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 29)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # จากบางขุนนนท์ 
            elif start_station in [station_list_mrt[3]]:
                if result[0][4] == '':
                    fares = [24 , 26 , 29 , 31 , 33 , 36]
                elif 60 > result[0][4] > 23: 
                    fares = [24 , 26 , 29 , 31 , 33 , 36]
                elif 23 >= result[0][4] >= 15: 
                    fares = [22 , 23 , 26 , 28 , 30 , 32] 
                else: 
                    fares = [12 , 13 , 15 , 16 , 17 , 18]

        
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 28)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # จากบางยี่ขัน
            elif start_station in [station_list_mrt[4]]:
                if result[0][4] == '':
                    fares = [26 , 29 , 31 , 33 , 36 , 38]
                elif 60 > result[0][4] > 23: 
                    fares = [26 , 29 , 31 , 33 , 36 , 38]
                elif 23 >= result[0][4] >= 15: 
                    fares = [23 , 26 , 28 , 30 , 32 , 34] 
                else: 
                    fares = [13 , 15 , 16 , 17 , 18 , 19]

        
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 27)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]
                    
            # จากสิรินธร
            elif start_station in [station_list_mrt[5]]:
                if result[0][4] == '':
                    fares = [29 , 31 , 33 , 36 , 38 , 41]
                elif 60 > result[0][4] > 23: 
                    fares = [29 , 31 , 33 , 36 , 38 , 41]
                elif 23 >= result[0][4] >= 15: 
                    fares = [26 , 28 , 30 , 32 , 34 , 37] 
                else: 
                    fares = [15 , 16 , 17 , 18 , 19 , 21]

                fares = [29 , 31 , 33 , 36 , 38 , 41]
        
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 26)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # จากบางพลัด
            elif start_station in [station_list_mrt[6]]:
                if result[0][4] == '':
                    fares = [31 , 33 , 36 , 38 , 41 , 43]
                elif 60 > result[0][4] > 23: 
                    fares = [31 , 33 , 36 , 38 , 41 , 43]
                elif 23 >= result[0][4] >= 15: 
                    fares = [28 , 30 , 32 , 34 , 37 , 39] 
                else: 
                    fares = [16 , 17 , 18 , 19 , 21 , 22]
        
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 25)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # บางอ้อ 
            elif start_station in [station_list_mrt[7]]:
                if result[0][4] == '':
                    fares = [33 , 36 , 38 , 41 , 43 , 43]
                elif 60 > result[0][4] > 23: 
                    fares = [33 , 36 , 38 , 41 , 43 , 43]
                elif 23 >= result[0][4] >= 15: 
                    fares = [30 , 32 , 34 , 37 , 39 , 39] 
                else: 
                    fares = [17 , 18 , 19 , 21 , 22 , 22]
        
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 24)
                
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # บางโพ  
            elif start_station in [station_list_mrt[8]]: 
                if result[0][4] == '':
                    fares = [36 , 38 , 41 , 43 , 43 , 43]
                elif 60 > result[0][4] > 23: 
                    fares = [36 , 38 , 41 , 43 , 43 , 43]
                elif 23 >= result[0][4] >= 15: 
                    fares = [32 , 34 , 37 , 39 , 39 , 39] 
                else: 
                    fares = [18 , 19 , 21 , 22 , 22 , 22]

                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 23)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]
            # เตาปูน 
            elif start_station in [station_list_mrt[9]]: 
                if result[0][4] == '':
                    fares = [38 , 41 , 43 , 43 , 43 , 43]
                elif 60 > result[0][4] > 23: 
                    fares = [38 , 41 , 43 , 43 , 43 , 43]
                elif 23 >= result[0][4] >= 15: 
                    fares = [34 , 37 , 39 , 39 , 39 , 39] 
                else: 
                    fares = [19 , 21 , 22 , 22 , 22 , 22]

                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 22)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]
            # บางซื่อ
            elif start_station in [station_list_mrt[10]]: 
                if result[0][4] == '':
                    fares = [41 , 43 , 43 , 43 , 43 , 43]
                elif 60 > result[0][4] > 23: 
                    fares = [41 , 43 , 43 , 43 , 43 , 23]
                elif 23 >= result[0][4] >= 15: 
                    fares = [37 , 39 , 39 , 39 , 39 , 39] 
                else: 
                    fares = [21 , 22 , 22 , 22 , 22 , 22]

                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(start_index - end_index + 21)

                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # กำแพงเพชร - สุขุมวิท
            else:
                if result[0][4] == '':
                    price = 43
                elif 60 > result[0][4] > 23: 
                    price = 43
                elif 23 >= result[0][4] >= 15: 
                    price = 39
                else: 
                    price = 22

    if start_station in [station_list_mrt[22] , station_list_mrt[23] , station_list_mrt[24] , station_list_mrt[25] , station_list_mrt[26] , station_list_mrt[27] , station_list_mrt[28] , station_list_mrt[29] , station_list_mrt[30] , station_list_mrt[31] , station_list_mrt[32] , station_list_mrt[33] , station_list_mrt[34] , station_list_mrt[35] , station_list_mrt[36] , station_list_mrt[37]]:
        if end_station in [station_list_mrt[22] , station_list_mrt[23] , station_list_mrt[24] , station_list_mrt[25] , station_list_mrt[26] , station_list_mrt[27] , station_list_mrt[28] , station_list_mrt[29] , station_list_mrt[30] , station_list_mrt[31] , station_list_mrt[32] , station_list_mrt[33] , station_list_mrt[34] , station_list_mrt[35] , station_list_mrt[36] , station_list_mrt[37]]:
            if result[0][4] == '':
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 41 , 43 , 43 , 43 , 43 , 43]
            elif 60 > result[0][4] > 23: 
                fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 41 , 43 , 43 , 43 , 43 , 43]
            elif 23 >= result[0][4] >= 15: 
                fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 37 , 39 , 39 , 39 , 39 , 39]
            else: 
                fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 21 , 22 , 22 , 22 , 22 , 22]

            start_index = station_list_mrt.index(start_station)
            end_index = station_list_mrt.index(end_station)
            distance = abs(end_index - start_index)
            print(distance - 1)
            if distance <= len(fares):
                price = fares[distance - 1]
            else:
                price = fares[-1]
        
        # ไปจรัญ - สุขุมวิท เหมือนกัน
        elif end_station in [station_list_mrt[1] , station_list_mrt[2] , station_list_mrt[3] , station_list_mrt[4] , station_list_mrt[5] , station_list_mrt[6] , station_list_mrt[7] , station_list_mrt[8] , station_list_mrt[9] , station_list_mrt[10] , station_list_mrt[11] , station_list_mrt[12] , station_list_mrt[13] , station_list_mrt[14] , station_list_mrt[15] , station_list_mrt[16] , station_list_mrt[17] , station_list_mrt[18] , station_list_mrt[19] , station_list_mrt[20] , station_list_mrt[21]]:
            # จากสิริกิต
            if start_station in [station_list_mrt[22]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21]
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]

            # จากคลองเตย
            elif start_station in [station_list_mrt[23]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากลุมพินี 
            elif start_station in [station_list_mrt[24]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากสีลม
            elif start_station in [station_list_mrt[25]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากสามย่าน
            elif start_station in [station_list_mrt[26]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 5]
                else:
                    price = fares[-1]  

            # จากหัวลำโพง
            elif start_station in [station_list_mrt[27]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากวัดมังกร
            elif start_station in [station_list_mrt[28]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากสามยอด
            elif start_station in [station_list_mrt[29]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากสนามไชย
            elif start_station in [station_list_mrt[30]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11]

                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากอิสรภาพ
            elif start_station in [station_list_mrt[31]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19 , 17]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11 , 10]

                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากบางไผ่
            elif start_station in [station_list_mrt[32]]:
                if result[0][4] == '':
                    fares = [21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19]
                elif 60 > result[0][4] > 23: 
                    fares = [21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21 , 19]
                elif 23 >= result[0][4] >= 15: 
                    fares = [19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19 , 17]
                else: 
                    fares = [11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11 , 10]


                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากบางหว้า
            elif start_station in [station_list_mrt[33]]:
                if result[0][4] == '':
                    fares = [19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21]
                elif 60 > result[0][4] > 23: 
                    fares = [19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24 , 21]
                elif 23 >= result[0][4] >= 15: 
                    fares = [17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22 , 19]
                else: 
                    fares = [10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12 , 11]
         
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากเพชรเกษม 48
            elif start_station in [station_list_mrt[34]]:
                if result[0][4] == '':
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24]
                elif 60 > result[0][4] > 23: 
                    fares = [17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26 , 24]
                elif 23 >= result[0][4] >= 15: 
                    fares = [15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23 , 22]
                else: 
                    fares = [9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13 , 12]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากภาษีเจริญ
            elif start_station in [station_list_mrt[35]]:
                if result[0][4] == '':
                    fares = [0 , 17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26]
                elif 60 > result[0][4] > 23: 
                    fares = [0 , 17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29 , 26]
                elif 23 >= result[0][4] >= 15: 
                    fares = [0 , 15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26 , 23]
                else: 
                    fares = [0 , 9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15 , 13]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากบางแค
            elif start_station in [station_list_mrt[36]]:
                if result[0][4] == '':
                    fares = [0 , 0 , 17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29]
                elif 60 > result[0][4] > 23: 
                    fares = [0 , 0 , 17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31 , 29]
                elif 23 >= result[0][4] >= 15: 
                    fares = [0 , 0 , 15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28 , 26]
                else: 
                    fares = [0 , 0 , 9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16 , 15]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]  

            # จากหลักสอง
            elif start_station in [station_list_mrt[35]]:
                if result[0][4] == '':
                    fares = [0 , 0 , 0 , 17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31]
                elif 60 > result[0][4] > 23: 
                    fares = [0 , 0 , 0 , 17 , 19 , 21 , 24 , 26 , 29 , 31 , 33 , 36 , 38 , 41 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 43 , 41 , 38 , 36 , 33 , 31]
                elif 23 >= result[0][4] >= 15: 
                    fares = [0 , 0 , 0 , 15 , 17 , 19 , 22 , 23 , 26 , 28 , 30 , 32 , 34 , 37 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 39 , 37 , 34 , 32 , 30 , 28]
                else: 
                    fares = [0 , 0 , 0 , 9 , 10 , 11 , 12 , 13 , 15 , 16 , 17 , 18 , 19 , 21 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 22 , 21 , 19 , 18 , 17 , 16]
                
                start_index = station_list_mrt.index(start_station)
                end_index = station_list_mrt.index(end_station)
                distance = abs(end_index - start_index)
                print(distance - 1)
                if distance <= len(fares):
                    price = fares[distance - 1]
                else:
                    price = fares[-1]   
    if start_station == end_station: 
        price = 0
    return price 

def calculate_and_show_fare_mrt():
    global start_station , end_station , fare

    try: 
        start_station = start_station_combo_mrt.get()
        end_station = end_station_combo_mrt.get()

        if start_station == "" or start_station == " == กรุณาเลือกสถานีต้นทาง ==": 
            messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีต้นทาง")

        elif end_station == "" or end_station == " == กรุณาเลือกสถานีปลายทาง ==": 
            messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีปลายทาง")    
        
        elif start_station == end_station: 
            messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีที่แตกต่างกัน")

        else:
            messagebox.showinfo("Skytrain App says : " , "ข้อมูลถูกต้อง กดยืนยันเพื่อเข้าสู่หน้าคำนวณราคา")
            calculate_price_detail_mrt()
            
    except ValueError: 
        messagebox.showwarning("Skytrain App says : " , "โปรดเลือกสถานีต้นทาง")   

def calculate_price_detail_mrt(): 
    global background_right_mrt_1 , background_price_mrt , text_start , text_end , fare , total_fare
    
    background_right_top_mrt.grid_forget()
    background_widget_mrt.grid_forget()
    
    background_right_mrt_1 = tk.Frame(root , background = "#F2F2F2")
    background_right_mrt_1.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_mrt_1.rowconfigure(0 , weight = 0)
    background_right_mrt_1.rowconfigure(1 , weight = 5)
    background_right_mrt_1.columnconfigure(0 , weight = 5)

    background_right_top_mrt_1 = tk.Frame(background_right_mrt_1 , background = '#FFFFFF')
    background_right_top_mrt_1.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_mrt_1.rowconfigure(0 , weight = 1)
    background_right_top_mrt_1.columnconfigure(0 , weight = 1)

    background_price_mrt = tk.Frame(root , background = "#25519A")
    background_price_mrt.grid(row = 1 , column = 1 , sticky = 's')
    background_price_mrt.rowconfigure(0 , weight = 0)
    background_price_mrt.rowconfigure(1 , weight = 0)
    background_price_mrt.rowconfigure(2 , weight = 0)
    background_price_mrt.rowconfigure(3 , weight = 0)
    background_price_mrt.rowconfigure(4 , weight = 0)
    background_price_mrt.rowconfigure(5 , weight = 0)
    background_price_mrt.rowconfigure(6 , weight = 0)
    background_price_mrt.rowconfigure(7 , weight = 0)
    background_price_mrt.columnconfigure(0 , weight = 1)
    background_price_mrt.columnconfigure(1 , weight = 1)
    
    tk.Label(background_right_mrt_1 , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news' , ipady = 15)

    tk.Label(background_right_top_mrt_1 , text = "•  Calculate MRT [menu] 🚄" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_mrt_1 , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Label(background_price_mrt , text = "Calculate Prices" , background = "#25519A" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'nw' , padx = 25 , pady = 11)
    
    tk.Label(background_price_mrt , text = "Start Station" , background = "#25519A" , foreground = "#C2CCFF" , font = "Calibri 16 bold").grid(row = 1 , column = 0 , sticky = 'nw' , padx = 55 , pady = 12)
    background_start_station = tk.Frame(background_price_mrt , background = "#0E4285")
    background_start_station.grid(row = 2 , columnspan = 2 , sticky = 'news' , padx = 45)
    background_start_station.rowconfigure(0 , weight = 1)
    background_start_station.columnconfigure(0 , weight = 1)
    tk.Label(background_start_station , text = start_station , background = "#0E4285" , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 0 , column = 0 , sticky = 'nws' , padx = 25 , pady = 10)
    
    print(start_station)
    print(end_station)
    
    tk.Label(background_price_mrt , text = "End Station" , background = "#25519A" , foreground = "#C2CCFF" , font = "Calibri 16 bold").grid(row = 3 , column = 0 , sticky = 'nw' , padx = 55 , pady = 12)
    background_end_station = tk.Frame(background_price_mrt , background = "#0E4285")
    background_end_station.grid(row = 4 , columnspan = 2 , sticky = 'news' , padx = 45)
    background_end_station.rowconfigure(0 , weight = 1)
    background_end_station.columnconfigure(0 , weight = 1)
    tk.Label(background_end_station , text = end_station , background = "#0E4285" , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 0 , column = 0 , sticky = 'nws' , padx = 25 , pady = 10)

    fare = sky_train_mrt(start_station , end_station)

    print(f"fefe{fare}")
    number_mrt = int(entry_number_mrt.get())
    total_fare = fare * number_mrt

    if result[0][4] == "": 
        text = f"จาก '{start_station}' ไป '{end_station}' \nโดยสั่งบัตรทั้งหมด {number_mrt} บัตรจะมีราคา {total_fare} บาท (บัตรละ {fare} บาท)"
        tk.Label(background_price_mrt , text = text , background = "#25519A" , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 5 , columnspan = 2 , pady = 10 , sticky = 'news')

    else: 
        text = f"จาก '{start_station}' ไป '{end_station}' \nเนื่องจากคุณอายุ {result[0][4]} ปี โดยสั่งบัตรทั้งหมด {number_mrt} บัตร ทำให้มีราคาอยู่ที่ {total_fare} บาท (บัตรละ {fare} บาท)"
        tk.Label(background_price_mrt , text = text , background = "#25519A" , foreground = "#FFFFFF" , font = ("Angsana new" , 19 , "bold")).grid(row = 5 , columnspan = 2 , pady = 20 , sticky = 'news')

    tk.Button(background_price_mrt , image = image_check_information , bd = 0 , activebackground = "#25519A" , background = "#25519A" , command = thank_you_order_mrt).grid(row = 6 , columnspan = 2 , sticky = 'ew')

    tk.Label(background_price_mrt , image = image_veg , background = "#25519A").grid(row = 7 , columnspan = 2)

def thank_you_order_mrt(): 
    global result_2
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 800  # Set the width of the window
    window_height = 770  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2)) - 35 

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    background_right_mrt_1.grid_forget()
    background_price_mrt.grid_forget()

    background_right_order = tk.Frame(root , background = "#F2F2F2")
    background_right_order.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_order.rowconfigure(0 , weight = 0)
    background_right_order.rowconfigure(1 , weight = 5)
    background_right_order.columnconfigure(0 , weight = 5)

    background_right_top_order = tk.Frame(background_right_order , background = '#FFFFFF')
    background_right_top_order.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_order.rowconfigure(0 , weight = 1)
    background_right_top_order.columnconfigure(0 , weight = 1)

    background_price_order = tk.Frame(root , background = "#25519A")
    background_price_order.grid(row = 1 , column = 1 , sticky = 's')
    background_price_order.rowconfigure(0 , weight = 0)
    background_price_order.rowconfigure(1 , weight = 0)
    background_price_order.rowconfigure(2 , weight = 0)
    background_price_order.rowconfigure(3 , weight = 0)
    background_price_order.columnconfigure(0 , weight = 1)
    background_price_order.columnconfigure(1 , weight = 1)
    
    tk.Label(background_right_top_order , text = "•  receipt [menu] 🧾" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_order , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Label(background_price_order , text = "Thank you for order!" , background = "#7AB420" , foreground = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , columnspan = 2 , sticky = 'ews' , pady = 10 , ipady = 5)

    background_receipt = tk.Frame(background_price_order , background = "#FFFFFF")
    background_receipt.grid(row = 1 , columnspan = 2 , pady = 10)
    background_receipt.rowconfigure(0 , weight = 0)
    background_receipt.rowconfigure(1 , weight = 0)
    background_receipt.rowconfigure(2 , weight = 0)
    background_receipt.rowconfigure(3 , weight = 0)
    background_receipt.rowconfigure(4 , weight = 0)
    background_receipt.rowconfigure(5 , weight = 0)
    background_receipt.rowconfigure(6 , weight = 0)
    background_receipt.rowconfigure(7 , weight = 0)
    background_receipt.rowconfigure(8 , weight = 0)
    background_receipt.rowconfigure(9 , weight = 0)
    background_receipt.rowconfigure(10 , weight = 0)
    background_receipt.rowconfigure(11 , weight = 0)
    background_receipt.rowconfigure(12 , weight = 0)
    background_receipt.rowconfigure(13 , weight = 0)
    background_receipt.rowconfigure(14 , weight = 0)

    background_receipt.columnconfigure(0 , weight = 1)
    background_receipt.columnconfigure(1 , weight = 1)
    background_receipt.columnconfigure(2 , weight = 1)
    background_receipt.columnconfigure(3 , weight = 1)

    # Get the current time
    current_time = datetime.datetime.now()

    current_date = datetime.datetime.now().date()

    formatted_time = current_time.strftime("%H:%M:%S")

    sql = "INSERT INTO orders (Start_Station , End_Station , Cards , Prices , Date , Time , Username , Name , Sky_Train) VALUES (? , ? , ? , ? , ? , ? , ? , ? , ?)"

    cursor.execute(sql , [start_station , end_station , entry_number_mrt.get() , total_fare , current_date , formatted_time , result[0][0] , f"{result[0][2]} {result[0][3]}" , "MRT"])
    
    database.commit()

    sql_select = "SELECT * FROM orders WHERE name = ? AND Username = ? AND Sky_Train = ? ORDER BY id DESC"
    cursor.execute(sql_select, [f"{result[0][2]} {result[0][3]}", result[0][0]  , "MRT"])
    result_2 = cursor.fetchall()

    tk.Label(background_receipt , text = "Sky Train Receipt" , background = "#FFFFFF" , font = ("Calibri" , 16 , "bold") , foreground = "#25519A").grid(row = 0 , columnspan = 4 , padx = 10 , sticky = 'ew')
    tk.Label(background_receipt , text = f"============================================\norder no. : {result_2[0][0]}\n============================================" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 14)).grid(row = 1 , columnspan = 4 , padx = 10 , sticky = 'n')
    tk.Label(background_receipt , text = "Code      |" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 0 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "Qty       |" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 1 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "Description       |" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 2 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "Price/Bath" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 4 , column = 3 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"{result_2[0][0]}       " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 0 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"{result_2[0][3]}       " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 1 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"MRT  Tickets         " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 2 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = f"{total_fare}฿" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12)).grid(row = 5 , column = 3 , padx = 10 , sticky = 'news')
    tk.Label(background_receipt , text = "-----------------------------------------------------------------" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 16)).grid(row = 6 , columnspan = 4 , padx = 10) 
    tk.Label(background_receipt , text = f"   • Start Station : {result_2[0][1]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Angsana new" , 12 , "bold")).grid(row = 7 , columnspan = 4 , padx = 10 , sticky = 'w')
    tk.Label(background_receipt , text = f"   • End Station   : {result_2[0][2]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Angsana new"  , 12 , "bold")).grid(row = 8 , columnspan = 4 , padx = 10 , sticky = 'w')

    if result[0][4] == '': 
        image_card = image_ticket
        text_card = "  You have one-way ticket."
    elif 60 > result[0][4] > 23: 
        image_card = image_adult
        text_card = "  You have adult ticket."
    elif 23 >= result[0][4]: 
        image_card = image_student_2
        text_card = "  You have Student ticket."
    elif 14 >= result[0][4]: 
        image_card = image_kid
        text_card = "  You have Child ticket."
    else: 
        image_card = image_old_2
        text_card = "  You have OldCard ticket."
        
    tk.Label(background_receipt , image = image_card , text = text_card , compound = "left", foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 9 , columnspan = 4 , padx = 10 , sticky = 'new') 
    tk.Label(background_receipt , text = "-----------------------------------------------------------------" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 16)).grid(row = 10 , columnspan = 4 , padx = 10 , sticky = 'n')     
    tk.Label(background_receipt , text = "Date : " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 11 , column = 0 , padx = 10 , sticky = 'news')     
    tk.Label(background_receipt , text = f"{result_2[0][5]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 11 , column = 1 , padx = 10 , sticky = 'ws')     
    tk.Label(background_receipt , text = "Time : " , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 12 , column = 0 , padx = 10 , sticky = 'news')     
    tk.Label(background_receipt , text = f"{result_2[0][6]}" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 11)).grid(row = 12 , column = 1 , padx = 10 , sticky = 'ws')  
    tk.Label(background_receipt , text = f"Total" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 11 , column = 2  , padx = 10 , sticky = 'e' )  
    tk.Label(background_receipt , text = f"{total_fare}฿" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 12 , column = 2 , padx = 10 , sticky = 'e')  
    tk.Label(background_receipt , text = "-----------------------------------------------------------------" , foreground = "#000000" , background = "#FFFFFF" , font = ("Calibri" , 16)).grid(row = 13 , columnspan = 4 , padx = 10)  
    tk.Label(background_receipt , text = "Thank you for order, We can't live without you!" , foreground = "#598723" , background = "#FFFFFF" , font = ("Calibri" , 12 , "bold")).grid(row = 14 , columnspan = 4 , padx = 10 , sticky = 'news')  
    
    tk.Button(background_price_order , image = image_check_history , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = detail_station_information_mrt).grid(row = 2 , column = 0 , pady = 10)
    tk.Button(background_price_order , image = image_back_to_bts_mrt , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = bts_mrt).grid(row = 2 , column = 1 , pady = 10)
    
    tk.Label(background_price_order , image = image_veg , background = "#25519A").grid(row = 3 , columnspan = 2)

def detail_station_information_mrt(): 
    global treeview_detail
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window position
    window_width = 1180  # Set the width of the window
    window_height = 720  # Set the height of the window

    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2)) - 35 

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    background_right_detail = tk.Frame(root , background = "#F2F2F2")
    background_right_detail.grid(row = 1 , column = 1 , sticky = 'news')
    background_right_detail.rowconfigure(0 , weight = 0)
    background_right_detail.rowconfigure(1 , weight = 5)
    background_right_detail.columnconfigure(0 , weight = 5)

    background_right_top_detail = tk.Frame(background_right_detail , background = '#FFFFFF')
    background_right_top_detail.grid(row = 0 , column = 0 , sticky = 'news')
    background_right_top_detail.rowconfigure(0 , weight = 1)
    background_right_top_detail.columnconfigure(0 , weight = 1)

    background_detail_mrt = tk.Frame(root , background = "#25519A")
    background_detail_mrt.place(x = 64 , y = 130 , relwidth = 0.946 , relheight = 0.82, anchor = "nw")
    background_detail_mrt.rowconfigure(0 , weight = 1)
    background_detail_mrt.rowconfigure(1 , weight = 0)
    background_detail_mrt.columnconfigure(0 , weight = 0)
    background_detail_mrt.columnconfigure(1 , weight = 0)
    background_detail_mrt.columnconfigure(2 , weight = 0)
    
    tk.Label(background_right_detail , image = image_bg_tree , background = '#F2F2F2').grid(row = 1 , column = 0 , sticky = 'news')

    tk.Label(background_right_top_detail , text = "•  Detail MRT [menu] 🚄" , background = "#FFFFFF" , font = "Calibri 16 bold").grid(row = 0 , column = 0 , sticky = 'w' , ipady = 12 , ipadx = 30)
    tk.Label(background_right_top_detail , text = f"Account of : {result[0][0]}" , background = "#FFFFFF" , font = ("angsana new" , 22 , 'bold')).grid(row = 0 , column = 0 , sticky = 'e' , ipadx = 50)

    tk.Label(background_detail_mrt , text = "Detail Station and information" , background = "#7AB420" , foreground = "#FFFFFF" , font = "Calibri 16 bold").place(relx = 0.5 , rely = 0.05 , anchor = "center" , relwidth = 1 , relheight = 0.08)

    scrollbary = tk.Scrollbar(background_detail_mrt , orient = 'vertical', width = 20)
    scrollbary.place(x = -4 , relx = 0.992 , rely = 0.39 , relheight = 0.558 , anchor = 'e')

    treeview_detail = ttk.Treeview(background_detail_mrt, columns = ("c1", "c2", "c3", "c4", "c5", "c6" , "c7"), height = 8)
    treeview_detail.place(relx = 0.485, rely = 0.39 , anchor = "center" , relwidth = 0.95 , relheight = 0.56)
    
    # Create a style object
    style = ttk.Style()

    # Configure the style to increase the line spacing
    style.configure("Treeview", rowheight = 30)  # Adjust the rowheight value as per your requirement

    # Apply the style to the Treeview widget
    treeview_detail["style"] = "Treeview"
    
    treeview_detail.configure(yscrollcommand = scrollbary.set)
    treeview_detail.configure(selectmode = "extended")
    scrollbary.configure(command = treeview_detail.yview)

    treeview_detail.heading('c1' , text = 'id' , anchor = 'center')
    treeview_detail.heading('c2' , text = 'Start Station' , anchor = 'w')
    treeview_detail.heading('c3' , text = 'End Station' , anchor = 'w')
    treeview_detail.heading('c4' , text = 'Cards' , anchor = 'center')
    treeview_detail.heading('c5' , text = 'Prices' , anchor = 'center')
    treeview_detail.heading('c6' , text = 'Date' , anchor = 'w')
    treeview_detail.heading('c7' , text = 'Time' , anchor = 'w')

    treeview_detail.column('c1' , width = 50 , anchor = ('center') , minwidth = 0 )
    treeview_detail.column('c2' , width = 365 , minwidth = 0)
    treeview_detail.column('c3' , width = 365 , minwidth = 0)
    treeview_detail.column('c4' , width = 50 , anchor = 'center' , minwidth = 0)
    treeview_detail.column('c5' , width = 40 , anchor = 'center' , minwidth = 0)
    treeview_detail.column('c6' , width = 70 , minwidth = 0)
    treeview_detail.column('c7' , width = 60 , minwidth = 0)
    treeview_detail.column('#0' , width = 0 , stretch = False)

    font_style = ("Angsana new" , 14)

    # Reverse the order of the result list
    result_2.reverse()

    # Clear the Treeview before inserting new data
    treeview_detail.delete(*treeview_detail.get_children())
    
    for index, data in enumerate(result_2):
        item = treeview_detail.insert('', 0, values = (data[0], data[1], data[2], data[3], data[4], data[5] , data[6]), tags=("custom_font"))

    database.commit()

    # Apply the font to the inserted item
    treeview_detail.tag_configure("custom_font" , font = font_style)  

    # Set the focus on the most recent data
    recent_item = treeview_detail.get_children()[0]  # Get the item identifier of the first item
    treeview_detail.selection_set(recent_item)  # Set the focus on the recent item

    treeview_detail.bind('<<TreeviewSelect>>', single_click)

    tk.Button(background_detail_mrt , image = image_delete_history , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = delete_selected_mrt).place(rely = 0.76 , relx = 0.05 , anchor = 'w')
    tk.Button(background_detail_mrt , image = image_exit , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command =  exit_program).place(rely = 0.76 , relx = 0.49 , anchor = 'center')
    tk.Button(background_detail_mrt , image = image_back_to_bts_mrt , background = "#25519A" , bd = 0 , activebackground = "#25519A" , command = bts_mrt).place(rely = 0.76 , relx = 0.8 , anchor = 'center')

    tk.Label(background_detail_mrt , text = "Thank you for using our application, we can't live without you!" , background = "#7AB420" , foreground = "#FFFFFF" , font = "Calibri 16 bold").place(relx = 0.5 , rely = 0.95 , anchor = "center" , relwidth = 1 , relheight = 0.08)

def exit_program():
    question = messagebox.askquestion("Skytrain App says : " , "Are you sure to Exit Application?")

    if question == "yes":
        exit()
    
def single_click(event): 
    global values
    selected_item = treeview_detail.selection()
    if not selected_item:
        return
    
    item = selected_item[0]
    values = treeview_detail.item(item, 'values')

def delete_selected_mrt():
    confirm = messagebox.askquestion("Skytrain App says:", "Confirm to Delete (Yes / No)!")
    if confirm == 'yes': 
        sql_delete = "DELETE FROM orders WHERE id = ?;"
        cursor.execute(sql_delete, [values[0]])
        database.commit()
        
        # Clear the existing data in the treeview_detail
        treeview_detail.delete(*treeview_detail.get_children())
        
        sql_select = "SELECT * FROM orders WHERE username = ? AND Sky_Train = ?;"
        cursor.execute(sql_select , [result[0][0] , "MRT"])
        result_mrt = cursor.fetchall()

        for index, data in enumerate(result_mrt):
            item = treeview_detail.insert('', 0, values = (data[0], data[1], data[2], data[3], data[4], data[5], data[6]), tags=("custom_font"))

        messagebox.showinfo("Admin:", "Delete Successfully!!")

connection()

root = create_window()

bigfont = Font(family = "Segoe Script" , size = 16 , weight = "bold")

style = ttk.Style()

# style.theme_use('default')
style.configure('RoundedEntry.TEntry', borderwidth = 0 , relief = 'flat' , 
                foreground = 'black' , font = ('Arial', 10), 
                padding = 10 , background = 'blue')

background_top_left = tk.Frame(root , background = "#2D3237")
background_top_right = tk.Frame(root , background = "#505254")
background_top_right_login = tk.Frame(root , background = "#505254")
background_left = tk.Frame(root , background = "#4BA5FF")
background_right = tk.Frame(root , background = "#F2F2F2")
background_right_top = tk.Frame(background_right , background = '#FFFFFF')
background_right_bottom = tk.Frame(root , background = "#FFFFFF")

# image photo logo skytrain
Photo_skylogo = Image.open("image/skytrain_logo.png")
Photo_skylogo_resize = Photo_skylogo.resize((40 , 50) , Image.LANCZOS)

image_open_skylogo = ImageTk.PhotoImage(Photo_skylogo_resize)

# image photo login button 
Photo_login = Image.open("image/login.png")
Photo_login_resize = Photo_login.resize((140 , 38) , Image.LANCZOS)

image_open_login = ImageTk.PhotoImage(Photo_login_resize)

# image photo sign up button 
Photo_sign_up = Image.open("image/Sign_up.png")
Photo_sign_up_resize = Photo_sign_up.resize((140 , 38) , Image.LANCZOS)

image_open_sign_up = ImageTk.PhotoImage(Photo_sign_up_resize)

# image photo skytrain
Photo_skytrain= Image.open("image/skytrain.png")
Photo_skytrain = Photo_skytrain.resize((700 , 600) , Image.LANCZOS)

image_skytrain = ImageTk.PhotoImage(Photo_skytrain)

# image photo login_one
Photo_login_one = Image.open("image/login_one.png")
Photo_login_one = Photo_login_one.resize((160 , 70) , Image.LANCZOS)

image_login_one = ImageTk.PhotoImage(Photo_login_one)

# image photo sign_up_one
Photo_sign_up_one = Image.open("image/sign_up_one.png")
Photo_sign_up_one = Photo_sign_up_one.resize((160 , 70) , Image.LANCZOS)

image_sign_up_one = ImageTk.PhotoImage(Photo_sign_up_one)

# image photo background tree 
Photo_bg_tree = Image.open("image/bg_tree.png")
Photo_bg_tree = Photo_bg_tree.resize((700 , 600) , Image.LANCZOS)

image_bg_tree = ImageTk.PhotoImage(Photo_bg_tree)

# image photo mrt button
Photo_login_account = Image.open("image/login_account.png")
Photo_login_account = Photo_login_account.resize((190 , 75) , Image.LANCZOS)

image_login_account = ImageTk.PhotoImage(Photo_login_account)

# image photo sign_up_in_login button
Photo_sign_up_in_login = Image.open("image/sign_up_in_login.png")
Photo_sign_up_in_login = Photo_sign_up_in_login.resize((215 , 40) , Image.LANCZOS)

image_sign_up_in_login = ImageTk.PhotoImage(Photo_sign_up_in_login)

# image photo sign up no card button
Photo_sign_up_no_card = Image.open("image/sign_up_no_card.png")
Photo_sign_up_no_card = Photo_sign_up_no_card.resize((385 , 70) , Image.LANCZOS)

image_sign_up_no_card = ImageTk.PhotoImage(Photo_sign_up_no_card)

# image photo sign up with card button
Photo_sign_up_with_card = Image.open("image/sign_up_with_card.png")
Photo_sign_up_with_card = Photo_sign_up_with_card.resize((385 , 70) , Image.LANCZOS)

image_sign_up_with_card = ImageTk.PhotoImage(Photo_sign_up_with_card)

# image photo sign up with card (add information) button
Photo_sign_up_with_card_complete = Image.open("image/sign_up_card_complete.png")
Photo_sign_up_with_card_complete = Photo_sign_up_with_card_complete.resize((385 , 70) , Image.LANCZOS)

image_sign_up_with_card_complete = ImageTk.PhotoImage(Photo_sign_up_with_card_complete)

# image Photo_veg
Photo_veg = Image.open("image/veg.png")
Photo_veg = Photo_veg.resize((740 , 70) , Image.LANCZOS)

image_veg = ImageTk.PhotoImage(Photo_veg)

# image text
Photo_text_you_must_login = Image.open("image/text_you_must_login.png")
Photo_text_you_must_login = Photo_text_you_must_login.resize((525 , 20) , Image.LANCZOS)

image_text_you_must_login = ImageTk.PhotoImage(Photo_text_you_must_login)

# image BTS CAR 
Photo_bts = Image.open("image/BTS_car.png")
Photo_bts = Photo_bts.resize((325 , 365) , Image.LANCZOS)

image_bts = ImageTk.PhotoImage(Photo_bts)

# image MRT CAR 
Photo_mrt = Image.open("image/MRT_car.png")
Photo_mrt = Photo_mrt.resize((325 , 365) , Image.LANCZOS)

image_mrt = ImageTk.PhotoImage(Photo_mrt)

# image photo logout button 
Photo_logout = Image.open("image/logout.png")
Photo_logout = Photo_logout.resize((140 , 38) , Image.LANCZOS)

image_logout = ImageTk.PhotoImage(Photo_logout)

# image calculate price 
Photo_cal_price = Image.open("image/calprice.png")
Photo_cal_price = Photo_cal_price.resize((240 , 75) , Image.LANCZOS)

image_cal_price = ImageTk.PhotoImage(Photo_cal_price)

# image check information 
Photo_check_information = Image.open("image/check_information.png")
Photo_check_information = Photo_check_information.resize((270 , 60) , Image.LANCZOS)

image_check_information = ImageTk.PhotoImage(Photo_check_information)

# image button positive 
photo_positive = Image.open("image/plus.png")
photo_positive = photo_positive.resize((47 , 60) , Image.LANCZOS)

image_positive = ImageTk.PhotoImage(photo_positive)

# image button negative 
photo_negative = Image.open("image/negative.png")
photo_negative = photo_negative.resize((47 , 60) , Image.LANCZOS)

image_negative = ImageTk.PhotoImage(photo_negative)

# image card one way 
photo_notmember = Image.open("image/OneCard1.png")
photo_notmember = photo_notmember.resize((24 , 24) , Image.LANCZOS)

image_notmember = ImageTk.PhotoImage(photo_notmember)

# image card prepaid
photo_prepaid = Image.open("image/TwoCard1.png")
photo_prepaid = photo_prepaid.resize((24 , 24) , Image.LANCZOS)

image_prepaid = ImageTk.PhotoImage(photo_prepaid)

# image card Student
photo_student = Image.open("image/ThreeCard1.png")
photo_student = photo_student.resize((24 , 24) , Image.LANCZOS)

image_student = ImageTk.PhotoImage(photo_student)

# image card old
photo_old = Image.open("image/FourCard1.png")
photo_old = photo_old.resize((24 , 24) , Image.LANCZOS)

image_old = ImageTk.PhotoImage(photo_old)

# image check history Button
Photo_check_history = Image.open("image/Check_history.png")
Photo_check_history = Photo_check_history.resize((270 , 60) , Image.LANCZOS)

image_check_history = ImageTk.PhotoImage(Photo_check_history)

# image back to bts&mrt Button
Photo_back_to_bts_mrt = Image.open("image/back_to_btsmrt.png")
Photo_back_to_bts_mrt = Photo_back_to_bts_mrt.resize((270 , 60) , Image.LANCZOS)

image_back_to_bts_mrt = ImageTk.PhotoImage(Photo_back_to_bts_mrt)

# image back to delete history Button
Photo_delete_history = Image.open("image/delete_history.png")
Photo_delete_history = Photo_delete_history.resize((270 , 60) , Image.LANCZOS)

image_delete_history = ImageTk.PhotoImage(Photo_delete_history)

# image finish application 
Photo_exit = Image.open("image/exit.png")
Photo_exit = Photo_exit.resize((270 , 60) , Image.LANCZOS)

image_exit = ImageTk.PhotoImage(Photo_exit)

# image button calculate mrt 
Photo_calculate_mrt = Image.open("image/calculate_price_mrt.png")
Photo_calculate_mrt = Photo_calculate_mrt.resize((320 , 60) , Image.LANCZOS)

image_calculate_mrt = ImageTk.PhotoImage(Photo_calculate_mrt)

# image card one way mrt
photo_kid = Image.open("image/OneCard2.png")
photo_kid = photo_kid.resize((24 , 24) , Image.LANCZOS)

image_kid = ImageTk.PhotoImage(photo_kid)

# image card prepaid mrt
photo_adult = Image.open("image/TwoCard2.png")
photo_adult = photo_adult.resize((24 , 24) , Image.LANCZOS)

image_adult = ImageTk.PhotoImage(photo_adult)

# image card Student mrt 
photo_student_2 = Image.open("image/ThreeCard2.png")
photo_student_2 = photo_student_2.resize((24 , 24) , Image.LANCZOS)

image_student_2 = ImageTk.PhotoImage(photo_student_2)

# image card old mrt
photo_old_2 = Image.open("image/FourCard2.png")
photo_old_2 = photo_old_2.resize((24 , 24) , Image.LANCZOS)

image_old_2 = ImageTk.PhotoImage(photo_old_2)

# image card one ticket mrt
photo_ticket = Image.open("image/Oneticket.png")
photo_ticket = photo_ticket.resize((44 , 24) , Image.LANCZOS)

image_ticket = ImageTk.PhotoImage(photo_ticket)

# image button calculate mrt 
Photo_next = Image.open("image/next.png")
Photo_next = Photo_next.resize((250 , 45) , Image.LANCZOS)

image_next = ImageTk.PhotoImage(Photo_next)

# image card one way mrt
photo_kid_2 = Image.open("image/OneCard2.png")
photo_kid_2 = photo_kid_2.resize((150 , 230) , Image.LANCZOS)

image_kid_2 = ImageTk.PhotoImage(photo_kid_2)

# image card prepaid mrt
photo_adult_2 = Image.open("image/TwoCard2.png")
photo_adult_2 = photo_adult_2.resize((150 , 230) , Image.LANCZOS)

image_adult_2 = ImageTk.PhotoImage(photo_adult_2)

# image card Student mrt 
photo_student_3 = Image.open("image/ThreeCard2.png")
photo_student_3 = photo_student_3.resize((150 , 230) , Image.LANCZOS)

image_student_3 = ImageTk.PhotoImage(photo_student_3)

# image card old mrt
photo_old_3 = Image.open("image/FourCard2.png")
photo_old_3 = photo_old_3.resize((150 , 230) , Image.LANCZOS)

image_old_3 = ImageTk.PhotoImage(photo_old_3)

# image card prepaid mrt
photo_adult_bts = Image.open("image/rabbit_2.png")
photo_adult_bts = photo_adult_bts.resize((150 , 230) , Image.LANCZOS)

image_adult_bts = ImageTk.PhotoImage(photo_adult_bts)

# image card Student mrt 
photo_student_bts = Image.open("image/rabbit_3.png")
photo_student_bts = photo_student_bts.resize((150 , 230) , Image.LANCZOS)

image_student_bts = ImageTk.PhotoImage(photo_student_bts)

# image card old mrt
photo_old_bts = Image.open("image/rabbit_4.png")
photo_old_bts = photo_old_bts.resize((150 , 230) , Image.LANCZOS)

image_old_bts = ImageTk.PhotoImage(photo_old_bts)

# image card old mrt
photo_dont_have = Image.open("image/dont_have.png")
photo_dont_have = photo_dont_have.resize((180 , 230) , Image.LANCZOS)

image_dont_have = ImageTk.PhotoImage(photo_dont_have)

# image eye close 
photo_eye_close = Image.open("image/eye_close.png")
photo_eye_close = photo_eye_close.resize((90 , 90) , Image.LANCZOS)

image_eye_close = ImageTk.PhotoImage(photo_eye_close)

# image eye open 
photo_eye_open = Image.open("image/eye_open.png")
photo_eye_open = photo_eye_open.resize((90 , 90) , Image.LANCZOS)

image_eye_open = ImageTk.PhotoImage(photo_eye_open)

set_background()
add_widget_in_background()
root.mainloop()