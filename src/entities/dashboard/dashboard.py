#!/usr/bin/env python

from src.exceptions.grafana_exceptions import EmptyDashboardTitleException

class Dashboard(object):
    id = ""
    title = ""
    tags = None
    style = "dark"
    timezone = "browser"
    editable = True
    hideControls = False
    sharedCrosshair = False

    schemaVersion = 12  # default
    version = 0         # default
    links = None
    gnetId = None       # default

    def __init__(self, title, id):
        if not (len(title) > 0):
            raise EmptyDashboardTitleException()
        #TODO if id == -1:
            # Generate an id for this dashboard.
        self.id = id
        self.title = title
        self.rows = None
        self.time = self.setTime("6h", "now")
        self.timePicker = self.initTimePicker()
        self.templating = self.initTemplating()
        self.annotations = self.initAnnotations()

        return

    def setId(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def setTags(self, tags):
        self.tags = tags

    def setStyle(self, style="dark"):
        self.style = style

    def setTZ(self, tz="browser"):
        self.timezone = tz

    def setEditable(self, editable=True):
        self.editable = editable

    def setHideControls(self, hide=False):
        self.hideControls = hide

    def setSharedCrosshair(self, val=False):
        self.sharedCrosshair = val

    def setSchemaVersion(self, version):
        self.schemaVersion = version

    def setVersion(self, version):
        self.version = version

    def setLinks(self, links):
        self.links = links

    def setGNetID(self, gnetID):
        self.gnetId = gnetID

    def setTime(self, fromTime, toTime):
        return {
            'from': "now-"+fromTime,
            'to':   "now",
        }

    def initTimePicker(self):
        return {
            'time_options':         ["5m", "15m", "1h", "6h", "12h", "24h", "2d", "7d", "30d"],
            'refresh_intervals':    ["5s", "10s", "30s", "1m", "5m", "15m", "30m", "1h", "2h", "1d"],
        }

    def initTemplating(self):
        return {
            'list': [],
        }

    def initAnnotations(self):
        return {
            'list': [],
        }

    def addRow(self, row):
        if self.rows is None:
            self.rows = []
        self.rows.append(row)
        return
