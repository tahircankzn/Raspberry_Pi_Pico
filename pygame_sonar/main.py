import serial 
import time 
import pygame

ser = serial.Serial('COM4', 9600)
time.sleep(2) 

def send():
    

    

    data = ser.readline() # bytes nesnesi
    text = data.decode("utf-8") # string nesnesi  ISO-8859-9   "utf-8"
    return text # metni yazdır



pygame.display.set_caption("Sonar")
pygame.init()
screen = pygame.display.set_mode((640, 480))

screen.fill((0, 0, 0)) 
line_x = [*range(-17,18,1)]
class line():
    def __init__(self,a):
        self.a = a
    
    def draw_hist(self):
        
        try:
            x = line_x[self.a]    
            y = -1*(x**2)+320
            #print(480-y)
            
            pygame.draw.line(screen,color = (50,0,0),start_pos=(320,470),end_pos=(320+x*18,480-y),width=5)
        except:
            pass
        

line_hold = []
line_hold_counter = 0
line_delete = 0

def draw(a):
    colors = [(0, 120, 0),(0, 0, 0)]
    radius = [*range(320,0,-5)]
    for i in radius:
        if radius.index(i)%2 == 0:
            color = colors[0]
        else:
            color = colors[1]
        pygame.draw.circle(screen, color=color, center = (320, 480), radius = i) 
        
    #line_x = [*range(-320,321,1)]
    for i in line_hold:
        i.draw_hist()

    #for x in line_x:
    try:
        x = line_x[a]    
        y = -1*(x**2)+320
        #print(480-y)
        
        pygame.draw.line(screen,color = (255,0,0),start_pos=(320,470),end_pos=(320+x*18,480-y),width=5)
    except:
        pass


    #pygame.draw.line(screen,color = (0,0,255),start_pos=(320,470),end_pos=(320+320,480-0),width=5)
    #pygame.draw.line(screen,color = (0,0,255),start_pos=(320,470),end_pos=(320,480-320),width=5)
    
    #pygame.draw.line(screen,color = (0,0,255),start_pos=(10,10),end_pos=(50,50),width=10)
    pygame.display.update()

clock = pygame.time.Clock()
running = True
a = 0
key = 0
hold_time = None
while running:
    clock.tick(120)
    data = int(send())
    if data >=100:
        data -=100
        line_hold.append(line(data))
    draw(data)
    
    if hold_time == None:
        hold_time = time.time()
    elif hold_time + 1 < time.time():
        line_hold = []
        hold_time = None

    # Test  ###########################
    """if a == 5 or a == -5 or a == 6 or a == 15:
        line_hold.append(line(a))"""
    ###################################


    """if key == 0:
        a+=1
        if a == 36:
            key = 1
        
    elif key == 1:
        a-=1
        if a == 0:
            key = 0"""

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                
                running = False


pygame.quit()
