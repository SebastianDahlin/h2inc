from tkinter import Tk, Label, Button
from tkinter import filedialog
from tkinter import *
import os
from os.path import expanduser
import platform
import sys
from h2inc import sourcedir_filecnt, sourcedir_foldercnt, cnt

class h2incGUI:
    def __init__(self, master):
        self.sourcedir = StringVar()
        self.destdir = StringVar()
        self.addinc = StringVar()
        self.infofolder = 'Number of folders: 0'
        self.infofile = 'Number of headers: 0'

        self.sourcedir.set('Select source directory!')
        self.destdir.set('Select destination directory!')

        self.master = master
        self.master.title('Translate C-header files to Nasm include files!')
        self.master.grid_columnconfigure(1, weight=1)

        self.frame = LabelFrame(master, text='Select folders')
        self.frame.grid(row=0, column=0, columnspan=3, sticky=N+S+E+W, padx=5, pady=5)
        self.frame.grid_columnconfigure(1, weight=1)

        self.sourcelabel = Label(self.frame, text='Source: ')
        self.sourcelabel.grid(row=0, column=0, sticky=E, padx=(5, 1), pady=5)

        self.sourceentry = Entry(self.frame, textvariable=self.sourcedir)
        self.sourceentry.grid(row=0, column=1, sticky=E+W, pady=5)

        self.sourcedir_button = Button(self.frame, text="Source directory...", command= lambda: self.select_sourcedir(self.sourcedir, self.infofiles))
        self.sourcedir_button.grid(row=0, column=2, sticky=W, padx=(3, 5), pady=5)

        self.destlabel = Label(self.frame, text='Destination: ')
        self.destlabel.grid(row=1, column=0, sticky=E, padx=(5, 1), pady=5)
        self.destlabel.config(state=DISABLED)

        self.destentry = Entry(self.frame, textvariable=self.destdir)
        self.destentry.grid(row=1, column=1, sticky=E+W, pady=5)
        self.destentry.config(state=DISABLED)

        self.destdir_button = Button(self.frame, text="Destination directory...", command= lambda: self.select_destdir(self.destdir))
        self.destdir_button.grid(row=1, column=2, sticky=W, padx=(3, 5), pady=5)
        self.destdir_button.config(state=DISABLED)

        self.incchkbox = Checkbutton(self.frame, text='Create "include" folder if it does not exist.', variable=self.addinc, onvalue='yes', offvalue='no')
        self.incchkbox.grid(row=2, column=0, columnspan=2, sticky=W, padx=5, pady=5)
        self.incchkbox.config(state=DISABLED)
        self.addinc.set('yes')

        self.transframe = LabelFrame(master, text='Translation')
        self.transframe.grid(row=1, rowspan=2, column=0, columnspan=3, sticky=N+S+E+W, padx=5, pady=5)
        self.transframe.grid_columnconfigure(1, weight=1)
        self.transframe.grid_rowconfigure(1, weight=1)

        self.infoframe = LabelFrame(self.transframe, text='Source information')
        self.infoframe.grid(row=1, rowspan=2, column=0, columnspan=3, sticky=N+S+E+W, padx=5, pady=5)
        self.infoframe.grid_columnconfigure(1, weight=1)

        self.infofolders = Label(self.infoframe, text=self.infofolder)
        self.infofolders.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.infofolders.config(state=DISABLED)

        self.infofiles = Label(self.infoframe, text=self.infofile)
        self.infofiles.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.infofiles.config(state=DISABLED)

        self.translate_button = Button(self.transframe, text="Translate!", command= lambda: self.select_destdir(self.destdir))
        self.translate_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.translate_button.config(state=DISABLED)

    def select_sourcedir(self, sourcedir, infofile):
        root.directory = os.path.abspath(filedialog.askdirectory())
        if root.directory:
            sourcedir.set(root.directory)
            filecnt = sourcedir_filecnt(root.directory)
            if filecnt > 0:
                tempstr = 'Number of headers: '+str(filecnt)
                print ('Source directory: ', sourcedir.get())
                self.destlabel.config(state=NORMAL)
                self.destentry.config(state=NORMAL)
                self.destdir_button.config(state=NORMAL)
                self.infofiles.config(text=tempstr)
                foldercnt = sourcedir_foldercnt(root.directory)
                if foldercnt > 0:
                    tempstr = 'Number of folders: '+str(foldercnt)
                    self.infofolders.config(text=tempstr)

    def select_destdir(self, destdir):
        root.directory = filedialog.askdirectory()
        if root.directory:
            destdir.set(root.directory)
            print ('Destination directory: ', destdir.get())
            self.incchkbox.config(state=NORMAL)
            self.infofolders.config(state=NORMAL)
            self.infofiles.config(state=NORMAL)
            self.translate_button.config(state=NORMAL)

        

root = Tk()
root.update()
#root.minsize(350, 210)
#width = (root.winfo_screenwidth()/2)-(350/2)
#height = (root.winfo_screenheight()/2)-(210/2)
#root.geometry('+%d+%d' % (width, height))
root.resizable(False, False)
h2incgui = h2incGUI(root)
root.mainloop()