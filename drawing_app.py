from tkinter import *
from PIL import ImageGrab, Image
import numpy

class DrawingApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("MNIST+")
        self.root.resizable(0,0)
        self.root.geometry("500x700")
        self.originx, self.originy = None, None
        self.root.bind("<B1-Motion>", self.paint)
        self.root.bind("<ButtonRelease-1>", self.reset)
        self.make_intro()
        self.make_guess_space()
        self.make_button()
        self.make_clear()
        self.make_canvas()
        self.root.mainloop()
    
    #GUI elements
    def make_intro(self):
        self.introframe = Frame(self.root)
        self.introframe.grid(row = 0)
        self.introduction = Label(self.introframe, text="Write a number, I'll guess it.", font="halvetica")
        self.introduction.grid(row = 0)

    def make_guess_space(self):
        self.guessframe = Frame(self.root)
        self.guessframe.grid(row = 1)
        self.result = None
        self.guess = Label(self.guessframe, text = "Hmmm... ",font = "halvetica")
        self.guess.grid(row = 1)
    
    def make_button(self):
        self.buttonframe = Frame(self.root)
        self.buttonframe.grid(row = 2)
        self.button = Button(self.buttonframe, text="Guess!", font = "halvetica", width=10, command = self.callback)
        self.button.grid(row = 2, column = 0)

    def make_clear(self):
        self.clear = Button(self.buttonframe, text = "Clear", font="halvetica", width = 10, command = self.clear_canvas)
        self.clear.grid(row = 2, column = 1)

    def make_canvas(self):
        self.canvas = Canvas(self.root, bg="white", width=500, height=500)
        self.canvas.grid(pady = 20,row = 3)
        self.canvas.update()

    #paint on the canvas, binded to b1-motion
    def paint(self, event):
        if self.originx and self.originy:
            self.canvas.create_line(self.originx, self.originy, event.x, event.y, width=5, fill="black")
        self.originx, self.originy = event.x, event.y

    def reset(self, event):
        self.originx, self.originy = None, None
        
    def callback(self):
        self.result = 5
        left = self.canvas.winfo_rootx() + self.canvas.winfo_x()
        upper = self.canvas.winfo_rooty()
        right = left + 500
        lower = upper + 500
        print("left", left)
        print("upper", upper)
        print("right", right)
        print("lower", lower)
        print("canvas width:", self.canvas.winfo_width())
        print("canvas height:", self.canvas.winfo_height())
        image = ImageGrab.grab(bbox = (left, upper, right, lower))
        self.guess.config(text="Hmmm... it's " + str(self.result) + "!")
    
        #try screenshotting with pilow first, and then having a "ghost" drawing in the background if that doesnt work.
        #rootx/y means dist from upper left corner
        #canvx/y means dist from the upper left window corner
        #implement the AI here, make the guess, feed it back as a string(self.result) to display

    def clear_canvas(self):
        self.canvas.delete("all")
        self.guess.config(text="Hmmm... ")

if __name__=="__main__":
    DrawingApp()
