import tkinter
from tkinter import *
from tkinter import messagebox
import json
dct={}
with open('users.json','w')as f:
    dct=json.dump(dct,f)

##for i in range (3):
##    user=input('user')
##    password=input('password')
##    if user  in  dct:
##        dct[user]= password
    
with open('users.json','w')as f:
    dct=json.dump(dct,f)
win=Tk()
win.title('REGISTRATION')
win.geometry("500x300")
win.configure(bg="whitesmoke")
lbl=Label(win,text="What Do You Want To Do?" ,font=("Arial" , 20), fg="navy",pady=20)
lbl.pack()
#username=Entry(win)
#username.pack()
with open('d:/users.json')as f:
    dct=json.load(f)
    
dct={}


def submit():  
    mywin1=tkinter.Toplevel(win)
    mywin1.geometry('300x200+500-200')
    
    
    lbl1=tkinter.Label(mywin1,text='new_user name')
    lbl1.pack()
    txt1=tkinter.Entry(mywin1,width=30,)
    txt1.pack()
    user=txt1.get()

    lbl2=tkinter.Label(mywin1,text='password')
    lbl2.pack()
    txt2=tkinter.Entry(mywin1,width=30,)
    txt2.pack()
    password=txt2.get()

    lbl=tkinter.Label(mywin1,text='')
    lbl.pack()

    username=txt1.get()
    password=txt2.get()

    
    with open('d:/users.json')as f:
        dct=json.load(f)

    if user not in dct:
        dct[user]=password



    if txt1 in dct:
        lbl.configure(text="already exist",fg="red",pady=10)
    else:
        dct[txt1]=password
        
    mybtn=tkinter.Button(mywin1,text='submit',command=submit)
    mybtn.pack()
    


        


    mywin1.mainloop()

with open('d:/users.json','w')as f:
    json.dump(dct,f)


def login():
  
    mywin2=tkinter.Toplevel(win)
    mywin2.geometry('300x200+500-200')
    
    lbl2=tkinter.Label(mywin2,text='user name')
    lbl2.pack()
    txt2=tkinter.Entry(mywin2,width=30,)
    txt2.pack()

    lbl3=tkinter.Label(mywin2,text='password')
    lbl3.pack()
    txt3=tkinter.Entry(mywin2,width=30,)
    txt3.pack()

    mybtn=tkinter.Button(mywin2,text='login',command=login)
    mybtn.pack()

    username=txt2.get()
    password=txt3.get()

    with open('d:/users.json')as f:
        dct=json.load(f)

        if username in dct:
            lbl.configure(text="welcome",fg="green",pady=10)




    
def delete():
    lbl.configure(text="")
        
    mywin2=tkinter.Toplevel(win)
    mywin2.geometry('300x200+500-200')
    
    lbl2=tkinter.Label(mywin2,text='user name')
    lbl2.pack()
    txt2=tkinter.Entry(mywin2,width=30,)
    txt2.pack()

    lbl3=tkinter.Label(mywin2,text='password')
    lbl3.pack()
    txt3=tkinter.Entry(mywin2,width=30,)
    txt3.pack()



    
    mybtn=tkinter.Button(mywin2,text='delete',command=delete)
    mybtn.pack()

    username=txt2.get()
    password=txt3.get()

    lbl4=tkinter.Label(mywin2,text='password')
    lbl4.pack()

    if(username=="" or password==""):
        lbl4.configure(text="caution: your accaunt will  delete !",fg="red")
        lbl4.pack()

    with open('d:/users.json')as f:
        dct=json.load(f)
        if username in dct:
            dct.pop(username)
            lbl.configure(text="deleted",fg="green",pady=10)
    

def exitt():
    win.destroy()

btn1=Button(text="submit",command=submit,padx=17,pady=8,bg='white')
btn1.pack()
btn2=Button(text="login",command=login,padx=22,pady=8,bg='white')
btn2.pack()
btn3=Button(text="delete",command=delete,padx=20,pady=8,bg='white')
btn3.pack()
btn4=Button(text="exit",command=exitt,padx=26,pady=8,bg='white')
btn4.pack()




win.mainloop()


