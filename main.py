#------------------------IMPORTS------------------------------------
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

#----------------------Functions--------------------------------------
def newFile():
    '''
    Opens a new file with name Untitled.txt
    '''
    global file
    #Title of window Untitled.txt
    root.title("Untitled-Notepad")
    file=None
    #Delete all the contents of previous file from 1st line 0th cloumn till End of file
    TextArea.delete(1.0,END)

def openFile():
    '''
    Opens an existing file
    '''
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        #Title of thw window will be the name of file.txt
        root.title(os.path.basename(file)+" - Notepad")
        #delete the existing content of previous file if any
        TextArea.delete(1.0,END)
        #open the file in read mode
        text=open(file,"r")
        #place the content in the TextArea from 1st line 0th column till end
        TextArea.insert(1.0,text.read())
        #close the file
        text.close()

def saveFile():
    '''
    Saves the file
    '''
    global file
    if file is None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            print("File saved")
    else:
        '''
        If file is present then only save the content of the file by opening it ad writing the contents in the existing file
        '''
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitApp():
    '''
    Closes the application
    '''
    root.destroy()

def cutText():
    '''
    Tkinters builtin event CUT
    '''

    TextArea.event_generate(("<<Cut>>"))

def copyText():
    '''
    Tkinters builtin event COPY
    '''
    TextArea.event_generate(("<<Copy>>"))

def pasteText():
    '''
    Tkinters builtin event PASTE
    '''
    TextArea.event_generate(("<<Paste>>"))

def details():
    '''
    Details of the Application
    Used Tkinter's messagebox.showinfo()
    '''
    message="This notepad application is made using Tkinter module of python"
    tmsg.showinfo("About Notepad Application",message=message)

def setFont():
    pass

root=Tk()
#application will open as Untitled.txt
root.title("Untitled-Notepad")
root.wm_iconbitmap("Tatice-Cristal-Intense-Notepad-Bloc-notes-2.ico")
width=644
height=788
root.geometry(f"{width}x{height}")
file=None
#Initial font Configurations
TextArea=Text(root,font=("Consolas 14"))
TextArea.pack(expand=True,fill=BOTH)
#expand takes the size of the window an fill enables to stretch across both axis

#Main Menu
menuBar=Menu(root)
#File Menu
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New File",command=newFile)
fileMenu.add_command(label="Open File",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitApp)
menuBar.add_cascade(label="File",menu=fileMenu)

#Edit Menu
editMenu=Menu(menuBar,tearoff=0)
editMenu.add_command(label="Cut",command=cutText)
editMenu.add_command(label="Copy",command=copyText)
editMenu.add_command(label="Paste",command=pasteText)
menuBar.add_cascade(label="Edit",menu=editMenu)
root.config(menu=menuBar)

#Format Menu
formatMenu=Menu(menuBar,tearoff=0)
formatMenu.add_command(label="Font",command=setFont)
menuBar.add_cascade(label="Format",menu=formatMenu)

#Help Menu
helpMenu=Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=details)
menuBar.add_cascade(label="Help",menu=helpMenu)
root.config(menu=menuBar)

#ScrollBar configured with TextArea
scrollBar=Scrollbar(TextArea,cursor="arrow")
scrollBar.pack(side=RIGHT,fill=Y)
scrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scrollBar.set)
root.mainloop()
