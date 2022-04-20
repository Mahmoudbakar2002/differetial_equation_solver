"""
            ODE SOLVER 

"""
###########################################################
##         IMPORT Libraries
###########################################################
#-----Tkinter--------
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import PhotoImage


#--------- sympy ---------------------
from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy  import *

#------ classes and functions -------
import equations_handling
from equations_handling import *
from root import Root
from widgets.dialogs import *





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
    
def set_equation_proparteies_state(props):
    for propartey in props:
       rootframe.set_equation_propartey_value(propartey,props[propartey])

#-------------------------------------------------------------------- 
   
# ----------- Handling Equautions solve button and view result --------------------
def de(entry):
    expr = entry.get()
    if check_input(expr):
        entry.state(["!invalid"])
    else:
        entry.state(["invalid"])
        worried = PhotoImage(file='img\worried2.png')
        show_message("Error in Equation", "you enter wrong equatoin in y'.\nCheck your entered equation.",icon=worried)

        return []
    
    
    # live_plot_eqution(expr)
    equation=equation_maliplation_sympy(expr)
    equation=sympify(equation)
    # print(expr)
    origin_equation  = "$ \\frac{dy}{dx} ="+latex(equation)+"$"
    solution = solve_equation(equation)
    
    #-------- Proparteies -----------
    props_eq=get_proparteies_classifcation(equation)
    set_equation_proparteies_state(props_eq)
    
    # ------ View latex original equation
    origin_equation=origin_equation.replace("log","ln")
    origin_equation=origin_equation.replace("y(x)","y")
    origin_equation=origin_equation.replace("y{\\left(x \\right)}","y")

    # print(origin_equation)
    rootframe.ax_entered_equation.clear()
    rootframe.ax_entered_equation.set_title("Entered Equation:",color=rootframe.title_plot_color)
    rootframe.ax_entered_equation.text(0.5, 0.5, txte, horizontalalignment='center',
    verticalalignment='center', transform=rootframe.ax_entered_equation.transAxes,fontsize='large')  
    
    #----- View latex solution
    # print(solution)
    txte = latex(solution)
    txte = "$"+txte+"$"
    txte=txte.replace("log","ln")
    # txte=txte.replace("y(x)","x")
    rootframe.ax_solution.clear()
    rootframe.ax_solution.set_title("Solution:",color=rootframe.title_plot_color)
    rootframe.ax_solution.text(0.5, 0.5, txte, horizontalalignment='center',
    verticalalignment='center', transform=rootframe.ax_solution.transAxes,fontsize='large')  
    
    # --- Draw cnvas after type equation in matploit
    rootframe.canvas.draw()
    return [equation,solution]
def change_theme():
    # NOTE: The theme's real name is sun-valley-<mode>
    # print(agreement.get())
    rootframe.change_theme_mode(agreement.get())
    if  agreement.get()=="light":#root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        frame.tk.call("set_theme", "light")

    else:
        # Set dark theme
        # rootframe.fig.set_facecolor('#1c1c1c')
        frame.tk.call("set_theme", "dark")

""""
============================================================
                    ^ Main Code ^ 
==============================================================
"""

#--- intialize frame size and data
frame = tk.Tk()       
frame.title("frist order DE solver")
# frame.configure(background='white')
width=750
height=420
screenwidth = frame.winfo_screenwidth()
screenheight = frame.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
frame.geometry(alignstr)
frame.resizable(width=True, height=True)

#----- load theme -----------
style = ttk.Style(frame)
frame.tk.call("source", "sun-valley/sun-valley.tcl")
frame.tk.call("set_theme", "light")

# style.theme_use('sun-valley')
ft = tkFont.Font(family='Times',size=10)
agreement = tk.StringVar()

# var_2.trace(mode, callback)
switch = ttk.Checkbutton(
            frame, text="Dark", style="Switch.TCheckbutton",
            variable=agreement,
            onvalue='dark',
                offvalue='light',command=change_theme
        )
switch.place(x=630,y=15,width=100,height=30)
# root Frame

style = ttk.Style()
style.theme_use('sun-valley-dark')
style.configure('Accent.TButton', font=('JF flat', 13),padding=0)

style.theme_use('sun-valley-light')
style.configure('Accent.TButton', font=('JF flat', 13),padding=0)



rootframe=Root(frame,de)

# run frame
frame.mainloop()
####################################################################


####################################################################






# my_buttons_functions_list=[  {"name":"cos"    ,"command":lambda: Add_to_entry_command("cos(")},
                          #    {"name":"sin"    ,"command":lambda: Add_to_entry_command("sin(")},
                          #    {"name":"tan"    ,"command":lambda: Add_to_entry_command("tan(")},
                          #    {"name":"ln"    ,"command":lambda: Add_to_entry_command("ln(")},
                          #    {"name":"ln"    ,"command":lambda: Add_to_entry_command("ln(")},
                          #
                          #
                          # ]


    # print(btn_x_location)
    # if btn_x_location % 655 == 0  :
    #         btn_x_location=328+60
    #         btn_y_location=btn_y_location+35
# btn_y_location=75
# btn_x_location=60   
# for btn in my_buttons_functions_list:
#     button_to_entrt=ttk.Button(equation_box ,style="Accentbutton",text = btn["name"],command =btn["command"])
#     button_to_entrt.place(x=btn_x_location,y=btn_y_location,width=50,height=30)
#     btn_x_location=btn_x_location+52   
#     if btn_x_location % 424 == 0  :
#             btn_x_location=60
#             btn_y_location=btn_y_location+35

        
