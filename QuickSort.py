#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame 
import random 


# In[2]:


pygame.font.init() 


# In[3]:


screen = pygame.display.set_mode((900, 650)) 


# In[4]:


pygame.display.set_caption("SORTING VISUALISER") 


# In[5]:


img = pygame.image.load('Tux.png') 
pygame.display.set_icon(img) 


# In[6]:


run = True


# In[7]:


width = 900
length = 600
array =[0]*151
arr_clr =[(0, 204, 102)]*151
clr_ind = 0
clr =[(0, 204, 102), (255, 0, 0), 
(0, 0, 153), (255, 102, 0)] 
fnt = pygame.font.SysFont("Cooper", 30) 
fnt1 = pygame.font.SysFont("Bookman Old Style", 17) 


# In[8]:


# Generate new Array 
def generate_arr(): 
    for i in range(1, 151): 
        arr_clr[i]= clr[0] 
        array[i]= random.randrange(1, 100) 
generate_arr() 


# In[9]:


def refill(): 
    screen.fill((255, 255, 255)) 
    draw() 
    pygame.display.update() 
    pygame.time.delay(5) 


# In[10]:


# Sorting Algo:Quick sort
def partition(arr,low,high):
    pygame.event.pump()
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high):
        refill()
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot:
            refill()
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high):
    pygame.event.pump()
    if low < high:
        #refill()
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)


# In[11]:


# Draw the array values 
def draw(): 
    # Text should be rendered 
    txt = fnt.render("PRESS 'ENTER' TO PERFORM SORTING.", 1, (0, 150, 200)) 
    # Position where text is placed 
    screen.blit(txt, (20, 20)) 
    txt1 = fnt.render("PRESS 'N' FOR NEW ARRAY.",1, (0, 150, 200)) 
    screen.blit(txt1, (20, 40)) 
    txt2 = fnt1.render("ALGORITHM USED: QUICK SORT", 1, (255,255,255), (0,0,0)) 
    screen.blit(txt2, (600, 60)) 
    element_width =(width-150)//150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 95), (900, 95), 6) 
    for i in range(1, 100): 
        pygame.draw.line(screen, 
                        (224, 224, 224), 
                        (0, boundry_grp * i + 100), 
                        (900, boundry_grp * i + 100), 1) 
    
    # Drawing the array values as lines 
    for i in range(1, 151): 
        pygame.draw.line(screen, arr_clr[i], 
                        (boundry_arr * i-3, 100), 
                        (boundry_arr * i-3, array[i]*boundry_grp + 100), element_width) 


# In[12]:


# Infinite loop to keep the window open 
while run: 
    # background 
    screen.fill((255, 255, 255)) 
    # Event handler stores all event 
    for event in pygame.event.get(): 
        # If we click Close button in window 
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                generate_arr() 
            if event.key == pygame.K_RETURN: 
                quickSort(array, 0, len(array)-1)	 
    draw() 
    pygame.display.update() 
    
pygame.quit() 


# In[ ]:




