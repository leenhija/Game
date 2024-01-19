import pygame
import sys
import time
import random
import math
import os
import sys
from pygame.sprite import Sprite
import time
screen = pygame.display.set_mode((626, 626))
#the game settings
class Settings:
    screen_width = 887
    screen_height = 600
    bg_color = (230, 230, 230)
class Button:
    def __init__(self,text,width,height,pos,elevation):
        font = pygame.font.SysFont('Arial', 35)
        gui_font = pygame.font.Font(None, 30)
        self.pressed=False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        #top rectangle
        self.top_rect=pygame.Rect(pos,(width,height))
        self.top_color='(255, 255, 255)'
        #bottom rectangle
        self.bottom_rect=pygame.Rect(pos,(width,height))
        self.bottom_color='(255, 49, 49)'
        #Render the text for the button
        self.text_surf=gui_font.render(text,True,'#000000')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
    def draw(self):
        #Adjust the position and elevation of the button based on user interactions
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
        pygame.draw.rect(screen, (255, 49, 49), self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    #Check if the button is clicked by detecting mouse positions and mouse button presses.
    #Change the button's appearance and behavior based on whether it is clicked or not.
    #If clicked, run the game by calling the run_game() function from the run_game module.
    #Stop the sound effect playing in the background.
    #Update the state of the button's "pressed" attribute.
    #If not clicked, restore the button's appearance and behavior.
    def check_click(self):
        mouse_pos=pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    run_game()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '(255,255,255)'

#set the car position and car rect on the screen
class car(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.image=pygame.image.load("photos/car.png")
        self.rec=self.image.get_rect()
        self.screen_rec=self.screen.get_rect()
        self.rec.centerx=self.screen_rec.centerx
        self.rec.bottom=self.screen_rec.bottom
        self.moving_right=False
        self.moving_left=False
    def updat(self,screen):
        #moving the carbased on  moving left and right
        if self.moving_right and self.rec.right<(self.screen_rec.right):
            self.rec.centerx+=20
        elif self.moving_left and self.rec.left>(self.screen_rec.left):
            self.rec.centerx-=20

    #draw the car on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rec)
    def get_rect(self):
        #return the car rect
        return self.rec
# updat screen status iand moving the car left and right if the player presses the left and the right key on the keyboard
def check(Car):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                Car.moving_right=True
            elif event.key==pygame.K_LEFT:
                Car.moving_left=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                Car.moving_right=False
            elif event.key==pygame.K_LEFT:
                Car.moving_left=False
# Set the width and height of the game window
width=887
height=600
class enemy(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        # scale the image down so it's not wider than the lane
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        # Set the position of the sprite

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def get_rect(self):
        # Return the rectangle of the sprite
        return self.rect

pygame.init()
pygame.mixer.init()
s_w=226
s_h=626
#Setting the font for the game
font=pygame.font.SysFont('RACING HARD',140)
#diplay surface for the title
gd=pygame.display.set_mode((s_w, s_h))
#display message on screen function
def message_to_screen(msg,color):
    text=font.render(msg,True,color)
    gd.blit(text,[s_w/6,s_h/8])
def start_game():
    #create an instance of the Settings class, which contains the game settings.
    settings=Settings()
    #Creating the start screen with a width and height of 800 and 600
    start_screen = pygame.display.set_mode((800, 600))
    #load background iimage
    bg=pygame.image.load("photos/strat7.jpg")
    #display the background image on the screen
    start_screen.blit(bg,(0,0))
    #set the caption for the start screen as START
    pygame.display.set_caption("START")
    #load the icone for the start screen
    icon = pygame.image.load("photos/icon.png")
    #set the icone for the start screen
    pygame.display.set_icon(icon)
    #display the title
    message_to_screen("SPEED4SPEED",'#e4d00a')
    pygame.display.update()
    #Creating a start button: We create an instance of the Button class called button1 with the text "START",
    #width and height of 150 and 50 pixels, and position of (330, 460) pixels on the start screen.
    button1=Button('START',150,50,(330,460),5)
    #function to update the start screen display
    pygame.display.flip()
    #game running
    while True:
        #exit the game if the player quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Drawing the start button ont he screen
        button1.draw()
        #update the start screen display
        pygame.display.update()

from pygame.sprite import Sprite
pygame.init()
pygame.mixer.init()
#This Clock object is used to track time within the game loop and control the frame rate.
# It can be used to limit the execution speed of the game to a specific frame rate,
# which helps in making the game run smoothly and consistently on different hardware.
clock=pygame.time.Clock()
fbs=60
#image list of enemy cars to be displayed randomly while the game is running
img=['1.png','2.png','3.png','4.png']
#append images to the vehicles image list
v_img=[]
for i in img:
    image=pygame.image.load("photos/"+i)
    v_img.append(image)
enemy_group = pygame.sprite.Group()
#hearts images
heart=['hearts.png','hearts.png','hearts.png']
heart_group=[]
for i in heart:
    image=pygame.image.load("photos/"+i)
    heart_group.append(image)
#crash photo if the game is over
crash = pygame.image.load('photos/crash.png')
crash_rect = crash.get_rect()
def run_game():
       #game settings
        settings=Settings()
       #display the screen with width and height
        screen=pygame.display.set_mode((887,600))
       #set a background image
        bg=pygame.image.load("photos/road11.jpg").convert()
       #set screen caption
        pygame.display.set_caption("SPEED4SPEED")
       #change the screen icone
        icon=pygame.image.load("photos/icon.png")
        pygame.display.set_icon(icon)
       #sound effect
        pygame.mixer.pre_init(44100,-16,4,512)
        sound_file = os.path.join('sound effect', 'car_sound2.mp3')
        sound_effect = pygame.mixer.Sound(sound_file)
        sound_effect.set_volume(0.5)
       #car object from Car class
        Car=car(screen)
       # define game variables
        bg_height=bg.get_height()
        bg_rect=bg.get_rect()
        scroll=0
        play_speed=3
        score=0
        flage = False
        flage2=False
        tiles=math.ceil(screen.get_height()/bg_height)+1
        car2=pygame.image.load("photos/1.png")
        f=True
        obs_startx = random.randrange(100, 887 - 100)
        obs_starty =0
        gameover=False
        left_boundary = pygame.Rect(0, 0, 80, 600)
        right_boundary = pygame.Rect(887 - 80, 0, 80, 600)
        hearts_left = 3
        while True:
            #play the sound effect
            sound_effect.play()
            clock.tick(fbs)
            #scrolling background
            for i in range(0,tiles):
                screen.blit(bg,(0,(i*bg_height+scroll)*-1))
                bg_rect=(i*bg_height+scroll)*-1
            #draw he car on the bottom center of the screen
            Car.draw(screen)
            scroll-=5
            if abs(scroll)>bg_height:
                scroll=0
            # ensure there's enough gap between vehicles
            add_veh=True
            for i in enemy_group:
                if i.rect.top<i.rect.height*7.5:
                    add_veh=False
            if add_veh:
                # select a random lane
                lane=random.randrange(100, 887 - 100)
                # select a random vehicle image
                image=random.choice(v_img)
                vehicle=enemy(image,lane,screen.get_height()/-2)
                enemy_group.add(vehicle)
            # make the vehicles move
            for vv in enemy_group:
                vehicle.rect.y+=(play_speed)
                if vv.rect.top>=screen.get_height():
                    vv.kill()
                    # add to score
                    score+=1
                    # speed up the game after passing 5 vehicles
                    if score > 0 and score % 5 == 0:
                      play_speed+=1
            # draw the vehicles
            enemy_group.draw(screen)
            #set score rect and display it on the screen
            font = pygame.font.SysFont('RACING HARD', 23)
            text = font.render('Score: ' + str(score), True, '#1F75FE')
            text_rect = text.get_rect()
            rec=pygame.draw.rect(screen,'#B9D9EB',pygame.Rect(15,20,120,50),0,20)
            text_rect=text.get_rect(center=rec.center)
            screen.blit(text, text_rect)
            #quit button if you want to exit the game
            quit_button=Button('QUIT',60,50,(5,550),5)
            m_p=pygame.mouse.get_pos()
            quit_button.draw()
            if quit_button.top_rect.collidepoint(m_p):
               if pygame.mouse.get_pressed()[0]:
                sys.exit()
            car_rect=Car.get_rect()
            # if the score is 50 give the player an extra heart as a reward
            #check if there is a collision detection and the player will lose one heart every collision detection
            #the player will lose one heart when he tries to pass the left and right boundaries
            c=0
            for i in range(hearts_left):
                screen.blit(heart_group[i],pygame.Rect(700+c,10,50,50))
                c+=60
            if car_rect.colliderect(vehicle.rect):
                hearts_left-=1
                vehicle.kill()
                continue
            if Car.get_rect().left<(screen.get_rect().left+70):
                hearts_left-=1
                car_rect.centerx=screen.get_rect().centerx
            if Car.get_rect().right > (screen.get_rect().right - 70):
                hearts_left -= 1
                car_rect.centerx = screen.get_rect().centerx
            if hearts_left ==0:
                car_rect.centerx = screen.get_rect().centerx
                gameover = True

            if gameover:
                rec=pygame.draw.rect(screen, '#CA0123', (0, 200, 887, 220))
                car_rect.centerx = screen.get_rect().centerx
                crash_rect.center = [Car.get_rect().center[0], Car.get_rect().top]
                font = pygame.font.Font(pygame.font.get_default_font(), 30)
                text1 = font.render('Game over your score is '+str(score), True, '#000000')
                text_rect1 = text1.get_rect()
                text_rect1.center = rec.center
                text_rect1.y = rec.y + 70
                screen.blit(text1,text_rect1)
                crash_rect.center = [Car.get_rect().center[0], Car.get_rect().top]
                screen.blit(crash, crash_rect)
                enemy_group.empty()
                scroll=0
                sound_effect.stop()
                flage2=True
                pygame.display.flip()
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        gameover = False
                        score = 0
                        sys.exit()
            #When the game is over the window should sleep for 3 sec and return to the start window.
            if flage2:
                enemy_group.empty()
                scroll = 0
                gameover = False
                score = 0
                time.sleep(3)
                start_game()
            # if the players reach score 100 they won and display win screen
            if score>100:
                rec=pygame.draw.rect(screen, '#3FFF00', (0, 200, 887, 220))
                font = pygame.font.Font(pygame.font.get_default_font(), 30)
                text1 = font.render('You won your score is '+str(score), True, '#ffffff')
                text_rect1 = text1.get_rect()
                text_rect1.center = rec.center
                text_rect1.y = rec.y + 70
                screen.blit(text1,text_rect1)
                car_rect.centerx=screen.get_rect().centerx
                enemy_group.empty()
                scroll=0
                sound_effect.stop()

                flage2=True
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        gameover = False
                        score = 0
                        hearts_left=2
                        sys.exit()

            #check for the game status
            check(Car)
            Car.updat(screen)
            pygame.display.update()
            pygame.display.flip()
start_game()
