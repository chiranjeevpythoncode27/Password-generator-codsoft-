import tkinter as tk
import random
import string

def generate_password():

    try:
        password_length = int(length_entry.get())
    except ValueError:
        password_label.config(text="Please enter the length of password")
        return
    
   
    characters = string.ascii_letters + string.digits + string.punctuation
    
   
    password = ''.join(random.choice(characters) for i in range(password_length))
    
    
    password_label.config(text=password)


root = tk.Tk()
root.title("Password Generator")
root.config(bg="light blue")





password_label = tk.Label(root, text="", font= 300, bg="gray")
password_label.pack(pady=20)


length_label = tk.Label(root, text="Enter the password length:", bg="beige", font= 300,width=40 , height=3)
length_label.pack()
length_entry = tk.Entry(root, width=30)
length_entry.pack(pady= 40, padx=20)

generate_button = tk.Button(root, text="Generate Password",width=40, height=6,  bg= "light yellow",font=400, command=generate_password)
generate_button.pack(pady=10,)


root.mainloop()
