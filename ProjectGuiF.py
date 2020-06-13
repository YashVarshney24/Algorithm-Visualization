#!/usr/bin/env python
# coding: utf-8

# In[40]:


# python program demonstrating 
# Combobox widget using tkinter 


import tkinter as tk 
from tkinter import ttk 
from tkinter import *
# Creating tkinter window 
window = tk.Tk() 
window.title('Algorithm Visualizer') 
window.geometry('1000x500')
window.configure(bg='LightBlue')

def close():
   window.destroy()
l1 = Label(text = '||||   ALGORITHM VISUALIZER    ||||', bg = 'black', fg='white', padx = '50', font = ('Courier', 30, 'bold','underline'), borderwidth = 3, relief = 'sunken')
l1.pack(fill = 'y')

# label 
l2 = tk.Label(window, text = "CHOOSE THE ALGORITHM :", fg='blue', 
		font = ("Courier", 15)) 

l2.pack(padx = 10, pady = 20)
# Combobox creation 
alg = tk.StringVar() 
ALGO = ttk.Combobox(window, width = 27, textvariable = alg) 

# Adding combobox drop down list 
ALGO['values'] = ('SORTING' , 'SEARCHING') 

ALGO.pack(padx = 5, pady = 5)
ALGO.current()

#al = Type of Algorithm

l3 = tk.Label(window, text = "CHOOSE THE SUB-TYPE OF ALGORITHM :", fg='blue', 
		font = ("Courier", 15)) 

l3.pack(padx = 10, pady = 20)
# Combobox creation 
subalg = tk.StringVar() 
subalgo = ttk.Combobox(window, width = 27, textvariable = subalg) 

# Adding combobox drop down list
subalgo['values'] = ('BUBBLE SORT','INSERTION SORT', 'SELECTION SORT', 'MERGE SORT', 'QUICK SORT', 'BINARY SEARCH', 'LINEAR SEARCH')     
subalgo.pack(padx = 5, pady = 5)
subalgo.current() 

l4 = tk.Label(window, text = "ENTER AN ARRAY :", fg='blue', 
		font = ("Courier", 15)) 

l4.pack(padx = 10, pady = 20)
array = StringVar()

En = tk.Entry(window , textvariable = array)
En.pack()

random = tk.Checkbutton(window , text = 'Initailise random array')
random.pack()

bu = tk.Button(window , text = 'SUBMIT', command = close, height = 2, width = 10, bg='pink', fg= 'blue')
bu.pack(padx = 5, pady = 5)

window.mainloop() 


# In[ ]:





# In[45]:


#ASSIGNING THE VALUES CHOOSEN BY USER
#al = Type of Algorithm
al = alg.get()

#sub = Type Of Sub Algorithm
sub = subalg.get()

#ARRAY INPUT FROM USER 
arr = array.get()

#The array input taken in String is COnverted into List 
li = list(arr.split(" "))


# In[42]:


import os


# In[44]:


if al=='SORTING' and sub=='BUBBLE SORT':
    os.system('Python BubbleSort.py')
elif al=='SORTING' and sub=='INSERTION SORT':
    os.system('Python InsertionSort.py')
elif al=='SORTING' and sub=='MERGE SORT':
    os.system('Python mergesort.py')
elif al=='SORTING' and sub=='QUICK SORT':
    os.system('Python QuickSort.py')
elif al=='SORTING' and sub=='SELECTION SORT':
    os.system('Python SelectionSort.py')
elif al == 'SEARCHING' and sub == 'BINARY SEARCH':
    os.system('Python BinarySearch.py')
elif al =='SORTING' and sub =='LINEAR SEARCH':
    os.system('Python LinearSearch.py')


# In[ ]:





# In[ ]:





# In[ ]:




