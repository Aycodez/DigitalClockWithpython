#pip install customtkinter
#Lets import the necessary libraries

import customtkinter as ctk
import time

ctk.set_appearance_mode('System')

# Lets create a function that will update the time every second

def update():
    current_time = time.strftime('%I:%M:%S %p')
    time_label.configure(text=current_time)
    time_label.after(1000, update)


# Lets create a GUI for the clock
clock = ctk.CTk()
clock.geometry('360x120')
clock.title('Clock')

time_label = ctk.CTkLabel(clock, text='', font=ctk.CTkFont('Arial', 50, 'bold'))
time_label.pack(padx=20, pady=20)

update()
clock.mainloop()
