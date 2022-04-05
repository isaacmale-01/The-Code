from tkinter import *
import tkinter
import os
import sys
from PIL import Image, ImageTk


class Window(Frame):

    
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()


    def init_window(self):

        self.master.title("The Sound of The Students")       
        self.pack(fill=BOTH, expand=1)

        
        menu = Menu(self.master)
        self.master.config(menu=menu)        
        file = Menu(menu)      
        file.add_command(label="Exit", command=self.client_exit)        
        menu.add_cascade(label="File", menu=file)        
        edit = Menu(menu)     

        file.add_command(label="Show Img", command=self.showImg)
        file.add_command(label="Show Text", command=self.showText)


        edit.add_command(label="Undo")       
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        logo = Image.open("projectlogoupdate3.jpg")
        #img = ImageTk.PhotoImage(image)
        image = logo.resize((550,70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)        

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=130, y=100)


    def showText(self):
        text = Label(self, text="Hey! Welcome to Isaac Male's Third Year Project!", font=("Helvetica", 25), bg= 'purple', foreground= 'green')
        text.pack()

        def run():
            os.system('main.py')


        startButton = Button(self, text="Let's Get Started!",command=run)        
        startButton.place(x=350, y=250)
        quitButton = Button(self, text="Quit", command=self.client_exit)        
        quitButton.place(x=380, y=300)
        

        self.configure(bg='purple')

    

    def client_exit(self):
        exit()


root = Tk()

root.geometry("800x600")

app = Window(root)   

root.mainloop()

#TODO - How can we make the text appear instead of it coming up through the menu?
#TODO - Make the labels bigger?
#TODO - Add event so that the start button runs the new code
#TODO - Fiddle with the other code such that visualisations are created for the user and the data is appended to a newer, bigger .csv file

#You've got this! Come on! :D