from tkinter import *
import tkinter


window = Tk()
window.title("The Sound of The Students")
window.geometry("800x600+10+30")
window.configure(background="purple")
samplewelcometext = "Welcome to Isaac Male's Third Year Project!"


lbl=Label(window, text=samplewelcometext, fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('Hello Python')
window.geometry("300x200+10+10")



btn=Button(window, text="Let's Get Started!", fg='blue')
btn.place(x=350, y=200)
window.title('Hello Python')

#insert image in this section - I tried but you can't get the exact file structure to work here?!

window.mainloop()