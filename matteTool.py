'''

written by Emily Pollacchi
  	file name alignX
  	Copyright (C) 2016 by Emily Pollacchi
  	epollacchi@gmail.com

'''

import maya.cmds as mc

def matteCreator():
    
    matteName   = mc.textField('matteName', query = True, text = True)
    if len(matteName) == 0:
        matteName = 'Matte_01'
    if matteName.isdigit():
        matteName = 'Matte_01'
        
    widthInput  = mc.floatField('widthInput', query = True, value = True)
    heightInput = mc.floatField('heightInput', query = True, value = True)

    myPlane = mc.polyPlane(n = matteName, sx=1, sy=1, w = widthInput, h = heightInput)
    
    mc.select(myPlane)
    mc.rotate('90deg', 0, 0, r=True )
    
    curSel = mc.ls(myPlane)
    for n in curSel:
        bbox = mc.exactWorldBoundingBox(n)
        bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
        mc.xform(n, piv=bottom, ws=True)
                
def myWindow():
       
    if mc.window('matteWindow', exists = True):
        mc.deleteUI('matteWindow')
      
    mc.window('matteWindow', title = 'Matte Creator', widthHeight = (122, 130), mnb = False, s = False, mxb = False, rtf = False)
    mc.columnLayout()
    
    mc.text(label = 'Enter Matte Name:')
    mc.textField('matteName', pht = 'Matte_01')
    
    mc.text(label = 'Enter Width:')
    mc.floatField('widthInput', minValue = 0.001, value = 19.2, precision = 2, step = 0.01)
    
    mc.text(label = 'Enter Height:')
    mc.floatField('heightInput', minValue = 0.001, value = 10.8, precision = 2, step = 0.01)
    
    mc.button(label = 'Create', command = 'matteCreator()')
    mc.showWindow()
    
myWindow()