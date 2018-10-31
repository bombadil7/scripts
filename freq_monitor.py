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


        ## Overview ----------------------------##
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


        ## CPU0 --------------------------------##
        self.cpu0 = ttk.Frame(relief=tk.RIDGE)
        self.cpu0.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.cpu0, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(block, text="CPU0 Current Freq:").pack(side=tk.LEFT, padx=3, pady=3)
        self.c0curfreqVar = tk.StringVar()
        self.ec0curfreq = ttk.Entry(block, width=9, textvariable=self.c0curfreqVar)
        self.ec0curfreq.pack(side=tk.LEFT, padx=3, pady=3)


        ## CPU1 --------------------------------##
        self.cpu1 = ttk.Frame(relief=tk.RIDGE)
        self.cpu1.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.cpu1, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(block, text="CPU1 Current Freq:").pack(side=tk.LEFT, padx=3, pady=3)
        self.c1curfreqVar = tk.StringVar()
        self.ec1curfreq = ttk.Entry(block, width=9, textvariable=self.c1curfreqVar)
        self.ec1curfreq.pack(side=tk.LEFT, padx=3, pady=3)


        ## CPU2 --------------------------------##
        self.cpu2 = ttk.Frame(relief=tk.RIDGE)
        self.cpu2.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.cpu2, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(block, text="CPU2 Current Freq:").pack(side=tk.LEFT, padx=3, pady=3)
        self.c2curfreqVar = tk.StringVar()
        self.ec2curfreq = ttk.Entry(block, width=9, textvariable=self.c2curfreqVar)
        self.ec2curfreq.pack(side=tk.LEFT, padx=3, pady=3)


        ## CPU3 --------------------------------##
        self.cpu3 = ttk.Frame(relief=tk.RIDGE)
        self.cpu3.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.cpu3, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(block, text="CPU3 Current Freq:").pack(side=tk.LEFT, padx=3, pady=3)
        self.c3curfreqVar = tk.StringVar()
        self.ec3curfreq = ttk.Entry(block, width=9, textvariable=self.c3curfreqVar)
        self.ec3curfreq.pack(side=tk.LEFT, padx=3, pady=3)


        ## CPU4 --------------------------------##
        self.cpu4 = ttk.Frame(relief=tk.RIDGE)
        self.cpu4.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.cpu4, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(block, text="CPU4 Current Freq:").pack(side=tk.LEFT, padx=3, pady=3)
        self.c4curfreqVar = tk.StringVar()
        self.ec4curfreq = ttk.Entry(block, width=9, textvariable=self.c4curfreqVar)
        self.ec4curfreq.pack(side=tk.LEFT, padx=3, pady=3)


        ## CPU5 --------------------------------##
        self.cpu5 = ttk.Frame(relief=tk.RIDGE)
        self.cpu5.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.cpu5, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Label(block, text="CPU5 Current Freq:").pack(side=tk.LEFT, padx=3, pady=3)
        self.c5curfreqVar = tk.StringVar()
        self.ec5curfreq = ttk.Entry(block, width=9, textvariable=self.c5curfreqVar)
        self.ec5curfreq.pack(side=tk.LEFT, padx=3, pady=3)


        ## Browser -----------------------------##
        self.browser = ttk.Frame(relief=tk.RIDGE)
        self.browser.pack(fill=tk.X, expand=1)

        ### Current Frequency
        block = ttk.Frame(self.browser, relief=tk.GROOVE)
        block.pack(side=tk.LEFT, padx=5, pady=5)

        self.lbrow = ttk.Label(block, text="Current Folder:")
        self.lbrow.pack(side=tk.TOP, padx=3, pady=3)


        # TODO: Add min, max, control options, controls, temperatures

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

            with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq') as device:
                self.c0curfreqVar.set(device.read().replace('\n', ''))

            with open('/sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq') as device:
                self.c1curfreqVar.set(device.read().replace('\n', ''))

            with open('/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq') as device:
                self.c2curfreqVar.set(device.read().replace('\n', ''))

            with open('/sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq') as device:
                self.c3curfreqVar.set(device.read().replace('\n', ''))

            with open('/sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq') as device:
                self.c4curfreqVar.set(device.read().replace('\n', ''))

            with open('/sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq') as device:
                self.c5curfreqVar.set(device.read().replace('\n', ''))



            sleep(1)




def main():
    root = tk.Tk()
    app = Application()
  #  root.geometry("250x100+900+600")
    root.mainloop()


if __name__=="__main__":
    main()
