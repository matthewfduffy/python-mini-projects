from tk import *

window = Tk()
window.geometry("600x650")
window.minsize(600, 650)
window.maxsize(600, 650)
window.config(bg="gray")
window.title("PyCalculator")
icon = PhotoImage(file="")
window.iconphoto(False, icon)

scvalue = StringVar()
scvalue.set("")
f = Frame(window, padx=20, pady=20)
screen = Entry(f, textvar=scvalue, font="lucida 50 bold", bg="light blue")
screen.pack(fill=X, padx=20, pady=15)
f.pack()

options1 = ["7", "8", "9", "+"]
options2 = ["4", "5", "6", "-"]
options3 = ["1", "2", "3", "*"]
options4 = ["0", "C", "=", "/"]

f = Frame(window, padx=30, pady=10, bg="gray")
for i in options1, options2, options3, options4:
    b = Button(f, text=i, padx=10, pady=10, font="lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()
window.mainloop()

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


