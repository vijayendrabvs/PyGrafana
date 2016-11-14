#!/usr/bin/env python

import requests
import json
from src.entities.datasource.datasource import DataSource
from src.exceptions.grafana_exceptions import DataSourceCreateFailedException
from src.exceptions.grafana_exceptions import InvalidDataSourceFormatException
from src.client.grafanaclient.grafanaEP import GrafanaEndPoint


class DataSourceClient(object):
    grafanaEndPoint = None
    dataSourceRequest = None
    dataSource = None

    def __init__(self, dataSourceReq, grafana_ip="localhost", grafana_port=3000, username="admin", pwd="admin"):
        if isinstance(dataSourceReq, DataSource):
            self.dataSourceRequest = dataSourceReq
        else:
            raise InvalidDataSourceFormatException()
        self.grafanaEndPoint = GrafanaEndPoint(grafana_ip, grafana_port, username, pwd)
        return

    def prepare_create_uri(self, protocol="http"):
        uri = protocol + "://" + self.grafanaEndPoint.username + ":" + self.grafanaEndPoint.password + "@" +\
              self.grafanaEndPoint.grafana_ip + ":" +\
              str(self.grafanaEndPoint.grafana_port) + "/api/datasources"
        return uri

    def prepare_delete_uri(self, dataSourceID, protocol="http"):
        uri = protocol + "://" +  self.grafanaEndPoint.username + ":" + self.grafanaEndPoint.password + "@" +\
              self.grafanaEndPoint.grafana_ip + ":" + \
              str(self.grafanaEndPoint.grafana_port) + "/api/datasources/" + str(dataSourceID)
        return uri

    def create(self):
        # Creates a datasource.
        uri = self.prepare_create_uri()
        print("uri for datasource create: " + uri)
        print("data is: " + json.dumps(self.dataSourceRequest.__dict__))
        headers = {'Content-Type': 'application/json'}
        res = requests.post(uri, json.dumps(self.dataSourceRequest.__dict__), headers=headers)
        if res.status_code != requests.codes.ok:
            print("Failed to create datasource, response: " + str(res))
            raise DataSourceCreateFailedException()
        print("Successfully created grafana data source, result: " + str(res.json()))
        self.dataSource = res.json()
        return res

    def delete(self, id):
        # Deletes this datasource.
        uri = self.prepare_delete_uri("http")
        r = requests.delete(uri)
        return

    def update(self):
        return

    def get(self, id=0):
        uri = self.prepare_create_uri()
        r = requests.get(uri)
        print("result of get datasources: " + str(r.text))
        return r

    def list(self):
        return


