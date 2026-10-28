import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 600

satellites = []
number_of_satellite = 8
next_satellite = 0

lines = []

start_time = 0
total_time = 0
end_time = 0

def c_sate():
    global start_time
    for i in range(number_of_satellite):
        satelite = Actor("thingy")
        satelite.pos = (random.randint(50,750),random.randint(50,550))
        satellites.append(satelite)
    start_time = time.time()    
def draw():
    global total_time
    screen.blit("bg",(0,0))
    number = 1
    
    for satelite in satellites:
        satelite.draw()
        screen.draw.text(str(number), (satelite.pos[0],satelite.pos[1]+20))
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    if next_satellite < number_of_satellite:
        total_time = time.time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)

    if next_satellite == number_of_satellite:
         screen.draw.text("You won...Do your homework lol",(175,300),fontsize=50)

def update():
    pass

def on_mouse_down(pos):
    global next_satellite
    global lines
    if next_satellite < number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite = next_satellite + 1
        else:
            lines = []
            next_satellite = 0    

   






























c_sate()
pgzrun.go()
