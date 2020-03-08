from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        text=open(file,"r")
        TextArea.insert(1.0,text.read())
        text.close()

def saveFile():
    global file
    if file is None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])


def quitApp():
    root.destroy()

def cutText():
    TextArea.event_generate(("<<Cut>>"))

def copyText():
    TextArea.event_generate(("<<Copy>>"))

def pasteText():
    TextArea.event_generate(("<<Paste>>"))

def details():
    message="This notepad application is made using Tkinter module of python"
    tmsg.showinfo("About Notepad Application",message=message)

def setFont():
    pass

root=Tk()
root.title("Untitled-Notepad")
root.wm_iconbitmap("Tatice-Cristal-Intense-Notepad-Bloc-notes-2.ico")
width=644
height=788
root.geometry(f"{width}x{height}")
file=None
TextArea=Text(root,font=("lucida 13 bold italic"))
TextArea.pack(expand=True,fill=BOTH)

menuBar=Menu(root)
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New File",command=newFile)
fileMenu.add_command(label="Open File",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitApp)
menuBar.add_cascade(label="File",menu=fileMenu)


editMenu=Menu(menuBar,tearoff=0)
editMenu.add_command(label="Cut",command=cutText)
editMenu.add_command(label="Copy",command=copyText)
editMenu.add_command(label="Paste",command=pasteText)
menuBar.add_cascade(label="Edit",menu=editMenu)
root.config(menu=menuBar)

formatMenu=Menu(menuBar,tearoff=0)
formatMenu.add_command(label="Font",command=setFont)
menuBar.add_cascade(label="Format",menu=formatMenu)

helpMenu=Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=details)
menuBar.add_cascade(label="Help",menu=helpMenu)
root.config(menu=menuBar)

scrollBar=Scrollbar(TextArea,cursor="arrow")
scrollBar.pack(side=RIGHT,fill=Y)
scrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scrollBar.set)
root.mainloop()
