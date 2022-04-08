"""
    this file contain all function and variables that use to handling and solve equation
    
    
"""
# import sympy
import sympy as sp
from sympy  import *
#-----------------------------

#    glopal x & y to use in equations
equation_x = sp.symbols('x')
equation_y_of_x= sp.Function('y')(equation_x)

## Sympols_Maliplation that use to replace sympol in equation by value of it
sympols_maliplation=[{"sympol":"√","value":"sqrt"},
                         {"sympol":"π","value":"pi"}
                    ]

def equation_maliplation_sympy(eq):    
    '''
        m.......
    '''
    for symp in sympols_maliplation:
        eq=eq.replace(symp["sympol"],symp["value"])
    return  eq


def get_differential_equation(equation):
    eqq = sympify(equation)
    return Eq(equation_y_of_x.diff(equation_x),eqq)
            
def solve_equation(equation):
    diffeq=get_differential_equation(equation)         
    return dsolve(diffeq,equation_y_of_x)

def get_proparteies_classifcation(equation):
    diffeq=get_differential_equation(equation)            
    print(classify_ode(diffeq))
    list_props={"homo":True,
              "exact":True}
    
    """ !!! IMPORTANT !!!!!
        Add some magic here to make classify_ode Data into list pros
    """
    
    return list_props
