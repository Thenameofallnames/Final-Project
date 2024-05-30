import pygame
import random
import cv2
import json
import MainLoop
import time
import datetime
import pysound
import math
from time import sleep
from multiprocessing import Process
with open('save.json', 'r') as in_file:
    savedat = json.load(in_file)
freddypath = ["1a", "1b", "2a", "2b"]
bonnipath = ["1a", "1b", "2a", "2b"]
chicapath = ["1a", "1b", "7", "4a", "4b"]
Won = False
night = "N1"
def mainMenu():
    global Won
    global Night
    print("Temp")
    print("")
    if night == 0:
        print("(1) Start")
    else:
        print("(1) Continue")
    print("(2) Options")
    print("(3) Credits")
    if Won:
        print("(4) Custom Night")
    selection = input("")
    if selection == "1":
        game()
    elif selection == "1987":
        print("Dev mode enabled")
        Won = True
        return
    else:
        print("Invalid Selection")
        return
def game():
    cap = cv2.VideoCapture('video.mp4')
    running, img = cap.read()
    shape = img.shape[1::-1]
    wn = pygame.display.set_mode(shape)
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        try:
            wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
            pygame.display.update() 
        except AttributeError:
            screen = create_screen()
            background = load_background_image()
            screen.blit(background, (0, 0))
            background = pygame.image.load('Office.bmp').convert()
            pressed = pygame.key.getpressed()
                
            
        
    pygame.quit()

def movement(target):
    global floc
    global cloc
    global bloc
    if target == "freddy":
        if freddypath[floc] == "2b":
            door("freddy")
        else:
            floc = floc + 1
        
    if target == "chica":
        if freddypath[cloc] == "4b":
            door("chica")
        else:
            cloc = cloc + 1

    if target == "bonnie":
        if freddypath[bloc] == "2b":
            door("bonnie")
        else:
            floc = floc + 1
def bots_loop():
    global night
    floc = 1
    cloc = 1
    bloc = 1
    fdif = int(savedat["Animatronics"][0][night]["freddy"])
    cdif = int(savedat["Animatronics"][0][night]["chica"])
    bdif = int(savedat["Animatronics"][0][night]["bonnie"])
    foxdif = int(savedat["Animatronics"][0][night]["foxy"])
    hour = 0
    time = 90
    ftime = 0
    ctime = 0
    btime = 0
    while hour < 6:
        while time > 0:
            if ftime == 3:
                if random.randint(0,100) < fdif*15:
                    movement("freddy")
                ftime = 0
            if ctime == 5:
                if random.randint(0,100) < cdif*15:
                    movement("chica")
                ctime = 0
            if btime == 5:
                if random.randint(0,100) < bdif*15:
                    movement("bonnie")
                btime = 0
            sleep(1)
            time = time - 1
            ftime = ftime + 1
            ctime = ctime + 1
            btime = btime + 1
        hour = hour + 1
        time = 90     
            
             
mainMenu()

