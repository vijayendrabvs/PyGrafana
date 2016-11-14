#!/usr/bin/env python

class ToolTip(object):
    value_type = "cumulative"   # default
    shared = True
    sort = 0
    msResolution = True

    def __init__(self, value_type="cumulative", shared=True, sort=0, msResolution=True):
        self.value_type = value_type
        self.shared = shared
        self.sort = sort
        self.msResolution = msResolution
        return

    # TODO - add more funcs to custom set each attribute.