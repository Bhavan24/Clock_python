import tkinter
from time import strftime
root = tkinter.Tk()
label1 = tkinter.Label(root, font=("Arial", 100), bg = '#F0EBE5', fg = '#000000')
def update():
	label1.config(text = strftime('%I:%M:%S'))
	label1.after(1000, update)
update()
label1.grid(sticky = 'news')
root.title('Clock')
root.mainloop()