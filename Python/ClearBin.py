#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pyautogui
import win32com.client as comctl
button = comctl.Dispatch("WScript.Shell")
import time

while True:
    #1 Detect the non empty Bin and clear
    if pyautogui.locateOnScreen('FullRecycleBin.png') != None:
        time.sleep(0.1)
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('FUllRecycleBin.png'))
        time.sleep(0.1)
        pyautogui.click(button='right')
        time.sleep(0.1)
        button.SendKeys("{Down 2}")
        time.sleep(0.1)
        button.SendKeys("{Enter}")
        time.sleep(2)
        button.SendKeys("{Enter}")
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Sound.png'))
        time.sleep(0.1)
        pyautogui.click()        
        break
    #2 Detect the empty bin with no action
    elif pyautogui.locateOnScreen('EmptyRecycleBin.png') != None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('EmptyRecycleBin.png'))
        break
    else:
        time.sleep(0.5)


# In[ ]:




