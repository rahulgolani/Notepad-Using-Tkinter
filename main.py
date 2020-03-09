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
    global file
    if file is None:
        saveAsFile()
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()


def saveAsFile():
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

def setValues():

    global new_Width, new_Height
    #print(f"{new_Width.get()},{new_Height.get()}")
    #print(new_Width.get())
    #print(new_Height.get())
    root.geometry(f"{new_Width.get()}x{new_Height.get()}")
    win.destroy()

def resizeWindow():
    '''
    Resizes the window as per the width and height values given by the user
    '''

    global new_Width,new_Height
    #variables to store the value of new Width and Height
    new_Width=StringVar()
    new_Height=StringVar()
    #creating a new window
    global win
    win=Toplevel()
    win_width=425
    win_height=200
    win.title("Resize Window")
    win.geometry(f"{win_width}x{win_height}")
    #limiting windowsize to 410x200
    win.minsize(410,200)
    #win.maxsize(700,700)

    frame1=Frame(win)
    label=Label(frame1,text="Enter the Width and Height values",font=("Consolas 14 bold"))
    label.config(anchor=CENTER)
    label.pack(fill=BOTH)
    #label.grid(row=0,column=6)
    frame1.pack()

    frame2=Frame(win)

    Label(frame2,text="Enter Width",pady=20,padx=5).pack(side=LEFT)
    #Width Box
    width_value=Entry(frame2,text="Enter Width",textvariable=new_Width)
    width_value.pack(side=LEFT,pady=20)

    Label(frame2,text="Enter Height",pady=20,padx=5).pack(side=LEFT)
    #Height Box
    height_value=Entry(frame2,text="Enter Height",textvariable=new_Height)
    height_value.pack(side=LEFT,pady=20)
    frame2.pack()

    frame3=Frame(win)
    button=Button(win,text="Set",width="10",height="1",command=setValues)
    button.config(anchor=CENTER,pady=5)
    button.pack()


def wrapText():
    global twrap,data
    print(twrap.get())
    #print(twrap.get())
    if twrap.get():
        TextArea.config(wrap=CHAR)
        TextArea.update()
    else:
        #data=TextArea.get(1.0,END)
        #TextArea.delete(1.0,END)
        TextArea.config(wrap="none")
        #TextArea.insert(1.0,data)
        TextArea.update()
    #TextArea.pack(expand=True,fill=BOTH)

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
TextArea.config(wrap="none")
TextArea.pack(expand=True,fill=BOTH)
#expand takes the size of the window an fill enables to stretch across both axis

#Main Menu
menuBar=Menu(root)
#File Menu
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New File",command=newFile)
fileMenu.add_command(label="Open File",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Save As",command=saveAsFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitApp)
menuBar.add_cascade(label="File",menu=fileMenu)
root.config(menu=menuBar)

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
root.config(menu=menuBar)

#View Menu
global twrap
twrap=BooleanVar()
viewMenu=Menu(menuBar,tearoff=0)
viewMenu.add_command(label="Resize Window",command=resizeWindow)
viewMenu.add_checkbutton(label="Toggle Wrap",variable=twrap,command=wrapText)
menuBar.add_cascade(label="View",menu=viewMenu)
root.config(menu=menuBar)

#Help Menu
helpMenu=Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=details)
menuBar.add_cascade(label="Help",menu=helpMenu)
root.config(menu=menuBar)

#Y-AXIS ScrollBar configured with TextArea
scrollBar=Scrollbar(TextArea,cursor="arrow",orient=VERTICAL)
scrollBar.pack(side=RIGHT,fill=Y)
scrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scrollBar.set)

#X-AXIS ScrollBar configured with TextArea
scrollBarX=Scrollbar(TextArea,cursor="arrow",orient=HORIZONTAL)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarX.config(command=TextArea.xview)
TextArea.config(xscrollcommand=scrollBarX.set)

root.mainloop()
