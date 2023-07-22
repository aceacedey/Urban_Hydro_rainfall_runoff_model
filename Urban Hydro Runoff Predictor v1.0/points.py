#import pyautogui 
import os
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import csv
from openpyxl import Workbook


class dragworking():
    def __init__(self,fl, roo, frame,frames, tt):
        
        self.root=roo
        self.i=0
        self.a=[]
        self.b=[]
        self.cb=[]
        self.endCounter = 1
        self.t= tt
        self.fr=frame
        self.fc=frames
        self.ti=StringVar()
        self.curcor = StringVar()
        #self.ima, self.img_org, self.counter, self.width_org, self.height_org, self.x, y, z,ChangeDx,ChangeDy 
        self.counter = 1
        self.ChangeDx = 0
        self.ChangeDy=0
        self.cx=0
        self.cy=0
            ### Start Entries
        self.entry1=Entry(self.fr,textvariable=self.ti)
        self.entry1.grid(row=0, column=0,sticky='nswe')
        self.entry2=Entry(self.fr,textvariable=self.curcor)
        self.entry2.grid(row=0, column=1,sticky='nswe')

        self.ResetButton = Button(self.fr,text = "rb", command = self.reset)
        self.ResetButton.grid(row=1, columnspan=6,sticky='nswe')
        ### End Entries

        self.b2 = Button(self.fr, text="End", command=self.see)  # to start selecting points
        self.b2.grid(row=0, column=3,sticky='nswe')
        self.b1 = Button(self.fr, text="Start", command=self.can)  # button to end selecting points
        self.b1.grid(row=0, column=2,sticky='nswe')
        self.b1 = Button(self.fr, text="delete prev point", command=self.delete)  # button to end selecting points
        self.b1.grid(row=0, column=4,sticky='nswe')

        ### Start Loading image 

        self.image_file = fl
        self.img_org = Image.open(self.image_file)
        self.width_org, self.height_org = self.img_org.size # get the size of the original image
        self.ima = ImageTk.PhotoImage(self.img_org)
        self.raw_image = ImageTk.PhotoImage(self.img_org)

        ### CANVAS SETTINGS
        self.canvas=tk.Canvas(self.fc, highlightbackground="RED", highlightcolor="BLUE", highlightthickness=2, bd=0, width=self.width_org, height=self.height_org)
        self.canvas.create_image(self.width_org/2, self.height_org/2,image=self.ima, tags='myPhoto')
        self.x1, self.y1 = self.canvas.coords('myPhoto')
        #print(x1,y1)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.bind("<ButtonPress-1>",self.dragStart) #self.canvas.bind('<Button-2>', lambda evt: self.canvas.scan_mark(evt.x, evt.y))
        self.canvas.bind("<ButtonRelease-1>",self.dragEnd)
        #canvas.bind("<MouseWheel>",scroll)
        self.canvas.bind("<Button-2>",self.zoomin)
        self.canvas.bind("<MouseWheel>",self.zoomout)
        #canvas.bind("<Button-2>",reset)
        self.canvas.bind("<Motion>",self.track)



        ### End Loading image 


    def zoom(self):
        #global counter, ima, ChangeDx, ChangeDy
        
        #####    scaling image
        z=0
        self.factor =  1 / self.counter
        self.width = int(self.width_org * self.factor)
        self.height = int(self.height_org * self.factor)
        self.img_anti = self.img_org.resize((self.width, self.height), Image.ANTIALIAS)
        #width_org, height_org = img_anti.size
        #####    scaling image
        #canvas.delete(image=ima)
        self.ima = ImageTk.PhotoImage(self.img_anti)
        #canvas.delete('myPhoto')
        self.canvas.config(width=self.width, height=self.height)
        self.canvas.create_image(self.width/2 - self.cx,self.height/2 - self.cy,image=self.ima,tags='myPhoto')
        self.x1, self.y1 = self.canvas.coords('myPhoto')
        #print( x1, y1)
        self.canvas.grid(row=0, column=0,sticky='nswe')
        self.ChangeDx = 0
        
        self.ChangeDy = 0
        self.canvas.delete("points")
        self.canvas.delete("text")
        for z in range (self.i):
            self.canvas.create_oval(self.a[z]/(self.counter*self.t)-self.cx-2/self.counter ,self.b[z]/(self.counter*self.t)-self.cy-2/self.counter , self.a[z]/(self.counter*self.t)-self.cx+2/self.counter, self.b[z]/(self.counter*self.t)-self.cy+2/self.counter,fill='red', tag='points')
            self.canvas.create_text(self.a[z]/(self.counter*self.t)-self.cx, self.b[z]/(self.counter*self.t)-self.cy, tags="text", text=str(z+1))
        #self.root.mainloop()

    def reset(self):
        self.counter = 1 
        #self.zoom()
        #self.ChangeDx=0
        #self.ChangeDy=0
        self.zoom()
       
      
    def coordinates(self,click):
        #global x,y,z, counter, ChangeDx, ChangeDy
        print("clicked at;", (click.x - self.ChangeDx)*self.t* self.counter,(click.y - self.ChangeDy)*self.t* self.counter)
        #print(self.counter, self.ChangeDx, self.ChangeDy)
        self.x,self.y= str(float((click.x - self.ChangeDx)*self.counter*self.t )),str(float((click.y - self.ChangeDy)* self.counter*self.t))
        self.z=self.x+"  "+self.y
        self.ti.set(self.z)
        self.i+=1
        self.a.append((click.x - self.ChangeDx)* self.counter*self.t)
        self.b.append((click.y - self.ChangeDy)* self.counter*self.t)
        self.cb.append(self.endCounter)
        self.canvas.create_oval(click.x-2/self.counter- self.ChangeDx, click.y-2/self.counter- self.ChangeDy, (click.x +2/self.counter- self.ChangeDx),  (click.y +2/self.counter- self.ChangeDy),fill='red',tag='points'  )
        self.canvas.create_text(click.x-self.ChangeDx, click.y- self.ChangeDy, tags="text", text=str(self.i))
        self.root.mainloop()

    def zoomin(self,event):
        
        self.counter = self.counter / 2
        #print(counter)
        self.zoom()

    def zoomout(self,event):
        #global counter
        self.counter = self.counter * 2
        #print(counter)
        self.zoom()       

    def track(self,event):
        #global curcor, icord, counter
        if (int(event.x) >= 0 & (event.y) >= 0):
            self.icordx = event.x
            self.icordy = event.y
            self.cord = str(round(float((event.x - self.ChangeDx )*self.t* self.counter ),2))+ " -- " + str(round(float((event.y-self.ChangeDy)*self.t* self.counter),2))
            #print(counter)
            self.curcor.set(self.cord)
        else:
            self.root.mainloop()
            
    def dragStart(self,event):
        #global dragStX, dragStY
        self.canvas.scan_mark(event.x , event.y)
        #root.mainloop()
        self.dragStX = event.x
        self.dragStY = event.y
        
        
        
    def dragEnd(self,event):
        #global dragEndX, dragEndY, ChangeDx, ChangeDy, counter
        self.dragEndX = event.x
        self.dragEndY = event.y
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        #x1, y1 = canvas.coords('myPhoto')
        #print( (event.x-x1 ), (event.y-y1) )
        print("---start---")
        #print( self.dragStX, self.dragStY )
        #print( self.dragEndX, self.dragEndY )
        self.ChangeDx = (self.dragEndX - self.dragStX + self.ChangeDx) 
        self.ChangeDy = (self.dragEndY - self.dragStY + self.ChangeDy)
        self.cx=(self.dragEndX - self.dragStX + self.cx)
        self.cy=(self.dragEndY - self.dragStY + self.cy)

        print(self.ChangeDx, self.ChangeDy)
        print("---end---")
        self.root.mainloop()

    def delete(self):
        self.i-=1
        z=0
        self.a.pop()
        self.b.pop()
        self.cb.pop()
        self.canvas.delete("points")
        self.canvas.delete("text")
        for z in range (self.i):
            self.canvas.create_oval(self.a[z]/(self.counter*self.t)-self.cx-2/self.counter ,self.b[z]/(self.counter*self.t)-self.cy-2/self.counter , self.a[z]/(self.counter*self.t)-self.cx+2/self.counter, self.b[z]/(self.counter*self.t)-self.cy+2/self.counter,fill='red', tag='points')
            self.canvas.create_text(self.a[z]/(self.counter*self.t)-self.cx, self.b[z]/(self.counter*self.t)-self.cy, tags="text", text=str(z+1))


    def can(self):
        self.canvas.bind("<Button-3>", self.coordinates)
                         

    def coo(self, eve):
        self.ti.set("invalid")

    def see(self):
        z=0
        wb = Workbook()
        ws = wb.active
        print(self.cb,z)
        for z in range(self.i):
                  ws.append((self.a[z],self.b[z],self.cb[z]))                 
                  z+=1
        wb.save('BoundaryPoints.xlsx')
        self.endCounter = self.endCounter + 1
        self.canvas.bind("<Button-3>", self.coo)

#root=Tk()
#frame=tk.Frame(root)
#frame.grid(row=0, column=0)
#frames=tk.Frame(root)
#frames.grid(row=1, column=0)
#dragworking("2.jpg",root,frame,frames,20)
#root.mainloop()
