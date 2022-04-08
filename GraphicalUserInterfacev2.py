from tkinter import *
import tkinter
from tkinter import messagebox
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
        credits = Menu(menu)     

        
        credits.add_command(label="By Isaac Male, for the Third Year Double Project 2022") 
        credits.add_command(label="Supervisor: Ed De Quincey")     
        credits.add_command(label="With Thanks To: Jason Hughes and Camilla Jones")     
        menu.add_cascade(label="Credits", menu=credits)

    
        logo = Image.open("projectlogoupdate3.jpg")
        #img = ImageTk.PhotoImage(image)
        image = logo.resize((550,70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)        

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=130, y=100)


   
        text = Label(self, text="Hey! Welcome to Isaac Male's Third Year Project!", font=("Helvetica", 25), bg= 'purple', foreground= 'green')
        text.pack()

        def run():
            messagebox.showinfo('What Happens Next','This program is firstly going to show you a graph of your top genres...')
            messagebox.showinfo('What Happens Next','...before showing you your top artists, but hold on - it may be different to what you are expecting!')
            messagebox.showinfo('What Happens After That','Once you have taken a look at the funky visuals, your top artists and genres will then be recorded anonymously and used as part of the wider project into what music Keele Students like.')
            messagebox.showinfo('And Finally','For now though, enjoy the visuals - and from me, Isaac Male - thank you very much for taking part in The Sound of The Students!')
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


#TODO - Turn the GUI into an EXE file (when the entire program is done!)

#You've got this! Come on! :D