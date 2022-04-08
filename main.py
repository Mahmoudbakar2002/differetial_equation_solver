"""
            ODE SOLVER 

"""
###########################################################
##         IMPORT Libraries
###########################################################

#-----Tkinter--------
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#------ matploit ---------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
from csv import excel
from builtins import input
matplotlib.use('TkAgg')

#--------- sympy ---------------------
from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy  import *

#------ classes and functions -------
from tooltip import *
import equations_handling
from equations_handling import *



# ----------- Handling live Entry View --------------------
def callback_entry_text_changed(input):
    '''
        Calling when text in entry changed it used StringVar
    '''
    live_plot_eqution(input.get())
    if check_input(equation_maliplation_sympy(input.get())):
        entry.state(["!invalid"])
    else:
        entry.state(["invalid"])
    # live_plot_eqution("2^{1/\sqrt{2}}")
    
       
def live_plot_eqution(text):
    """
        function to check input(text) is validate for view or not  then if validate 
        maliplation text and plot it  
    """
    #------Check input Here----------
    if(not check_input(text)):
        ax_entered_equation.clear()
        ax_entered_equation.set_title("Entered Equation:")
        ax_entered_equation.text(0.2, 0.6, "", fontsize=20)  
        canvas.draw()
        return;
    #print(text)
    xt=equation_maliplation_sympy(text)
    tmptext = "$ \\frac{dy}{dx} ="+latex(sympify(xt))+"$"
    
    ax_entered_equation.clear()
    ax_entered_equation.set_title("Entered Equation:")
    ax_entered_equation.text(0.05, 0.45, tmptext, fontsize=20)  
    canvas.draw()
    


def check_input(input):
    """
        To check if input text is validate or not
    """
    try:
        xt=equation_maliplation_sympy(input)
        sympify(xt)
        return True
    except:  
        return False    
    

#-------------------------------------------------------------------- 
   
# ----------- Handling Equautions solve button and view result --------------------
def de():
    expr = entry.get()
    if check_input(expr):
        entry.state(["!invalid"])
    else:
        entry.state(["invalid"])
        return 
    
    
    
    equation=equation_maliplation_sympy(expr)
    # print(expr)
    solution = solve_equation(equation)
    
    #-------- Proparteies -----------
    props_eq=get_proparteies_classifcation(equation)
    set_equation_proparteies_state(props_eq)
    
    #----- View latex solution
    txte = latex(solution)
    txte = "$"+txte+"$"
    ax_solution.clear()
    ax_solution.set_title("Solution:")
    ax_solution.text(0.05, 0.45, txte, fontsize=20)  
    canvas.draw()
    
def set_equation_proparteies_state(props):
    for propartey in props:
        equation_probarteies[propartey]["state"]=props[propartey]
        if props[propartey]:
            equation_probarteies[propartey]["btn"].config(image=correct_img)
        else:
            equation_probarteies[propartey]["btn"].config(image=wrong_img)
             
        # print(propartey)


""""
============================================================
        Draw Frame and components in it Tkiniter
                    ^ Main Code ^ 
==============================================================
"""

frame = tk.Tk()       
frame.title("frist order DE solver")
width=800
height=500
screenwidth = frame.winfo_screenwidth()
screenheight = frame.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frame.geometry(alignstr)
frame.resizable(width=True, height=True)
style = ttk.Style(frame)
frame.tk.call("source", "azure/azure.tcl")



style.theme_use('azure')
ft = tkFont.Font(family='Times',size=10)


############################################################################
###            Figure for plots
############################################################################
entered_equation_live_view_width=500
entered_equation_live_view_height=300
entered_equation_live_view_dpi=100

entered_equation_live_view=ttk.Label(frame)
entered_equation_live_view.place(x=10,y=140,width=entered_equation_live_view_width,height=entered_equation_live_view_height)

fig = matplotlib.figure.Figure(figsize=((entered_equation_live_view_width/entered_equation_live_view_dpi),
                                        (entered_equation_live_view_height/entered_equation_live_view_dpi)),
                                         dpi=entered_equation_live_view_dpi)

canvas = FigureCanvasTkAgg(fig, master=entered_equation_live_view)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
canvas._tkcanvas.pack(side="top", fill="both", expand=True)
fig.subplots_adjust(left=0,hspace=0.5)



ax_entered_equation = fig.add_subplot(211)
ax_entered_equation.get_xaxis().set_visible(False)
ax_entered_equation.get_yaxis().set_visible(False)
ax_entered_equation.set_title("Entered Equation:")

ax_solution = fig.add_subplot(212)
ax_solution.get_xaxis().set_visible(False)
ax_solution.get_yaxis().set_visible(False)
ax_solution.set_title("Solution:")


####################################################################
####################################################################
        
solution_button=ttk.Button(frame,style='Accentbutton' ,text = "solution",command = de)
solution_button.place(x=240,y=430,width=120,height=30)


####################################################################

equation_proparty_box = ttk.LabelFrame(frame, text='Differential equation Propartey:', width=200, height=210)
equation_proparty_box.place(x=480, y=200)


equation_probarteies={"homo":{"name":"Homomgenius","state":False},
                      "exact":{"name":"Exact","state":False}}

correct_img = PhotoImage(file='img\correct.png')
wrong_img = PhotoImage(file='img\wrong.png')

y_axis_props=5;
for prop in equation_probarteies:
    lblimg=ttk.Label(equation_proparty_box,image=wrong_img,text=equation_probarteies[prop]["name"],font=("JF Flat", 14))
    lblimg.place(x=5,y=y_axis_props,width=190,height=30)
    lblimg["compound"]=tk.RIGHT
    equation_probarteies[prop]["btn"]=lblimg
    y_axis_props=y_axis_props+35

#######################################################################################
#                  Equation Box 
#######################################################################################
equation_box = ttk.LabelFrame(frame, text='Enter Equation', width=500, height=100)
equation_box.place(x=10, y=10)

label_for_y_prime = ttk.Label(equation_box,text = "y′",font=("Arial", 14))
label_for_y_prime.place(x=20,y=5,width=30,height=30)

#----------------Entry     --------------------

var_trace_string_changed = tk.StringVar(value = "")         
var_trace_string_changed.trace("w", lambda name, index, mode, sv=var_trace_string_changed: callback_entry_text_changed(var_trace_string_changed))
# reg = (frame.register(validate_entry))

entry=ttk.Entry(equation_box,textvariable=var_trace_string_changed)
# entry.config(validate="key", validatecommand=(reg, '%P'))
# entry.bind('<Key>',press)
# entry.bind('<BackSpace>',clear)
entry.place(x=60,y=5,width=328,height=30)


#--------------- info Button ---------------------------- 
infoTxt="enter y prime then press solution you will get the answer.\r\nfor write equtions:\n + :plus\n - :minus\n * :multibly\n / :division\n x^y : xpowery\n  "

Button_help=ttk.Button(equation_box,text = "?" ,
                       style="" ,
                       command = lambda: messagebox.showinfo("showinfo", infoTxt))
Button_help.place(x=390,y=5,width=30,height=30)
CreateToolTip(Button_help,infoTxt)



# ----------------- Buttons to add & edit in entry -----------------

btn_x_location=60

Button_clr=ttk.Button(equation_box,text = "clr" , command = lambda: entry.delete(0, END) )
Button_clr.place(x=btn_x_location,y=40,width=40,height=30)
btn_x_location=btn_x_location+45




Add_to_entry_command = lambda x: entry.insert(INSERT, str(x))
my_buttons_list=[  {"name":"+"    ,"command":lambda: Add_to_entry_command("+")},
                   {"name":"-"    ,"command":lambda: Add_to_entry_command("-")},
                   {"name":"x"    ,"command":lambda: Add_to_entry_command("*")},
                   {"name":"÷"   ,"command":lambda: Add_to_entry_command("/")},
                   {"name":"^"    ,"command":lambda: Add_to_entry_command("^")},
                   {"name":"√(" ,"command":lambda: Add_to_entry_command("√(")},
                   {"name":"π"   ,"command":lambda: Add_to_entry_command("π")},
                   {"name":"("    ,"command":lambda: Add_to_entry_command("(")},
                   {"name":")"    ,"command":lambda: Add_to_entry_command(")")},
                ]


for btn in my_buttons_list:
    button_to_entrt=ttk.Button(equation_box ,style="Accentbutton",text = btn["name"],command =btn["command"])
    button_to_entrt.place(x=btn_x_location,y=40,width=35,height=30)
    btn_x_location=btn_x_location+37



        
frame.mainloop()