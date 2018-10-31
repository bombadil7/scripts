"""
Read  and possibly control active processor cores,
frequencies, temperatures etc.
"""

import tkinter as tk 
from tkinter import ttk 
from time import sleep
from threading import Thread


class Application(ttk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Processor Performance")
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.info = ttk.Frame(relief=tk.RIDGE)
        self.info.pack(fill=tk.X, expand=1)
        
        self.lpresent = ttk.Label(self.info, text="Present Cores:")
        self.lpresent.grid(row=0, column=0, padx=10, pady=10)

        self.presentVar = tk.StringVar()
        self.epresent = ttk.Entry(self.info, textvariable=self.presentVar)
        self.epresent.grid(row=0, column=1, padx=10, pady=10)

        self.start_updates()

    def start_updates(self):
        self.t = Thread(target=self.update_status, daemon=True)
        self.t.start()

    def update_status(self):
        while True:
            with open('/sys/devices/system/cpu/present') as present:
                self.presentVar.set(present.read().replace('\n', ''))
            sleep(1)




def main():
    root = tk.Tk()
    app = Application()
    root.geometry("250x100+900+600")
    root.mainloop()


if __name__=="__main__":
    main()
