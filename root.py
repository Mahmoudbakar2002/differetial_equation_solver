""""
============================================================
        Draw Frame and components in it Tkiniter
                    
==============================================================
"""



#-----Tkinter--------
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

import tkinter.font as tkFont
import tkinter.font as font

from widgets.tooltip import *
from widgets.dialogs import *
from graphdialog import  *

#------ matploit ---------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
matplotlib.use('TkAgg')

class Root:
    def __init__(self,frame,solve_function):
        ############################################################################
        ###            Figure for plots
        ############################################################################
        self.frame=frame
        self.solve_function=solve_function
        
        self.equation_probarteies={"homo":{"name":"Homomgenius","state":False},
                              "exact":{"name":"Exact","state":False},
                              "bernoulli":{"name":"Bernoulli","state":False},
                              "linear":{"name":"linear","state":False},
                              "separable":{"name":"separable","state":False}
                              }
        Add_to_entry_command = lambda x: self.entry.insert(INSERT, str(x))
        self.my_buttons_list=[  {"name":"+"    ,"command":lambda: Add_to_entry_command("+")},
                   {"name":"-"    ,"command":lambda: Add_to_entry_command("-")},
                   {"name":"x"    ,"command":lambda: Add_to_entry_command("*")},
                   {"name":"÷"   ,"command":lambda: Add_to_entry_command("/")},
                   {"name":"^"    ,"command":lambda: Add_to_entry_command("^")},
                   {"name":"√(" ,"command":lambda: Add_to_entry_command("√(")},
                   {"name":"π"   ,"command":lambda: Add_to_entry_command("π")},
                   {"name":"("    ,"command":lambda: Add_to_entry_command("(")},
                   {"name":")"    ,"command":lambda: Add_to_entry_command(")")},
                ]
        
        self.title_plot_color="black"
        self.__build_equtions_view()
        self.__build_eqution_propartey_box()
        self.__build_equation_box()
    def set_equation_propartey_value(self,prop,val):
        self.equation_probarteies[prop]["state"]=val
        if val:
            self.equation_probarteies[prop]["btn"].config(image=self.correct_img)
        else:
            self.equation_probarteies[prop]["btn"].config(image=self.wrong_img)
             
    def __build_equation_box(self):
        '''
            fuction to build eqution box that contain entry and buttons to add to it and 
            solution button
        '''
        
        # -----------eauation box frame-------------
        equation_box = ttk.LabelFrame(self.frame, text='Enter Equation', width=600, height=100)
        equation_box.place(x=20, y=10)
        
        #---------- label that view y' sign---------------
        label_for_y_prime = ttk.Label(equation_box,text = "y′",font=("Arial", 14))
        label_for_y_prime.place(x=40,y=10,width=30,height=30)
        
        
        ####################################################################
        # -------- Solution Button
        # s = ttk.Style()
        # s.configure('Accentbutton', font=('JF Flat', 15))        
        
        # style.map('Accent.TButton', foreground=[('active', "white"), ])


        solution_button=ttk.Button(equation_box,style='Accent.TButton'  ,text = "Solve it!",command =lambda: self.solve_function(self.entry))
        # solution_button.configure(font=('JF flat', 14))
        solution_button.place(x=480,y=40,width=90,height=35)
        # myFont = font.Font(size=30)
        # solution_button.configure(font= myFont)
        # solution_button.configure("my.TButton",font=("Tahoma",14))
        ####################################################################

        
        #----------------Entry     --------------------
        var_trace_string_changed = tk.StringVar(value = "")         
        # var_trace_string_changed.trace("w", lambda name, index, mode, sv=var_trace_string_changed: callback_entry_text_changed(var_trace_string_changed))
        # reg = (frame.register(validate_entry))
        self.entry=ttk.Entry(equation_box,textvariable=var_trace_string_changed)
        # entry.config(validate="key", validatecommand=(reg, '%P'))
        # entry.bind('<Key>',press)
        # entry.bind('<BackSpace>',clear)
        self.entry.place(x=75,y=5,width=400,height=30)
        
        
        #--------------- info Button ---------------------------- 
        infoTxt="enter y prime then press 'solve it' you will get the answer.\r\nfor write equtions:\n + :plus\n - :minus\n * :multibly\n / :division\n x^y : xpowery\n  "
        
        think = PhotoImage(file='img\\think.png')

        Button_help=ttk.Button(equation_box,text = "?" ,
                                style="" ,
                                command = lambda:show_message("How to use?", infoTxt,icon=think))
        Button_help.place(x=480,y=5,width=30,height=30)
        CreateToolTip(Button_help,infoTxt)
        
        
         #--------------- info Button ----------------------------
        def onClickGraph():
            eqs=self.solve_function(self.entry)
            if len(eqs)==0:return
            
            graphDialog = GraphDialog(self.frame,eqs[0],eqs[1])
            self.frame.wait_window(graphDialog.graph_window)
        
          
        graph_img = PhotoImage(file='img\graph.png')
        buttion_graph=ttk.Button(equation_box,
                                 image=graph_img,
                                style="Accent.TButton" ,
                                command = onClickGraph)
        buttion_graph.image = graph_img
        buttion_graph.place(x=515,y=5,width=55,height=30)
       
        # ----------------- Buttons to add & edit in entry -----------------
        btn_x_location=75
        btn_y_location=40
        
        Button_clr=ttk.Button(equation_box,text = "clr" , command = lambda: entry.delete(0, END) )
        Button_clr.place(x=btn_x_location,y=btn_y_location,width=45,height=30)
        btn_x_location=btn_x_location+50
        for btn in self.my_buttons_list:
            button_to_entrt=ttk.Button(equation_box ,style="",text = btn["name"],command =btn["command"])
            button_to_entrt.place(x=btn_x_location,y=btn_y_location,width=35,height=30)
            btn_x_location=btn_x_location+37

        '''
======================================================================
        end build_equation_box
========================================================================
        '''
    def __build_eqution_propartey_box(self):
        '''
            function to build equtions Propartey view  in frame
        
        '''
        equation_proparty_box = ttk.LabelFrame(self.frame, text='Differential equation Propartey:', width=200, height=240)
        equation_proparty_box.place(x=490, y=150)
        
        
        
        self.correct_img = PhotoImage(file='img\correct.png')
        self.wrong_img = PhotoImage(file='img\wrong.png')
        
        y_axis_props=5;
        for prop in self.equation_probarteies:
            lblimg=ttk.Label(equation_proparty_box,image=self.wrong_img,text=self.equation_probarteies[prop]["name"],font=("JF Flat", 14))
            lblimg.place(x=5,y=y_axis_props,width=190,height=30)
            lblimg["compound"]=tk.RIGHT
            self.equation_probarteies[prop]["btn"]=lblimg
            y_axis_props=y_axis_props+35
    

    def __build_equtions_view(self):
        '''
            function to build equtions matploit views in frame
        '''
        
        entered_equation_live_view_width=500
        entered_equation_live_view_height=300
        entered_equation_live_view_dpi=100
        
        entered_equation_live_view=ttk.Label(self.frame)
        entered_equation_live_view.place(x=10,y=120,width=entered_equation_live_view_width,height=entered_equation_live_view_height)
        
        self.fig = matplotlib.figure.Figure(figsize=((entered_equation_live_view_width/entered_equation_live_view_dpi),
                                                (entered_equation_live_view_height/entered_equation_live_view_dpi)),
                                                 dpi=entered_equation_live_view_dpi)
        
        self.fig.set_facecolor('#fafafa')
        self.canvas = FigureCanvasTkAgg(self.fig, master=entered_equation_live_view)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        self.canvas._tkcanvas.pack(side="top", fill="both", expand=True)
        self.fig.subplots_adjust(left=0,hspace=0.5)
        
        
        self.ax_entered_equation = self.fig.add_subplot(211)
        # self.ax.set_facecolor('xkcd:salmon')
        self.ax_entered_equation.get_xaxis().set_visible(False)
        self.ax_entered_equation.get_yaxis().set_visible(False)
        self.ax_entered_equation.set_title("Entered Equation:")
        
        self.ax_solution = self.fig.add_subplot(212)
        self.ax_solution.get_xaxis().set_visible(False)
        self.ax_solution.get_yaxis().set_visible(False)
        self.ax_solution.set_title("Solution:")
        
    def change_theme_mode(self,them_mode):
        
        
        if them_mode=="light":
            self.title_plot_color='black'
            self.fig.set_facecolor('#fafafa')
        else :
            self.title_plot_color='white'
            self.fig.set_facecolor('#1c1c1c')
        self.ax_entered_equation.set_title("Entered Equation:",color=self.title_plot_color)
        self.ax_solution.set_title("Solution:",color=self.title_plot_color)
        self.canvas.draw()
    