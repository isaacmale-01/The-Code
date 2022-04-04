from tkinter import *
import tkinter
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
        load = Image.open("projectlogoupdate2.jpg")
        resize_image = load.resize((300,300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=40, y=100)

    def showText(self):
        text = Label(self, text="Hey! Welcome to Isaac Male's Third Year Project!")
        text.pack()


        startButton = Button(self, text="Let's Get Started!")        
        startButton.place(x=340, y=350)
        quitButton = Button(self, text="Quit", command=self.client_exit)        
        quitButton.place(x=370, y=400)

        self.configure(bg='purple')

    def client_exit(self):
        exit()


root = Tk()

root.geometry("800x600")

app = Window(root)   

root.mainloop()

#TODO - Work some more on the photo - how and why does the image appear like that?
#TODO - How can we make the text appear instead of it coming up through the menu?
#TODO - Make the labels bigger?
#TODO - Add event so that the start button runs the new code
#TODO - Fiddle with the other code such that visualisations are created for the user and the data is appended to a newer, bigger .csv file

#You've got this! Come on! :D