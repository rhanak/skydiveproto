from pygame import *
font.init()
from scoredisplayer import ScoreDisplayer

scr = display.set_mode((600,300))

format_ = "0000.00"
myfont = font.Font(font.match_font('arial'),12)
color = 'red'

sd = ScoreDisplayer(format_, myfont, color) 
sd.center = 150,250 

time.set_timer(USEREVENT,20)

score = 0
while 1:
    ev = event.wait()

    if ev.type == USEREVENT:    
    	scr.fill(0,sd)          
    	scr.blit(sd.image,sd)   
    	display.update(sd)

    if ev.type == KEYDOWN:

        if ev.key == K_UP:      
            score += 183.73
            sd.set(score,200)  

        elif ev.key == K_ESCAPE:
            score = 0
            sd.set(score)

    elif ev.type == QUIT: break
