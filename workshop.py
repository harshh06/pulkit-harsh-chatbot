from tkinter import *
import workshop1
root = Tk()
root.configure(bg = "#E67E22")
root.title('Chat Bot')
root.geometry('650x750')
l1=Listbox(root,width=80,height=23)
l1.place(x=1,y=1)
def hi():
    a="hello i am skala"
    l1.insert(END,a)

def how():
    a="I am fine . Thank you"
    l1.insert(END,a)
    
def where():
    a="I am JUET,GUNA"
    l1.insert(END,a)

def created():
    a="I am created by Skala development group,CSI JUET"
    l1.insert(END,a)

def recommend():
    a="You should listen Haaye Garmi from Street Dancer 3"
    l1.insert(END,a)

def movie():
    a="Highest imbd rated movie is Shawshank Redemption "
    l1.insert(END,a)

def hi():
    a="hello i am skala"
    l1.insert(END,a)

def restaurant():
    a=" 'Varun' is one of best restaurant near college situated in Guna ."
    l1.insert(END,a)

def clear():
    root.destroy()
    
Button(root,text='Hi !!',command=hi , bg ='#F7F9F9').place(x=24,y=450)
Button(root,text='How are you ?',command=how , bg ='#F7F9F9').place(x=24,y=500)
Button(root,text='Where are you from ?',command=where , bg ='#F7F9F9').place(x=24,y=550)
Button(root,text='Who created you ?',command=created , bg ='#F7F9F9').place(x=24,y=600)
Button(root,text='Recommend me a song !!',command=recommend , bg ='#F7F9F9').place(x=300,y=450)
Button(root,text='Highest imdb rated movie ?',command=movie , bg ='#F7F9F9').place(x=300,y=500)
Button(root,text='Best restaurant near your college ?',command=restaurant, bg ='#F7F9F9').place(x=300,y=550)
Button(root,text='Exit..',command=clear, bg = "red", fg="white").place(x=300,y=600)

root.mainloop()
