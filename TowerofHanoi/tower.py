from tkinter import * #tkinter is a library used to build GUI in python
from PIL import Image,ImageTk #Python Imaging Library - 2 functions built in
import turtle #library to make objects using code
import pygame.mixer #to play sound in a window
import time #to prove delay of certain seconds ( for execute time proceesses)


W=''
W1=''
moves=0
pygame.mixer.init()
global sound #sound is a type of object in pygame sound library

def play():
     global moves
     pole_maxheight = 300  #sets max height of all 3 black towers
     ring_width_max = 150  #sets the max allowed breadth of the rectangle
     ring_delta_max = 30   #max diff b/w sizes of the all ring stacked else same rect for all
     ring_height = 20      #sets the height of the ring
     speed = 7            #speed of transferring
     
     A=[]#stack for first pole 
     B=[]#stack for first pole 
     C=[]#stack for first pole 
     T=[]#list of turtles object

     def play_sound():
          global sound
          sound = pygame.mixer.Sound("DRIVE.mp3")
          sound.play()
          
     def stop_sound():
          global sound
          sound.stop()

     #to draw 3 vertical poles
     def draw_line(x,y,angle,length,pensize,color): #x,y corrd, angle,how much move,font and color
         turtle.up()
         turtle.goto(x,y)
         turtle.seth(angle)
         turtle.down()
         turtle.color(color)
         turtle.pensize(pensize)
         turtle.fd(length) #forwrd move 
         
     def draw_scene():
         play_sound() 
         turtle.bgcolor('light blue') 
         draw_line(-600,-100,0,1200,15,'brown') #draw horizontal line 
         for i in range(-250,251,250):
             draw_line(i,-93,90,pole_maxheight,5,'black') #draw three poles above 
         turtle.up()
         turtle.goto(-220,270)
         turtle.down()
         turtle.write("Number of moves: 0",font=("Courier",30,"bold"))
         
         turtle.up()
         turtle.goto(0,-200)
         turtle.down()
         turtle.color("black")
         turtle.write("A: ",font=("Courier", 100, "bold"))
         turtle.update() 
      
        
     # it is used to draw first n rings on the first pole    
     def initialize():    
         global ring_width_max,ring_width_min,ring_ratio,ring_delta #control dimensions
         for i in range(n): #n is our number of rings
             A.append(i) # A is storing (for ex, 3 rings so A has [0,1,2] - index of the rings
             t = turtle.Turtle()
             t.hideturtle()
             t.speed(0)
             t.pencolor('red')
             t.fillcolor('light green')
             T.append(t)#our ring object is added one by one
         ring_delta = min(135/(n-1),ring_delta_max)
         #It controls the difference in width or height between rings.
         #It is set as the minimum value between 135/(n-1) and ring_delta_max

     # it will draw the single ring(rectangle) on the needed pole - 1 2 or 3     
     def draw_single_ring(r, x, k, extra=0):
         #r is the size of the ring
         #x-cord of pole on whch ring is placed , k is pos of ring
         #extra for animation purposes - vertically adjust the position of the ring.
         global ring_delta
         w = ring_width_max - ring_delta*(r-1)#represents the width of the ring
         T[r].up() #access the rin object in the T stack
         T[r].goto(x-w/2,-95+ring_height*k + extra)
         T[r].down()
         T[r].seth(0)
         T[r].begin_fill()
         for i in range(2):
             T[r].fd(w)
             T[r].left(90)
             T[r].fd(ring_height)
             T[r].left(90)
         T[r].end_fill()

     #access the all 3 stack(3 towers) using indices so that they can be moved in algo
     def draw_rings():
         for i in range(len(A)): #take indexes of ring and give to above function
             draw_single_ring(A[i],-250,i)
         for i in range(len(B)):
             draw_single_ring(B[i],0,i)
         for i in range(len(C)):
             draw_single_ring(C[i],250,i)
         
     def move_ring(PP,QQ):#PP is source pole and QQ is destination Pole
         global moves
         moves+=1
         if PP == "A": #identify in algo like if source is A then move A to etc
             x = -250 #next pole coord to move
             P = A
         elif PP == "B":
             x = 0
             P = B
         else:
             x = 250
             P = C
         if QQ =="A":
             x2 = -250
             Q = A
         elif QQ == "B":
             x2 = 0
             Q = B
         else:
             x2 = 250
             Q = C
         print("Pop {} Push {}".format(PP,QQ))    
         turtle.clear() 
         draw_line(-600,-100,0,1200,15,'brown')
         for i in range(-250,251,250):
             draw_line(i,-93,90,pole_maxheight,5,'black')
         turtle.update()  
         turtle.up()
         turtle.goto(-220, 270)
         turtle.down()
         turtle.write("Number of moves: {}".format(moves), font=("Courier", 30, "bold"))
         for extra in range(1, 250 - (-95 + ring_height * (len(P) - 1)), speed): 
             T[P[len(P) - 1]].clear()
             #here P[len-1] represents topmost ring and get clear - means vanish
             draw_single_ring(P[len(P)-1], x, len(P), extra) #draw on that position 
             turtle.update()
         T[P[len(P)-1]].clear()
         draw_single_ring(P[len(P)-1],x,len(P)-1,extra)
         turtle.update()
         tp = x #tp stores coord of source pole 
         if x2 > x: #if x corrd(destina) > x(source)
             step = speed #forward move
         else:
             step = -speed #backward move

         #responsible for animating the movement of the ring horizontally.    
         for tp in range(x,x2,step):
             T[P[len(P)-1]].clear()
             draw_single_ring(P[len(P)-1],tp,len(P)-1,extra)
             turtle.update() #traces the above horizontal path
             
         T[P[len(P)-1]].clear() #clears image of topmost ring in source pole
         draw_single_ring(P[len(P)-1],x2,len(P)-1,extra)
         turtle.update()
         Q.append(P[len(P)-1]) #the ring lets say delete from first move to now second one
         P.pop() #source pole ring removed
         

         #this for vertically animation
         for extra in range(250-(-95+ring_height*(len(Q)-1)),0,-speed):
             T[Q[len(Q)-1]].clear()
             draw_single_ring(Q[len(Q)-1],x2,len(Q)-1,extra)
             turtle.update()
             
         T[Q[len(Q)-1]].clear() #clears image of topmost ring in final pole
         draw_single_ring(Q[len(Q)-1],x2,len(Q)-1,extra)
         for i in range(-250, 251, 250):
             draw_line(i, -93, 90, pole_maxheight, 5, 'black') 
         turtle.update()   
         return

     #move rings in X to Z
     #recursive alogorithm
     def tower_of_hanoi(X,Y,Z,n):
         if n == 1:
             move_ring(X,Z) #if only 1 ring then move from X to Z 
             return
         tower_of_hanoi(X,Z,Y,n-1)
         #moving n-1 rings from the source pole X to the auxiliary pole Y,
         #using the destination pole Z as the (intermediate pole.)
         move_ring(X,Z)
         tower_of_hanoi(Y,X,Z,n-1)
         #n-1 rings from the auxiliary pole Y to the destination pole Z,
         #using the source pole X as the intermediate pole
         
     W.destroy() 
     n = int(turtle.numinput('Number of Rings','Please enter number of rings:',3,2,15)) #upto 15 done
     turtle.setup(700,700)
     turtle.hideturtle()
     turtle.title("Tower of Hanoi")
     turtle.speed(0)
     turtle.tracer(0,0)    
     draw_scene()
     turtle.update()
     
     initialize()
     draw_rings()
     print("\n")
     print("STACK STATUS IN TOWER OF HANOI.......")
     print("\n")
     tower_of_hanoi("A","B","C",n)
     turtle.update()
     turtle.up()
     turtle.goto(-10,-220)
     turtle.down()
     turtle.color("red")
     turtle.write("Tower of Hanoi Solved",align="center",font=("Courier",30,"bold"))
     time.sleep(3)
     turtle.bye()
     stop_sound()
     GUI()

def instruct():
     W.destroy()
     def console():
          W1.destroy()
          GUI()
     global W1
     W1=Tk()
     W1.geometry("650x420")
     W1.configure(bg="orange")
     W1.title("READ INSTRUCTIONS")
     L1=Label(W1,text=" GAME  INSTRUCTIONS",bg="yellow",font=("TIMES NEW ROMAN",27,"bold"))
     L1.pack(fill=BOTH,padx=0,pady=0)

     L2=Label(W1,text=" HOW  TO  PLAY ? ",bg="yellow",font=("TIMES NEW ROMAN",27,"bold"))
     L2.place(x=0,y=50)
     L2.pack(fill=BOTH)
     
     L3=Label(W1,text=" 1) Only one disk can be moved at a time. ",bg="green",font=("TIMES NEW ROMAN",17,"bold"))
     L3.pack(fill=BOTH)
     L3.place(x=0,y=120)
     
     L4=Label(W1,text=" 2) A disk can only be moved if it is the uppermost disk on a stack.",bg="green",font=("TIMES NEW ROMAN",17,"bold"))
     L4.pack(fill=BOTH)
     L4.place(x=0,y=180)
     
     L5=Label(W1,text=" 3) No larger disk may be placed on top of a smaller disk. ",bg="green",font=("TIMES NEW ROMAN",17,"bold"))
     L5.pack(fill=BOTH)
     L5.place(x=0,y=240)

     L5=Label(W1,text=" 4) You have to transfer the stack of rings to the third tower. ",bg="green",font=("TIMES NEW ROMAN",17,"bold"))
     L5.pack(fill=BOTH)
     L5.place(x=0,y=300)

     B1=Button(W1,text="RETURN TO HOME SCREEN",bg="light blue",command=console,fg="red",font=("Arial",12,"bold")).place(x=145,y=360)

def GUI():
    global W
    W=Tk() #creates a window stored in W
    W.geometry("840x540")
    W.configure(bg="#9A32CD")
    W.title("TOWER OF HANOI SIMULATOR")
    image=Image.open("stick.png") #open func to take image 
    R=image.resize((400,400))     #crop and it is pixels
    R1=ImageTk.PhotoImage(R)      #type of image that can be displayed in a Tkinter window.
    Lb=Label(W,image=R1)          #box where image is to be displayed on window
    Lb.place(x=20,y=100)
    L1=Label(W,text="TOWER  OF  HANOI  SIMULATOR",bg="yellow",font=("TIMES NEW ROMAN",27,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0) #label so pad , and to start and end filled completely.fill both means take both xy

    F=Frame(height=400,bg="#E066FF",width=350)
    F.place(x=460,y=100)

    B1=Button(F,text="START",relief=SUNKEN,bg="#E0FFFF",fg="black",command=play,font=("TIMES NEW ROMAN",26,"bold")).place(x=105,y=155)
    B2=Button(F,text="INSTRUCTIONS",relief=GROOVE,bg="#E0FFFF",command=instruct,fg="black",font=("TIMES NEW ROMAN",28,"bold")).place(x=15,y=40)
    B3=Button(F,text=" EXIT",relief=GROOVE,bg="#E0FFFF",command=W.destroy,fg="black",font=("TIMES NEW ROMAN",28,"bold")).place(x=115,y=265)
    W.mainloop() #interactions in a timely and efficient manner.
     #relief is txt on button how to display - raised , flat,etc.

GUI()
