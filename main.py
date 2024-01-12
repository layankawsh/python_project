from tkinter import  *
def btnClick1():
    ser=Tk()
    ser.configure(background="#f2f3f4")
    l=Label()
    l1=Label(ser,text=" if you want to add it to your receipt\n just click on it ",fg="#915c83",font=("Century Gothic",50))
    b1 = Button(ser, text="Nails 20JD ",font=("Century Gothic",25),fg="#f2f3f4",background="#915c83",command=btnClick3)
    b2 = Button(ser, text="Skin 30JD",font=("Century Gothic",25),fg="#f2f3f4",background="#915c83",command=btnClick4)
    b4 = Button(ser, text="Makeup 50JD", font=("Century Gothic",25),fg="#f2f3f4",background="#915c83",command=btnClick5)
    b5 = Button(ser, text="Hair 45JD",font=("Century Gothic",25),fg="#f2f3f4",background="#915c83",command=btnClick6)
    l1.pack()
    b1.pack(pady=20)
    b2.pack(pady=20)
    b4.pack(pady=20)
    b5.pack(pady=20)
def btnClick2():
    ofr = Tk()
    ofr.configure(background="#f2f3f4")
    l = Label()
    l1 = Label(ofr, text=" if you want to add the offer to your receipt\n just click on it ", fg="#915c83",
               font=("Century Gothic", 40))

    b1 = Button(ofr, text="Nails+hair 55JD ", font=("Century Gothic", 25), fg="#f2f3f4", background="#915c83",command=btnClick7)
    b2 = Button(ofr, text="Skin + makeup 70JD", font=("Century Gothic", 25), fg="#f2f3f4", background="#915c83",command=btnClick8)
    l1.pack()
    b1.pack(pady=20)
    b2.pack(pady=20)
def btnClick3():
     myfile=open("receipt.txt","a")
     myfile.writelines("Services,Nails,20,end\n")

def btnClick4():
        myfile = open("receipt.txt", "a")
        myfile.writelines("Services,Nails,30,end\n")
def btnClick7():
    myfile = open("receipt.txt", "a")
    myfile.writelines("offers,Nails+hair, 55,end\n")
def btnClick8():
    myfile = open("receipt.txt", "a")
    myfile.writelines("offers,Skin + makeup ,70,end\n")
def btnClick5():
            myfile = open("receipt.txt", "a")
            myfile.writelines("Services,Nails,50,end\n")
def btnClick6():
 myfile = open("receipt.txt", "a")
 myfile.writelines("Services,Nails,45,end\n")
def btnClick9():

    cl=Tk()
    l4=Label()
    myfile=open("receipt.txt","r")
    alldata=myfile.readlines()
    total=0
    for x in alldata:
      data=x.split(",")
      total=total+float(data[2])
      t=(" your total :",total)
    l5 = Label(cl, text=t, font=("Century Gothic", 25), fg="#f2f3f4", background="#915c83")
    l5.pack()

myfile = open("receipt.txt", "w")
myfile.writelines(" ")
tk=Tk()
tk.configure(background="#f2f3f4")
main=Label(tk,text=" Welcome To Our Beauty Center  ",fg="#915c83",font=("Century Gothic",60))
lbl1=Button(tk,text="our services ",font=("Century Gothic",30),fg="#f2f3f4",background="#915c83",command=btnClick1)
lbl2=Button(tk,text="our offers",font=("Century Gothic",30),fg="#f2f3f4",background="#915c83",command=btnClick2)
lbl3=Button(tk,text="close",font=("Century Gothic",30),fg="#f2f3f4",background="#915c83",command=btnClick9)
main.pack()
lbl1.pack(pady=20)
lbl2.pack(pady=20)
lbl3.pack()
tk.mainloop()
