from tkinter import *
from tkinter import messagebox
import os

root = Tk()
package_name_var = StringVar()

def packageInstaller():
    package_name = package_name_var.get()
    print("Download")
    res = os.system("cmd /c pip install %s"%package_name)
    if res:
        messagebox.showerror("ERROR","Could not find a version that satisfies the requirement %s (from versions: none) \nERROR: No matching distribution found for %s"%(package_name,package_name))
    else:
        messagebox.showinfo("Info","Successfully installed %s"%(package_name))

root.geometry("390x250+450+200")
root.title("Python Package Installer") 
root.iconbitmap('app_icon.ico')
root.resizable(0,0)

frame = Frame(bg='white')
frame.pack(fill=BOTH, pady=30)

Label(frame, text='Python Package Installer', bg="white", fg="#000", font=('arial',16)).grid(row=0, column=0, padx=10, pady=10)

Label(frame, text='Enter package or module name', bg="white", fg="#000", font=('arial',10)).grid(row=1,column=0, padx=10, pady=5) 
Entry(frame, width=50, bd=2, relief=GROOVE, textvariable=package_name_var).grid(row=2, column=0, padx=40, pady=5)

Button(frame, text="Download", width=15, bg='#242323', fg="white", bd=0, relief=GROOVE, command=packageInstaller).grid(row=3, column=0, padx=10, pady=20)

root.mainloop()