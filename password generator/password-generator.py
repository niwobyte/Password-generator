import customtkinter as ctk
import secrets
import pyperclip

icon_photo_link = "icon/passwort-generator-icon.ico"


def passwordGeneration():
    label.configure(text_color = "black")
    layout_for_password = check_var()

    if not layout_for_password:
        label.configure(text = "settings not found", text_color = "black")
        return

    password = ''.join(secrets.choice(layout_for_password) for _ in range(16))
    label.configure(text=password)
    

    
def copy_password():

    password_to_copy = label.cget("text")
    
    if password_to_copy in ["Password", "settings not found"]:
        text_info("unable to copy", "red", password_to_copy, "black")
        return

    pyperclip.copy(password_to_copy)
    text_info("copied", "green", password_to_copy, "black")



def text_info(message, color, password, after_color):

    button_copy.configure(state = "disabled")
    button_generate.configure(state = "disabled")
    label.configure(text = message, text_color = color)

    window.after(400, lambda: label.configure(text = password, text_color = after_color))
    window.after(400, lambda: button_copy.configure(state = "normal"))
    window.after(400, lambda: button_generate.configure(state = "normal"))



def check_var():

    Uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    Numbers = "1234567890"
    Symbols = "!@#$%^&*()_?"

    checkBoxes = [(Uppercase_var.get(), Uppercase_letters),
                  (Lowercase_var.get(), Lowercase_letters),
                  (Numbers_var.get(), Numbers),
                  (Symbols_var.get(), Symbols)]

    return "".join(text for status_var, text in checkBoxes if status_var)




window = ctk.CTk()
window.geometry("500x500")
window.resizable(False, False) 
window.title("Password generator")
try:
    window.iconbitmap(icon_photo_link)
except: pass

Uppercase_var = ctk.BooleanVar()
Lowercase_var = ctk.BooleanVar()
Numbers_var = ctk.BooleanVar()
Symbols_var = ctk.BooleanVar()

Uppercase_var.set(True)
Lowercase_var.set(True)
Numbers_var.set(True)
Symbols_var.set(True)

label = ctk.CTkLabel(master=window, 
                     text="Password", 
                     font=("Arial", 16))

label.pack(pady=30)


button_generate = ctk.CTkButton(text="Generate",
                        master=window,                      
                        command=passwordGeneration,
                        width=150,
                        height=40,
                        corner_radius=8)

button_generate.pack(pady = 10)


button_copy = ctk.CTkButton(text="Copy",
                            master=window,
                            command=copy_password,
                            width=150,
                            height=40,
                            corner_radius=8)

button_copy.pack(pady=10)


checkBox_Uppercase_letter = ctk.CTkCheckBox(master=window,
                           text="Uppercase letters",
                           variable=Uppercase_var
                           )

checkBox_Uppercase_letter.place(x = 10, y = 300)


checkBox_Lowercase_letter = ctk.CTkCheckBox(master=window,
                           text="Lowercase letters",
                           variable=Lowercase_var
                           )

checkBox_Lowercase_letter.place(x = 10, y = 330)


checkBox_numbers = ctk.CTkCheckBox(master=window,
                           text="Numbers",
                           variable=Numbers_var
                           )

checkBox_numbers.place(x = 10, y = 360)


checkBox_symbols = ctk.CTkCheckBox(master=window,
                           text="Symbols",
                           variable=Symbols_var
                           )

checkBox_symbols.place(x = 10, y = 390)



window.mainloop()
