###################################################################
# File: camera_test but i don't have
# Date: 2020-07-29
###################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys

# For windows 10, install VideoCapture 
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#videocapture

# Open Terminal in VSCode and run the following command
# $  pip install VideoCapture 


scr_w, scr_h = 1280, 720
pygame.init()

class block() :
    def __init__(self,left,top,rw,rh) :
        self.left = left
        self.top = top
        self.rw = rw
        self.rh = rh
        self.rect = (self.left ,self.top ,self.rw ,self.rh)
    def draw(self) :
        pygame.draw.rect( surface, (0,255,0), self.rect,1)
        surface.blit( surface, self.rect, self.rect )

def cheak(pos,rect_list,img) :
    for r in rect_list :
        if int(r.left) <int(pos[0]) < int(r.left)+128 and int(r.top) <int(pos[1]) < int(r.top+90) :

            return r

        else : 
            pass


screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

rect_list = []
 # draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        square = block(i*rw, j*rh, rw, rh)
        rect_list.append(square)

img = None
is_running = True 
while is_running:

    for f in rect_list :
        f.draw()

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
        if e.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            op = cheak(pos,rect_list,img)
            if op == None :
                pass

            else :

                pygame.draw.rect( img, (0,255,0), op,1)
                surface.blit( img, op, op )
                screen.blit( surface, (0,0) )
                pygame.display.update()
                print("Hey",pos)
                
    # try to capture the next image from the camera 
    img = pygame.image.load("C:/Users/User/Desktop/cyka.jpg")
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h



    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()


print('Done....')
#print(rect_list)
###################################################################