

# -*- coding: utf-8 -*-

# Copyright (c) Juliette Monsel 2018
# For license see LICENSE
import re
from sympy  import *
from equations_handling import *
import numpy as np
from numpy import *


print(latex("x"))
eq=sympify("2*x")

solution = solve_equation(eq)


print(eq.subs("x",2))
print(solution)
print(solution.subs("x",0))
print("--------------")
sol=Eq(solution.subs("x",1).rhs,11)

con=solve([sol])
# constants = solve([solution.subs('x',0).rhs, (solution.subs('x', 0).rhs -5)])
print(con)
final_answer = solution.subs(con)
print(final_answer)
print(final_answer.subs("x",5).rhs)
consol=remove_constants(solve_equation("2*x"),10,0)
f2=lambda x: consol.subs({"x":x}).rhs
xlist=np.arange(0,4,1)#values of x in f(x)   
ylist=[]
for x in xlist :ylist.append(f2(x))#values of y in f(x)
       
print(xlist)
print(ylist)

print(f2(0))














'''
import tkinter as tk

class MyDialog:

    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='Enter your username below')
        self.myLabel.pack()
        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        self.username = self.myEntryBox.get()
        self.top.destroy()

def onClick():
    inputDialog = MyDialog(root)
    root.wait_window(inputDialog.top)
    print('Username: ', inputDialog.username)

root = tk.Tk()
mainLabel = tk.Label(root, text='Example for pop up input box')
mainLabel.pack()

mainButton = tk.Button(root, text='Click me', command=onClick)
mainButton.pack()

root.mainloop()
'''

'''

import tkinter

class Mbox(object):

    root = None

    def __init__(self, msg, dict_key=None):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        tki = tkinter
        self.top = tki.Toplevel(Mbox.root)

        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        label = tki.Label(frm, text=msg)
        label.pack(padx=4, pady=4)

        caller_wants_an_entry = dict_key is not None

        if caller_wants_an_entry:
            self.entry = tki.Entry(frm)
            self.entry.pack(pady=4)

            b_submit = tki.Button(frm, text='Submit')
            b_submit['command'] = lambda: self.entry_to_dict(dict_key)
            b_submit.pack()

        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(padx=4, pady=4)

    def entry_to_dict(self, dict_key):
        data = self.entry.get()
        if data:
            d, key = dict_key
            d[key] = data
            self.top.destroy()
            



root = tkinter.Tk()

Mbox = Mbox
Mbox.root = root

D = {'user':'Bob'}

b_login = tkinter.Button(root, text='Log in')
b_login['command'] = lambda: Mbox('Name?', (D, 'user'))
b_login.pack()

b_loggedin = tkinter.Button(root, text='Current User')
b_loggedin['command'] = lambda: Mbox(D['user'])
b_loggedin.pack()

root.mainloop()



'''







# str="as asf"
# print(str[0:str.rfind(' ')]+"ss")
#
# pattern = re.compile(".*"+re.escape("asd co".split()[-1]) + '.*', re.IGNORECASE)
#
#         #print(fieldValue)
#         #print(acListEntry)
# print(re.match(pattern, "acos"))
#
# my_buttons_list=[{"name":"ss","command":lambda:print("hello")}]
#
# print(my_buttons_list[0]["name"])
# my_buttons_list[0]["command"]