from PIL import ImageGrab
import time
import autopy


# Globals

x_pad = 518
y_pad = 103

def hitTheRightKey():

    if getPixelValuesOfGame(Cord.target_bloc_a) == (17,17,17,255):
        pressAButton()
    elif getPixelValuesOfGame(Cord.target_bloc_b) == (17,17,17,255):
        pressSButton()
    elif getPixelValuesOfGame(Cord.target_bloc_c) == (17,17,17,255):
        pressDButton()
    elif getPixelValuesOfGame(Cord.target_bloc_d) == (17,17,17,255):
        pressFButton()
    else:
        print getPixelValuesOfGame(Cord.target_bloc_a) 
        print getPixelValuesOfGame(Cord.target_bloc_b) 
        print getPixelValuesOfGame(Cord.target_bloc_c) 
        print getPixelValuesOfGame(Cord.target_bloc_d)

def getPixelValuesOfGame(x):
    box = (x_pad+x[0], y_pad+x[1], x_pad+x[0]+1, y_pad+x[1]+1)
    im = ImageGrab.grab(box)
    return im.getpixel((0,0))

def mouseclick(posx,posy):
    autopy.mouse.move( posx,posy)
    time.sleep(.1)
    autopy.mouse.click()
    time.sleep(.1)

def pressAButton():
    autopy.key.type_string('a')
    time.sleep(.1)

def pressSButton():
    autopy.key.type_string('s')
    time.sleep(.1)

def pressDButton():
    autopy.key.type_string('d')
    time.sleep(.1)

def pressFButton():
    autopy.key.type_string('f')
    time.sleep(.1)

def pressDownButton():    
    autopy.key.tap(long(autopy.key.K_DOWN))
    time.sleep(.1)

class Cord:
    
    classic_menu = (x_pad+1,y_pad+1)
    arcade_menu = (x_pad+201,y_pad+1)
    zen_menu = (x_pad+1,y_pad+201)
    rush_menu = (x_pad+201,y_pad+201)
    relay_menu = (x_pad+1, y_pad+401)
    mode_menu = (x_pad+201,y_pad+401)

    target_bloc_a = (5, 305)
    target_bloc_b = (105, 305)
    target_bloc_c = (205, 305)
    target_bloc_d = (305, 305)
 
def main():

    mouseclick( Cord.classic_menu[0],Cord.classic_menu[1]+100)

    pressDownButton()
    pressDownButton()
    pressDownButton()
    pressDownButton()

    mouseclick( Cord.classic_menu[0],Cord.classic_menu[1])
    mouseclick( Cord.classic_menu[0],Cord.classic_menu[1])

    while getPixelValuesOfGame((1,550)) != (0, 226, 108, 255):
        hitTheRightKey()

 
if __name__ == '__main__':
    main()

