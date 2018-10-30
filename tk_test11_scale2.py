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

        self.pack(fill=BOTH, expand=True)

        self.scale = Scale(self, from_=0, to=100,
            command=self.onScale)
        self.scale.grid(row=0, column=0,
                    padx=10, pady=10, sticky=E+W)

        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.grid(row=0, column=1, sticky=W, padx=10)

        self.grid_columnconfigure(0, weight=1)

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
