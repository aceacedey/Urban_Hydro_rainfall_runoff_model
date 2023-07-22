from openpyxl import Workbook
import xlrd
import numpy as np
import scipy.linalg


class quad:
    def __init__(self):
        z=0
        
        wb = xlrd.open_workbook('contourN.xlsx')
        sheet = wb.sheet_by_name('Sheet')
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        a=np.empty([len(data),3])
        p=[]
        for z in range (len(data)):
            p=data[z]
            a[z,0],a[z,1],a[z,2]=p[0],p[1],p[2]
        
        wb = xlrd.open_workbook('ANodeData.xlsx')
        sheet = wb.sheet_by_name('Sheet1')
        coord= [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        x=np.empty([len(coord),1])
        y=np.empty([len(coord),1])
        z=0
        for z in range (len(coord)):
            p=coord[z]
            x[z,0],y[z,0]=p[1],p[2]
            print(x)
            print(y)
        
        A = np.c_[np.ones(a.shape[0]), a[:,:2], np.prod(a[:,:2], axis=1),a[:,:2]**2]
        C,_,_,_ = scipy.linalg.lstsq(A, a[:,2])
        B= np.c_[np.ones(x.shape[0]), x, y, x*y, x**2, y**2]
        Z = np.dot(B, C).reshape(x.shape)
        z=0
        wb = Workbook()
        ws = wb.active
        for z in range(x.shape[0]):
                  ws.append((z+1,x[z,0],y[z,0],Z[z,0]))
                  z+=1
        wb.save('ANodeDataZ.xlsx')

#quad()
