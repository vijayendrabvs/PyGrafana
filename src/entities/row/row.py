#!/usr/bin/env python

class Row(object):
    height = "250px"    # default
    title = "Row"       # default
    collapse = False    # default
    editable = True     # default
    panels = None

    def __init__(self):
        return

    def addPanel(self, panel):
        if self.panels is None:
            self.panels = []
        self.panels.append(panel)
        return

    def setHeight(self, height):
        self.height = height

    def setTitle(self, rowTitle):
        self.title = rowTitle

    def setCollapse(self, val):
        self.collapse = val

    def setEditable(self, val):
        self.editable = val