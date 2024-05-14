'''

written by Emily Pollacchi
  	file name matteTool
  	Copyright (C) 2024 by Emily Pollacchi
  	epollacchi@gmail.com

'''

import maya.cmds as cmds

def matteCreator():
    
    matteName   = cmds.textField('matteName', query = True, text = True)
    if len(matteName) == 0:
        matteName = 'Matte_01'
    if matteName.isdigit():
        matteName = 'Matte_01'
        
    widthInput  = cmds.floatField('widthInput', query = True, value = True)
    heightInput = cmds.floatField('heightInput', query = True, value = True)

    myPlane = cmds.polyPlane(n = matteName, sx=1, sy=1, w = widthInput, h = heightInput)
    
    cmds.select(myPlane)
    cmds.rotate('90deg', 0, 0, r=True)

    
    curSel = cmds.ls(myPlane)
    for n in curSel:
        bbox = cmds.exactWorldBoundingBox(n)
        lower = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
        cmds.xform(n, piv=lower, ws=True)
        cmds.move(0,0,0, ws=True, rpr=True)
        cmds.makeIdentity(apply=True, translate=True, rotate=True, scale=True)
	                
def myWindow():
       
    if cmds.window('matteWindow', exists = True):
        cmds.deleteUI('matteWindow')
      
    cmds.window('matteWindow', title = 'Matte Creator', widthHeight = (122, 130), mnb = False, s = False, mxb = False, rtf = False)
    cmds.columnLayout()
    
    cmds.text(label = 'Enter Matte Name:')
    cmds.textField('matteName', pht = 'Matte_01')
    
    cmds.text(label = 'Enter Width:')
    cmds.floatField('widthInput', minValue = 0.001, value = 19.2, precision = 2, step = 0.01)
    
    cmds.text(label = 'Enter Height:')
    cmds.floatField('heightInput', minValue = 0.001, value = 10.8, precision = 2, step = 0.01)
    
    cmds.button(label = 'Create', command = 'matteCreator()')
    cmds.showWindow()
        
myWindow()
