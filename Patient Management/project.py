'''
    This program is a GUI based program using Tkinter and files for maintaining a simple patient database
'''
'''
*************************************************************************************************************************
*                                                    MODULES USED                                                       *
*************************************************************************************************************************
'''
import tkinter as tk
import os.path
from os import path
'''
*************************************************************************************************************************
*                                                   FUNCTIONS USED                                                    *
*************************************************************************************************************************
'''
def display(string):
    for i in range(70):
        print("=",end='')
        if(i==69):
            print("\n\t\t\t ",string,end='\n')
            for j in range(70):
                print("=",end='')
            print(end='\n')
            

def fetch(datas):
    display("PATIENT'S DETAILS")
    print("\n\tThe patient's datas are:",end='\n')
    for data in datas:
        q=data[0]
        ans=data[1].get()
        print(q,":",ans)


def save(datas):
    if(path.exists("patient.txt")==1):
        f=open("patient.txt.","a+")
    else:
        f=open("patient.txt","w+")
    for data in datas:
        q=data[0]
        ans=data[1].get()
        f.write(ans)
        f.write('\n')
    f.write('\n')
    print("\t\tSUCCESSFULLY SAVED THE DETAILS IN THE FILE !!")
    f.close()
    
    
def make(root,info):
    entry=[]
    a=tk.Label(root,width=40,text="Use 'tab' key to switch between Entries",font=('Helvitica',11,'bold'))
    a.pack(side=tk.TOP)
    for data in info:
        r=tk.Frame(root)
        l=tk.Label(r,width=15, text=data,anchor='w')
        e=tk.Entry(r)
        r.pack(side=tk.TOP,fill=tk.X,padx=5,pady=5)
        l.pack(side=tk.LEFT)
        e.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.X)
        entry.append((data,e))
    b=tk.Label(root,width=40,text="If you want to save the details, \nthen please click on 'save' button",font=('Helvitica',8,'bold'))
    b.pack(side=tk.TOP)
    return entry


def main():
    info=["Patient's Name","age","Sex","Phone number","Address","Doctor's name"]
    root=tk.Tk()
    ent=make(root,info)
    b1=tk.Button(root,text='Save',command=(lambda e=ent:save(e)))
    b1.pack(side=tk.LEFT,padx=5,pady=5)
    b2=tk.Button(root,text='Display',command=(lambda e=ent:fetch(e)))
    b2.pack(side=tk.LEFT,padx=5,pady=5)
    b3= tk.Button(root, text='Exit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
    
'''
*************************************************************************************************************************
*                                                    MAIN PROGRAM                                                       *
*************************************************************************************************************************
'''
main()
