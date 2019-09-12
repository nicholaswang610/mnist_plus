# mnist_plus
My journey to "personalize" the MNIST dataset in a way.  The MNIST dataset is almost a rite of passage for novices delving into AI, and I wanted to put my basic knowledge to the test.  I created an application through which you can draw a number that can be guessed in real time.  However, I did come across many flaws... in fact, the neural network seems to recognize certain numbers (2, 3, and 4) really well, while consistently failing at recognizing others (it strangely likes to guess 6).  Below is a rundown of my process.

# training the network
To train my network, I utilized the tools supplied by tensorflow to easily whip up a decently working model with MNIST data.  I trained the network for about 20 minutes and yielded a decent 73% accuracy.  

Now, this is also most likely the main reason why my final product is not that accurate.  I should've avoided the MNIST data when training, instead creating my own mock-MNIST data with my drawing app.  However, I did not for three reasons.

1. I did not want to save that many images on my computer (the MNIST dataset has 60,000 images!)

2. I wanted to test my image processing skills by creating a "clone" of the MNIST data.

3. Curiosity!  How would the NN fare against my own inputs?  Inputs that would most definitely be at least slightly different from MNIST.

# the drawing app
I created the drawing application using the Tkinter library from python.  Pretty boring stuff.  There's tons of tutorials online on how to work with Tkinter.

# creating test data, processing images, the juicy part
I used Pillow.  This is where I faced the greatest hurdle.  There were my obstacles:

<b> CAPTURING THE DRAWING </b
This was an absolute pain that could've been avoided if I actually knew what I was doing with Tkinter inside and out.  When designing the drawing app, my widgets appeared in the right place, but I was definitely inputting the wrong pixel coordinates when using Pillow's Image.grab() method to screenshot a 500x500 pixel box of the canvas.  Knowing the nature of neural networks, I needed my screenshot to be pixel-perfect since NNs are very particular about the dimensions of the input data they receive.  This was especially so since I trained my NN on different data than what I was feeding.  Eventually, some toying around resulted in what I wanted (a miracle!).

<b> RESIZING THE IMAGE </b>
Luckily, Pillow has a resize method to handle this.  Then I converted the image into a numpy array matching the dimensionality of MNIST(28x28 pixels).

<b> GREYSCALING/B&W QUALITY </b>
Not too bad.  First, I found out I had to greyscale the image data since by default it's captured in RGB values (I needed 1 value per pixel since that's how the MNIST data is).  Then, I just iterated throught the numpy array and changed the values of what was drawn to 255 (white) and everything else 0 (black background).  I found that the right threshold was 10 - anything above was cranked up, anything below was just black background.

<b> PLUG INTO THE NN AND PRAY </b>
Fingers crossed.



# it worked... kinda
The program could guess the numbers 2, 3, and 4 very well.  However, not once did it recognize a 1, 7, or 9 and had confusion between 5, 6, and 8.  It loved to guess the number 6.  My suspicion is that this happened due to the miniscule pixel differences between my numbers and MNIST data.  5, 6, and 8 all have a lot weight in pixel values at the middle.  Likely, the NN interpreted a bunch of pixels going through the middle as 6.  2, 3, and 4 however are very distinguishable.  

# lessons learned
I learned a ton about manipulating image data, and the limitations of my neural network!  I recognized clear patterns in what my NN was doing and the numbers it was guessing.  Also, I did plan my method of attack a bit, but probably could've used more pre-planning as to what I needed to do.

<b> in the future... </b>
Perhaps I'll use actual data from my drawing app (instead of MNIST) to train a NN and see how things go.  
Also, maybe centering the images around the center of mass of the pixels would've made my data more resemblant of MNIST data (they mention using this method to create their dataset).  However, after the miracle of figuring out how to screenshot my drawing canvas, I didn't want to touch image-grabbing again and ruin it all.

Thanks for reading if you went through all of this!
Nicholas Wang
