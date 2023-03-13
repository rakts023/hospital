from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def delete_patient():
    if not op.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
    else:
        dele.pos(op.get())
        
        messagebox.showwarning("Succes","Deleted Successfully.")

        

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    #root.maxsize(935, 455)
    root.title("BLOOD BANK")
    root.configure(bg='lightblue')

   
    label=Label(root,text="DELETE",font="bold",fg="Red")
    label.place(x=450,y=50)

    op=StringVar()


    label2=Label(root,text="PATIENT NAME:")
    label2.place(x=300,y=170)



    e2=Entry(root,textvariable=op,width=40)
    e2.place(x=420,y=170)

   
    b4=Button(root,text="Delete",command=delete_patient,activebackground="red",bg="lightblue",width=30)
    b4.place(x=363,y=240)
    b3=Button(root,text="Back",command=clse,bg="lightblue",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

