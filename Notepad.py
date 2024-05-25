from tkinter import *
from tkinter import messagebox as msg
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename
def newfile():
    global file
    root.title("Untitled NotePad")
    file=None
    textarea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                    ("Text Document",
    "*.txt")])
    if file == " ":
       file=None
    else:
        root.title(os.path.basename(file)+"- NotePad")
        textarea.delete(1.0,END)
        f=open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()   
    
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                    ("Text Document",
    "*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- NotePad")
            msg.showinfo("Saved","File Saved Successfully")
            
    else:
          f=open(file,"w")
          f.write(textarea.get(1.0,END))
          f.close()
        
def quitapp():
    root.destroy()

    # this event generator Automatically support Paste and letter should be Capital 
    
def cut():
    textarea.event_generate(("<<Cut>>"))

    # this event generator Automatically support Paste and letter should be Capital 
    
def copy():
    textarea.event_generate(("<<Copy>>"))
    
    # this event generator Automatically support Paste and letter should be Capital 
def paste():
    textarea.event_generate(("<<Paste>>"))
    
def about():
    msg.showinfo("NotePad"," Simple Notepad by Mohammed Abdul Akif Ahmed")



if __name__=='__main__':
    root=Tk()
    root.title("NotePad")
    root.geometry("600x500")
    textarea=Text(root,font="lucida 15")
    textarea.pack(expand=True,fill=BOTH)
    file=None
    menubar=Menu(root)
    # file menu start
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="New",command=newfile)
    filemenu.add_command(label="Open",command=openfile)
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitapp)
    menubar.add_cascade(label="File",menu=filemenu)
    # file menu end
    
    # editmenu starts
    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=editmenu)
    
    # editmenu ends
    
    # helpmenu starts
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About NotePad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)
    # helpmenu ends
    scrollbar=Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    root.config(menu=menubar)
    
    
    
    
    
    
    
    
    
    
    root.mainloop()