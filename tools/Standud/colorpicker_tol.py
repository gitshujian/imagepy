# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:35:09 2016

@author: yxl
"""
from core.engines import Tool
from core.managers import ColorManager

class Plugin(Tool):
    title = 'Color Picker'
    para = {'front':(255,255,255), 'back':(0,0,0)}
    view = [('color', 'front', 'front', 'color'),
            ('color', 'back', 'back', 'color')]
        
    def config(self):
        ColorManager.set_front(self.para['front'])
        ColorManager.set_back(self.para['back'])
        
    def mouse_down(self, ips, x, y, btn, **key):
        if btn == 1:ColorManager.set_front(ips.get_img()[int(y), int(x)])
        if btn == 3:ColorManager.set_back(ips.get_img()[int(y), int(x)])
        print ips.get_img()[int(y), int(x)]
        print ColorManager.get_front()
    
    def mouse_up(self, ips, x, y, btn, **key):
        pass
    
    def mouse_move(self, ips, x, y, btn, **key):
        pass
        
    def mouse_wheel(self, ips, x, y, d, **key):
        pass
    