from tkinter import *

def finish():
    root.destroy()
    print('zakrito')



root = Tk()
root.title("Приложения")
root.geometry("1080x720")
root.minsize(700, 350)
# root.attributes("-fullscreen", True)
# root.attributes("-alpha", 0.01)
root.protocol("WM_DELETE_WINDOW", finish)

icon = PhotoImage (file="icon.png")
root.iconphoto(False, icon)
Label = Label(text='MONKECOIN ON BANANS!!!')
Label.pack()

def full():
    root.attributes("-fullscreen", True)
    btn["state"] = ["disabled"]     
    btn2["state"] = ["normal"]

def unfull():
    root.attributes("-fullscreen", False)
    btn2["state"] = ["disabled"]
    btn["state"] = ["normal"]

btn = Button(text='на весь экран', command=full, state=["normal"])
btn.pack()
btn2 = Button(text='на весь экран', command=unfull, state=["disabled"])
btn2.pack()
root.mainloop()