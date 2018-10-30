#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we show how to
use the Scale widget.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from tkinter import Tk, BOTH, X, IntVar, LEFT, SUNKEN, E, W
from tkinter.ttk import Frame, Label, Scale, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.master.title("Scale")
        self.style = Style()
        self.style.theme_use("default")

        self.frame = Frame(height=10, width=100, relief=SUNKEN)
        self.frame.pack(fill=X, expand=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.scale = Scale(self.frame, from_=0, to=100,
            command=self.onScale)
        self.scale.grid(row=0, column=0, columnspan=2,
                    padx=10, pady=10, sticky=E+W)
        #scale.pack(fill=X, padx=15, expand=1)
        #scale.pack(fill=X, padx=15)

        self.var = IntVar()
        self.label = Label(self.frame, text=0, textvariable=self.var)
        self.label.grid(row=0, column=2, sticky=W, padx=10)
        # self.label.pack(side=LEFT)


    def onScale(self, val):

        v = int(float(val))
        self.var.set(v)


def main():

    root = Tk()
    ex = Example()
    root.geometry("250x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
