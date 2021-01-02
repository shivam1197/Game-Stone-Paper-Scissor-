from tkinter import *
import tkinter.font as tkfont
import random


global StringValue
def stone():
    StringValue="Stone"
    btn = Button(root, text="Stone", font=fontStyle)
    btn.grid(row=4, column=0)
    computer(StringValue)
    return
def paper():
    StringValue="Paper"
    btn = Button(root, text="Paper", font=fontStyle)
    btn.grid(row=4, column=0)
    computer(StringValue)
    return
def Scissor():
    StringValue="Scissor"
    btn = Button(root, text="Scissor", font=fontStyle)
    btn.grid(row=4, column=0)
    computer(StringValue)
    return

def computer(str):
    string=""
    value=random.randint(1,3)
    if value==1:
        string="Stone"
    elif value==2:
        string="Paper"
    elif value==3:
        string="Scissor"

    btn1 = Button(root, text=f"{string}", font=fontStyle)
    btn1.grid(row=4, column=2)
    compare(str,string)

def compare(StringValue,string):
    if StringValue=="Stone" and string=="Stone":
        #print("Tied")
        lbl_result = Label(root, text="Tied", font=fontStyle)
        lbl_result.grid(row=4, column=1)
    elif StringValue=="Paper" and string=="Paper":
        lbl_result = Label(root, text="Tied", font=fontStyle)
        lbl_result.grid(row=4, column=1)
    elif StringValue=="Scissor" and string=="Scissor":
        lbl_result = Label(root, text="Tied", font=fontStyle)
        lbl_result.grid(row=4, column=1)
    elif StringValue=="Stone" and string=="Paper" or StringValue=="Paper" and string=="Stone":
        lbl_result = Label(root, text="Paper Won", font=fontStyle)
        lbl_result.grid(row=4, column=1)
    elif StringValue=="Stone" and string=="Scissor" or StringValue=="Scissor" and string=="Stone":
        lbl_result = Label(root, text="Stone Won", font=fontStyle)
        lbl_result.grid(row=4, column=1)
    elif StringValue=="Paper" and string=="Scissor" or StringValue=="Scissor" and string =="Paper":
        lbl_result = Label(root, text="Scissor Won", font=fontStyle)
        lbl_result.grid(row=4, column=1)
    else:
        print("not possible")



root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry(f"{w}x{h}")

fontStyle=tkfont.Font(family="Lucida Grande",size=97)
fontsize=tkfont.Font(family="Lucida Grande",size=40)
lbl=Label(root,text="Welcome to Stone Paper Scissor",font=fontStyle,bg="Cyan")
lbl.grid(row=0,column=0,columnspan=3)

lbl1=Label(root,text="Choose",font=fontStyle)
lbl1.grid(row=1,column=0,columnspan=3)

stone=Button(root,text="Stone",font=fontsize,command=stone)
stone.grid(row=2,column=0)
paper=Button(root,text="Paper",font=fontsize,command=paper)
paper.grid(row=2,column=1)
scissor=Button(root,text="Scissor",font=fontsize,command=Scissor)
scissor.grid(row=2,column=2)

lbl1=Label(root,text=" ",font=fontStyle)
lbl1.grid(row=3,column=0,columnspan=3)


# btn=Button(root,text="Pressmee",font=fontStyle)
# btn.grid(row=4,column=0)
lbl_name=Label(root,text="You",font=fontStyle)
lbl_name.grid(row=5,column=0)


# btn1=Button(root,text="Pressmee",font=fontStyle)
# btn1.grid(row=4,column=2)
lbl_ai=Label(root,text="Computer",font=fontStyle)
lbl_ai.grid(row=5,column=2)

root.mainloop()