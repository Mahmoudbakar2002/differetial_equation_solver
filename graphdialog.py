# your code goes here#KENAA
# I CAN DO IT
from cProfile import label
from calendar import c
from tkinter import *
import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np
from numpy import *
from sympy  import *

from equations_handling import *
from _testcapi import MyList

class GraphDialog:
    def __init__(self, parent,equation,solution):
               
        graph_window = self.graph_window = tk.Toplevel(parent)
        graph_window.title("graph")
        
        width=750
        height=600
        screenwidth = parent.winfo_screenwidth()
        screenheight = parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        graph_window.geometry(alignstr)
        
        
        
        self.f=lambda x,y: equation.subs({"x":x,"y":y})
        self.solution=solution 
        
        #y(X)=the entry
        text1=Label(graph_window,text="y(x)=",height=1,font=("Arial",20)).place(x=0,y=10)
        # y var
        self.y =IntVar()
        #enter y(x)
        y_input =Entry(graph_window,width=3,font=("Arial",15),textvariable=self.y).place(x=65,y=19)
        #X=the entry
        text2=Label(graph_window,text="when x=",height=1,font=("Arial",20)).place(x=130,y=10)
        # x var
        self.x =IntVar()
        #enter x
        x_input =Entry(graph_window,width=3,font=("Arial",15),textvariable=self.x).place(x=240,y=19)
        # enter x[ , ]
        text3=Label(graph_window,text="x [     ,     ]",height=1,font=("Arial",23)).place(x=400,y=10)
        # x1 var
        self.x1 =IntVar()
        #enter x
        x1_input =tk.Entry(graph_window,width=3,font=("Arial",15),textvariable=self.x1).place(x=440,y=19)
        # x2 var
        self.x2 =IntVar()
        #enter x
        x2_input =Entry(graph_window,width=3,font=("Arial",15),textvariable=self.x2).place(x=493,y=19)
        #enter N
        text1=Label(graph_window,text="N=",height=1,font=("Arial",20)).place(x=0,y=50)
        # N var
        self.N =IntVar()
        #enter N
        N_input =Entry(graph_window,width=3,font=("Arial",15),textvariable=self.N).place(x=65,y=55)
        
        
        #graph button
        # btn= tk.Button(graph_window,text="graph",width=10,height=1,background="#1e90ff",fg="#ffffff",borderwidth=0,font=("Arial",15),command=self.gr).place(x=580,y=17)
        btn= ttk.Button(graph_window,text="graph",style='Accent.TButton' ,command=self.gr)
        btn.place(x=580,y=15,width=80,height=40)
        
        self.fig = plt.figure(num=0,dpi=110)# the fig size
        self.ax=self.fig.add_subplot(111)
        
        self.chart = FigureCanvasTkAgg(self.fig,master=graph_window)
        self.chart.get_tk_widget().place(x=5,y=90)
           
        
        #run app infinitely

        # self.myLabel = tk.Label(top, text='Enter your username below')
        # self.myLabel.pack()
        graph_window.transient(parent)
        graph_window.grab_set()

        # graph_window.wait_window()
    # def f(self,x,y):
    #     return 1/x
    # def f2 (self,x):
    #     return log(x)

#-----------------------------------------------------#

#method
    def gr(self):
        eulerX=[]#values of x in euler
        eulerY=[]#values of y in euler
        
        consol=remove_constants(self.solution,self.y.get(),self.x.get())
        f2=lambda x: consol.subs({"x":x}).rhs
     
        
        #euler method
        w = self.y.get() 
        x0=self.x1.get()
        h=(self.x2.get()-self.x1.get())/self.N.get()
        for i in range(1,self.N.get()+1):
            w=w+h*self.f(x0,w)
            eulerX.append(x0)
            eulerY.append(w)
            x0=self.x1.get()+(i*h)
    #----------------------------------------------------#    
    #f(x) graph
        xlist=np.arange(self.x1.get(),self.x2.get(),0.1)#values of x in f(x)   
        ylist=[]
        for x in xlist :ylist.append(f2(x))#values of y in f(x)

        
        #set the points in the graph 
    
        self.ax.clear()
        self.ax.grid(True)
        # print(xlist)
        # print(ylist)
        
        self.ax.plot(xlist,ylist,label="f(x)")
        self.ax.plot(eulerX,eulerY,label="eular")
        #display the graph
        
        self.ax.legend()# display labels in graph
        self.chart.draw()    