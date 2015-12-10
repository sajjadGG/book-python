#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def create_hi_button(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

    def create_quit_button(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

    def create_yesno_button(self):
        self.yesno = Button(self)
        self.yesno['text'] = 'Ask me a question'
        self.yesno['fg'] = 'white'
        self.yesno['command'] = self.show_yesno_screen
        self.yesno.pack({'side': 'right'})

    def show_yesno_screen(self):
        messagebox.askyesno(
                message='Do you like it?',
                icon='question',
                title='Hi there!')

    def create_widgets(self):
        self.create_quit_button()
        self.create_hi_button()
        self.create_yesno_button()

    def __init__(self, master=None):
        self.frame = Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
