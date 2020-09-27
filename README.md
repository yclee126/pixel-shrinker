# pixel-shrinker
Shrinks a pixel art image to original size using FFT analysis

usage: python input.png output.png

It finds the most dominant edge frequency and resizes the image to the frequency.

At the moment this only works well with non-cropped images.
To get the best result align the large pixels to image canvas, leaving no chopped pixels in the image.
