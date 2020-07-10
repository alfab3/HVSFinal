#Main File for High Voltage System
#Written by Albert Fabrizi
#Version 0.1
#Date: July 10, 2020

from Tkinter import *
import Tkinter as tk
import time
import random

mainWindow = Tk()

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()#main window and menu bar
        self.main_widgets()#objects that inhabit the main page

    def init_window(self):
        self.master.title('High Voltage System')

        #cascade menus
        menu = Menu(mainWindow)
        mainWindow.config(menu = menu)

        #file cascade menu
        file_C = Menu(menu)
        file_C.add_command(label='Exit', command = self.close_window)
        menu.add_cascade(label='File', menu=file_C)

    def main_widgets(self):
        Label(mainWindow, text = 'Enter Desired Voltage: ').grid(row = 0)
        
