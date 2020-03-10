#------------------------IMPORTS------------------------------------
from tkinter import *
import tkinter.font as tkFont
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

def fontFaceValueSelect(event):
    global fontface_value
    fontface_value="Consolas"
    '''
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    print(picked)
    value=fontFace.get(ANCHOR)
    value=fontFace.get(fontFace.curselection())
    '''
    index=fontFace.curselection()[0]
    fontface_value=fontFace.get(index)
    print(fontface_value)

def fontStyleValueSelect(event):
    global fontstyle_value
    fontstyle_value="Regular"
    '''
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    print(picked)
    value1=fontStyle.get(ANCHOR)
    value1=fontStyle.get(fontStyle.curselection())
    print(value1)
    '''
    index=fontStyle.curselection()[0]
    fontstyle_value=fontStyle.get(index)
    print(fontstyle_value)


def fontSizeValueSelect(event):
    global fontsize_value
    fontsize_value=14
    '''
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(ANCHOR)
    print(picked)
    value=fontSize.get(ANCHOR)
    value=fontSize.get(fontSize.curselection())
    print(value)
    '''
    index=fontSize.curselection()[0]
    fontsize_value=fontSize.get(index)
    print(fontsize_value)


def setFont():

    global win
    #print(tkFont.families())
    #for i in tkFont.families():
    #    print(i)
    win=Toplevel()
    win_width=550
    win_height=300
    win.geometry(f"{win_width}x{win_height}")
    win.resizable(width=False,height=False)
    win.title("Font")

    frame0=Frame(win)

    Label(frame0,text="Font Face",font=("comicsans",13, "bold"),fg="black").pack(side=LEFT,padx="40",pady="10")
    Label(frame0,text="Font Style",font=("comicsans",13, "bold"),fg="black").pack(side=LEFT,padx="50",pady="10")
    Label(frame0,text="Font Size",font=("comicsans",13, "bold"),fg="black").pack(side=LEFT,padx="40",pady="10")

    frame0.pack(anchor="w")

    frame1=Frame(win)

    global fontFace,fontSize,fontStyle

    fontFace=Listbox(frame1,borderwidth="4",selectmode=SINGLE,exportselection=0)
    fontFace.pack(side=LEFT,fill=Y,padx="2",pady="20")
    fontFace.bind("<<ListboxSelect>>",fontFaceValueSelect)

    for i in tkFont.families():
        fontFace.insert(END,f"{i}")

    #fontFace.insert(END,"First Item")
    #fontFace.insert(ACTIVE,"Second Item")

    scrollBarFont=Scrollbar(frame1,cursor="arrow",orient=VERTICAL)
    scrollBarFont.config(command=fontFace.yview)
    fontFace.config(yscrollcommand=scrollBarFont.set)
    scrollBarFont.pack(side=LEFT,fill=Y,pady="20")

    frame1.pack(anchor="w")


    fontStyle=Listbox(frame1,borderwidth="4",selectmode=SINGLE,exportselection=0)
    fontStyle.pack(side=LEFT,fill=Y,pady="20")
    fontStyle.bind("<<ListboxSelect>>",fontStyleValueSelect)

    fontStyle.insert(END,"normal")
    fontStyle.insert(END,"bold")
    fontStyle.insert(END,"italic")
    fontStyle.insert(END,"bold italic")
    fontStyle.pack(side=LEFT,padx="50")

    '''
    scrollBarStyle=Scrollbar(frame1,cursor="arrow",orient=VERTICAL)
    scrollBarStyle.pack(side=RIGHT,fill=Y,pady="20",padx="20")
    scrollBarStyle.config(command=fontStyle.yview)
    fontStyle.config(yscrollcommand=scrollBarStyle.set)
    '''

    fontSize=Listbox(frame1,borderwidth="4",selectmode=SINGLE,exportselection=0)
    fontSize.pack(side=LEFT,fill=Y,pady="20")
    fontSize.bind("<<ListboxSelect>>",fontSizeValueSelect)

    for i in range(1,101):
        fontSize.insert(END,str(i))

    scrollBarSize=Scrollbar(frame1,cursor="arrow",orient=VERTICAL)
    scrollBarSize.pack(side=LEFT,fill=Y,pady="20")
    scrollBarSize.config(command=fontSize.yview)
    fontSize.config(yscrollcommand=scrollBarSize.set)

    frame1.pack(anchor="w")

    frame3=Frame(win)
    button=Button(win,text="Apply Changes",width="15",height="1",borderwidth="2",command=setFontValues)
    button.config(anchor=CENTER,pady=5)
    button.pack()
    frame3.pack()

def setFontValues():
    values=[fontface_value,fontstyle_value,fontsize_value]


    print(f"({fontface_value} {fontsize_value} {fontstyle_value} )")
    if fontstyle_value=="italic":
        TextArea.configure(font=tkFont.Font(family=fontface_value,size=fontsize_value,slant=fontstyle_value))
    elif fontstyle_value=="bold italic":
        TextArea.configure(font=tkFont.Font(family=fontface_value,size=fontsize_value,weight=fontstyle_value.split()[0],slant=fontstyle_value.split()[1]))
    else:
        TextArea.configure(font=tkFont.Font(family=fontface_value,size=fontsize_value,weight=fontstyle_value))
    TextArea.update()
    win.destroy()


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
