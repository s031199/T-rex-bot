from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (479,371)
    dinosaur = (248,380)
    # x = 3160 (cordinate to check for tree)
    # y = 390 (cordinate of half tree

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    #print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinosaur[0] + 74, Cordinates.dinosaur[1], Cordinates.dinosaur[0] + 80, Cordinates.dinosaur[1]+25)
    image = ImageGrab.grab(box)
    #image.show()
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(a)
    #if (a.sum() != 1980):
    #    print(a.sum())
    print(a.sum())
    return (a.sum())

def main():
    restartGame()
    while True:
        if(imageGrab()!=397):
            pressSpace()
            time.sleep(0.1)

main()




