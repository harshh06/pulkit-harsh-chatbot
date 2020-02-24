from tkinter import *
root = Tk()

root.title('My first Project :)')
root.geometry('650x350')
root.configure(bg='#E67E22')

Label(root, text = "Welcome to 'SKALA : The Chatbot'", font = 'ariel 18', bg='#E67E22' ).pack()
Label(root, text = '-------------------------------------', bg='#E67E22').pack()
Label(root, text = "Move mouse over the window to move to the Chatbot" ,bg='#E67E22',  font = 'ariel 16').pack()

def close(e=1):
    root.destroy()

root.bind('<Motion>',close)
root.mainloop()

