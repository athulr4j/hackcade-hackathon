from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno


win = tk.Tk()
win.geometry('800x500')
win.config(border=0)

def exit():
    win12.destroy()

def slide11():
    global win12
    win11.destroy()
    win12 = tk.Tk()
    win12.geometry('1000x900')
    bg = PhotoImage(file = "9.png")
    bglabel = Label(win12, image = bg)
    bglabel.place(x = 0,y = 0)
    text1 = Label(win12, text = "Detective Alex Mercer is sad that he couldnt arrest the culprit whereas\n he is happy in one way that we helped him out...", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    text2 = Label(win12, text = "TO BE CONTINUED...", font=('Times New Roman', 15))
    text2.place(x=600,y=350)


    btn1 = tk.Button(win12, text='exit', command= exit, width= 10,height=3, bg="red", activebackground='green', border=0)
    btn1.place(x =650, y = 400)

    win12.mainloop()

def slide10():
    global win11
    win10.destroy()
    win11 = tk.Tk()
    win11.geometry('1000x900')
    bg = PhotoImage(file = "8.png")
    bglabel = Label(win11, image = bg)
    bglabel.place(x = 0,y = 0)
    text1 = Label(win11, text = "From unlocking the masterkey and analysing it we recovered a file stating \nProf Nolan commited suicide soon after the murder", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win11, text='Continue', command= slide11, width= 10,height=3, bg="red", activebackground='green', border=0)
    btn1.place(x =850, y = 700)

    win10.mainloop()

def slide9():
    global win10
    win9.destroy()
    win10 = tk.Tk()
    win10.geometry('1000x900')
    bg = PhotoImage(file = "7.png")
    bglabel = Label(win10, image = bg)
    bglabel.place(x = 0,y = 0)
    text1 = Label(win10, text = "From the computer we could get informations regarding Blackwood blackmailing Prof Nolan\n We got information regarding the recreating of masterkey also", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win10, text='Continue', command= slide10, width= 10,height=3, bg="red", activebackground='green', border=0)
    btn1.place(x =850, y = 700)

    win10.mainloop()

def slide8():
    global win9
    win8.destroy()
    win9 = tk.Tk()
    win9.geometry('800x500')
    bg = PhotoImage(file = "lighton.png")
    bglabel = Label(win9, image = bg)
    bglabel.place(x = 0,y = 0)
    text1 = Label(win9, text = "Vital evidences have been found!!\nWith those informations we are trying to recreate the masterkey", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win9, text='Continue', command= slide9, width= 10,height=3, bg='#DC8377', activebackground='green', border=0)
    btn1.place(x = 550, y = 400)

    win9.mainloop()

def slide7():
    global win8
    win7.destroy()
    win8 = tk.Tk()
    win8.geometry('800x500')
    bg = PhotoImage(file = "6.png")
    bglabel = Label(win8, image = bg)
    bglabel.place(x = 0,y = 0)
    text1 = Label(win8, text = "It seems dark here. Find the switch and turn the lights on!!!", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win8, text='', command= slide8, width= 1,height=1, bg='#DC8377', activebackground='green', border=0)
    btn1.place(x = 245, y = 147)

    win8.mainloop()


def slide6():
    global win7
    win6.destroy()
    root.destroy()
    win7 = tk.Tk()
    win7.geometry('800x500')
    bg = PhotoImage(file = "4.png")
    bglabel = Label(win7, image = bg)
    bglabel.place(x = 0,y = 0)

    text1 = Label(win7, text = "When the blood stains were further examined, \nit was found matching with Prof Nolan.... Lets hurry to his lab", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win7, text='Go to Lab', command= slide7, width= 20,height=3, bg='red', activebackground='green')
    btn1.place(x = 550, y = 400)

    win7.mainloop()


def slide5():
    global win4
    def scan():
        global root
        root = tk.Tk()
        def update_progressbar():
            current_value = progress['value']
    
            if current_value < 100:
                progress['value'] = current_value + 10
                root.after(500, update_progressbar)
            else:
                answer = askyesno(title='confirmation', message='Blood Stains Found!!! Continue???')
                if answer:
                    slide6()

        root.title("Scan")

        progress = ttk.Progressbar(root, length=200, mode='determinate', maximum=100)
        progress.grid(row=0, column=0, padx=10, pady=10)

        start_button = tk.Button(root, text="SCAN", command=update_progressbar)
        start_button.grid(row=1, column=0, pady=10)

        root.mainloop()


    global win4, win6
    win5.destroy()
    root.destroy()
    win6 = tk.Tk()
    win6.geometry('800x500')
    bg = PhotoImage(file = "4.png")
    bglabel = Label(win6, image = bg)
    bglabel.place(x = 0,y = 0)

    text1 = Label(win6, text = "This is Blackwood's rival's scarf. It was found on the crime scene. Lets scan it....", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win6, text='SCAN', command=scan, width= 20,height=3, bg='red', activebackground='green')
    btn1.place(x = 550, y = 400)

    win6.mainloop()

def slide4():
    global win5
    def password():
        global root
        def password_sub():
            password = password_entry.get()
            if str(password) == '7777':
                slide5()
            else:
                password_entry.delete(0, tk.END)

# Create the main window
        root = tk.Tk()
        root.title("Password")
        root.geometry("200x150")

        tk.Label(root, text="Enter Password:").pack(pady=5)
        password_entry = tk.Entry(root, show="*")
        password_entry.pack(pady=5)

        tk.Button(root, text="SUBMIT", command=password_sub).pack(pady=5)

        result_label = tk.Label(root, text="")
        result_label.pack(pady=5)

        root.mainloop()

    root.destroy()
    win4.destroy()
    
    win5 = tk.Tk()
    win5.geometry('1020x635')
    bg = PhotoImage(file = "3.png")
    bglabel = Label(win5, image = bg)
    bglabel.place(x = 0,y = 0)
    text1 = Label(win5, text = "On hacking no significant evidence were found from his tab. \nThis is his suitcase. Ohh its locked!!!. Find the password to open it", font=('Times New Roman', 15))
    text1.place(x=15,y=15)
    text2 = Label(win5, text = "7777", font=('Times New Roman', 10), bg='#BF7066')
    text2.place(x=990,y=5)

    btn1 = tk.Button(win5, text='ENTER PASSWORD', command=password, width= 20,height=3, bg='red', activebackground='green')
    btn1.place(x = 450, y = 500)

    win5.mainloop() 

def slide3():
    global win4
    def hack():
        global root
        root = tk.Tk()
        def update_progressbar():
            current_value = progress['value']
    
            if current_value < 100:
                progress['value'] = current_value + 10
                root.after(500, update_progressbar)
            else:
                slide4()

    
        root.title("HACK")

        progress = ttk.Progressbar(root, length=200, mode='determinate', maximum=100)
        progress.grid(row=0, column=0, padx=10, pady=10)

        start_button = tk.Button(root, text="HACK", command=update_progressbar)
        start_button.grid(row=1, column=0, pady=10)

        root.mainloop()


    global win4
    win3.destroy()
    win4 = tk.Tk()
    win4.geometry('800x500')
    bg = PhotoImage(file = "2.png")
    bglabel = Label(win4, image = bg)
    bglabel.place(x = 0,y = 0)

    text1 = Label(win4, text = "This is Blackwood's personal Tablet. This might contain something crucial. Lets hack into it...", font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win4, text='HACK TABLET', command=hack, width= 20,height=3, bg='red', activebackground='green')
    btn1.place(x = 550, y = 400)

    win4.mainloop()
    

def slide2():
    global win3
    win2.destroy()
    win3 = tk.Tk()
    win3.geometry('1000x600')
    bg = PhotoImage(file = "dead.png")
    bglabel = Label(win3, image = bg)
    bglabel.place(x = 0,y = 0)

    text1 = Label(win3, text = 'This guy was found dead in his bedroom. ON further investigation it was found that he is \nJuilan Blackwood, a genius author known for his dark and intricate mystery novel.\n 4 suspecious leads were found near his deadbody. Let us examine each one them', font=('Times New Roman', 15))
    text1.place(x=15,y=15)

    btn1 = tk.Button(win3, text='LETS BEGIN -->', command=slide3, width= 20,height=3, bg='red', activebackground='green')
    btn1.place(x = 810, y = 280)

    win3.mainloop()

def start():
    global win2
    win.destroy()
    win2 = tk.Tk()
    win2.geometry('1000x600')
    bg = PhotoImage(file = "detective.png")
    bglabel = Label(win2, image = bg)
    bglabel.place(x = 0,y = 0)

    text_det = Label(win2, text = 'Hello I am Alex Mercer. I am a detective. I am currently on a mission. My super power is DATA VISION.\n Come join me in my hunt!!', font=('Times New Roman', 14))
    text_det.place(x = 10, y = 525)
    
    btn1 = tk.Button(win2, text='START INVESTIGATION', width= 20,height=3, bg='red', activebackground='green', command=slide2)
    btn1.place(x = 825, y = 520)

    win2.mainloop()
    

def quito():
    win.destroy()

bg = PhotoImage(file = "intro.png")
bglabel = Label(win, image = bg)
bglabel.place(x = 0,y = 0)
start_button = tk.Button(text='START',height=1,width=10,bg='#37bf22',command=start, font=("Orator Std", 20)) # background colour
start_button.place(x = 540, y = 200)
quitbutton = tk.Button(text='QUIT',height=1,width=10,bg='#37bf22',command=quito, font=("Orator Std", 20)) # background colour
quitbutton.place(x = 540, y = 300)

win.mainloop()