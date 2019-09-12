from tkinter import *
from PIL import ImageGrab, Image
import numpy as np
import pickle

class DrawingApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("MNIST+")
        self.root.resizable(0,0)
        self.root.geometry("500x700")
        self.root.grid_columnconfigure((0,1,2), weight = 1)
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
        self.canvas = Canvas(self.root, bg="black", width=500, height=500)
        self.canvas.grid(pady = 20,row = 3, sticky = "ew")
        self.canvas.update()

    #paint on the canvas, binded to b1-motion
    def paint(self, event):
        if self.originx and self.originy:
            self.canvas.create_line(self.originx, self.originy, event.x, event.y, width=10, fill="white")
        self.originx, self.originy = event.x, event.y

    def reset(self, event):
        self.originx, self.originy = None, None
        
    def callback(self):
        left = self.canvas.winfo_rootx() + self.canvas.winfo_x()+5
        upper = self.canvas.winfo_rooty() + 5
        right = left + 490
        lower = upper + 490
        self.image = ImageGrab.grab(bbox = (left, upper, right, lower))
        #resize image and convert to np.array (28,28) and then binarize the pixel values
        self.resize_image(self.image)
        self.neural_net()
        self.guess.config(text="Hmmm... it's " + str(self.answer) + "!")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.guess.config(text="Hmmm... ")
    
    def resize_image(self, image):
        self.image = self.image.resize((28,28),Image.ANTIALIAS)
        self.image = self.image.convert("L")
        self.image_as_array = np.array(self.image)
        for i in range(len(self.image_as_array)):
            for j in range(len(self.image_as_array[0])):
                if self.image_as_array[i][j]>10:
                    self.image_as_array[i][j] = 255
                else: 
                    self.image_as_array[i][j]=0
        self.image = Image.fromarray(self.image_as_array)
        self.image.save("test.png", quality = 95)
        self.image = Image.open("test.png")
    def neural_net(self):
        pickled = open("best_model.pickle", "rb")
        model = pickle.load(pickled)
        self.image_as_array.resize(1,28,28)
        predictions = model.predict(self.image_as_array)
        self.answer = np.argmax(predictions)
if __name__=="__main__":
    DrawingApp()
