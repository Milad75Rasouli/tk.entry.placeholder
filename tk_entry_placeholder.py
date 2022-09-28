import tkinter as tk
from tkinter import * 
from tkinter import messagebox
window = tk.Tk()
window.geometry('260x110')
window.resizable(0,0)
window.title("Release Tool")
frame_1 = tk.Frame()
frame_2 = tk.Frame()
frame_3 = tk.Frame()
version_lable = tk.Label(master=frame_1,text="Enter Release Version:")
version_input = tk.Entry(master=frame_1,width=40,fg='Gray')
version_placeholder = "Major.Minor.Build.Revision"
version_input.insert(0,version_placeholder)

post_lable = tk.Label(master=frame_2,text="Enter Substation Name:")
post_input = tk.Entry(master=frame_2,width=40,fg='Gray')
post_input.insert(0,"default is Trial")
confirm = tk.Button(master=frame_3,text="OK",width=5)
version = None

def handle_click(event):
    print("The button was clicked!")
    global version
    version = version_input.get()
    global post 
    post = post_input.get()
    window.destroy()

def clear_entry(event, entry):
    if entry['fg'] == 'Gray':
        entry['fg'] = 'Black'
        entry.delete(0,100)

version_input.bind("<FocusIn>", lambda event: clear_entry(event, version_input))
post_input.bind("<FocusIn>", lambda event: clear_entry(event, post_input))
confirm.bind("<Button-1>", handle_click)
confirm.pack()

version_lable.pack()
version_input.pack()
post_lable.pack()
post_input.pack()
confirm.pack()
frame_1.pack()
frame_2.pack()
frame_3.pack()

window.mainloop()

if version != None:
    print(f"{version} ---- {post}")




  

  