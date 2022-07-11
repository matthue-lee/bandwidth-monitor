from email import message
import time
from tkinter import messagebox
import tkinter
import psutil
import atexit
import sys
import csv 
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


###### THIS ISN'T NEEDED IF CODE IS RUNNING ONCE A DAY SINCE BYTES_RECV RESETS ON SHUTDOWN. 
# f1 = open("data.csv", "r", encoding="utf-8-sig", errors="ignore")
# final_line = f1.readlines()[-2].strip().split(',')
# f1.close()

# print(final_line)
# last_received = float(final_line[0])
# last_sent = float(final_line[1])
# last_total = float(final_line[2])



day = datetime.today().weekday()
if day == 2:
    #bytes recv measure bytes recieved since pc has been turned on. Thus code need to run at shutdown. 
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent


    mb_new_rec = bytes_received/1024/1024
    mb_new_sent = bytes_sent/1024/1024
    mb_new_total = (bytes_sent+bytes_received)/1024/1024



    all_dat = [mb_new_rec, mb_new_sent, mb_new_total, datetime.today().weekday()]

    f = open('data.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(all_dat)
    f.close


    
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    tkinter.messagebox.showinfo("Data Usage", f"MB Received: {mb_new_rec:.2f}, MB Sent: {mb_new_sent:.2f}, MB Total: {mb_new_total:.2f}")


def exit_handler():
    #bytes recv measure bytes recieved since pc has been turned on. Thus code need to run at shutdown. 
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    mb_new_rec = bytes_received/1024/1024
    mb_new_sent = bytes_sent/1024/1024
    mb_new_total = (bytes_sent+bytes_received)/1024/1024

    all_dat = [mb_new_rec, mb_new_sent, mb_new_total, datetime.today().weekday()]

    f = open('data.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(all_dat)
    f.close

atexit.register(exit_handler)

# Set to run on startup each day, on sunday it will show statistics
# as a graph of usage by day for the last week. This means each day it will log the day, so the corressponding 
# data has been from the previous days usage. On sunday the summary will include data from 6 (sunday) down to 
# (inclusive) of the lowest number above 1. (since 1 refers to tuesday, which would contain the data from monday)



