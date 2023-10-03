import tkinter as tk
import random
import string

background_color = "#2B2D42"  
button_color = "#8D99AE"  
text_color = "#EDF2F4"  

def generate_password():
    password_length = int(length_entry.get())
    complexity = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(complexity) for _ in range(password_length))

    password_display.config(state="normal")
    password_display.delete(1.0, "end")
    password_display.insert("insert", password)
    password_display.config(state="disabled")
    
    copy_button.config(text="Copy to Clipboard", bg=button_color, fg=background_color)

def copy_to_clipboard():
    generated_password = password_display.get(1.0, "end-1c")
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()  
    
    copy_button.config(text="Copied!", bg=text_color, fg=background_color)
    
    root.after(2000, reset_copy_button_text)

def reset_copy_button_text():
    copy_button.config(text="Copy to Clipboard", bg=button_color, fg=background_color)

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x250")

root.configure(bg=background_color)

length_frame = tk.Frame(root, bg=background_color)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:     ", font=("Helvetica", 16), bg=background_color, fg=text_color)
length_label.pack(side="left")

length_entry = tk.Entry(length_frame, font=("Helvetica", 14))
length_entry.pack(side="left")

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 14), bg=button_color, fg=background_color, borderwidth=2, relief="ridge")
generate_button.pack(pady=5)

password_display = tk.Text(root, width=20, height=2, font=("Helvetica", 30), state="disabled")
password_display.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 14), bg=button_color, fg=background_color, borderwidth=2, relief="ridge")
copy_button.pack(pady=5)

root.mainloop()
