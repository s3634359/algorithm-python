from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (255, 255, 0) #Yellow
r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) # Black

colours = [y, r, g, b]
faces = []

for i in colours:
    faces.append([
    i, i, i, i, i, i, i, i, 
    i, i, i, i, i, i, i, i, 
    i, k, k, i, i, k, k, i,
    i, k, k, i, i, k, k, i,
    i, i, i, i, i, i, i, i, 
    i, k, k, i, i, k, k, i,
    i, i, i, k, k, i, i, i,
    i, i, i, i, i, i, i, i
    ])

a = 0
while a < 5:
    sense.set_pixels(faces[a])
    sleep(3)
    a += 1