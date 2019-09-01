from tkinter import *
import PIL

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
        self.introframe.pack()
        self.introduction = Label(self.introframe, text="Write a number, I'll guess it.", font="halvetica")
        self.introduction.pack(pady=10)

    def make_guess_space(self):
        self.guessframe = Frame(self.root)
        self.guessframe.pack()
        self.result = None
        self.guess = Label(self.guessframe, text = "Hmmm... ",font = "halvetica")
        self.guess.pack(pady = 10)
    
    def make_button(self):
        self.buttonframe = Frame(self.root)
        self.buttonframe.pack()
        self.button = Button(self.buttonframe, text="Guess!", font = "halvetica", width=10, command = self.callback)
        self.button.pack(pady = 10, side = LEFT)

    def make_clear(self):
        self.clear = Button(self.buttonframe, text = "Clear", font="halvetica", width = 10, command = self.clear_canvas)
        self.clear.pack(padx = 10, side = RIGHT)
    def make_canvas(self):
        self.canvas = Canvas(self.root, bg="white", width=500, height=500)
        self.canvas.pack()

    #paint on the canvas, binded to b1-motion
    def paint(self, event):
        if self.originx and self.originy:
            self.canvas.create_line(self.originx, self.originy, event.x, event.y, width=5, fill="black")
        self.originx, self.originy = event.x, event.y

    def reset(self, event):
        self.originx, self.originy = None, None
        
    def callback(self):
        self.result = 5
        self.guess.config(text="Hmmm... it's " + str(self.result) + "!")
        #implement the AI here, make the guess, feed it back as a string(self.result) to display
        #canvas is roughly 625x625, beginning at pixel y position 200

    def clear_canvas(self):
        self.canvas.delete("all")
        self.guess.config(text="Hmmm... ")

if __name__=="__main__":
    DrawingApp()