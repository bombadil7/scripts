"""
Read  and possibly control active processor cores,
frequencies, temperatures etc.
"""

import tkinter as tk 
from tkinter import ttk 
from time import sleep
from threading import Thread
from datetime import datetime


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
        block = ttk.Frame(self.info, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        self.lpresent = ttk.Label(block, text="Present Cores:")
        self.lpresent.pack(side=tk.LEFT, padx=3, pady=3)

        self.presentVar = tk.StringVar()
        self.epresent = ttk.Entry(block, width=5, textvariable=self.presentVar)
        self.epresent.pack(side=tk.LEFT, padx=3, pady=3)

        ### Online
        block = ttk.Frame(self.info, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        self.lonline = ttk.Label(block, text="Online Cores:")
        self.lonline.pack(side=tk.LEFT, padx=3, pady=3)

        self.onlineVar = tk.StringVar()
        self.eonline = ttk.Entry(block, width=5, textvariable=self.onlineVar)
        self.eonline.pack(side=tk.LEFT, padx=3, pady=3)

        ### Offline
        block = ttk.Frame(self.info, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        self.loffline = ttk.Label(block, text="Offline Cores:")
        self.loffline.pack(side=tk.LEFT, padx=3, pady=3)

        self.offlineVar = tk.StringVar()
        self.eoffline = ttk.Entry(block, width=5, textvariable=self.offlineVar)
        self.eoffline.pack(side=tk.LEFT, padx=3, pady=3)

        ### Time 
        block = ttk.Frame(self.info, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        self.lnow = ttk.Label(block, text="Time Stamp:")
        self.lnow.pack(side=tk.LEFT, padx=3, pady=3)

        self.nowVar = tk.StringVar()
        self.enow = ttk.Entry(block, width=8, textvariable=self.nowVar)
        self.enow.pack(side=tk.LEFT, padx=3, pady=3)


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
            with open('/sys/devices/system/cpu/offline') as device:
                self.offlineVar.set(device.read().replace('\n', ''))
            now = datetime.now()
            self.nowVar.set(now.strftime("%H:%M:%S"))
            sleep(1)




def main():
    root = tk.Tk()
    app = Application()
  #  root.geometry("250x100+900+600")
    root.mainloop()


if __name__=="__main__":
    main()
