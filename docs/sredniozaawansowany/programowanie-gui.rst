*****************
Projektowanie GUI
*****************

Biblioteka Tkinter
==================

* http://www.tkdocs.com/tutorial/index.html

.. code-block:: python

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
            self.QUIT["command"] =  self.quit
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


.. code-block:: python

    #!/usr/bin/env python3

    from tkinter import *
    from tkinter import ttk



    def print_hello():
        print('Hello World!')


    root = Tk()

    content = ttk.Frame(root, padding=(3, 3, 12, 12))
    frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
    namelbl = ttk.Label(content, text="Name")
    name = ttk.Entry(content)

    onevar = BooleanVar()
    twovar = BooleanVar()
    threevar = BooleanVar()

    onevar.set(True)
    twovar.set(False)
    threevar.set(True)

    one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
    two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
    three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
    ok = ttk.Button(content, text="Okay")
    cancel = ttk.Button(content, text="Cancel")

    ok['command'] = print_hello

    content.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
    one.grid(column=0, row=3)
    two.grid(column=1, row=3)
    three.grid(column=2, row=3)
    ok.grid(column=3, row=3)
    cancel.grid(column=4, row=3)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.columnconfigure(3, weight=1)
    content.columnconfigure(4, weight=1)
    content.rowconfigure(1, weight=1)

    root.mainloop()

.. code-block:: python

    #!/usr/bin/env python3

    from tkinter import *
    from tkinter import ttk


    root = Tk()

    l = Listbox(root, height=5)
    l.grid(column=0, row=0, sticky=(N,W,E,S))

    s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
    s.grid(column=1, row=0, sticky=(N,S))

    l['yscrollcommand'] = s.set

    ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)


    for i in range(1, 101):
        l.insert('end', 'Line %d of 100' % i)

    root.mainloop()

