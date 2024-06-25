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

clicks = 0

def click_button():
    global clicks
    clicks += 123523424
    btn["text"] = f"У ТЕБЯ {clicks} МONKECOINS!"

btn = Button(text='click me', command=click_button)
btn.pack()
root.mainloop()

