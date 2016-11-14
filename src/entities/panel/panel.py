#!/usr/bin/env python

from src.entities.grid.grid import Grid
from src.entities.legend.legend import Legend
from src.entities.tooltip.tooltip import ToolTip
from src.exceptions.grafana_exceptions import InvalidPanelIDFormatException

class Panel(object):
    title = ""
    error = False
    span = 12           # default
    editable = True
    type = "graph"      # default
    isNew = True
    fill = 1
    linewidth = 2       # default

    lines = True
    points = False
    bars = False
    stack = False
    pointradius = 5     # default

    percentage = False
    nullPointMode = "connected"
    steppedLine = False
    timeFrom = None
    timeShift = None
    aliasColors = {}
    seriesOverrides = []
    links = []

    def __init__(self, id, dataSource):
        if isinstance(id, int):
            self.id = id    # must be an integer.
        else:
            raise InvalidPanelIDFormatException()
        self.targets = self.initTargets()
        self.datasource = dataSource
        self.renderer = "flot"
        self.yaxes = self.initYaxes()
        # TODO - add the 2 yaxes in the main program.
        self.xaxis = self.initXAxis()
        self.grid = self.initGrid()
        self.legend = self.initLegend()
        self.tooltip = self.initToolTip()

    def initTargets(self):
        return []

    def addTarget(self, target):
        self.targets.append(target)

    def initYaxes(self):
        return []

    def initXAxis(self):
        return {
            "show": True,
        }

    def addYaxis(self, yaxis):
        self.yaxes.append(yaxis)
        return

    def initGrid(self):
        return Grid(None, None)

    def initLegend(self):
        return Legend()

    def initToolTip(self):
        return ToolTip("cumulative", True, 0, True)

