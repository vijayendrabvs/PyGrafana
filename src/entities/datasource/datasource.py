#!/usr/bin/env python

import json

class DataSource(object):
    """
    DataSource represents the generic DataSource class.
    A data source is anything that can feed data into
    grafana - the types are prometheus, graphite.
    """
    url = ""
    Name = ""
    Type = ""
    Access = ""

    """
    Getters
    """
    def getURL(self):
        return self.url

    def getName(self):
        return self.Name

    def getType(self):
        return self.Type

    def getAccess(self):
        return self.Access

    """
    Setters
    """
    def setURL(self, url):
        self.url = url

    def setName(self, name):
        self.Name = name

    def setType(self, type):
        self.Type = type

    def setAccess(self, access):
        self.Access = access

    def __init__(self, name, url, type, access="direct"):
        self.setURL(url)
        self.setName(name)
        self.setType(type)
        self.setAccess(access)

    def create(self):
        # Prepare a datasource object and
        # issue the grafana HTTP API to create the
        # datasource.
        create_json = json.dumps(self)

        print(create_json)

    def delete(self):
        print("Deleting Data source " + self.Name)




