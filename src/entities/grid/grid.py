#!/usr/bin/env python

class Grid(object):
    threshold1 = None
    threshold2 = None
    threshold1Color = ""
    threshold2Color = ""

    def __init__(self, threshold1=None, threshold2=None, threshold1Color="rgba(216, 200, 27, 0.27)", threshold2Color="rgba(234, 112, 112, 0.22)"):
        self.threshold1 = threshold1
        self.threshold1Color = threshold1Color
        self.threshold2 = threshold2
        self.threshold2Color = threshold2Color
        return