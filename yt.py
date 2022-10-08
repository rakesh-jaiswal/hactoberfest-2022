from email import message
from sysconfig import get_path
from tabnanny import check
from tkinter import *
from tkinter import filedialog
from pytube import YouTube,Playlist
import os

def d():
    gp=filedialog.askdirectory()
    lu=t.get()

    if check.get()==1:
        yt=YouTube(lu)
        yt.stream.get_highest_resolution().download(got_path)
    elif check.get()==2:
        ytp=Playlist(lu)
        for videos in ytp.videos:
            videos.stream.get_highest_resolution().download(got_path)
    message.showinfo('Download Succesfully')
    os.startfile(got_path)

root=Tk()

root.title("Downloader")
root.config(bg="red2")

of=Frame(root)
of.grid(row=0,column=0,padx=20,pady=30)

li=PhotoImage(file="youtube.png")
ll=Label(of,image=li)
ll.grid(row=0,column=0,pady=20)

ifr=LabelFrame(of,text="Download",font=('arial black',14,'bold'))
ifr.grid(row=1,column=0)

check=IntVar()
ri1=PhotoImage(file="multimedia.png")
vb=Radiobutton(ifr,image=ri1,text="  Single video",compound=LEFT,font=('arial black',14,'bold'),padx=20,pady=30,variable=check,value=1)
vb.grid(row=0,column=0)

ri2=PhotoImage(file="videos.png")
vb2=Radiobutton(ifr,image=ri2,text="  Playlist",compound=RIGHT,font=('arial black',14,'bold'),padx=20,pady=30,variable=check,value=2)
vb2.grid(row=0,column=1)

t=StringVar()
uef=Entry(of,width=50,font=('arial black',14,'bold'),justify='center',textvariable=t,fg='gray')
uef.grid(row=2,column=0,padx=20,pady=30)
t.set('Enter URL')

def c(event):
    uef.delete(0,END)
    uef.config(fg='black')

uef.bind('<Button-1>',c)

dip=PhotoImage(file="download.png")
db=Button(of,image=dip,command=d)
db.grid(row=3,column=0,pady=30)

root.mainloop()