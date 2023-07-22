#import pyautogui 
import os
import xlrd
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image



class dragworking():
    def __init__(self,fl, roo, frame,frames,tt):
        
        self.root=roo
        self.i=0
        self.k=0
        self.t= tt
        self.fc=frames
        self.fr=frame
        self.ti=StringVar()
        self.curcor = StringVar()
        self.ty=StringVar()
        #self.ima, self.img_org, self.counter, self.width_org, self.height_org, self.x, y, z,ChangeDx,ChangeDy 
        self.counter = 1
        self.ChangeDx = 0
        self.ChangeDy=0
        self.cx=0
        self.cy=0
            ### Start Entries
        
        self.entry3=Entry(self.fr,textvariable=self.curcor)
        self.entry3.grid(row=0, column=0,sticky='nswe')

        self.ResetButton = Button(self.fr,text = "rb", command = self.reset)
        self.ResetButton.grid(row=1, columnspan=3,sticky='nswe')
        ### End Entries

        self.b2 = Button(self.fr, text="lines", command=self.lines)  # to start selecting points
        self.b2.grid(row=0, column=1,sticky='nswe')
        

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
        if(self.k==1):
            self.canvas.delete("line")
            self.canvas.delete("text")
            self.lines()
        #self.root.mainloop()

    def reset(self):
        self.counter = 1 
        #self.zoom()
        #self.ChangeDx=0
        #self.ChangeDy=0
        self.zoom()
       
      
    def coordinatesclick(self,click):
        #global x,y,z, counter, ChangeDx, ChangeDy
        print("clicked at;", (click.x - self.ChangeDx)*self.t* self.counter,(click.y - self.ChangeDy)*self.t* self.counter)
        #print(self.counter, self.ChangeDx, self.ChangeDy)

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
        
    def lines(self):
        self.k=1
        m=0
        wb = xlrd.open_workbook('ANodeData.xlsx')
        sheet = wb.sheet_by_name('Sheet1')
        coords = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        wb = xlrd.open_workbook('AEdgesData.xlsx')
        sheet = wb.sheet_by_name('Sheet1')
        points = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
    
        for m in range(len(points)-1):
            j=points[m]
            p1=j[0]
            p2=j[1]
            a=coords[int(p1-1)]
            b=coords[int(p2-1)]
            x1=a[1]/(self.counter*self.t)-self.cx+self.ChangeDx
            y1=a[2]/(self.counter*self.t)-self.cy+self.ChangeDy
            x2=b[1]/(self.counter*self.t)-self.cx+self.ChangeDx
            y2=b[2]/(self.counter*self.t)-self.cy+self.ChangeDy
            self.canvas.create_line((x1,y1,x2,y2), fill='blue',tag='line')
            self.canvas.create_text((x1+x2)/2,(y1+y2)/2, tags="text", text=str(m+1))
            x1,y1,x2,y2= 0.0,0.0,0.0,0.0
            m+=1
            
#root=Tk()
#frame=tk.Frame(root)
#frame.grid(row=0, column=0)
#frame1=tk.Frame(root)
#frame1.grid(row=1, column=0)
#dragworking("2.jpg",root,frame,frame1,1)
#root.mainloop()
