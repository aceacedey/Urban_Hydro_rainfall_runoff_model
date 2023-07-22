# This is the main program creating and calling the three window
from tkinter import *
import os
from PIL import Image # calling the module tryimage which has function to be displayed in 2 window
import points # calling the module tryimage which has function to be displayed in
import reading
import quad
import contourpoints
class creating():
    def __init__(self, root, fr1, fr2, fr3,fr4,fr5,fr6,fr7,fr8,fr9,fr10):  # passing the root window and 3 frames
        self.f1 = fr1  # creating objects of the 3 frames
        self.f2 = fr2
        self.f3 = fr3
        self.f4 = fr4
        self.f5 = fr5
        self.f6 = fr6
        self.f7 = fr7
        self.f8 = fr8
        self.f9 = fr9
        self.f10= fr10
        self.roo = root
        self.cf1()
        #self.cf2()
        #self.cf3()
        #self.cf4()
        #self.cf5()
        #self.callf1()

    def cf1(self):
        f1label1 = Label(self.f1, text="WELCOME to URBAN-HYDRO MODELLING GUI")  # label to display heading
        f1label1.grid(row=10,column=7,padx=5,pady=20)  # placing the label

        f1label2 = Label(self.f1, text="Raster Image Directory")  # label to instruct to enter image filename
        f1label2.grid(row=30, column=5,padx=5)

        f1label3 = Label(self.f1,text="Georeferencing Factor")  # label to instruct to enter multiplicative parameter for coordinates
        f1label3.grid(row=30, column=10)

        self.e = Entry(self.f1,textvariable=StringVar)  # entry widget to accept multiplicative parameter for coordinates
        self.e.grid(row=40, column=10)

        f1button3 = Button(self.f1, text="Save", command=self.saveit1)  # button to save all the details from all entries
        f1button3.grid(column=5, row=70,padx=5)

        self.e2 = Entry(self.f1, textvariable=StringVar)  # entry widget to accept image filename
        self.e2.grid(row=40, column=5,padx=5)

        
        f1button1 = Button(self.f1, text="help", command=self.help_i)  # button to save all the details from all entries
        f1button1.grid(column=10, row=70)       


    #def cf2(self):

        #f1label4 = Label(self.f2, text="filename for points")  # label to instruct to enter filename for storing points
        #f1label4.grid(row=0, column=0)
        #self.e3 = Entry(self.f2, textvariable=StringVar)  # entry widget to accept filename of points
        #self.e3.grid(row=0, column=1)
        #f1button3 = Button(self.f2, text="Save", command=self.saveit2)  # button to save all the details from all entries
        #f1button3.grid(column=2, row=0)
        
    def cf3(self):
        f3button3 = Button(self.f3, text="Next", command=self.callf4)  # button to save all the details from all entries
        f3button3.grid(column=5, row=0, sticky='nswe')
        points.dragworking(self.f,self.roo,self.f3,self.f2,self.t)

    def cf4(self):
        f4button1= Button(self.f4, text="Press This first", command= self.geo)
        f4button1.grid(column=0, row=0, sticky='nwes')
        f4button2= Button(self.f4, text="create mesh using this", command= self.msh)
        f4button2.grid(column=1, row=0, sticky='nwes')
        f4button3= Button(self.f4, text="Press and wait 2 min", command= self.triangle)
        f4button3.grid(column=2, row=0, sticky='nwes')
        f4button4= Button(self.f4, text="Next", command= self.callf5)
        f4button4.grid(column=3, row=0, sticky='nwes')
                        
    def cf5(self):
        reading.dragworking(self.f,self.roo, self.f5,self.f2,self.t)
        f5button3= Button(self.f5, text="Next", command= self.callf6)
        f5button3.grid(column=2, row=0, sticky='nwes')
        
                
    def cf6(self):

        f6button1= Button(self.f6, text="guide", command= self.guide)
        f6button1.grid(column=0, row=0, sticky='nwes')
        f6button2= Button(self.f6, text="Next Select Counter Points", command= self.callf7)
        f6button2.grid(column=1, row=0, sticky='nwes')

    def cf7(self):

        f7button1 = Button(self.f7, text="Press this first", command=self.instruct)  # button to save all the details from all entries
        f7button1.grid(column=2, row=1, sticky='nswe')
        f7button2 = Button(self.f7, text="Interpolate", command=self.inter)  # button to save all the details from all entries
        f7button2.grid(column=3, row=1, sticky='nswe')
        f7button3 = Button(self.f7, text="Next", command=self.callf8)  # button to save all the details from all entries
        f7button3.grid(column=4, row=1, sticky='nswe')
        contourpoints.dragworking(self.f,self.roo,self.f7,self.f2,self.t)

    def cf8(self):
        
        f8button1 = Button(self.f8, text="First", command=self.triangledata)  # button to save all the details from all entries
        f8button1.grid(column=0, row=0, sticky='nswe')
        f8button2 = Button(self.f8, text="Create Final Database", command=self.draintriangle)  # button to save all the details from all entries
        f8button2.grid(column=1, row=0, sticky='nswe')
        f8button3 = Button(self.f8, text="Generate Hydrograph", command=self.flowcode)  # button to save all the details from all entries
        f8button3.grid(column=2, row=0, sticky='nswe')
        f8button4 = Button(self.f8, text="Next", command=self.callf9)  # button to save all the details from all entries
        f8button4.grid(column=3, row=0, sticky='nswe')
        #f8button4 = Button(self.f8, text="DrawLines", command=self.callf99)  # button to save all the details from all entries
        #f8button4.grid(column=3, row=0, sticky='nswe')
        

    def cf9(self):
        f9button3 = Button(self.f9, text="Next", command=self.callf10)  # button to save all the details from all entries
        f9button3.grid(column=0, row=0, sticky='nswe')

    def cf10(self):
        f1label1 = Label(self.f10, text="BYE")  # label to display heading
        f1label1.grid(row=0, columnspan=2)  # placing the label
        
    def callf3(self):
        self.f1.grid_forget()
        self.f4.grid_forget()
        self.f5.grid_forget()
        self.f6.grid_forget()
        self.f7.grid_forget()
        self.f8.grid_forget()
        self.f9.grid_forget()
        self.f10.grid_forget()
        self.f3.grid(column=0, row=0, sticky=N + W + E + S)
        self.f2.grid(column=0, row=1, sticky=N + W + E + S)
        self.cf3()

    def callf4(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f5.grid_forget()
        self.f6.grid_forget()
        self.f7.grid_forget()
        self.f8.grid_forget()
        self.f9.grid_forget()
        self.f10.grid_forget()
        self.f4.grid(column=0, row=0, sticky=N + W + E + S)
        self.cf4()

    def callf5(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.f6.grid_forget()
        self.f7.grid_forget()
        self.f8.grid_forget()
        self.f9.grid_forget()
        self.f10.grid_forget()
        self.f5.grid(column=0, row=0, sticky=N + W + E+S)
        self.cf5()
        
    def callf6(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.f5.grid_forget()
        self.f7.grid_forget()
        self.f8.grid_forget()
        self.f9.grid_forget()
        self.f10.grid_forget()
        self.f6.grid(column=0, row=0, sticky=N + W + E+S)
        self.cf6()

    def callf7(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.f5.grid_forget()
        self.f6.grid_forget()
        self.f8.grid_forget()
        self.f9.grid_forget()
        self.f10.grid_forget()
        self.f7.grid(column=0, row=0, sticky=N + W + E+S)
        self.cf7()

    def callf8(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.f5.grid_forget()
        self.f6.grid_forget()
        self.f7.grid_forget()
        self.f9.grid_forget()
        self.f10.grid_forget()
        self.f8.grid(column=0, row=0, sticky=N + W + E+S)
        self.cf8()

    def callf9(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.f5.grid_forget()
        self.f6.grid_forget()
        self.f7.grid_forget()
        self.f8.grid_forget()
        self.f10.grid_forget()
        self.f9.grid(column=0, row=0, sticky=N + W + E+S)
        self.cf9()

    def callf10(self):
        self.f1.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.f5.grid_forget()
        self.f6.grid_forget()
        self.f7.grid_forget()
        self.f8.grid_forget()
        self.f9.grid_forget()
        self.f10.grid(column=0, row=0, sticky=N + W + E+S)
        self.cf10()
    #def callf99(self):
        #reading.dragworking(self.f,self.roo,self.f8,self.f2,self.t)
        #reading.dragworking.lines(self)

    def help_i(self):
        dire = self.e2.get()
        print(dire)
        Pathstring = self.e2.get() + '\Help Files\help.txt'
        print(Pathstring)
        os.startfile(Pathstring)
        
    def saveit1(self):
        self.f=self.e2.get() + '\PL.png'
        self.t=round(float(self.e.get()),2)
        self.callf3()
        
    def geo(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\exe and Input Files\gmsh_formatting.exe")

    def msh(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\exe and Input Files\gmsh.exe")

    def triangle(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\exe and Input Files\msh_read.exe")

    def guide(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\Help Files\guide.txt")
        self.callf5()

    def instruct(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\Help Files\contourinstruct.txt")

    def triangledata(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\exe and Input Files\Triangle_data.exe")

    def draintriangle(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\exe and Input Files\Drain_Triangle.exe")
    def flowcode(self):
        os.startfile(r"C:\Users\14GS71P01\OneDrive\Urban Hydro Runoff Predictor v1.0\exe and Input Files\overlandflow.exe")

    def inter(self):
        quad.quad()


roo = Tk()  # root window
# creating the frames used in class
f2 = Frame(roo)
f2.grid(column=0, row=1, sticky=N + W + E + S)

f1 = Frame(roo)
f1.grid(column=0, row=0, sticky=N + W + E + S)
f3 = Frame(roo)
f3.grid(column=0, row=0, sticky=N + W + E + S)
f4 = Frame(roo)
f4.grid(column=0, row=0, sticky=N + W + E + S)
f5 = Frame(roo)
f5.grid(column=0, row=0, sticky=N + W + E + S)
f6 = Frame(roo)
f6.grid(column=0, row=0, sticky=N + W + E + S)
f7 = Frame(roo)
f7.grid(column=0, row=0, sticky=N + W + E + S)
f8 = Frame(roo)
f8.grid(column=0, row=0, sticky=N + W + E + S)
f9 = Frame(roo)
f9.grid(column=0, row=0, sticky=N + W + E + S)
f10 = Frame(roo)
f10.grid(column=0, row=0, sticky=N + W + E + S)
f3.grid_forget()
f2.grid_forget()
f4.grid_forget()
f5.grid_forget()
f6.grid_forget()
f7.grid_forget()
f8.grid_forget()
f9.grid_forget()
f10.grid_forget()

# calling the class
creating(roo, f1, f2, f3,f4,f5,f6,f7,f8,f9,f10)
# create.cf1()
# create.cf2()
# create.cf3()
# hinding frames other than first frame


roo.mainloop()
