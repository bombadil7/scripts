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
        
        ### Present
        self.lpresent = ttk.Label(self.info, text="Present Cores:")
        self.lpresent.grid(row=0, column=0, padx=10, pady=10)

        self.presentVar = tk.StringVar()
        self.epresent = ttk.Entry(self.info, width=5, textvariable=self.presentVar)
        self.epresent.grid(row=0, column=1, padx=10, pady=10)

        ### Online
        self.lonline = ttk.Label(self.info, text="Online Cores:")
        self.lonline.grid(row=0, column=2, padx=10, pady=10)

        self.onlineVar = tk.StringVar()
        self.eonline = ttk.Entry(self.info, width=5, textvariable=self.onlineVar)
        self.eonline.grid(row=0, column=3, padx=10, pady=10)

        self.start_updates()

    def start_updates(self):
        self.t = Thread(target=self.update_status, daemon=True)
        self.t.start()

    def update_status(self):
        while True:
            with open('/sys/devices/system/cpu/present') as device:
                self.presentVar.set(device.read().replace('\n', ''))
            with open('/sys/devices/system/cpu/online') as device:
                self.onlineVar.set(device.read().replace('\n', ''))
            sleep(1)




def main():
    root = tk.Tk()
    app = Application()
  #  root.geometry("250x100+900+600")
    root.mainloop()


if __name__=="__main__":
    main()
